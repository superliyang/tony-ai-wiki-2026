---
title: A2A 与 Multi-Agent Coordination
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent
  - ai/a2a
  - ai/multi-agent
created: 2026-03-25
updated: 2026-03-25
---

# A2A 与 Multi-Agent Coordination

## 为什么这层值得单独讨论

到了 agent 体系的后半段，很多争论已经不是：

- 要不要 tool calling
- 用不用 MCP

而是：

- 一个 agent 是不是该找另一个 agent 协作
- 协作是内部 orchestration，还是外部协议互通
- supervisor / worker 就够了，还是要 A2A 这类协议层

## 先把三个层次分开

### `single runtime orchestration`

- 所有 agent 都在一个系统里
- coordinator 可以直接访问每个 worker 的状态
- 更容易调试和治理

### `multi-agent coordination`

- 任务被拆给多个角色 agent
- 重点是任务切分、依赖管理、结果聚合

### `A2A`

- 不同 agent 可能来自不同 runtime、不同团队、不同厂商
- 重点是能力发现、任务协商、状态交换、身份与授权

## 为什么 A2A 不等于 multi-agent

很多系统即使是 multi-agent，也完全不需要 A2A。

例如：

- 一个 planner
- 两个 worker
- 一个 reviewer

如果这些都在同一 runtime 里，直接内部 handoff 就够了。

A2A 只有在“agent 之间需要跨边界协作”时才真正变得重要。

## 一个 A2A 协调层往往要回答什么

- 怎么发现远端 agent
- 怎么声明 skill / capability
- 一个任务怎么创建、取消、重连、订阅
- 结果是消息、artifact 还是长期任务状态
- 身份和权限如何处理
- 对方 agent 的失败如何反馈给本地 orchestration

## 为什么这比工具调用更难

因为工具调用通常默认：

- 输入输出相对结构化
- 生命周期很短
- host 对调用链有较强控制权

A2A 则经常意味着：

- 对方是 opaque system
- 生命周期更长
- 中间事件更多
- 调试边界更模糊
- trust 问题更重

## 什么时候适合先用内部协调，不要上 A2A

- 所有 agent 都归同一团队控制
- 共享状态很重
- 需要统一审批、统一日志、统一 rollback
- 你还在快速迭代任务设计

## 什么时候 A2A 更合理

- 不同团队有独立 agent 平台
- 一个 agent 的输出天然就是另一个 agent 的输入
- 远端 agent 需要作为“完整能力单元”存在，而不是被压扁成普通工具

## 真正难的地方

- capability mismatch：名字像同一个 skill，语义却不同
- trust boundary：谁能代表谁做动作
- artifact semantics：传的是文本、结构化对象，还是 task 结果状态
- observability gap：跨 agent 边界后 trace 断裂
- cost multiplication：多 agent 协作让 token、latency、审批成本一起上升

## 一句最该记住的话

- `multi-agent` 解决的是分工问题
- `A2A` 解决的是边界协作问题

## 推荐继续往下读

- [[Agent Security、Sandbox 与 Approval Architecture]]
- [[长期运行 Agent 的记忆系统]]
- [[Harness Engineering]]
- [[Eval Harness 与 Regression Suites]]
- [[../../AI-Learning/06-Topics/A2A（Agent-to-Agent）与协作协议|A2A（Agent-to-Agent）与协作协议]]
- [[../../AI-Learning/06-Topics/Multi-Agent Systems|Multi-Agent Systems]]

## 相关

- [[Harness Engineering]]
- [[Agent Runtime Architecture]]
- [[长期运行 Agent 的记忆系统]]
- [[../08-Maps/Agent 协作、记忆与信任边界图|Agent 协作、记忆与信任边界图]]
