---
title: App Server 与 Rich Agent Protocols
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent
  - ai/protocol
  - ai/app-server
created: 2026-03-25
updated: 2026-03-25
---

# App Server 与 Rich Agent Protocols

## 为什么这层值得单独拿出来

很多 `MCP vs CLI` 的争论，其实漏掉了第三层：

- 不只是直接执行命令
- 不只是协议化暴露工具
- 还要不要一个更完整的 `task / session / approval / event` 协议层

这就是 `App Server` 或更广义 `rich agent protocol` 要解决的问题。

## 这个主题是什么

`App Server` 可以理解成：把 agent loop、任务会话、审批请求、事件流和客户端交互，暴露成一个稳定协议。

它通常不只传一个 tool call，而是传：

- task / thread / session
- streaming events
- approvals
- artifacts
- diffs
- checkpoints
- reconnect / resume 信息

## 为什么 MCP 不总是够用

`MCP` 很擅长：

- 标准化 tools / resources / prompts
- 把集成沉淀成可复用接口

但当系统要承载更复杂的 agent runtime 语义时，仅靠 MCP 不一定最顺手，比如：

- 一个请求对应大量中间事件
- server 需要主动向 client 发审批请求
- 需要维护 thread / task 生命周期
- 需要传递 diff、artifact、timeline、resume state

这时候系统常常会往 richer protocol 演化。

## 你可以把三层分开理解

1. `CLI / shell`
   - 直接动作面
2. `MCP`
   - 标准化集成层
3. `App Server / Rich Protocol`
   - 任务与会话控制层

这三者不是单选题，而是系统可能同时拥有的三层结构。

## 一个 richer protocol 往往包含什么

- `thread / task identity`
- `request / notification / event stream`
- `approval request / response`
- `artifact and diff surfaces`
- `resume and replay`
- `backward-compatible client bindings`

## 为什么这对 coding agents 特别关键

coding agent 不只是“调工具”，而是要：

- 维护一个长期任务
- 持续回传中间状态
- 接收人工审批
- 把结果组织成 diff / PR / artifact
- 允许客户端重连并恢复状态

这比单次 tool invocation 丰富很多。

## 典型判断

### 更偏向 MCP 的情况

- 你主要在做共享工具接入
- 重点是让多个 host 复用同一 server
- 任务对象本身不复杂

### 更偏向 App Server 的情况

- 你要支撑完整 agent 会话
- 你要接 IDE、桌面、web、CLI 等多个前端
- 你要把 approval、event、artifact 作为一等公民

## 它和 harness engineering 的关系

- harness 是“工作台”
- rich protocol 是工作台暴露给客户端的控制面之一

所以 app server 常常就是 harness 的对外界面。

## 推荐继续往下读

- [[MCP 与 CLI 模式]]
- [[Harness Engineering]]
- [[Tool Calling and Action Execution]]
- [[Session and Memory Design]]
- [[../../AI-Learning/09-Systems/Codex|Codex]]

## 相关

- [[MCP 与 CLI 模式]]
- [[Harness Engineering]]
- [[Session and Memory Design]]
- [[Long-Running Agent Operations]]
- [[../08-Maps/Agent Action Surfaces and Protocols Map|Agent Action Surfaces and Protocols Map]]
