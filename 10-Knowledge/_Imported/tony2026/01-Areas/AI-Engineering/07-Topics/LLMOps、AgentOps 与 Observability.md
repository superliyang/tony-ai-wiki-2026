---
title: LLMOps、AgentOps 与 Observability
type: topic
status: learning
tags:
  - ai/engineering
  - ai/llmops
  - ai/agentops
  - ai/observability
created: 2026-03-26
updated: 2026-03-26
---

# LLMOps、AgentOps 与 Observability

## 先把三个词分开

- `MLOps`：模型生命周期工程
- `LLMOps`：大模型应用生命周期工程
- `AgentOps`：多步执行、tool use、memory、approval 和 long-running workflow 的运营工程

所以 `AgentOps` 更像是 `LLMOps` 在 action systems 里的延伸，而不是完全独立的新宇宙。

## 为什么 observability 会变成核心

因为在 agent / LLM 系统里，你不再只需要看：

- request latency
- error rate

你还要看：

- prompt version
- session / thread
- tool call tree
- retrieval context
- scores / eval result
- user feedback
- approval / interrupt event

这使得可观测性从“补充项”变成平台主干。

## 这一层通常由什么组成

### 1. Trace Layer

- model call spans
- tool spans
- retrieval spans
- session / thread aggregation

### 2. Evaluation Layer

- offline eval
- online eval
- model-graded scoring
- human review overlays

### 3. Release Layer

- prompt / model / agent version
- dataset run comparison
- canary / rollout decision

### 4. Reliability Layer

- regression detection
- failure clustering
- alerting / issue triage

## 常见平台怎么分工

- `Langfuse`：prompt、trace、dataset、scores、release comparison
- `Phoenix`：observability、OpenTelemetry-friendly traces、eval debugging
- `Promptfoo`：pre-release eval / CI / red team
- `MLflow`：tracking、registry、prompt registry、lifecycle governance

## 为什么很多团队卡在这里

- 只有 traces，没有稳定的 eval set
- 只有 eval，没有 trace 诊断能力
- 只有 observability，没有 release gate
- 只有人工 review，没有 dataset 回流

## 学习这页最该记住什么

- `AgentOps` 不是“agent 多了一个 ops 团队”
- 它本质上是在 `LLMOps` 里增加：action surface、trust boundary、approval 和 long-running state

## 关联

- [[Online Evals、Human Feedback 与 Annotation]]
- [[Prompt Registry、Datasets 与 Evals]]
- [[../../AI-Learning/06-Topics/MLOps 与 LLMOps|MLOps 与 LLMOps]]
- [[../../AI-Learning/09-Systems/Langfuse|Langfuse]]
- [[../../AI-Learning/09-Systems/Arize Phoenix|Arize Phoenix]]
- [[../../AI-Learning/09-Systems/Promptfoo|Promptfoo]]
- [[../../Cloud-Native/02-Projects/OpenTelemetry|OpenTelemetry]]
- [[MCP 与 CLI 模式]]
- [[Agent Security、Sandbox 与 Approval Architecture]]
- [[Long-Running Agent Operations]]
