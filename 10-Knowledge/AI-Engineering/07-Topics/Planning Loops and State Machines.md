---
title: Planning Loops and State Machines
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent-runtime
  - ai/planning
created: 2026-03-22
updated: 2026-03-22
---

# Planning Loops and State Machines

## 为什么重要

- 很多 agent 失败，不是因为模型不够聪明，而是因为控制循环太松散
- 一旦任务变长、动作变多，系统就需要明确状态，而不是靠“下一轮再想想”硬撑

## 系统视角

这页关注两层：

- planning loop：plan -> act -> observe -> revise
- state machine：任务当前处于什么状态、允许进入什么下一状态

前者更像策略循环，后者更像工程约束。

## 为什么二者要一起看

只有 planning loop，没有状态机，系统容易：

- 无限循环
- 重复动作
- 乱跳步骤
- 无法恢复

只有状态机，没有 planning，系统又会太死板，难以处理开放任务。

## 常见状态

- initialized
- waiting_for_context
- ready_to_act
- acting
- awaiting_result
- awaiting_approval
- blocked
- completed
- failed

## 工程难点

- 什么状态由模型决定，什么状态由系统硬编码
- 状态迁移是否可审计
- 中断、恢复、人工接管如何进入状态机
- 多 agent 情况下，局部状态和全局状态如何同步

## 推荐治理方法

- 把高风险状态迁移做成显式规则
- 模型负责局部决策，系统负责生命周期约束
- 为每一步保留 observation log，方便恢复和复盘
- 不要让模型单独掌控“何时继续、何时停止、何时升级权限”这三类关键决策

## 系统案例

- [[../../AI-Learning/09-Systems/OpenClaw|OpenClaw]]
- [[../../AI-Learning/09-Systems/Devin|Devin]]
- [[../../AI-Learning/09-Systems/Codex|Codex]]

## 相关

- [[Agent Runtime Architecture]]
- [[Tool Calling and Action Execution]]
- [[Human-in-the-Loop and Approval Gates]]
- [[Long-Running Agent Operations]]
- [[../../AI-Learning/06-Topics/Planning and Control|Planning and Control]]
