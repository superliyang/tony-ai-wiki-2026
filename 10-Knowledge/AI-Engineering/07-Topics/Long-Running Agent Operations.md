---
title: Long-Running Agent Operations
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent-ops
created: 2026-03-22
updated: 2026-03-25
---

# Long-Running Agent Operations

## 为什么重要

- 一旦 agent 不再是单轮请求，而是长期在线系统，运维问题会立刻成为核心问题
- 很多“看起来像智能问题”的故障，实际是 agent ops 问题

## 系统视角

长期运行的 agent，必须回答这些问题：

- 什么时候主动醒来
- 什么时候保持安静
- 异常怎么发现
- 错误动作怎么止损
- 成本怎么控制
- 任务和记忆如何长期维持而不腐烂

所以 `Long-Running Agent Operations` 的本质是：

- 让 agent 持续工作
- 但又不失控、不打扰、可审计

## 核心问题

- heartbeat 和 cron 的职责边界是什么
- hooks 应该触发哪些动作，不该触发哪些动作
- agent 的 retry、timeout、escalation 怎么设计
- 长期运行时如何做成本治理和告警治理
- thread state、checkpoint、memory compaction 如何配合

## 关键模块

- scheduler：cron / delayed jobs / retry queues
- liveness：heartbeat / health checks
- event hooks：session lifecycle / command logging / memory sync
- state management：checkpoint、resume、stuck-task handling
- guardrails：权限、预算、频率限制、审批
- observability：logs、trace、metrics、audit trail
- human handoff：人工介入、暂停、恢复、回滚

## 典型运行节律

- 被动型：用户发消息才执行
- 巡检型：heartbeat 定期检查状态
- 计划型：cron 在固定时间触发任务
- 事件型：hooks 在 session / tool / command 事件上触发动作

## 真正难的地方

- 主动性越强，系统越容易 noisy
- 自动化越多，错误传播越快
- 长期 memory 越强，历史污染影响越大
- 工具权限越大，止损要求越高
- thread 太长、state 太脏时，恢复会越来越困难

## 常见失败模式

- heartbeat 过于频繁，产生大量低价值 turn
- cron 任务重复执行，没有幂等保护
- hook 链太复杂，系统行为越来越难解释
- agent 失败后没人接手，任务在后台悄悄烂掉
- 成本监控缺失，长期运行后预算失控
- checkpoint 与 memory 没分层，导致恢复后状态混乱

## 推荐治理方法

- 把 heartbeat 当巡检，不当强制执行器
- 把 cron 当明确任务调度，不当“万能定时器”
- 所有自动动作都要有频率、预算和审计边界
- 高风险动作必须设计 human-in-the-loop
- memory 写入与自动化触发都要可追溯
- 周期性做 compaction、re-summary、task cleanup

## 学习这页时最该记住什么

- 长期在线 agent 的挑战，不在“能不能多跑几轮”，而在“能不能长期稳定、低噪声、可治理地跑下去”

## 相关主题

- [[Agent Runtime Architecture]]
- [[Session and Memory Design]]
- [[长期运行 Agent 的记忆系统]]
- [[Serving and Scaling]]
- [[Security and Privacy]]
- [[Cost Optimization]]

## 系统案例

- [[../../AI-Learning/09-Systems/OpenClaw 工作原理与架构|OpenClaw 工作原理与架构]]
- [[../../AI-Learning/09-Systems/OpenClaw 的准自进化工作流|OpenClaw 的准自进化工作流]]
