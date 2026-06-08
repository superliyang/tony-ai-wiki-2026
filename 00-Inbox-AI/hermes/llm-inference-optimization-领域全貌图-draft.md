---
title: "LLM推理优化工程 — 领域全貌图"
domain: llm-inference-optimization
status: draft
source: exa-search
created: 2026-06-07
updated: 2026-06-07
---

# LLM 推理优化工程 — 领域全貌图

## 1. 目标 (Goals)

LLM 推理优化的核心目标不是单一维度的"快"，而是在四个互相冲突的维度上做多目标优化：

| 维度 | 定义 | 典型目标值 |
|------|------|-----------|
| **吞吐 (Throughput)** | 单位时间生成的 token 数 | 1000-4000 tok/s (H100, 70B) |
| **延迟 (Latency)** | TTFT (首 token 时间) + TPOT (每 token 时间) | TTFT < 200ms, TPOT < 50ms |
| **成本 (Cost)** | 每百万 token 的 GPU/电力成本 | 量化可降低 80%+ 成本 |
| **质量 (Quality)** | 精度损失 vs 原始模型 | FP8 < 1%, INT4 < 3-8% |

**核心张力**：这四个维度相互冲突。提高吞吐 → 增大 batch → 延迟上升；降低延迟 → 减小 batch → 吞吐下降；降精度加速 → 质量可能受损。没有银弹，只有场景化取舍。

**推理的两个瓶颈革命**：
- **Prefill（预填充）**：Compute-bound。编码 prompt，构建 KV Cache。受限于 GPU 算力（FLOPS）。
- **Decode（解码）**：Memory-bandwidth-bound。逐 token 生成，每次前向需要读取全部模型权重 + KV Cache。受限于显存带宽（HBM BW）。

> 一个 H200 上 70B FP8 模型的 decode：约 70GB 权重需从 HBM 流到 SM 寄存器，仅产生 1 个 token。H200 的 ~4.8 TB/s 带宽理论上每 token 最低延迟 ≈ 14ms——这还没算 Attention。

## 2. 角色与核心对象 (Roles & Objects)

### 生态系统分层

```
┌──────────────────────────────────────────────────────┐
│  应用层 │ LiteLLM Proxy, NVIDIA Dynamo, OpenRouter   │ ← API 网关/路由/负载均衡
├──────────────────────────────────────────────────────┤
│  编排层 │ LangChain, LlamaIndex, vLLM Semantic Router│ ← 多模型编排/智能体调度
├──────────────────────────────────────────────────────┤
│  服务层 │ vLLM, SGLang, TGI, TensorRT-LLM, LMDeploy  │ ← 推理引擎核心
├──────────────────────────────────────────────────────┤
│  内核层 │ PagedAttention, FlashAttention, CUDA kernels│ ← 算子级优化
├──────────────────────────────────────────────────────┤
│  运行时 │ llama.cpp, MLC LLM, Ollama                  │ ← 跨平台/端侧
├──────────────────────────────────────────────────────┤
│  硬件层 │ NVIDIA GPU, AMD GPU, Apple Silicon, 昇腾    │ ← 物理算力
└──────────────────────────────────────────────────────┘
```

### 核心引擎定位（2026）

| 引擎 | 定位 | 核心创新 | 最佳场景 |
|------|------|----------|----------|
| **vLLM** | 通用生产默认 | PagedAttention + Continuous Batching | 广泛模型支持，中大规模 GPU 集群 |
| **SGLang** | 结构化/高缓存 | RadixAttention（前缀树缓存）+ XGrammar | 结构化输出、RAG、Agent 循环 |
| **TensorRT-LLM** | NVIDIA 极速 | 编译时优化 + FP8/FP4 一等到位 | 纯 NVIDIA 集群，模型稳定不常变 |
| **llama.cpp** | 跨平台轻量 | GGUF 量化 + CPU/Metal 优化 | 端侧、Mac、无 GPU 场景 |
| **TGI** | HF 原生 | HuggingFace 生态集成 | 快速原型、HF 用户 |
| **LMDeploy** | 国产替代 | 阿里自研，昇腾适配 | 国产芯片、阿里云生态 |

## 3. 关键流程 (Key Process)

### 推理请求全生命周期

