---
title: 飞书与 Lark 作为 Agent Channel Adapter
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent
  - ai/channel
  - ai/feishu
created: 2026-03-25
updated: 2026-03-25
---

# 飞书与 Lark 作为 Agent Channel Adapter

## 为什么飞书这一层值得单独拿出来

很多团队说“支持飞书 webhook 就行”，但一旦要做真正的 `agent platform`，你会发现 Feishu / Lark 不只是一个消息出口，而是一个完整的 `channel adapter` 问题。

平台需要处理的不是“发一条消息”，而是：

- 用户是谁
- 来自哪个 tenant / team
- 当前 thread 是什么
- 哪条消息触发了审批或 tool action
- 哪些回调属于同一个任务

## 先给一个工程判断

下面这条不是 Feishu 官方架构结论，而是结合 `Lark Developer` 的平台能力做的工程判断：

- `webhook` 更适合作为单向通知出口
- 真正的交互式 agent，更适合进入 `app bot + event-driven` 模式

因为一旦你需要：

- 收用户输入
- 维护 thread / session
- 做 approval card 或结构化交互
- 建立用户/群/租户身份映射

你本质上就不再只是“发通知”，而是在做 channel runtime。

## Channel Adapter 要做什么

### 1. 事件归一化

把来自 Feishu / Lark 的事件统一成平台自己的：

- `TurnRequest`
- `UserIdentity`
- `ChannelContext`
- `ConversationRef`

### 2. 身份与租户映射

- user id
- open id / union id
- tenant id
- chat / group context

这些字段需要映射到平台的 auth / policy / trace 体系里。

### 3. thread / session 对齐

一个成熟的 agent 平台，不能只凭“用户发来一句话”就开始新任务。它必须把消息归到：

- 哪个 thread
- 哪个 approval stage
- 哪个 long-running task

### 4. 响应模式分层

Feishu 侧至少要考虑：

- 即时回复
- 异步结果回推
- 审批 / 确认请求
- 错误与 fallback 通知

### 5. 安全与权限

channel adapter 不能绕过平台：

- approval 仍然由平台统一控制
- tool action 仍然经过 policy / gateway
- Feishu 只是一层入口和出口

## 我更推荐的集成方式

- `Feishu / Lark` 作为 channel layer
- 平台网关把消息归一化后，再进入 `LangGraph` runtime
- trace / approval / tool call 依然走平台公共层
- 输出再回到 Feishu adapter

也就是：Feishu 不应该直接拥有业务 agent 逻辑，它更像是一个受控接入面。

## 为什么 webhook 不该承担太多职责

如果把大量 agent 逻辑写死在 webhook handler 里，很快会出现：

- channel-specific branching 爆炸
- thread state 混乱
- 无法复用到 Web / API
- trace / audit 难统一

所以更稳的方式是：

- webhook / event handler 只负责 adapter 职责
- 真正的业务逻辑进入平台 runtime 与 SDK contract

## 推荐继续往下读

- [[Agent SDK 设计]]
- [[Tool Gateway、MCP Servers 与 SDK Tools]]
- [[Agent 平台架构（LangGraph、Langfuse、ADK）]]
- [[Human-in-the-Loop and Approval Gates]]

## 关联

- [[../../AI-Learning/06-Topics/Agent 平台|Agent 平台]]
- [[Agent SDK 设计]]
- [[Tool Gateway、MCP Servers 与 SDK Tools]]
- [[Agent 平台架构（LangGraph、Langfuse、ADK）]]
- [[Human-in-the-Loop and Approval Gates]]
- [[Agent Security、Sandbox 与 Approval Architecture]]
- [[../08-Maps/Agent 平台技术栈图|Agent 平台技术栈图]]

## 资料

- [Lark Developer](https://open.larksuite.com/?lang=en-US)
- [Feishu Open Platform](https://open.feishu.cn/)
