# 行业理解 Growth Track — AI 基础设施：推理市场 2026

日期: 2026-06-08 (周一)
方向: AI 基础设施（推理/训练市场）
状态: pending

---

## 今日行业

**AI 推理正在吞噬 AI 基础设施市场。** 2026 年初发生了"推理翻转"（Inference Flip）——全球累计推理算力支出历史性超越训练支出。推理现在占全球 AI 算力支出的 ~2/3，占企业 AI 预算的 ~85%。但与此同时，LLM API 价格在 2025-2026 年暴跌了约 80%（GPT-4 级能力从 $30/M tokens 到 $0.40/M tokens）。

这创造了一个悖论：**单价暴跌 × 用量暴涨 = 总支出继续攀升**。Agentic 工作流让推理 token 消耗放大 5-30 倍，Fortune 500 公司月度推理账单已达数千万美元。

## 为什么值得学

1. **推理是 Tony 工作栈的底层基础设施** — Hermes 每次调用 LLM 都涉及推理成本。理解推理经济学直接影响 agent 系统架构决策。
2. **市场结构正在发生根本性变化** — 英伟达从 92%（2023）降至 ~80%（2026），定制 ASIC 以 44.6% CAGR 增长。理解竞争格局有助于判断技术选型方向。
3. **Inference FinOps 是新学科** — 多模型路由、语义缓存、量化、spot 实例套利等技术可以降低 80% 以上的推理成本。这些是 agent 系统设计的核心关注点。
4. **产业链极宽** — 从硅芯片到冷却系统，从 GPU cloud 到 serverless，从 MLOps 到推理优化，每个环节都有独立的竞争动态和商业机会。

## 3 个核心概念

### 1. 推理翻转（The Inference Flip）
- 推理占 AI 算力支出的 ~67%（2026），预计 2028-2030 达 70-80%
- 驱动因素：模型部署规模扩大、Agentic 工作流的非线形 token 膨胀、实时应用需求
- 影响：推理价格敏感度远高于训练 → 有利于 AMD（成本优势）和定制 ASIC（TCO 优化）

### 2. 三线战争（NVIDIA vs AMD vs 定制硅）
- **NVIDIA**: ~80% 份额（$193.7B FY2026 DC 收入），但峰值已过（2024 年 87%）
- **AMD**: ~5-7% 份额（$7-8B），内存容量领先（288GB vs 192GB），推理性价比有真实优势。OpenAI 6GW 交易和 Meta $60-100B 承诺是结构性变化
- **Custom ASIC**: 44.6% CAGR vs GPU 16.1%。Google TPU 运行 >75% Gemini，AWS Trainium 处理 >50% Bedrock token。Broadcom AI ASIC 收入 $20B+，$73B backlog
- 关键：定制硅的增速比 AMD 更大，因为 NVIDIA 40% 收入来自正在自研芯片的 4 家超大规模客户

### 3. 推理经济学（Inference FinOps）
LLM API 价格暴跌 80% 但 Agentic 工作流让 token 消耗放大 5-30 倍。核心优化手段：
- **多模型路由**: 按请求复杂度分级，用最小够用的模型（减少 20-80% 成本）
- **语义缓存**: 对相似查询返回缓存响应（3-10x 成本节省）
- **量化**: FP16 → INT8/INT4 减少 2-4x 内存，成本减半
- **Blackwell 代际飞跃**: B200 比 H100 成本降低 3x，GB200 比 Hopper 降低 10x
- **去中心化 GPU 网络** (DePIN): Akash/io.net 等比中心化云便宜 70-75%

## 1 个真实案例

**Anthropic 的双栈策略**：同时使用 Google TPU v5p/Trillium 和 AWS Trainium 2，作为对单一供应商（NVIDIA）风险的明确对冲。这是前沿 AI 实验室中最具代表性的多加速器策略——不完全依赖 CUDA，而是让 PyTorch/JAX/vLLM/SGLang 在多个硅后端上运行。这表明：训练仍以 NVIDIA 为主，但推理已经可以通过编译器抽象层（Triton、torch.compile）实现硬件可移植。