```
请求到达 → [API Gateway: LiteLLM]
              │
    ┌─────────▼─────────┐
    │  Scheduler 调度器  │ ← 决定何时将请求插入 batch
    │  (Continuous Batching / IFB)  │
    └─────────┬─────────┘
              │
    ┌─────────▼─────────┐
    │  Prefill 阶段      │ Compute-bound
    │  处理 prompt → KV Cache │ 大 batch 高效
    │  时间: O(n²) with n=seq_len │
    └─────────┬─────────┘
              │
    ┌─────────▼─────────┐
    │  Decode 阶段       │ Memory-bandwidth-bound
    │  逐 token 自回归生成│ 小 batch 延迟低
    │  每步: Load Weights + KV Cache │
    │  ┌── 投机解码循环 ──┐ │
    │  │ Draft→Verify→Accept │ │
    │  └────────────────┘ │
    └─────────┬─────────┘
              │
        流式返回 token → 客户端
```

### 关键时序约束

```
请求到达
  │
  ├─ TTFT (Time To First Token) ──────────── 首 token 出现
  │  └─ Prefill 耗时 + 调度等待 + 排队延迟
  │
  ├─ TPOT (Time Per Output Token) ─ 每 token 间隔
  │  └─ Decode 单步耗时（通常 10-50ms）
  │
  └─ Total Latency = TTFT + N × TPOT (N=输出token数)
```

### Prefill-Decode Disaggregation (解耦架构，2025+)

传统：同一 GPU 既做 prefill 又做 decode → 资源争抢。

解耦后：
- **Prefill Pool**：compute-bound → 需要大算力 GPU（H100），大 batch
- **Decode Pool**：memory-bandwidth-bound → 需要大显存 GPU（H200），小 batch
- **KV Cache Transfer**：prefill 池构建 KV Cache → RDMA/网络传输 → decode 池消费

> RTP-LLM（阿里）实测：解耦后 TTFT P95 降低 35-37%，prefill 机器数减少 75%。

## 4. 核心指标体系 (Core Metrics)

### 一级指标（直接用户感知）

| 指标 | 英文 | 定义 | 典型 SLO |
|------|------|------|----------|
| 首 Token 时间 | TTFT | 请求到达 → 第一个 token 输出 | P95 < 500ms |
| 每 Token 时间 | TPOT / ITL | 连续 token 之间的平均间隔 | P50 < 50ms |
| Token 吞吐 | Throughput | 系统整体 tok/s | 1000-4000 tok/s/H100 |
| 有效吞吐 | Goodput | 满足 SLO 的请求的吞吐 | 必须 > 90% 请求量 |

### 二级指标（系统内部）

| 指标 | 定义 | 健康范围 |
|------|------|----------|
| GPU 利用率 | SM 占用率 | decode 阶段 60-85% |
| KV Cache 利用率 | 已分配页数 / 总可用页数 | < 90%（>95% 有 OOM 风险） |
| Batch Size | 并发处理的请求数 | 动态，取决于序列长度 |
| 请求排队深度 | 等待调度的请求数 | 应 < 峰值吞吐的 2× |
| 缓存命中率 | Prefix cache hit rate | 越高越好，Agent 场景 > 50% |

### 各引擎性能参考（H100，LLaMA-70B，BF16）

| 引擎 | 峰值吞吐 | P50 TTFT | P50 TPOT | 显存开销 |
|------|---------|----------|----------|----------|
| TensorRT-LLM | 2400 tok/s | 105ms | 12ms | 1.5-2GB |
| vLLM | 2100 tok/s | 120ms | 15ms | 2-3GB |
| SGLang | 1800 tok/s | 112ms | 18ms | 3-4GB |
| TGI | 1600 tok/s | 110ms | 22ms | 1-2GB |

> 注：实际数字因模型、batch size、序列长度、量化精度而异。这是相对比较而非绝对值。

## 5. 关键问题 (Key Problems)

### 问题矩阵：结构性瓶颈

```
                    Compute-Bound          Memory-Bandwidth-Bound
                      (Prefill)                (Decode)
┌─────────────┬──────────────────────┬──────────────────────────┐
│ 显存容量     │ 模型权重放不下       │ KV Cache 溢出（长上下文） │
│ (Capacity)   │ → TP/PP 切分         │ → Offload / Eviction      │
├─────────────┼──────────────────────┼──────────────────────────┤
│ 显存带宽     │ 权重读取成为瓶颈     │ 每 token 都重读全部权重    │
│ (Bandwidth)  │ → Kernel Fusion      │ → 投机解码 / 量化权重     │
├─────────────┼──────────────────────┼──────────────────────────┤
│ 调度效率     │ Prefill 长尾阻塞     │ 请求生命周期不一，浪费槽位 │
│ (Scheduling) │ → Chunked Prefill    │ → Continuous Batching     │
├─────────────┼──────────────────────┼──────────────────────────┤
│ 硬件锁定     │ 不同 GPU 架构适配     │ NVIDIA  vs AMD vs 昇腾    │
│ (Vendor Lock)│ → 编译器/运行时抽象   │ → 跨平台框架（llama.cpp）  │
└─────────────┴──────────────────────┴──────────────────────────┘
```

