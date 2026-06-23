---
title: Mac AI 深度实战学习总纲
status: learning
created: 2026-06-21
updated: 2026-06-21
tags:
  - knowledge
  - ai-engineering
  - mac-ai-lab
  - learning-path
---

# Mac AI 深度实战学习总纲

这条路线不是“会调用 LLM API”，而是把 `Mac` 当成本地 AI 实验室，系统建立 5 类能力：

1. **模型原理**：tokenizer、embedding、attention、transformer、loss、sampling。
2. **训练能力**：tensor、autograd、optimizer、dataset、batching、训练稳定性。
3. **微调能力**：LoRA、QLoRA、PEFT、SFT、数据构造、baseline、failure analysis。
4. **推理与部署能力**：Ollama、llama.cpp、GGUF、quantization、MLX-LM、serving、latency、memory。
5. **系统能力**：RAG、agent、eval、observability、release gate、从本地原型到云上系统。

## 学习边界

### 这条路线要学什么

- 能解释模型为什么这样工作，而不是只记 API。
- 能写最小训练循环，而不是只运行别人 notebook。
- 能做一次小规模 LoRA / SFT，并判断它有没有真的变好。
- 能比较 `Ollama`、`llama.cpp`、`MLX-LM`、`PyTorch MPS` 的边界。
- 能把本地实验翻译成生产系统设计：serving、评测、监控、安全、成本。

### 这条路线不追求什么

- 不在 Mac 上假装做 frontier-scale pretraining。
- 不把“调用云端大模型 API”当成核心实战。
- 不堆工具名；每个工具都必须回答一个工程问题。
- 不用一次性大而全项目替代每周可验证的实验闭环。

## 能力地图

| 层 | 你要理解的问题 | 必做实验 | 产物 |
|---|---|---|---|
| Model Basics | token 怎么变成向量，模型怎么预测下一个 token | 手写 tokenizer / sampling 小实验 | 原理笔记 + 小脚本 |
| Transformer Core | attention、MLP、residual、layer norm 为什么能工作 | 跑一个 tiny transformer 或 nanoGPT 级训练 | 训练曲线 + failure notes |
| Training Loop | loss、backward、optimizer、batch size、overfit 怎么互动 | PyTorch MPS 最小训练 | CPU vs MPS 对比 |
| Local Inference | runtime、量化、上下文、sampling 怎么影响体验 | Ollama / llama.cpp / MLX-LM 对比 | runtime 选型表 |
| Data & SFT | 什么数据值得进入训练集，怎么拆 train/eval/bad-case | 20-100 条小数据集 | dataset card |
| LoRA / PEFT | 为什么只训练 adapter 能改变行为 | MLX-LM 或 PEFT 跑一次 LoRA | baseline vs tuned |
| Evaluation | 怎么不靠感觉判断模型变好 | 固定 eval prompts + bad cases | eval set + scorecard |
| RAG | 模型能力和外部知识怎么组合 | 本地文档问答 | retrieval failure report |
| Agent | tools、memory、approval、trace 怎么组成 agent | 本地 agent + 2 个工具 | tool-call trace |
| Deployment | 本地原型怎么走向服务 | 本地 API / UI + README | serving design |
| Cloud Mapping | 哪些东西必须上云，怎么估算成本和风险 | 云上迁移设计 | architecture tradeoff |

## 推荐学习顺序

### Phase 0：先把实验室建稳

入口：

- [[Mac AI 工作台：从今天开始]]
- [[第 0 章：环境与工具链搭建]]
- [[第 0 章实操：把 Mac 变成 AI 实验室]]

目标：

- `Python / uv / git` 可复现。
- `PyTorch MPS` 可用。
- `Ollama` 可用。
- `MLX-LM` 可用。
- 每次实验都复制 [[Mac AI 实验记录模板]]。

### Phase 1：模型工作原理

目标不是背 transformer，而是能解释一条文本如何变成模型输出：

```text
text -> tokens -> embeddings -> attention blocks -> logits -> sampling -> text
```

必学主题：

- tokenizer 和 vocabulary
- embedding 与 positional information
- attention、KV cache、context window
- logits、temperature、top-p、top-k
- loss、perplexity、next-token prediction

推荐连接：

- [[10-Knowledge/AI-Engineering/07-Topics/Tokenization]]
- [[10-Knowledge/AI-Engineering/07-Topics/Training Stack Overview]]
- [[10-Knowledge/AI-Engineering/07-Topics/KV Cache、Prefill-Decode 与 Continuous Batching]]

### Phase 2：训练基础

这一步必须亲手写训练循环。会推理不代表理解训练。

必学主题：

- tensor shape
- forward / loss / backward / optimizer
- dataset / dataloader / batching
- learning rate、gradient、overfit
- CPU / MPS 差异和 fallback

推荐连接：

