---
title: Promptfoo
type: system
status: learning
tags:
  - ai/system
  - ai/evals
  - ai/promptfoo
created: 2026-03-26
updated: 2026-03-26
---

# Promptfoo

## 它是什么

`Promptfoo` 是一个很典型的 `LLM app testing / eval / red teaming` 工具链。

它特别适合回答这种问题：

- 这次 prompt / model / RAG 变更是不是退化了
- 我能不能把 eval 放进 CI
- 我能不能在上线前做一轮 red team

## 为什么它值得单独看

因为它代表的是一条很实际的工程路径：

- 不先做大而全平台
- 先把测试、断言、模型评分和 red team 建起来
- 让 prompt / RAG / agent 变更能进入正常工程流程

## 它最值得抓住的 4 个点

### 1. 它是 pre-release quality gate 工具

这意味着它特别适合放在：

- CI
- regression test
- prompt comparison
- red-team quick checks

### 2. 它强调配置化测试

这对于把 LLM evaluation 变成团队流程很有帮助，因为测试定义不必都写死在代码里。

### 3. 它能用 model-graded assertions

这让它比传统字符串断言更适合自然语言系统。

### 4. 它不等于完整 observability 平台

`Promptfoo` 很强，但它不负责长期 production trace 或 full experiment registry。

所以它更适合：

- pre-release eval harness
- CI / regression / red-team layer

## 在这条学习线上怎么放它

- prompt regression
- RAG regression
- agent test harness
- red team test pack

## 和 Phoenix / Langfuse / MLflow 的关系

- `Promptfoo`：pre-release tests 与 red-team
- `Phoenix`：trace + eval + debugging
- `Langfuse`：prompt / trace / dataset / score / release comparison
- `MLflow`：tracking / registry / prompt registry / lifecycle governance

## 推荐继续往下读

- [[Arize Phoenix]]
- [[Langfuse]]
- [[../../AI-Engineering/07-Topics/Prompt Registry、Datasets 与 Evals|Prompt Registry、Datasets 与 Evals]]
- [[../../AI-Engineering/07-Topics/Online Evals、Human Feedback 与 Annotation|Online Evals、Human Feedback 与 Annotation]]
- [[../../AI-Engineering/07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]]

## 关联

- [[../06-Topics/MLOps 与 LLMOps|MLOps 与 LLMOps]]
- [[../../AI-Engineering/07-Topics/Evaluation and Benchmarks|Evaluation and Benchmarks]]
- [[../../AI-Engineering/07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]

## 资料

- [Promptfoo Intro](https://www.promptfoo.dev/docs/intro/)
- [Promptfoo Configuration Guide](https://www.promptfoo.dev/docs/configuration/guide/)
- [Promptfoo Model-Graded Assertions](https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/)
- [Promptfoo Red Team Quickstart](https://www.promptfoo.dev/docs/red-team/quickstart/)
