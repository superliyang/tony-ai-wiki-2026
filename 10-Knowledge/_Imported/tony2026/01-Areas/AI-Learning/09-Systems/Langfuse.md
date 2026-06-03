---
title: Langfuse
type: system
status: learning
tags:
  - ai/system
  - ai/langfuse
  - ai/observability
created: 2026-03-25
updated: 2026-03-25
---

# Langfuse

## 它是什么

`Langfuse` 更接近一个 `LLM engineering platform` 或 `agent observability platform`。

如果说：

- `LangGraph` 更像执行内核
- `ADK` 更像 agent framework / interoperability layer

那 `Langfuse` 更像：

- tracing / observation
- prompt management
- eval / scoring
- experiment / regression
- self-hosted control surface

## 为什么它在 Agent 平台里特别关键

很多团队先把 agent 跑起来，过一阵子才发现真正难的是：

- 我到底看到了什么 trace
- 哪个 tool span 出错
- 哪个 prompt version 退化了
- 哪个 workflow 失败率变高
- 哪个 release 引入了 regression

`Langfuse` 就是用来承接这些问题的一层。

## 它最值得抓住的 4 个点

### 1. 它不是单纯日志，而是围绕 LLM / agent 语义建的观测层

这和普通 APM 不一样。agent 平台需要看到的不只是 HTTP latency，而是：

- prompt
- model call
- tool use
- trace tree
- score / eval
- artifacts / sessions 的关联

### 2. Self-hosting 对很多团队很重要

官方 `self-hosting` 文档把 Kubernetes / Helm / Terraform 等部署方式写得很明确。这意味着它不是只能作为 SaaS 用，而是能进入更受控的企业环境。

### 3. 它天然适合放进 LangChain / LangGraph 生态

官方有 `LangChain Tracing` 文档。这让它在 `LangGraph` 场景下很自然，因为你可以把 runtime trace 和平台 eval / prompt 管理串起来。

### 4. 它更像平台的“看”和“评”，不是“跑”

这点很重要。

`Langfuse` 很关键，但它不是执行 runtime。

所以在平台里，它更应该放在：

- `observability layer`
- `prompt / experiment layer`
- `eval and regression layer`

而不是被误当成运行内核。

## 在 Agent 平台里，我会怎么放它

如果要做 `agent platform`，我通常会从第一天就把 `Langfuse` 接进来，至少覆盖：

- trace
- prompt version
- score / evaluator
- release comparison
- regression suite input

因为这些东西后补会非常痛。

## 一个现实判断

对很多平台团队来说，`Langfuse` 的价值不在“让 demo 更酷”，而在让平台开始具备：

- 可调试性
- 可解释性
- 可回归
- 可发布治理

## 它和 Harness Engineering 的关系

- `Harness Engineering` 更偏工作台结构
- `Langfuse` 更偏这个工作台上的观测、评分与版本控制面

所以它们不是替代关系，而是互补关系。

## 推荐继续往下读

- [[LangGraph]]
- [[Google Agent Development Kit（ADK）]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
- [[../../AI-Engineering/07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]]
- [[../../AI-Engineering/07-Topics/Agent 平台架构（LangGraph、Langfuse、ADK）|Agent 平台架构（LangGraph、Langfuse、ADK）]]

## 关联

- [[../06-Topics/Agent 平台|Agent 平台]]
- [[LangGraph]]
- [[Google Agent Development Kit（ADK）]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
- [[../../AI-Engineering/07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]]
- [[../../AI-Engineering/07-Topics/Agent Evaluation and Reliability|Agent Evaluation and Reliability]]
- [[../../AI-Engineering/07-Topics/Task Success and Failure Recovery|Task Success and Failure Recovery]]
- [[../../AI-Engineering/07-Topics/Agent 平台架构（LangGraph、Langfuse、ADK）|Agent 平台架构（LangGraph、Langfuse、ADK）]]

## 资料

- [Langfuse Self-Hosting](https://langfuse.com/docs/self-hosting)
- [Langfuse LangChain Tracing](https://langfuse.com/docs/integrations/langchain/tracing)
- [Langfuse Docs](https://langfuse.com/docs)
