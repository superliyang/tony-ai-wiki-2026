---
title: Prompt Registry、Datasets 与 Evals
type: topic
status: learning
tags:
  - ai/engineering
  - ai/llmops
created: 2026-03-26
updated: 2026-03-26
---

# Prompt Registry、Datasets 与 Evals

## 为什么它会变成单独一层

在传统 `MLOps` 里，团队主要治理的是：

- data
- code
- model artifact

但到了 `LLMOps`，还必须治理：

- prompt version
- eval dataset
- rubric / scorer
- retrieval context shape
- tool schema

这意味着 prompt 已经不只是“字符串”，而是发布资产的一部分。

## 这一层真正要解决的问题

- 哪个 prompt 版本正在生产中
- 哪套 eval dataset 能代表真实任务
- 哪个 scorer / rubric 负责判断退化
- prompt、dataset、trace 和 release gate 如何关联

## 一个成熟团队会把这层拆成什么

### 1. Prompt Registry

要能回答：

- prompt 是哪版
- 谁改的
- 为什么改
- 它绑定了哪些模型参数和上下文约定

### 2. Eval Datasets

要区分：

- smoke set
- regression set
- domain set
- adversarial set
- human-labeled set

### 3. Eval Execution

要知道：

- 离线跑哪套
- CI 跑哪套
- staging 跑哪套
- production 线上抽样怎么跑

## 常见平台怎么分工

- `MLflow`：prompt registry + lifecycle metadata
- `Weights & Biases / Weave`：prompt / dataset / scorer 组合式工作台
- `Langfuse`：prompt management + dataset + scores + traces
- `Promptfoo`：pre-release eval / CI / red team

## 这一层为什么经常出问题

- prompt 有版本，dataset 没版本
- dataset 有版本，scorer 在代码里偷偷变了
- regression set 太小，看不出真实退化
- 只做 benchmark，不做任务集
- 只做离线，不做上线后的采样复核

## 学习这页最该记住什么

- prompt 是资产
- dataset 是资产
- scorer 也是资产
- 只有把三者一起治理，release gate 才可信

## 关联

- [[Experiment Tracking]]
- [[Evaluation and Benchmarks]]
- [[Model Registry and Deployment]]
- [[Online Evals、Human Feedback 与 Annotation]]
- [[../04-Evaluation/评测索引|评测索引]]
- [[../../AI-Learning/09-Systems/MLflow|MLflow]]
- [[../../AI-Learning/09-Systems/Weights & Biases Platform|Weights & Biases Platform]]
- [[../../AI-Learning/09-Systems/Langfuse|Langfuse]]
- [[../../AI-Learning/09-Systems/Promptfoo|Promptfoo]]
