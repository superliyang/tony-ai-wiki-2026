---
title: Inspect AI
type: system
status: learning
tags:
  - ai/system
  - ai/evals
  - ai/agent
created: 2026-04-14
updated: 2026-04-14
---

# Inspect AI

## 它是什么

`Inspect AI` 是一个更偏“可编排评测框架”的 agent / model evaluation 系统。

它最值得注意的点是：官方把评测拆成了一组非常工程化的部件：

- tasks
- datasets
- solvers
- scorers
- tools
- sandboxing
- agents
- eval sets

## 为什么它重要

很多 agent 评估工具擅长：

- 打分
- 看 trace
- 做发布前回归

但如果你想要的是“明确任务、明确环境、明确 scorer、明确 agent 行为”的可重复实验，`Inspect AI` 这条路很值得单独学。

## 它最值得抓住的 4 个点

### 1. 它是 task-oriented，而不是 dashboard-oriented

这意味着它很适合：

- 研究化 benchmark
- sandbox 任务
- 复杂 tool / agent 任务的可重复实验

### 2. `solver` 和 `scorer` 分离很关键

这让你更容易看清：

- 被评对象是什么
- 判分逻辑是什么
- 环境约束是什么

### 3. 它把 tools、sandboxing 和 agents 放进同一语境

这对 agent eval 特别重要，因为很多问题并不在最终答案，而是在：

- 工具如何被调用
- 环境是否可重复
- 代理行为是否符合边界

### 4. 它适合做高控制度的基准和实验

如果你的目标是：

- 复现实验
- 严格对照版本
- 在受控环境里比较 agent 行为

那它比单纯 trace 平台更贴近“实验系统”。

## 在 Agent 效果评估这条线上怎么放它

- 作为 `offline / sandbox evaluation framework`
- 作为 task、environment、scorer 明确分层的工作台
- 和 `Ragas`、`Promptfoo`、`Phoenix` 互补

## 它不解决什么

- 它不是主要的线上 tracing 平台
- 它不是 prompt / release management 平台
- 它也不是面向产品团队的轻量操作面板

## 推荐继续往下读

- [[../../AI-Engineering/07-Topics/Agent 效果评估：方法论、开源工具与判断框架|Agent 效果评估：方法论、开源工具与判断框架]]
- [[../../AI-Engineering/07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]]
- [[../../AI-Engineering/07-Topics/Agent Evaluation and Reliability|Agent Evaluation and Reliability]]
- [[Ragas]]
- [[Promptfoo]]

## 关联

- [[../06-Topics/Agent|Agent]]
- [[../../AI-Engineering/07-Topics/Tool Calling and Action Execution|Tool Calling and Action Execution]]
- [[../../AI-Engineering/07-Topics/Computer Use Runtime and Safety|Computer Use Runtime and Safety]]
- [[../../AI-Engineering/07-Topics/Agent 效果评估：方法论、开源工具与判断框架|Agent 效果评估：方法论、开源工具与判断框架]]

## 资料

- [Inspect Docs](https://inspect.aisi.org.uk/)