### 五大未完全解决的问题（2026）

1. **长上下文（100K+ token）的 KV Cache 爆炸**：1M 上下文 + 70B 模型 = KV Cache 可达数百 GB，单卡根本放不下。方案在演进：分层 KV Cache（GPU→CPU→SSD）、KV 压缩、滑动窗口，但尚无通用生产方案。

2. **MoE 模型的高效调度**：Mixture-of-Experts（如 DeepSeek-V3、Mixtral）引入 Expert Parallelism，prefill 和 decode 的专家激活模式完全不同，现有调度器对 MoE 的优化仍不成熟。

3. **混合模型架构（Gemma 3、Jamba、Llama 4）**：混合 Attention（全局+滑动窗口）+ 混合 SSM + 混合专家，需要"统一混合 KV Cache"架构，vLLM Jenga、SGLang CUDA Virtual Memory 正在尝试。

4. **SLO 约束下的 Goodput 最大化**：无条件吞吐（"我能跑 4000 tok/s"） ≠ 有效服务能力。在 TTFT < 200ms 约束下，实际吞吐可能只有无约束的 30-50%。

5. **推理成本的经济模型**：GPU 选型 + 量化精度 + batch策略 + 解耦架构 的四维组合空间太大，缺乏系统化的成本建模工具。

## 6. 核心技术架构 (Technical Architecture)

### 推理引擎的四层架构

```
Layer 4: API & Protocol
┌─────────────────────────────────────┐
│ OpenAI-compatible REST/gRPC Server  │
│ Streaming, Tool Calling, Logprobs   │
└──────────────┬──────────────────────┘
               │
Layer 3: Scheduler（调度）
┌─────────────────────────────────────┐
│ Continuous Batching / In-Flight Batching │
│ Prefix-aware Scheduling (RadixAttention)│
│ Chunked Prefill, SLO-aware Scheduling  │
└──────────────┬──────────────────────┘
               │
Layer 2: KV Cache Manager（显存管理）
┌─────────────────────────────────────┐
│ PagedAttention (vLLM) —— 分页虚拟化  │
│ RadixAttention (SGLang) —— 前缀树缓存│
│ Hierarchical Multi-Tier (RTP-LLM)    │
│ GPU → CPU → RDMA → SSD               │
└──────────────┬──────────────────────┘
               │
Layer 1: Kernel（算子）
┌─────────────────────────────────────┐
│ FlashAttention / FlashInfer          │
│ CUDA Graph / Kernel Fusion           │
│ FP8/FP4/INT4 量化 GEMM               │
│ Speculative Decoding Kernels         │
└─────────────────────────────────────┘
```

### KV Cache 管理演进：5 个时代

| 时代 | 方案 | 代表 | 核心机制 |
|------|------|------|----------|
| Era 1 | 连续分配 | 原始实现 | 每个请求分配连续显存块 |
| Era 2 | 分页虚拟化 | vLLM PagedAttention | 4KB 页，非连续分配，消除碎片 |
| Era 3 | 前缀感知缓存 | SGLang RadixAttention | Radix Tree 管理，共享前缀自动复用 |
| Era 4 | 分布式 KV Cache | NVIDIA Dynamo | 跨节点 KV 路由，发送到已有 cache 的节点 |
| Era 5 | 统一混合架构 | vLLM Jenga / SGLang CUDA Virtual | 文本+VLM+MoE+SSM 多种 KV 统一管理 |

### 三大优化范式的对比

| 范式 | 代表引擎 | 优化时机 | 优势 | 代价 |
|------|----------|---------|------|------|
| **运行时优化** | vLLM, SGLang | 在线调度 | 即插即用，模型灵活 | 理论峰值不如编译 |
| **编译时优化** | TensorRT-LLM | 部署前编译 | 极致性能（+20-40%） | 编译 30-60min，硬件锁定 |
| **量化时优化** | llama.cpp, AWQ | 模型转换 | 跨平台，显存大幅降低 | 精度损失 |

