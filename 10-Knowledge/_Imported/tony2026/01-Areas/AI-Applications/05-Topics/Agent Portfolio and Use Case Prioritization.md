---
title: Agent Portfolio and Use Case Prioritization
type: topic
status: learning
tags:
  - ai/applications
  - ai/portfolio
  - ai/agent
created: 2026-03-23
updated: 2026-03-23
---

# Agent Portfolio and Use Case Prioritization

## 这个主题在讲什么

当一个组织开始同时尝试很多 agent 时，真正的问题不再是“能不能做”，而是“先做哪些、哪些值得平台化、哪些先不要碰”。

## 为什么要做 portfolio 管理

- agent 用例天然会扩散，如果没有优先级机制，团队会被大量零散需求拖住
- 不同用例的价值、风险、可观测性和 rollout 成本差异很大
- portfolio 管理能把试点、放大、淘汰、平台化这几类动作区分开

## 一个简单的优先级框架

从 5 个维度打分：

- `business value`
- `workflow clarity`
- `tool readiness`
- `risk level`
- `measurement readiness`

## 最值得先做的场景

- 高价值、高频、低歧义
- 已经有清晰单一事实源
- 容易做人工 review 和失败恢复
- 可以在 2-6 周内拿到明确指标变化

## 暂时不该优先做的场景

- 任务边界模糊
- 风险高但没有治理能力
- 依赖过多脏数据或隐式知识
- 很难定义 success metric

## 组合管理建议

- 把用例分成：`pilot`、`scale`、`platform candidate`、`hold`
- 每月做一次 portfolio review
- 不要让所有团队都从头造自己的 agent
- 对重复出现的能力需求，优先平台化成共享能力

## 相关

- [[Agent Operating Model and Governance]]
- [[Agent Rollout and Change Program]]
- [[../07-Templates/Agent 用例优先级模板|Agent 用例优先级模板]]
- [[../../AI-Engineering/07-Topics/Cost, Latency, and Safety Tradeoffs|Cost, Latency, and Safety Tradeoffs]]
