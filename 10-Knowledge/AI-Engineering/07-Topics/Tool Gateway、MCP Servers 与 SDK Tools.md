---
title: Tool Gateway、MCP Servers 与 SDK Tools
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent
  - ai/tools
  - ai/mcp
created: 2026-03-25
updated: 2026-03-25
---

# Tool Gateway、MCP Servers 与 SDK Tools

## 先给结论

成熟的 `agent platform`，不应该只靠一种工具接入模式。

更稳的做法通常是三层并存：

- `MCP servers`：协议化、可共享、边界清晰
- `SDK / HTTP tools`：平台内部的一等公民工具
- `safe CLI`：强动作、本地环境、受控执行

而 `Tool Gateway` 的价值，就是把这三类入口收进同一个治理层。

## 为什么不能把一切都塞进 MCP

`MCP` 很好，但不是所有东西都适合：

- 本地工作目录强依赖动作，`CLI` 往往更直接
- 平台内部高频工具，直接 `SDK` 或 HTTP 接口可能更轻
- 某些 long-running task 还需要更完整的 app-server / task layer

所以真正的平台问题不是“全量 MCP 化”，而是“怎么把多种工具面收成一致的 contract 和治理方式”。

## Tool Gateway 负责什么

### 1. 统一 contract

不管底层是 `MCP`、HTTP 还是 `CLI`，上层 agent 看到的都应该是统一的 `ToolSpec`。

### 2. 统一治理

- auth
- timeout
- retry
- budget
- audit
- rate limit
- tenant scope

### 3. 统一 trace

所有工具调用都应该能把 `thread id`、`agent id`、`tool id`、`trace id` 传到 `Langfuse` 或其他观测层。

### 4. 统一 policy

- 哪些工具默认允许
- 哪些工具必须审批
- 哪些工具只能在 sandbox 里跑

## 三类工具面的典型分工

### MCP servers

适合：

- 团队共享能力
- 远程服务接入
- 想把 integration 做成标准协议层

### SDK / HTTP tools

适合：

- 自家平台内部服务
- 高频稳定、schema 明确的能力
- 需要强 observability 和低接入成本的工具

### safe CLI

适合：

- 本地文件、repo、脚本、构建链路
- coding agent / ops agent 的强动作场景

但它必须被 sandbox、approval、allowlist 收紧。

## 我更推荐的默认策略

- 优先把团队共享、远程服务型能力做成 `MCP` 或内部 HTTP tools
- 优先把平台内部核心动作做成 `SDK / HTTP tools`
- 把 `CLI` 保留给真正需要本地执行面的任务

## 一个可操作的 tool model

```text
Tool Gateway
├── MCP Registry
├── Internal Tool Registry
├── CLI Executor
├── Policy / Approval
├── Auth / Secret Broker
└── Trace / Audit Export
```

## 和 Agent SDK 的关系

- `Agent SDK` 定义 `ToolSpec`
- `Tool Gateway` 把 `ToolSpec` 路由到真实 transport

这样平台 contract 和实际 transport 就能解耦。

## 推荐继续往下读

- [[Agent SDK 设计]]
- [[飞书与 Lark 作为 Agent Channel Adapter]]
- [[Agent 平台架构（LangGraph、Langfuse、ADK）]]
- [[MCP 与 CLI 模式]]
- [[Harness Engineering]]

## 关联

- [[../../AI-Learning/06-Topics/MCP（Model Context Protocol）|MCP（Model Context Protocol）]]
- [[../../AI-Learning/06-Topics/Tool Use|Tool Use]]
- [[../../AI-Learning/09-Systems/Google Agent Development Kit（ADK）|Google Agent Development Kit（ADK）]]
- [[Agent SDK 设计]]
- [[飞书与 Lark 作为 Agent Channel Adapter]]
- [[Agent 平台架构（LangGraph、Langfuse、ADK）]]
- [[MCP 与 CLI 模式]]
- [[Tool Calling and Action Execution]]
- [[Harness Engineering]]
- [[Agent Security、Sandbox 与 Approval Architecture]]