## 1 个反直觉点

**NVIDIA 的"威胁"不是 AMD，而是它自己的客户。** 
- NVIDIA 约 40% 的收入来自 4 家正在自研芯片的云巨头（Google、Amazon、Microsoft、Meta）
- 定制 ASIC 增长 44.6% vs GPU 16.1% — 差距在加速扩大
- Google 根本不买 NVIDIA GPU 来跑 Gemini；Meta 不用通用 GPU 服务 30 亿用户
- "客户即竞争对手"是 NVIDIA 面临的最大结构性风险，比 AMD 的性能追赶严重得多

## 和 Tony 当前工作的连接

1. **Hermes Agent 推理成本** — 每次 agent 调用都在消耗 token。理解多模型路由和语义缓存可以直接优化 Hermes 的运行成本
2. **Agent 架构设计** — 三层部署架构（编排层/推理层/执行层）、FinOps 原语（per-agent cost attribution、budget guardrails、anomaly detection）可直接应用于 Hermes 的生产部署优化
3. **技能选择** — 何时用 mini 模型、何时升级到 frontier 模型，应该有明确的路由策略，而不是所有请求都走最强模型
4. **GPU 利用率** — 如果未来需要 self-host 推理，理解 on-prem vs cloud 的经济学断点（~50-83% GPU 利用率时自建集群开始优于云）

## 可实践的小动作

1. **在 Hermes 中实施隐性模型路由** — 至少区分两个 tier：简单分类/格式化用小模型，复杂推理用大模型。这是一个配置变更，不需要代码改动
2. **审计 Hermes 的 token 消费模式** — 统计一周内各 agent 调用的 token 分布，识别浪费
3. **在 skill 中记录「用小模型优先」的默认策略** — 让 Hermes 在技能加载时默认选择最经济的模型
4. **关注云 GPU 定价趋势** — H100 spot 已降至 $0.60-0.90/hr，如果未来需要 GPU 计算，spot 实例是极高性价比的选择

## 是否建议 Codex 深挖

**建议，优先级中等。** 值得 Codex 深挖的方向：
- 为 Hermes 实现一个 token 使用追踪仪表板（per-agent cost attribution）
- 研究 LiteLLM / OpenRouter 集成的可行性，实现多模型路由
- 评估语义缓存在 Hermes 场景下的 ROI（查询重复率有多高？）
- 对比 self-host vs API 的经济学（给定 Tony 的使用量级）

不建议立即行动，但应在下一轮系统优化中纳入评估。

## 来源

1. **Zylos Research**: "Inference Economics: AI Agent Compute Markets in 2026" — https://zylos.ai/research/2026-04-13-inference-economics-ai-agent-compute-markets
2. **Castle Rock Digital**: "The 2026 AI Infrastructure Market Map" — https://www.castlerockdigital.com/insights/ai-infrastructure-market-landscape-2026
3. **Silicon Analysts**: "AMD vs NVIDIA AI GPU Market Share 2026" — https://siliconanalysts.com/analysis/amd-vs-nvidia-ai-gpu-market-share-2026
4. **TrendForce**: "Aggressive Procurement of NVIDIA GB and Rubin Racks... 122% Surge in AI Inference Computing Power" — https://www.trendforce.com/presscenter/news/20260520-13053.html
5. **Presenc AI**: "Hyperscaler Custom Silicon Tracker 2026" — https://presenc.ai/research/hyperscaler-custom-silicon-tracker-2026
6. **Turion AI**: "State of AI Infrastructure 2026: Mid-Year Reality Check" — https://turion.ai/blog/state-of-ai-infrastructure-2026/

---

*由 Hermes 自动生成 | 行业理解 Growth Track | 周一例行任务*