## 7. 解决方案族 (Solution Families)

### Problem → Solution → Tool 矩阵

| 问题 | 解决方案族 | 具体技术/工具 | 收益 |
|------|-----------|-------------|------|
| **显存不够放模型** | 量化 (Quantization) | FP8(W8A8), INT8, AWQ(W4A16), GPTQ, GGUF(Q4/Q2) | 显存降低 50-75%，损失 < 3% |
| **显存不够放 KV Cache** | KV 分页 + 卸载 | PagedAttention, RadixAttention, KV Offload | 碎片消除 + 延长上下文 |
| **GPU 利用率低** | 连续批处理 | Continuous Batching / IFB | 吞吐提升 5-23x |
| **长 prompt 拖慢 TTFT** | 分块预填充 | Chunked Prefill | 消除首 token 长尾 |
| **重复前缀浪费算力** | 前缀缓存 | Prefix Caching, RadixAttention | 系统 prompt 自动复用 |
| **decode 太慢** | 投机解码 | EAGLE/EAGLE-3, Medusa, P-EAGLE | 速度提升 2-3x |
| **prefill 和 decode 互相拖累** | 解耦架构 | Prefill-Decode Disaggregation | TTFT P95 ↓35%, 资源效率提升 |
| **结构化输出慢** | 受限解码 | XGrammar, Guided Decoding | 零 overhead 约束生成 |
| **多模型/多 LoRA** | 多 Adapter | Multi-LoRA serving, Hot Swap | 一卡服务 N 个适配器 |
| **多租户/多模型网关** | API 网关 | LiteLLM, NVIDIA Dynamo, OpenRouter | 统一计费/限流/路由 |

### 量化方案全景

```
精度降序 ──────────────────────────────►

FP32 ──► FP16/BF16 ──► FP8 ──► INT8 ──► INT4 ──► INT2
  │         │           │        │        │        │
 基准    无损压缩     A100+/H100  SmoothQuant AWQ/GPTQ  极限
140GB     70GB       35GB      17.5GB    8.7GB    4.4GB
(70B)                (<1%损)   (1-3%损) (3-8%损) (>10%损)
                     ▲                     ▲
                  GPU服务器首选         消费级GPU首选

格式缩写说明：
- W8A8: 权重 INT8 + 激活 INT8（TensorRT-LLM）
- W4A16: 权重 INT4 + 激活 FP16（AWQ/GPTQ）
- GGUF Q4_K_M: llama.cpp 的 4-bit 混合精度格式
- NVFP4: Blackwell GPU 原生 FP4 格式
```

## 8. 常见失败模式 (Common Failure Modes)

| # | 失败模式 | 根因 | 后果 | 预防 |
|---|---------|------|------|------|
| 1 | **KV Cache 耗尽 → OOM Kill** | gpu_memory_utilization 设太高 | 服务 Crash，请求丢失 | 留 10% 缓冲，监控利用率 |
| 2 | **首 Token 长尾（Long-tail TTFT）** | 一个长 prompt 阻塞整个 batch | P99 TTFT 爆炸，用户体验差 | 启用 Chunked Prefill |
| 3 | **假高吞吐（Fake Throughput）** | 无 SLO 约束测吞吐 | 实际生产 50% 请求超时 | 用 Goodput 代替 Throughput |
| 4 | **量化精度塌陷** | 不当精度的量化（如 INT4 用于数学推理） | 模型输出质量崩溃 | 按任务选精度；数学/代码 → FP8+ |
| 5 | **编译僵化（Compile Lock-in）** | TensorRT-LLM 编译新模型需 30-60min | 模型迭代周期变长 | 稳定模型才走编译路线 |
| 6 | **投机解码反效果** | Draft 模型不匹配，接受率 < 50% | 比不用还慢（1.2x tax） | Draft 模型需领域对齐 |
| 7 | **批量效应不可见** | 单请求测延迟，高并发才暴露 | 上线后延迟飙升 | 压测需覆盖峰值并发 |
| 8 | **缓存失效风暴** | 系统 prompt 微改 → 所有前缀缓存失效 | 瞬时算力需求激增 | 版本化系统 prompt + 渐进切换 |

## 9. 新手误区 vs 高手权衡

