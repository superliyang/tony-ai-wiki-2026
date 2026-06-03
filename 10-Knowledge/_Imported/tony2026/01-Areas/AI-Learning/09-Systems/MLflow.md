---
title: MLflow
type: system
status: learning
tags:
  - ai/system
  - ai/mlops
  - ai/mlflow
created: 2026-03-26
updated: 2026-03-26
---

# MLflow

## 它是什么

`MLflow` 是最经典的 open-source `MLOps` 平台之一。

它最核心的几层能力是：

- experiment tracking
- model registry
- evaluation
- tracing（GenAI / agent 场景）
- prompt registry（GenAI 场景）

所以它不是单独某一个点工具，而是一条从实验到发布的治理主线。

## 为什么它在这条学习线上很重要

因为它代表的是一种很强的工程观：

- run 要可追溯
- model 要可注册
- prompt 要可版本化
- eval 要能和 release gate 连起来

也就是说，`MLflow` 不是在帮你“记日志”，而是在帮你把模型资产标准化。

## 它最值得抓住的 4 个点

### 1. Tracking 是它的入口，但不是它的终点

很多人对 `MLflow` 的第一印象是 experiment tracking。这个没错，但如果只停在 tracking，就低估它了。

它真正重要的是：tracking 能和 registry、evaluate、prompt registry 连起来。

### 2. Model Registry 让实验资产开始变成发布资产

一旦进入 registry，团队讨论的就不是“某个 run 看起来不错”，而是：

- 哪个 version 可以进入 `staging`
- 哪个 version 可以 `promote`
- 哪个 version 可以 `rollback`

### 3. Prompt Registry 说明它已经进入 LLMOps 语境

这很关键。因为大模型应用里，真正需要治理的不只有模型权重，还有 prompt 本身。

### 4. 它仍然更偏“资产治理主线”，不是完整 agent 平台

`MLflow` 很强，但它不是：

- end-user channel product
- human approval runtime
- full agent orchestration layer

所以它更适合放在：

- experiment system
- registry system
- evaluation and release-gate system

## 在 LLMOps 里我会怎么放它

- 训练 / fine-tuning 实验追踪
- evaluation artifact 管理
- model / prompt version registry
- release gate metadata source of truth

## 和 Langfuse / Phoenix / Promptfoo 的关系

- `MLflow`：更像资产与生命周期治理主线
- `Langfuse`：更像 LLM / agent prompt、trace、dataset、score 和 release 对比平台
- `Phoenix`：更像 tracing / eval / observability
- `Promptfoo`：更像 pre-release eval / CI / red team harness

## 推荐继续往下读

- [[Weights & Biases Platform]]
- [[Arize Phoenix]]
- [[Promptfoo]]
- [[../../AI-Engineering/07-Topics/Experiment Tracking|Experiment Tracking]]
- [[../../AI-Engineering/07-Topics/Model Registry and Deployment|Model Registry and Deployment]]
- [[../../AI-Engineering/07-Topics/Prompt Registry、Datasets 与 Evals|Prompt Registry、Datasets 与 Evals]]

## 关联

- [[../06-Topics/MLOps 与 LLMOps|MLOps 与 LLMOps]]
- [[Langfuse]]
- [[../../AI-Engineering/07-Topics/Evaluation and Benchmarks|Evaluation and Benchmarks]]
- [[../../AI-Engineering/07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]]

## 资料

- [MLflow Tracking](https://mlflow.org/docs/latest/ml/tracking/)
- [MLflow Model Registry](https://mlflow.org/docs/latest/ml/model-registry/)
- [MLflow Prompt Registry](https://mlflow.org/docs/latest/genai/prompt-registry/)
- [MLflow Tracing](https://mlflow.org/docs/latest/genai/tracing/)
- [MLflow Evaluate and Monitor](https://mlflow.org/docs/latest/genai/eval-monitor/)
