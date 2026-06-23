---
title: Experiment Tracking
type: topic
status: learning
tags:
  - ai/engineering
  - ai/mlops
created: 2026-03-13
updated: 2026-03-26
---

# Experiment Tracking

## 为什么重要

- 大模型工程里最容易丢的是“这次到底为什么有效”
- 实验跟踪是复现、比较和协作的基础设施
- 在 `LLMOps` 里，它还要继续承接 prompt、dataset、trace 和 eval lineage

## 系统视角

实验跟踪解决的不是“把日志记下来”，而是把一次实验变成一个可比较、可复现、可移交的工程对象。一个完整实验通常需要同时记录：

- 代码版本
- 数据版本
- tokenizer 与模型配置
- 超参数与训练环境
- prompt 与上下文配置（大模型应用里）
- 评测结果与生成 artifact
- trace / session 证据（LLM / agent 场景）

## 核心问题

- 参数、数据版本、代码版本和评测结果如何一起保存
- 团队如何避免实验记录碎片化
- 何时应该把实验升级为可复用流程
- prompt、dataset 和 eval 是否也纳入同一条 lineage

## 关键内容

- 超参数与配置管理
- 数据、模型与 prompt 版本
- 指标面板与结果对比
- 运行日志、artifact 与复现实验
- trace 与 release gate 的可追溯性

## 为什么很多团队明明有日志，还是复现不了

- 只保存了 loss 曲线，没有保存完整配置
- 数据版本或采样策略没记录
- prompt 改了，但 run 记录里没有把 prompt 当成正式资产
- 代码在跑完后被改了，但实验结果还在引用旧结论
- 评测脚本和训练脚本没有共同版本管理

## 常见平台怎么分工

- `MLflow`：tracking、registry、prompt registry、tracing
- `Weights & Biases Platform`：tracking、artifacts、registry、Weave tracing/evals
- `Langfuse`：更偏 LLM / agent traces、prompt、dataset、scores

## 实践里要形成什么纪律

- 每次关键实验都能唯一标识
- 能从一个 run 反查完整配置、数据和代码
- 模型进入部署前，要能追溯它对应的训练和评测证据
- prompt / dataset / eval 也要能追溯到具体 release

## 学习这页时最该记住什么

- 实验跟踪是规模化协作的前提
- 复现能力本身就是 AI 工程能力
- 到 `LLMOps` 时代，tracking 的对象已经不只是模型训练 run

## 关联

- [[Evaluation and Benchmarks]]
- [[Prompt Registry、Datasets 与 Evals]]
- [[Model Registry and Deployment]]
- [[../../AI-Learning/09-Systems/MLflow|MLflow]]
- [[../../AI-Learning/09-Systems/Weights & Biases Platform|Weights & Biases Platform]]
- [[../../AI-Learning/09-Systems/Langfuse|Langfuse]]