- [[第 2 章：PyTorch MPS 与训练基础]]
- [[第 2 章实操：PyTorch MPS 最小训练实验]]
- [[10-Knowledge/AI-Engineering/07-Topics/PyTorch MPS 实战]]

### Phase 3：本地推理、量化与 runtime

这一步要把“模型能跑”拆成格式、runtime、量化、内存、速度、质量。

必学主题：

- `Ollama`：最快接应用。
- `llama.cpp`：理解 GGUF、quantization、server 和底层参数。
- `MLX-LM`：Apple silicon 原生推理和微调。
- sampling、上下文长度、batch、KV cache。

推荐连接：

- [[第 1 章：本地推理与模型运行]]
- [[第 1 章实操：本地推理对比实验]]
- [[10-Knowledge/AI-Engineering/07-Topics/本地 LLM 工具链：Ollama、llama-cpp、MLX-LM]]
- [[10-Knowledge/AI-Engineering/07-Topics/MLX 与 Apple Silicon 原生大模型实践]]

### Phase 4：数据、SFT、LoRA 与评测

这是从“玩模型”进入“改变模型行为”的关键阶段。

必学主题：

- task definition
- dataset curation
- train / eval / bad-case split
- LoRA、QLoRA、PEFT、SFT
- baseline、tuned、regression
- overfit、prompt leakage、catastrophic forgetting

推荐连接：

- [[第 4 章：微调、LoRA 与评测]]
- [[第 4 章实操：微调评测与 Failure Analysis]]
- [[10-Knowledge/AI-Engineering/07-Topics/Mac 本地微调：LoRA、QLoRA 与 MLX-LM]]
- [[10-Knowledge/AI-Engineering/07-Topics/Prompt Registry、Datasets 与 Evals]]
- [[10-Knowledge/AI-Engineering/04-Evaluation/评测索引]]

### Phase 5：RAG、Agent 与系统化应用

模型能力要进入系统，不能停留在 notebook。

必学主题：

- chunking、embedding、retrieval、rerank
- answer grounding 和 citation
- tools、schema、memory、approval
- trace、eval、observability
- prompt injection 和 tool safety

推荐连接：

- [[第 5 章：RAG、Agent 与本地应用开发]]
- [[第 5 章实操：本地 RAG 与 Agent Prototype]]
- [[10-Knowledge/AI-Engineering/07-Topics/Agent Runtime Architecture]]
- [[10-Knowledge/AI-Engineering/07-Topics/Prompt Injection Defense 与 Tool Safety]]
- [[10-Knowledge/Security/03-Industry-Controls/AI Coding Agent 安全控制清单]]

### Phase 6：部署、云上映射与工程判断

最后要能回答：如果这个原型给团队用，会变成什么系统？

必学主题：

- serving API
- latency、throughput、memory、cost
- model routing、fallback、cache
- observability、eval gate、release gate
- security boundary、secret、data access
- 本地能力到云上架构的迁移

推荐连接：

- [[第 6 章：从 Mac 实验室到云上系统]]
- [[第 6 章实操：从本地原型到云上系统设计]]
- [[10-Knowledge/AI-Engineering/05-Deployment/部署索引]]
- [[10-Knowledge/AI-Engineering/07-Topics/Serving and Scaling]]
- [[10-Knowledge/AI-Engineering/07-Topics/Runtime 发布门槛、灰度与 Blast Radius 控制]]

## 每周学习节奏

每周只做 4 件事：

1. **读一个核心主题**：不是泛读资料，而是回答一个问题。
2. **跑一个实验**：必须能复现。
3. **写一份实验记录**：包括 bad cases。
4. **更新一条判断**：例如“什么时候用 MLX-LM，什么时候不用”。

## 第一轮学习建议

不要从微调开始。第一轮应该这样走：

1. [[第 0 章实操：把 Mac 变成 AI 实验室]]
2. [[第 1 章实操：本地推理对比实验]]
3. [[第 2 章实操：PyTorch MPS 最小训练实验]]
4. [[第 3 章实操：MLX-LM 原生推理与最小 LoRA 实验]]
5. [[第 4 章实操：微调评测与 Failure Analysis]]

这 5 步跑完，你就不是“会调 API”，而是已经有模型、训练、推理、微调和评测的身体经验。

## 官方资料入口

- [Apple: Accelerated PyTorch training on Mac](https://developer.apple.com/metal/pytorch/)
- [PyTorch MPS backend](https://docs.pytorch.org/docs/stable/notes/mps.html)
- [MLX GitHub](https://github.com/ml-explore/mlx)
- [MLX-LM GitHub](https://github.com/ml-explore/mlx-lm)
- [llama.cpp GitHub](https://github.com/ggml-org/llama.cpp)
- [Hugging Face GGUF](https://huggingface.co/docs/hub/en/gguf)
- [Hugging Face PEFT](https://huggingface.co/docs/peft/en/index)
- [Hugging Face LoRA](https://huggingface.co/docs/peft/package_reference/lora)

