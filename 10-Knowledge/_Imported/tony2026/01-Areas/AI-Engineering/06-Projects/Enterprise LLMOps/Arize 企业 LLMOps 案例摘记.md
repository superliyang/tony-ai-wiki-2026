---
title: Arize 企业 LLMOps 案例摘记
type: case-note
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# Arize 企业 LLMOps 案例摘记

## 为什么看 Arize 客户案例

因为它们很适合回答一个问题：

- 当团队真的进入线上 LLM / agent 运营后，为什么 trace-aware eval 会变得刚需

## 我从官方客户页里提炼出的模式

### 模式 1：从 day-one eval 开始

像 `Handshake` 这类案例强调的不是“模型多强”，而是：

- 用 eval 从第一天开始管理 use case
- 快速扩多个 LLM use case 时，用 evaluation discipline 控制质量漂移

### 模式 2：online eval 直接接业务指标

像 `TheFork` 这类案例说明：

- eval 不只是工程分数
- 它已经开始和 conversion / user outcome 绑在一起

### 模式 3：生产中的 agent observability

客户案例反复出现的模式是：

- agent 不是只要离线评测
- 真正难的是 production traces、intervention 和 predictable behavior

## 这对选型的启发

如果你的团队已经进入：

- 多 use case 并行
- 线上质量波动明显
- retrieval / tool / agent path 难以诊断

那 `Phoenix / Arize` 这种 trace-aware observability 路线就会很值钱。

## 官方来源

- [Arize Customers](https://arize.com/customers)
- [Arize Phoenix Docs](https://arize.com/docs/phoenix)
