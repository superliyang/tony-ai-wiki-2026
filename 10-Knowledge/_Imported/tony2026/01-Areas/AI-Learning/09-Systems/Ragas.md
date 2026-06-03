---
title: Ragas
type: system
status: learning
tags:
  - ai/system
  - ai/evals
  - ai/ragas
created: 2026-04-14
updated: 2026-04-14
---

# Ragas

## 它是什么

`Ragas` 是一个面向 `RAG` 和 `agent / tool-use` 场景的开源评估框架。

它最值得注意的地方，不只是“能打分”，而是把下面几层收进了同一套工作流：

- evaluation metrics
- evaluation datasets
- testset generation
- multi-turn evaluation
- agent / tool-use case evaluation

## 为什么它重要

很多团队卡住，不是因为没有 trace，而是：

- 不知道该用什么指标
- 没有足够像真的测试集
- judge 模型和任务结构没有统一组织

`Ragas` 正在补这层。

## 它最值得抓住的 4 个点

### 1. 它不是 observability 平台，而是 metric 与 dataset 工具层

这意味着它更适合：

- 设计评估指标
- 构造或生成评估集
- 跑多轮或 agent 场景评估

而不是直接替代线上 tracing 平台。

### 2. 它对 `RAG` 和 `agent / tool use` 都有明确入口

官方文档把：

- `RAG evaluation`
- `testset generation`
- `agents or tool use cases`

都放成了独立使用路径。

### 3. 它特别适合“从真实任务往回长出测试集”

如果你已经知道哪些任务容易坏，`Ragas` 很适合把这些任务逐步变成：

- evaluation dataset
- reusable metrics
- synthetic long-tail cases

### 4. 它适合和 tracing / release 工具组合

它自己不是完整 AgentOps 平台，更像：

- `metric library`
- `testset generation engine`
- `evaluation runner`

所以常见组合会更像：

- `Ragas + Langfuse`
- `Ragas + Phoenix`
- `Ragas + Promptfoo`

## 在 Agent 效果评估这条线上怎么放它

- 用它定义和运行 `quality metrics`
- 用它生成 `agent / tool-use` 测试样本
- 用它补齐多轮、语义型 judge 的评估层

## 它不解决什么

- 它不是主要的 production tracing 平台
- 它不是完整 release governance 工作台
- 它不是 registry / deployment 底座

## 推荐继续往下读

- [[../../AI-Engineering/07-Topics/Agent 效果评估：方法论、开源工具与判断框架|Agent 效果评估：方法论、开源工具与判断框架]]
- [[../../AI-Engineering/07-Topics/Agent Evaluation and Reliability|Agent Evaluation and Reliability]]
- [[../../AI-Engineering/07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]]
- [[Langfuse]]
- [[Arize Phoenix]]
- [[Promptfoo]]

## 关联

- [[../06-Topics/MLOps 与 LLMOps|MLOps 与 LLMOps]]
- [[../../AI-Engineering/07-Topics/Evaluation and Benchmarks|Evaluation and Benchmarks]]
- [[../../AI-Engineering/07-Topics/Prompt Registry、Datasets 与 Evals|Prompt Registry、Datasets 与 Evals]]
- [[../../AI-Engineering/07-Topics/Agent 效果评估：方法论、开源工具与判断框架|Agent 效果评估：方法论、开源工具与判断框架]]

## 资料

- [Ragas Docs](https://docs.ragas.io/en/stable/)
