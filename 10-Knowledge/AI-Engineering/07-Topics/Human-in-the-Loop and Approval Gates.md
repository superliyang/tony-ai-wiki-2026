---
title: Human-in-the-Loop and Approval Gates
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent-runtime
  - ai/governance
created: 2026-03-22
updated: 2026-03-22
---

# Human-in-the-Loop and Approval Gates

## 为什么重要

- 真正的 agent 系统不是“尽量完全自治”，而是“在合适的地方自动，在关键点可控”
- 一旦 agent 能执行代码、访问数据、发消息、改配置，人类审批就从体验问题变成治理问题

## 系统视角

`Human-in-the-Loop` 关注人类如何参与系统决策；`Approval Gates` 关注哪些动作必须先过权限门。

它们通常落在这些点上：

- 高风险工具调用前
- 外部副作用发生前
- 长时间任务继续前
- 多 agent 结果汇总进入主线前

## 常见审批对象

- shell / exec
- 网络请求
- 代码写入与合并
- 数据库写操作
- 对外发送消息
- 凭据相关动作

## 真正难的地方

- 审批太少，系统风险高
- 审批太多，用户被打断到无法使用
- 审批上下文不足，用户不知道自己在批什么
- agent 可能在“安全动作”外衣下拼出高风险组合动作

## 推荐治理方法

- 用风险等级决定审批密度，而不是一刀切
- 审批请求必须包含：意图、影响范围、参数摘要、回滚方式
- 高风险动作默认需要显式人类确认
- 对低风险、可回滚动作可以设定策略性放行

## 在 coding agent 里尤其重要

coding agent 常见的审批点包括：

- 是否允许运行命令
- 是否允许联网
- 是否允许安装依赖
- 是否允许直接写文件
- 是否允许发起 PR 或推送结果

## 系统案例

- [[../../AI-Learning/09-Systems/Claude Code|Claude Code]]
- [[../../AI-Learning/09-Systems/Codex|Codex]]
- [[../../AI-Learning/09-Systems/Cursor|Cursor]]
- [[../../AI-Learning/09-Systems/OpenClaw|OpenClaw]]

## 相关

- [[Tool Calling and Action Execution]]
- [[Planning Loops and State Machines]]
- [[Background Agents]]
- [[Delegation and Task-Oriented Agents]]
- [[../../AI-Learning/06-Topics/Tool Use|Tool Use]]
