---
title: Evaluation and Benchmarks
type: topic
status: learning
tags:
  - ai/engineering
  - ai/evaluation
created: 2026-03-13
updated: 2026-03-26
---

# Evaluation and Benchmarks

## 为什么重要

- 没有评测，训练只是“算出来了”，不是“证明有进步了”
- 工程团队需要用评测把能力、成本和风险一起量化
- 在 `LLMOps` 里，评测还要和 prompt、dataset、trace、release gate 绑定

## 系统视角

评测系统在 AI 工程里扮演的是“决策控制台”的角色。它不只是告诉你某个模型分数高不高，而是回答：

- 这个版本值不值得继续训练
- 这个 prompt / workflow 能不能上线
- 这个优化是不是只是换了一个 benchmark 看起来更好
- 这个线上退化是否能在线下重现

## 核心问题

- 离线 benchmark 和真实业务指标如何结合
- 通用能力、领域能力和安全能力如何分别评估
- 自动 judge、人工评审和线上反馈如何组合
- 评测是否会被训练数据污染，是否能真实反映上线表现

## 关键维度

- 任务正确率与鲁棒性
- 成本、延迟与吞吐
- 安全、偏见与越狱风险
- 人工评测与自动评测结合
- regression 与 release gate 一致性

## 评测通常分几层

- 离线 benchmark：快速比较基础能力
- 任务评测：面向真实产品或业务任务
- 模型评分 / rubric 评测：在自然语言任务中补足自动指标
- 人审与偏好评测：补足自动指标看不到的细节
- 线上指标：留存、成功率、投诉、成本、延迟

## 为什么评测经常失真

- benchmark 被训练数据污染
- 指标只覆盖“能答对”，没覆盖“是否稳定、是否安全”
- 过于追求排行榜，忽略真实业务目标
- 线上使用方式与离线测试方式根本不同
- prompt 和 dataset 变化没有跟 release 绑定

## 常见平台怎么分工

- `Promptfoo`：pre-release eval / CI / red team
- `Arize Phoenix`：trace-aware evaluation 与 production debugging
- `Langfuse`：dataset runs、scores、release comparison
- `Weights & Biases / Weave`：scorers、datasets、application quality
- `MLflow`：evaluation 结果与 registry / lifecycle 绑定

## 学习这页时最该记住什么

- 评测体系决定团队会朝什么方向优化
- 错的评测，比没有评测更危险
- 真正成熟的评测不是单点 benchmark，而是 lifecycle 上的多层评测

## 关联

- [[Experiment Tracking]]
- [[Prompt Registry、Datasets 与 Evals]]
- [[Online Evals、Human Feedback 与 Annotation]]
- [[Safety Evaluation]]
- [[../../AI-Learning/09-Systems/Arize Phoenix|Arize Phoenix]]
- [[../../AI-Learning/09-Systems/Promptfoo|Promptfoo]]
- [[../../AI-Learning/09-Systems/Langfuse|Langfuse]]
