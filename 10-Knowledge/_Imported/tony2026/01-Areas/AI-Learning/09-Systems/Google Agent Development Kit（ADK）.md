---
title: Google Agent Development Kit（ADK）
type: system
status: learning
tags:
  - ai/system
  - ai/agent
  - ai/google
  - ai/adk
created: 2026-03-25
updated: 2026-03-29
---

# Google Agent Development Kit（ADK）

## 它是什么

`Google Agent Development Kit`，简称 `ADK`，是 Google 提供的一套 agent 开发框架。官方首页把它定义成“用于构建 powerful multi-agent systems 的 Agent Development Kit”。

它值得注意的，不只是“Google 也有一个 agent SDK”，而是它把几个最近很热的方向放到了同一个体系里：

- `multi-agent`
- `MCP`
- `A2A`
- agent workflow / tool integration

## 为什么它值得单独学

如果你现在研究的是 `Agent 平台`，`ADK` 特别值得学的原因是：它不是单一聊天产品，而是一个面向 agent system building 的开发框架。

也就是说，它更接近：

- agent runtime / developer framework
- Google 生态里的 agent 开发入口
- 与 `A2A`、`MCP` 更自然靠近的一层系统

## 先抓住它的 4 个关键点

### 1. 它从一开始就把 multi-agent 当成正式问题

官方首页和 `Agents` 文档都把 `multi-agent systems` 放在显著位置。这说明它不是“先把单 agent 跑通，再顺便加协调”，而是默认承认 agent system 会走向分工、协作和组合。

### 2. 它天然靠近 Google 的 agent 互操作生态

`ADK` 官方文档里单独列了 `A2A`，这让它和“只关心本地 workflow 的单运行时框架”不太一样。

如果你要的是：

- remote worker
- sub-agent handoff
- cross-agent interoperability

那 `ADK` 会比纯本地图执行框架更值得关注。

### 3. 它把 MCP 当成正式接入面

`ADK` 官方文档单独有 `MCP Tools` 页面。这意味着它并不是把 tool integration 只看成“本地函数调用”，而是默认支持协议化工具接入。

### 4. `State + Compaction + Artifacts` 是它很值得学的 memory 入口

`ADK` 官方文档把 `state`、`context compaction`、`artifacts` 分开讲，这一点非常像现代 agent framework 的 memory engineering 思路。

也就是说，它不只是“有上下文”，而是在明确承认：

- session / app / user 级 state 需要分层
- context 需要 compaction
- artifacts 不应该和 memory 混成一团

这对理解 `state vs memory vs artifact` 很有帮助。

### 5. 它更像 runtime / framework，而不是完整平台

这点很重要。

`ADK` 很适合做：

- agent implementation layer
- Google ecosystem adapter
- multi-agent / A2A-friendly runtime

但如果你的目标是做 `tenant + thread + approval + trace + eval + channel adapter` 这类平台问题，那么 `ADK` 本身通常还不够，它更像平台里的一块运行时能力。

## 在 Agent 平台里，我会怎么放它

如果目标是做自己的 `agent platform`，我更倾向把 `ADK` 放在下面这几个角色里：

- `adapter runtime`
- `remote worker runtime`
- `Google/A2A integration layer`
- `specialized agent service`

换句话说，它很强，但我不建议一上来就把 `ADK` 和所有平台控制面深耦合成一个唯一底座。

## 一个工程上的判断

基于当前官方资料，我更推荐的策略是：

- `LangGraph` 做主 runtime 和 thread/checkpoint/interrupt 内核
- `Langfuse` 做 trace/eval/prompt/experiment 平台
- `ADK` 做 Google 生态和 `A2A` 互操作层

这里的“更推荐”是工程判断，不是 Google 官方给出的架构结论。

## 什么时候优先考虑 ADK

- 你明确要进 Google 的 agent 生态
- 你非常在意 `A2A` 兼容与多 agent 结构
- 你想把 agent 封成相对独立的服务单元
- 你希望 `MCP`、`A2A`、agent framework 在同一套生态里自然衔接

## 推荐继续往下读

- [[LangGraph]]
- [[LangMem]]
- [[Langfuse]]
- [[../06-Topics/A2A（Agent-to-Agent）与协作协议|A2A（Agent-to-Agent）与协作协议]]
- [[../../AI-Engineering/07-Topics/A2A 与 Multi-Agent Coordination|A2A 与 Multi-Agent Coordination]]
- [[../../AI-Engineering/07-Topics/Agent 平台架构（LangGraph、Langfuse、ADK）|Agent 平台架构（LangGraph、Langfuse、ADK）]]
- [[../../AI-Engineering/08-Maps/Agent 平台技术栈图|Agent 平台技术栈图]]

## 关联

- [[../06-Topics/Agent 平台|Agent 平台]]
- [[../06-Topics/MCP（Model Context Protocol）|MCP（Model Context Protocol）]]
- [[../06-Topics/A2A（Agent-to-Agent）与协作协议|A2A（Agent-to-Agent）与协作协议]]
- [[LangGraph]]
- [[LangMem]]
- [[Langfuse]]
- [[../../AI-Engineering/07-Topics/Agent SDK 设计|Agent SDK 设计]]
- [[../../AI-Engineering/07-Topics/Agent 平台架构（LangGraph、Langfuse、ADK）|Agent 平台架构（LangGraph、Langfuse、ADK）]]
- [[../../AI-Engineering/07-Topics/Tool Gateway、MCP Servers 与 SDK Tools|Tool Gateway、MCP Servers 与 SDK Tools]]

## 资料

- [ADK Overview](https://google.github.io/adk-docs/)
- [ADK State](https://google.github.io/adk-docs/sessions/state/)
- [ADK Context Compaction](https://google.github.io/adk-docs/context/compaction/)
- [ADK Artifacts](https://google.github.io/adk-docs/artifacts/)
- [ADK Agents](https://google.github.io/adk-docs/agents/)
- [ADK MCP Tools](https://google.github.io/adk-docs/tools-custom/mcp-tools/)
- [ADK A2A Introduction](https://google.github.io/adk-docs/a2a/intro/)
