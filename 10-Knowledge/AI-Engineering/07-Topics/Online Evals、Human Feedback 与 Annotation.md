---
title: Online Evals、Human Feedback 与 Annotation
type: topic
status: learning
tags:
  - ai/engineering
  - ai/llmops
  - ai/evals
created: 2026-03-26
updated: 2026-03-26
---

# Online Evals、Human Feedback 与 Annotation

## 为什么离线 eval 还不够

离线 eval 能告诉你“这个版本看起来更好”，但线上系统经常因为这些因素失真：

- 用户输入分布变了
- tool / retrieval 质量在变化
- UI、latency、fallback、guardrail 影响了体验
- benchmark 只覆盖了你以为重要的那部分

所以真正成熟的 `LLMOps` 必须把在线反馈闭环建起来。

## 这一层最核心的 4 个问题

### 1. 线上到底要抽什么样本

不是所有流量都要标注，但要有：

- high-risk sample
- disagreement sample
- low-confidence sample
- business-critical sample

### 2. 谁来打标

常见三层：

- model-graded / rule-based scoring
- ops / analyst review
- domain expert review

### 3. 标注结果怎么回流

如果 annotation 不能回流到 dataset、prompt 和 release gate，这层就会退化成“看过了，但没形成系统学习”。

### 4. 指标怎么避免被 vanity numbers 污染

要把：

- task success
- human preference
- business outcome
- failure pattern

一起看，而不是只看平均分。

## 常见平台怎么分工

- `Langfuse`：trace、scores、dataset runs、prompt comparison
- `Phoenix`：production tracing + eval + debugging
- `W&B / Weave`：scorers、comparison、application quality
- `OpenTelemetry`：把 trace 带进更大 observability stack

## 这层为什么很难

- 线上样本天然脏
- 人审成本高
- 自动 judge 会漂移
- annotation taxonomy 很容易失控
- 很多团队只做“收 feedback”，不做“把 feedback 变成 release decision”

## 学习这页最该记住什么

- 线上反馈不是附加项，而是 `LLMOps` 真正开始成熟的标志
- annotation 不是目的，能否回流到 prompt / dataset / release gate 才是重点

## 关联

- [[Evaluation and Benchmarks]]
- [[Prompt Registry、Datasets 与 Evals]]
- [[LLMOps、AgentOps 与 Observability]]
- [[../../AI-Learning/09-Systems/Langfuse|Langfuse]]
- [[../../AI-Learning/09-Systems/Arize Phoenix|Arize Phoenix]]
- [[../../AI-Learning/09-Systems/Weights & Biases Platform|Weights & Biases Platform]]
- [[../../Cloud-Native/02-Projects/OpenTelemetry|OpenTelemetry]]
