---
title: Arize Phoenix
type: system
status: learning
tags:
  - ai/system
  - ai/llmops
  - ai/observability
created: 2026-03-26
updated: 2026-03-26
---

# Arize Phoenix

## 它是什么

`Arize Phoenix` 是面向 LLM / agent 的 open-source tracing、evaluation 和 observability 平台。

它最值得注意的点是：它明确把 `OpenTelemetry` 带进了 LLM / agent tracing 语境。

## 为什么它重要

因为很多团队在进入 LLMOps / AgentOps 后，发现原来的模型评测工具不够用了，缺的是：

- trace
- span
- retrieval / tool context
- evaluation over traces
- production debugging

`Phoenix` 就是在补这一层。

## 它最值得抓住的 4 个点

### 1. 它是 tracing-first，而不是 benchmark-first

这意味着它更擅长回答：

- 这次调用链里到底发生了什么
- 哪一步 retrieval / tool / prompt 出了问题
- 线上 regression 来自哪里

### 2. 它把 eval 建在 trace 之上

这很重要。因为 LLM / agent 系统经常不是一个“单输出正确率”问题，而是一个多步系统问题。

### 3. OpenTelemetry 让它更像平台基础设施，而不是单独面板

这使它很适合进入更开放的 observability stack。

### 4. 它更适合 production debugging 和 eval iteration

如果你已经有运行系统，`Phoenix` 很容易成为“为什么这里退化了”的诊断层。

## 在这条学习线上怎么放它

- trace observability
- eval over traces
- retrieval / RAG / agent debugging
- OpenTelemetry-friendly LLMOps layer

## 和 Langfuse / Promptfoo 的关系

- `Phoenix` 更偏 tracing / observability / eval
- `Langfuse` 更偏 prompt、dataset、score、trace、release comparison 的一体化工作台
- `Promptfoo` 更偏 pre-release test / CI / red team

## 推荐继续往下读

- [[Promptfoo]]
- [[Langfuse]]
- [[../../AI-Engineering/07-Topics/Online Evals、Human Feedback 与 Annotation|Online Evals、Human Feedback 与 Annotation]]
- [[../../AI-Engineering/07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]]
- [[../../Cloud-Native/02-Projects/OpenTelemetry|OpenTelemetry]]

## 关联

- [[../06-Topics/MLOps 与 LLMOps|MLOps 与 LLMOps]]
- [[../../AI-Engineering/07-Topics/Evaluation and Benchmarks|Evaluation and Benchmarks]]
- [[../../AI-Engineering/07-Topics/Prompt Registry、Datasets 与 Evals|Prompt Registry、Datasets 与 Evals]]

## 资料

- [Phoenix Docs](https://arize.com/docs/phoenix)
- [Phoenix Tracing Setup](https://arize.com/docs/phoenix/tracing/how-to-tracing/setup-tracing)
- [Phoenix LLM Evals](https://arize.com/docs/phoenix/evaluation/llm-evals)
