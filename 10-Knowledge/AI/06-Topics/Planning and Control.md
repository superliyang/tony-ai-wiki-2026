---
title: Planning and Control
type: topic
status: draft
tags:
  - ai/topic
  - ai/agent
  - ai/planning
created: 2026-03-22
updated: 2026-03-22
---

# Planning and Control

## 这个主题是什么

`Planning and Control` 关注 agent 如何把目标拆成步骤、根据中间结果调整策略，并在循环中控制自己不要失控。

## 为什么重要

- agent 不是只要会调用工具就够了；它还要知道什么时候该做什么
- 规划能力决定 agent 能否处理多步、长链、存在不确定性的任务
- 控制能力决定 agent 是否安全、可预测、可治理

## 你先要抓住什么

- planning 不一定是先生成一份大计划再执行
- 很多系统更像“边计划、边执行、边修正”
- control 不是让系统更保守，而是确保任务在预算、权限、状态边界内推进

## 常见控制问题

- 什么时候继续循环，什么时候停
- 什么时候请求人工确认
- 什么时候改计划，什么时候回滚
- 什么情况下要降级为更简单的策略
- 多步执行如何避免 drift 和 hallucination

## 规划的几种常见形式

- upfront planning：先给一份粗计划
- iterative planning：每完成一步再决定下一步
- hierarchical planning：高层任务拆成更小子任务
- delegated planning：把部分子任务交给其他 agent 或后台任务

## 真正难的地方

- 计划太粗，落不到工具调用层
- 计划太细，开销过大且脆弱
- 控制过松，系统容易乱跑
- 控制过紧，agent 失去行动价值

## 系统案例

- [[../09-Systems/OpenClaw|OpenClaw]]
- [[../09-Systems/Codex|Codex]]
- [[../09-Systems/Devin|Devin]]
- [[../09-Systems/Claude Code|Claude Code]]

## 从工程角度继续往下读

- [[../../AI-Engineering/07-Topics/Planning Loops and State Machines|Planning Loops and State Machines]]
- [[../../AI-Engineering/07-Topics/Human-in-the-Loop and Approval Gates|Human-in-the-Loop and Approval Gates]]
- [[../../AI-Engineering/07-Topics/Delegation and Task-Oriented Agents|Delegation and Task-Oriented Agents]]

## 相关

- [[Agent]]
- [[Tool Use]]
- [[Agent Memory]]
- [[Multi-Agent Systems]]
- [[Reasoning Models]]
- [[../07-Maps/AI Agent Capability Map|AI Agent Capability Map]]
