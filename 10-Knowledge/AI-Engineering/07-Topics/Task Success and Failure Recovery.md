---
title: Task Success and Failure Recovery
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent-runtime
  - ai/reliability
created: 2026-03-22
updated: 2026-03-22
---

# Task Success and Failure Recovery

## 为什么重要

- agent 最容易“看起来会了”，但真实任务里一出错就彻底卡住
- 所以一个能不能上线的 agent，关键不只在成功时有多聪明，更在失败时有多可恢复

## 系统视角

这页关注两件事：

- 任务成功到底怎么定义
- 当任务没有顺利完成时，系统如何恢复、降级、重试或升级给人类

对 agent 来说，failure recovery 不是补救机制，而是核心能力。

## 任务成功要怎么定义

很多 agent 任务都不是简单的 `pass / fail`。

更实用的定义方式通常包括：

- objective completion：任务目标是否达成
- artifact quality：交付物是否可用
- policy compliance：执行过程中是否遵守权限和规则
- efficiency：是否在合理时间和成本内完成
- human intervention：是否需要大量人工修正

## 常见失败类型

- 目标理解错：一开始方向就偏了
- 工具失败：命令执行、网络请求、权限调用出错
- 状态丢失：上下文、session、memory 断掉
- 计划漂移：越做越偏，任务 scope 被污染
- 外部依赖失败：环境、API、仓库状态与预期不一致

## 恢复路径通常有哪些

- retry：同一动作短重试
- re-plan：承认当前路径失败，重新规划
- rollback：撤回高风险或错误动作
- degrade：降级为更保守、更简单的执行模式
- escalate：升级给人类或 reviewer agent

## 真正难的地方

- 什么情况值得重试，什么情况必须停下来
- 重试是否会放大副作用或成本
- 恢复时如何避免重复动作
- 系统如何让失败对用户可见，而不是“默默坏掉”

## 推荐治理方法

- 为常见失败类型建立显式恢复策略
- 高副作用动作必须可回滚或可审计
- 对连续失败设置硬上限，避免无限循环
- 失败恢复要写入状态，不要让下一轮像失忆一样重来
- 对“需要人工接管”的条件提前定义清楚

## 适合看的关键指标

- recovery success rate
- retry count per task
- escalation rate
- rollback frequency
- stuck-session rate

## 系统案例

- [[../../AI-Learning/09-Systems/Codex|Codex]]
- [[../../AI-Learning/09-Systems/Devin|Devin]]
- [[../../AI-Learning/09-Systems/OpenClaw|OpenClaw]]

## 相关

- [[Agent Evaluation and Reliability]]
- [[Planning Loops and State Machines]]
- [[Human-in-the-Loop and Approval Gates]]
- [[Long-Running Agent Operations]]
- [[../../AI-Learning/06-Topics/Planning and Control|Planning and Control]]