| # | 新手误区 | 为什么错 | 高手做法 |
|---|---------|---------|----------|
| 1 | "选最快的引擎就行" | 不同 workload 最优引擎不同 | 按场景选：结构化 → SGLang；通用 → vLLM；极致吞吐+纯NVIDIA → TRT-LLM |
| 2 | "量化越激进越省钱" | INT4 对推理/代码任务损害大 | 简单 chat → INT4；通用 → FP8；数学/代码 → FP16+ |
| 3 | "吞吐越高越好" | 无 SLO 约束的吞吐是虚假指标 | 用 Goodput：满足延迟约束的前提下的吞吐 |
| 4 | "多卡 TP 就是线性加速" | 跨卡通信成为新瓶颈 | TP 适合 prefill，decode 阶段收益递减 |
| 5 | "投机解码总是有效" | Draft 模型不匹配时反而更慢 | 先测接受率，低于 60% 不要上 |
| 6 | "OOM 就加 GPU" | 可能是 KV Cache 碎片化而非容量不足 | 先调整 gpu_memory_utilization + 启用 prefix caching |

## 10. 关键趋势 (Key Trends, 2025-2026)

### 六大趋势

| 趋势 | 说明 | 代表性进展 |
|------|------|-----------|
| **1. Prefill-Decode 解耦成为主流** | 独立 scaling，解耦部署 | vLLM Disaggregated Serving, RTP-LLM, DistServe |
| **2. MoE 推理专用优化** | Expert 并行 + 动态路由 | SGLang MoE 优化, DeepSeek-V3 部署方案 |
| **3. 长上下文生产化（100K→1M）** | 分层 KV Cache + 压缩 | OrbitFlow, Jenga, 阿里混合架构 |
| **4. Blackwell GPU 原生 FP4** | NVFP4/MXFP4 新量化标准 | TensorRT-LLM FP4, vLLM Blackwell 适配 |
| **5. 推理引擎竞争白热化** | SGLang 获 $100M 融资，挑战 vLLM | SGLang RadixArk 2025 年 8 月成立 |
| **6. 端侧推理崛起** | llama.cpp + Ollama + Apple Silicon | GGUF 生态成熟，Mac Studio 跑 70B |

### vLLM 2026 年 3 月四大更新（标志性事件）

- **Semantic Router v0.2 Athena**：多模型语义路由，智能体调度
- **P-EAGLE**：并行投机解码，GPU 端输入准备，消除同步点
- **Nemotron 3 Super**：120B MoE 模型，完善高效 MoE 生态
- **Model Runner V2**：引擎底层重构，异步调度与投机解码共存

## 11. 专家问题清单 (Expert Question List)

以下 10 个问题按照 Tony 的 5 要素公式（对象 → 变量 → 权衡 → 边界 → 演化）设计：

### Serving 层（问题 1-4）

**Q1**：在服务 1000+ 并发用户的场景下，如果目标是 TTFT P95 < 300ms + TPOT P50 < 50ms，你们如何在 prefill batch size、chunked prefill 块大小、和 GPU 显存利用率之间取舍？当上下文从 8K 扩展到 128K 时，这个策略最先在哪里失效？

**Q2**：Prefill-Decode Disaggregation 看起来很美，但在实际生产中，你们如何决定 prefill 池和 decode 池的 GPU 配比？KV Cache 的网络传输延迟成为新瓶颈后，你们用 RDMA 还是 NVLink 来解决？什么场景下解耦反而不如合并？

**Q3**：SGLang 的 RadixAttention 在有大量共享前缀的场景（如 RAG + 固定 system prompt）中优势明显。但在前缀多样化（每个用户不同的上下文）时，Radix Tree 的管理开销是否会吃掉收益？vLLM 的 Automatic Prefix Caching 和 SGLang 的 RadixAttention 的边界在哪里？

**Q4**：TensorRT-LLM 编译后比 vLLM 快 20-40%，但编译需要 30-60 分钟。你们如何设计 CI/CD 流水线来支持"模型迭代"和"极致性能"的兼顾？是否尝试过 NVIDIA AutoDeploy beta 来简化？

### 模型压缩层（问题 5-7）

**Q5**：量化精度选择（FP8 vs INT8 vs INT4）背后，你们用什么方法论来决定"精度损失可接受"？是跑标准 benchmark（MMLU/GSM8K），还是针对自己的业务数据做端到端评估？什么任务类型绝对不能低于 FP8？

**Q6**：投机解码中，draft 模型的选择（EAGLE vs Medusa vs 小参数独立模型）实际上是一个"接受率 × draft 开销"的优化问题。你们在实践中如何选定 draft 模型和 speculative token 数？接受率低于多少时你们会放弃投机解码？

