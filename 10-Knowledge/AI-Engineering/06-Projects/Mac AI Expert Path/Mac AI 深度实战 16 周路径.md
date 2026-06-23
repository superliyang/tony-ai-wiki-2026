---
title: Mac AI 深度实战 16 周路径
status: learning
created: 2026-06-21
updated: 2026-06-21
tags:
  - knowledge
  - ai-engineering
  - mac-ai-lab
  - learning-path
---

# Mac AI 深度实战 16 周路径

这条 16 周路径是 [[Mac AI 深度实战学习总纲]] 的执行版。目标不是每天打卡，而是每周形成一个可复现产物。

## Week 1：实验室与学习闭环

问题：我的 Mac 是否已经是一个可复现实验环境？

任务：

- 完成 [[第 0 章实操：把 Mac 变成 AI 实验室]]。
- 建立实验目录和记录习惯。
- 跑通 `PyTorch MPS`、`Ollama`、`MLX-LM` 至少两条链路。

产物：

- 环境记录。
- 第一次 [[Mac AI 实验记录模板|实验记录]]。

## Week 2：Token、Sampling 与本地推理

问题：为什么同一个模型、不同参数，输出会不同？

任务：

- 跑 [[第 1 章实操：本地推理对比实验]]。
- 对比 temperature、top-p、context length。
- 记录 5 个 bad cases。

产物：

- sampling 参数观察表。
- 本地模型体感记录。

## Week 3：llama.cpp、GGUF 与量化

问题：模型格式和量化为什么会影响速度、内存和质量？

任务：

- 用 `llama.cpp` 或现成 GGUF 模型做量化对比。
- 比较至少 2 个量化版本。
- 记录内存、速度、质量差异。

产物：

- GGUF / quantization 选型表。

## Week 4：PyTorch MPS 与最小训练循环

问题：训练到底发生了什么？

任务：

- 完成 [[第 2 章实操：PyTorch MPS 最小训练实验]]。
- 手写 forward / loss / backward / optimizer。
- 对比 CPU 与 MPS。

产物：

- 最小训练脚本。
- CPU vs MPS 观察笔记。

## Week 5：Transformer 最小理解

问题：attention 和 next-token prediction 如何连接？

任务：

- 读 [[10-Knowledge/AI-Engineering/07-Topics/Training Stack Overview]] 和 [[10-Knowledge/AI-Engineering/07-Topics/Tokenization]]。
- 跑一个 tiny transformer / nanoGPT 级实验，或至少画出数据流。
- 解释 logits、loss、sampling、KV cache。

产物：

- “text -> token -> logits -> text” 数据流笔记。

## Week 6：MLX 与 Apple Silicon 原生路线

问题：为什么 Mac 上不能只学 PyTorch MPS？

任务：

- 完成 [[第 3 章实操：MLX-LM 原生推理与最小 LoRA 实验]] 的推理部分。
- 对比 `MLX-LM` 与 `Ollama`。
- 记录 unified memory 的优势和限制。

产物：

- MLX vs Ollama vs PyTorch MPS 对比表。

## Week 7：数据集与任务定义

问题：什么样的数据值得拿去微调？

任务：

- 选一个真实小任务，例如 Obsidian 笔记分类、技术问答、支付术语解释、代码审查摘要。
- 做 20-100 条样本。
- 划分 train / eval / bad-case。

产物：

- dataset card。
- eval prompts 初版。

## Week 8：LoRA / SFT 第一次闭环

问题：微调有没有真的改变模型行为？

任务：

- 完成 [[第 4 章实操：微调评测与 Failure Analysis]] 的最小 LoRA / SFT。
- 先跑 baseline，再跑 tuned。
- 对比固定 eval set。

产物：

- baseline vs tuned 表。
- failure analysis。

## Week 9：评测、坏例子与回归

问题：怎么不靠感觉判断模型？

任务：

- 扩展 eval set。
- 给 bad cases 分类。
- 标注哪些问题来自数据、prompt、模型、runtime、任务定义。

产物：

- eval scorecard。
- bad-case library。

## Week 10：本地 RAG

问题：什么时候该微调，什么时候该 RAG？

任务：

- 选一批本地文档。
- 做 chunking、embedding、retrieval。
- 对比检索失败和生成失败。

产物：

- 本地 RAG demo。
- retrieval failure report。

## Week 11：本地 Agent 与工具边界

问题：Agent 的能力和风险来自哪里？

任务：

- 做一个本地 agent，至少接 2 个工具。
- 记录 tool call trace。
- 设计 approval boundary。

产物：

- agent prototype。
- tool safety notes。

## Week 12：Observability 与 Eval Gate

问题：如果这个系统持续运行，怎么知道它变差了？

任务：

- 给 RAG / agent 加日志。
- 固定一组回归测试。
- 写最小 release gate。

产物：

- eval gate checklist。
- trace 样例。

## Week 13：本地 Serving

问题：怎么把实验变成一个别人能调用的服务？

任务：

- 包装一个本地 API 或 CLI。
- 加配置、README、错误处理。
- 记录延迟、内存、并发边界。

产物：

- local serving prototype。
- 使用说明。

## Week 14：部署与成本

问题：本地可用和生产可用差在哪里？

任务：

- 读 [[10-Knowledge/AI-Engineering/05-Deployment/部署索引]]。
- 画出本地原型迁移到云上的部署图。
- 估算 latency、throughput、GPU、cache、fallback。

产物：

- serving architecture draft。

## Week 15：安全、权限与数据边界

问题：模型接触真实工具和数据后，风险在哪里？

任务：

- 对照 [[10-Knowledge/Security/03-Industry-Controls/MCP Server 安全控制清单]] 和 [[10-Knowledge/Security/03-Industry-Controls/AI Coding Agent 安全控制清单]]。
- 给本地 agent 做权限边界设计。

产物：

- AI app security checklist。

## Week 16：总复盘与作品集

问题：我现在真的具备哪些 AI 工程能力？

任务：

- 整理 3 个最有价值的实验。
- 写一份“从 Mac 实验室到云上系统”的总设计。
- 更新 [[Mac AI 专家验收清单]]。

产物：

- 作品集 README。
- 16 周学习复盘。

## 完成标准

完成这条路线，不是看完 16 篇文章，而是至少留下：

- 8 份实验记录。
- 1 个最小训练脚本。
- 1 个 runtime / quantization 对比。
- 1 个 LoRA / SFT 实验。
- 1 个 eval set 和 bad-case library。
- 1 个 RAG 或 agent 原型。
- 1 份云上迁移设计文档。

