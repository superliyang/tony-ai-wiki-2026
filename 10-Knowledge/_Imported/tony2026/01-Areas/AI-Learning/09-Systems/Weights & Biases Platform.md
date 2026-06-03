---
title: Weights & Biases Platform
type: system
status: learning
tags:
  - ai/system
  - ai/mlops
  - ai/wandb
created: 2026-03-26
updated: 2026-03-26
---

# Weights & Biases Platform

## 它是什么

`Weights & Biases` 更像一整套 AI development platform，而不只是 experiment logger。

它至少有三条主线：

- experiments / tracking
- model registry
- `Weave`：LLM / agent tracing、eval 和 application quality 工作台

所以它覆盖的是从 research collaboration 到 LLM application evaluation 的一整条线。

## 为什么它值得单独看

因为它代表了另一种非常典型的平台路径：

- 从研究实验协作切入
- 再把模型注册、比较、artifact 管理接上
- 再进入大模型应用质量与 eval 层

这使它和 `MLflow` 很像，但产品形态更强，也更强调团队协作界面。

## 它最值得抓住的 4 个点

### 1. Experiment Tracking 依然是它的基本盘

如果一个团队训练实验很多、协作很重，`W&B` 很容易成为默认入口。

### 2. Registry 让它不只是研究工具

一旦进入 registry，它就开始进入 release management 语境，而不是只看面板。

### 3. `Weave` 让它进入 LLMOps / AgentOps

`Weave` 很关键，因为它把：

- traces
- evaluations
- datasets
- scorers
- prompt / app quality

接进来了。也就是说，`W&B` 不再只是一套训练实验平台。

### 4. 它很适合“研究 -> 应用”一体化团队

如果一个团队既有模型实验，又有 LLM app / agent app，这条路径会非常自然。

## 在这条学习线上怎么放它

我会把 `Weights & Biases Platform` 理解成：

- 研究协作和实验管理平台
- registry 与 artifact 管理层
- 通过 `Weave` 进入 LLM / agent quality 平台

## 和 MLflow / Langfuse / Phoenix 的关系

- `MLflow` 更偏 open-source 生命周期主线
- `W&B` 更偏 productized team workflow
- `Langfuse` 更偏 LLM / agent prompt、dataset、trace、score 与 release comparison
- `Phoenix` 更偏 open-source observability + eval

## 推荐继续往下读

- [[MLflow]]
- [[Arize Phoenix]]
- [[Promptfoo]]
- [[../../AI-Engineering/07-Topics/Experiment Tracking|Experiment Tracking]]
- [[../../AI-Engineering/07-Topics/Online Evals、Human Feedback 与 Annotation|Online Evals、Human Feedback 与 Annotation]]

## 关联

- [[../06-Topics/MLOps 与 LLMOps|MLOps 与 LLMOps]]
- [[Langfuse]]
- [[../../AI-Engineering/07-Topics/Prompt Registry、Datasets 与 Evals|Prompt Registry、Datasets 与 Evals]]
- [[../../AI-Engineering/07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]]

## 资料

- [W&B Track](https://docs.wandb.ai/models/track)
- [W&B Registry](https://docs.wandb.ai/models/registry)
- [Weave Overview](https://docs.wandb.ai/weave)
- [Weave Evaluation Scorers](https://docs.wandb.ai/weave/guides/evaluation/scorers)
- [What is Weave](https://docs.wandb.ai/weave/concepts/what-is-weave)
