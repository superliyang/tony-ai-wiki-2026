---
title: Agent SDK 设计
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent
  - ai/sdk
created: 2026-03-25
updated: 2026-03-25
---

# Agent SDK 设计

## 为什么平台里还要单独有一层 SDK

如果把业务逻辑直接写死在 `LangGraph` 节点、`ADK` agent class、或者某个 channel handler 里，短期看很快，长期会很痛：

- runtime 一换就很难迁
- tool contract 不统一
- approval / policy 无法做成平台能力
- channel adapter 会把业务语义带乱
- trace / eval 也难统一

所以平台里通常需要一层自己的 `Agent SDK`。

## 这一层到底要抽什么

最核心的是：把“平台 contract”从“具体 runtime 实现”里抽出来。

我更推荐 SDK 至少抽出这些对象：

- `AgentSpec`
- `WorkflowSpec`
- `ToolSpec`
- `PolicySpec`
- `ApprovalRule`
- `MemoryPolicy`
- `ChannelAdapter`
- `TraceContext`
- `ArtifactRef`

## 这些对象各自解决什么

### AgentSpec

定义一个 agent 的身份和边界，例如：

- agent id
- role
- capability set
- default tools
- model policy
- memory policy

### WorkflowSpec

定义任务如何流经节点、审批点、回调和状态迁移。

### ToolSpec

把工具从 runtime 里抽象出来：

- transport 是 `MCP`、HTTP、SDK 还是 CLI
- input / output schema 是什么
- auth、timeout、budget 怎么配

### PolicySpec / ApprovalRule

把“什么时候允许执行、什么时候必须人审”做成正式 contract，而不是散在业务代码里的 if/else。

### MemoryPolicy

明确 thread state、durable memory、artifact retention、compaction 的边界。

### ChannelAdapter

把 `Feishu / Web / API` 这些入口统一成同一类 request / response contract。

### TraceContext

把 trace id、thread id、session id、user id、tenant id、release version 串起来，方便 `Langfuse` 和回归体系接入。

## SDK 层最重要的价值

- 让 `LangGraph` 可以是主 runtime，但不是唯一耦合点
- 让 `ADK` 可以变成 adapter runtime，而不是平台全部逻辑的宿主
- 让 tool 和 policy 先统一，再映射到不同 runtime
- 让 channel 接入先归一，再交给执行层

## 一个实用的 SDK 设计原则

### 1. 先定义 contract，再接 runtime

不要先问“LangGraph 节点怎么写”，先问：

- 平台真正稳定的对象是什么
- 哪些对象以后换 runtime 也不该变

### 2. platform-facing type 和 runtime-facing type 分离

- `platform types`：tenant、thread、approval、artifact、policy
- `runtime types`：graph state、agent invocation、tool call

### 3. tool schema 要比 prompt 更稳定

在平台里，`ToolSpec` 往往比 prompt 更像长期 contract。

### 4. channel model 要统一

Feishu、Web、API 的输入事件虽然长得不一样，但最好都先进入统一的 `TurnRequest` / `TurnResponse`。

## 一个很实用的最小接口集

```python
class AgentSpec: ...
class WorkflowSpec: ...
class ToolSpec: ...
class PolicySpec: ...
class ApprovalRule: ...
class MemoryPolicy: ...
class ChannelAdapter: ...
class TraceContext: ...
```

这不是官方标准，而是更适合做自家平台的一组稳定抽象。

## 什么时候你真的需要这一层

- 已经不只一个 agent
- 已经不只一个 channel
- 已经不只一个 tool transport
- 已经开始需要 approval / audit / replay / eval
- 已经在考虑 `LangGraph` 和 `ADK` 的双栈互操作

## 推荐继续往下读

- [[Agent 平台架构（LangGraph、Langfuse、ADK）]]
- [[Tool Gateway、MCP Servers 与 SDK Tools]]
- [[飞书与 Lark 作为 Agent Channel Adapter]]
- [[Session and Memory Design]]
- [[Harness Engineering]]

## 关联

- [[../../AI-Learning/06-Topics/Agent 平台|Agent 平台]]
- [[../../AI-Learning/09-Systems/Google Agent Development Kit（ADK）|Google Agent Development Kit（ADK）]]
- [[../../AI-Learning/09-Systems/LangGraph|LangGraph]]
- [[../../AI-Learning/09-Systems/Langfuse|Langfuse]]
- [[Tool Gateway、MCP Servers 与 SDK Tools]]
- [[飞书与 Lark 作为 Agent Channel Adapter]]
- [[Agent 平台架构（LangGraph、Langfuse、ADK）]]
- [[Agent Runtime Architecture]]
- [[Session and Memory Design]]
- [[Harness Engineering]]