**Q7**：vLLM 的 Multi-LoRA serving 允许多个 LoRA adapter 共享同一个 base model。在 100+ adapter 的生产环境中，adapter 的加载/卸载策略、显存碎片、和调度优先级如何管理？有没有遇到过 adapter 之间的 KV Cache 污染问题？

### 应用层（问题 8-10）

**Q8**：LiteLLM Proxy / NVIDIA Dynamo 作为推理网关层，你们在实际生产中是如何做多模型路由的？是基于 token 成本（route to cheapest that meets SLO），还是基于语义（route by task type），还是基于负载（least connections）？混合策略的权重如何配置？

**Q9**：Semantic Cache（语义缓存）在降低推理成本上潜力巨大，但缓存的失效策略是个难题。当系统 prompt 微调、模型版本升级、或 RAG 文档更新时，你们的缓存一致性策略是什么？有没有遇到过"缓存命中但结果过时"的生产事故？

**Q10**：从全局架构看，推理优化最终是一个"GPU 选型 × 量化精度 × batch 策略 × 解耦架构"的四维优化空间。你们是如何系统化地做这个决策的？有没有内部成本建模工具，还是靠经验 + 压测迭代？

## 12. 推荐学习路径 (Learning Path)

### 五阶段学习路线

```
Phase 1: 建立心智模型（1-2天）
├── 理解 Prefill vs Decode 的本质差异（compute-bound vs memory-bound）
├── 读懂一篇推理引擎对比文章
└── 动手：用 Ollama 本地跑一个模型，用 vLLM 启动一个 server

Phase 2: 核心优化技术（3-5天）
├── PagedAttention 论文精读（vLLM SOSP'23）
├── Continuous Batching 原理
├── KV Cache 管理与卸载
├── 量化基础：FP16 → FP8 → INT4 的精度-成本曲线
└── 动手：用 AWQ/GGUF 量化一个模型，对比推理速度

Phase 3: 引擎深入（1-2周）
├── vLLM 源码阅读（scheduler, block manager, worker）
├── SGLang RadixAttention 与 Radix Tree 管理
├── TensorRT-LLM 编译流程（graph capture → engine build）
├── 投机解码：EAGLE-3 原理与实现
└── 动手：配置 vLLM 的生产参数（tensor-parallel, prefix-caching, chunked-prefill）

Phase 4: 生产化（1-2周）
├── Prefill-Decode Disaggregation 部署
├── LiteLLM / NVIDIA Dynamo 网关配置
├── 监控体系：TTFT / TPOT / KV Cache / Goodput 仪表盘
├── Multi-LoRA serving 的运维
└── 动手：搭建一个支持灰度/回滚的推理部署流水线

Phase 5: 前沿与架构（持续）
├── 长上下文（100K→1M）的 KV 分层管理
├── MoE 模型的推理优化
├── 端侧推理（llama.cpp + Apple Silicon）
├── 推理成本建模与 FinOps
└── 阅读：MLSys/OSDI 相关论文，跟踪 vLLM/SGLang release notes
```

### 核心论文阅读清单

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| PagedAttention (vLLM) | SOSP 2023 | KV Cache 分页虚拟化 |
| FlashAttention / FlashInfer | 2022-2024 | IO-aware 注意力计算 |
| Continuous Batching (Orca) | OSDI 2022 | 迭代级调度 |
| DistServe | OSDI 2024 | Prefill-Decode Disaggregation |
| EAGLE / EAGLE-3 | 2024-2025 | 投机解码 SOTA |
| SGLang (RadixAttention) | 2024 | 前缀树缓存 + 结构化生成 |

### 动手实验路线

```bash
# Day 1: 本地体验
ollama run llama3.1:8b

# Day 2: vLLM 生产部署
pip install vllm
vllm serve meta-llama/Llama-3.1-8B-Instruct \
  --gpu-memory-utilization 0.90 \
  --enable-prefix-caching \
  --max-model-len 8192

# Day 3: 压测
# 使用 benchmark 工具压测 TTFT/TPOT/Throughput

# Week 2: 量化对比
# AWQ 量化 + 精度评估 + 速度对比

# Week 3: 生产配置
# tensor-parallel + chunked-prefill + prefix-caching 组合调优
```

---

*状态: draft | 下一步: Tony 确认方向后进入 Phase 2 专家问题深挖*
