---
title: Agent 平台
type: topic
status: learning
tags:
  - ai/topic
  - ai/agent
  - ai/platform
created: 2026-03-25
updated: 2026-03-25
---

# Agent 平台

## 这里说的 Agent 平台是什么

`Agent 平台` 不是单个 agent，也不是单个 SDK，而是一整套让 agent 能够被开发、接入、运行、观测、治理和演进的系统。

如果把 `prompt`、`context`、`tool use`、`MCP`、`browser / computer use` 看成 agent 的能力面，那么 `Agent 平台` 讨论的就是：这些能力如何被收进一个可持续维护的工作台。

## 它通常至少包含哪几层

- `channel layer`：Feishu / Lark、Web、API 这些入口
- `gateway layer`：身份、tenant、thread、request normalization
- `runtime layer`：图执行、session、checkpoint、interrupt、resume
- `tool layer`：MCP servers、内部 SDK / HTTP tools、受控 CLI
- `control layer`：approval、policy、budget、secret、sandbox
- `observability layer`：trace、prompt、eval、regression、artifact
- `interop layer`：A2A、remote agent、不同 runtime 的适配层

## 为什么它最近变得更重要

因为 agent 讨论已经从“怎么 prompt”推进到了“怎么把 agent 真正变成系统”。

这时你会同时遇到几类问题：

- `Google ADK` 这类 runtime / framework 适合做什么
- `LangGraph` 这类状态图 runtime 为什么会成为平台内核候选
- `Langfuse` 这类 tracing / eval / prompt 平台为什么要从第一天接入
- `MCP`、`CLI`、`browser` 这些动作面如何同时存在
- `Feishu / Lark`、Web、internal API 这些渠道如何进入同一个控制平面

## 它和 Harness Engineering 的关系

- `Harness Engineering` 更偏 agent 工作台本身：环境、反馈回路、评测、审批、可读性
- `Agent 平台` 更偏把这个工作台做成可复用、可接入、可运维的系统产品

可以把它理解成：

- `harness` 更像单个 agent 或单类 agent 的工作台
- `platform` 更像多个 agent、多个渠道、多个租户共享的一层公共基础设施

## 什么时候你已经进入 Agent 平台问题

- 你不满足于单个 demo agent，而是想承接多个业务 agent
- 你需要 thread / session / approval / auditability
- 你需要把 tool 接入做成团队可复用的 integration layer
- 你需要把 trace、prompt、eval 和回归从第一天接入
- 你需要把 Feishu / Web / API 统一到同一个 request model

## 这一层最值得先学什么

推荐顺序：

1. [[Agent]]
2. [[提示词工程]]
3. [[上下文工程]]
4. [[Tool Use]]
5. [[MCP（Model Context Protocol）]]
6. [[Browser Agents 与 Computer Use]]
7. [[Agent Memory]]
8. [[A2A（Agent-to-Agent）与协作协议]]
9. [[../09-Systems/Google Agent Development Kit（ADK）|Google Agent Development Kit（ADK）]]
10. [[../09-Systems/LangGraph|LangGraph]]
11. [[../09-Systems/Langfuse|Langfuse]]
12. [[../../AI-Engineering/07-Topics/Agent SDK 设计|Agent SDK 设计]]
13. [[../../AI-Engineering/07-Topics/Tool Gateway、MCP Servers 与 SDK Tools|Tool Gateway、MCP Servers 与 SDK Tools]]
14. [[../../AI-Engineering/07-Topics/飞书与 Lark 作为 Agent Channel Adapter|飞书与 Lark 作为 Agent Channel Adapter]]
15. [[../../AI-Engineering/07-Topics/Agent 平台架构（LangGraph、Langfuse、ADK）|Agent 平台架构（LangGraph、Langfuse、ADK）]]

## 先给一个平台侧判断

如果目标是做自己的 `agent platform`，一个很稳的第一阶段工程判断通常是：

- `LangGraph` 更像主 runtime
- `Langfuse` 更像 observability / eval control surface
- `ADK` 更适合做互操作层、Google 生态层、`A2A` 兼容层，而不是一上来就变成唯一平台内核

这不是官方结论，而是我基于这些系统职责做的工程推断。

## 关联系统

- [[../09-Systems/Google Agent Development Kit（ADK）|Google Agent Development Kit（ADK）]]
- [[../09-Systems/LangGraph|LangGraph]]
- [[../09-Systems/Langfuse|Langfuse]]
- [[../09-Systems/OpenClaw|OpenClaw]]
- [[../09-Systems/ChatGPT Agent|ChatGPT Agent]]
- [[../09-Systems/Codex|Codex]]
- [[../09-Systems/Claude Code|Claude Code]]

## 关联工程页

- [[../../AI-Engineering/07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
- [[../../AI-Engineering/07-Topics/MCP 与 CLI 模式|MCP 与 CLI 模式]]
- [[../../AI-Engineering/07-Topics/App Server 与 Rich Agent Protocols|App Server 与 Rich Agent Protocols]]
- [[../../AI-Engineering/07-Topics/Agent SDK 设计|Agent SDK 设计]]
- [[../../AI-Engineering/07-Topics/Agent 平台架构（LangGraph、Langfuse、ADK）|Agent 平台架构（LangGraph、Langfuse、ADK）]]
- [[../../AI-Engineering/08-Maps/Agent 平台技术栈图|Agent 平台技术栈图]]

## 相关地图

- [[../07-Maps/Agent Prompt-Context-Harness Map|Agent Prompt-Context-Harness Map]]
- [[../07-Maps/Agent 平台生态图|Agent 平台生态图]]
- [[../../AI-Engineering/08-Maps/Agent Context and Integration Engineering Map|Agent Context and Integration Engineering Map]]
- [[../../AI-Engineering/08-Maps/Agent 平台技术栈图|Agent 平台技术栈图]]

## 资料

- [Agent Development Kit (ADK)](https://google.github.io/adk-docs/)
- [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview)
- [LangGraph Durable Execution](https://docs.langchain.com/oss/python/langgraph/durable-execution)
- [Langfuse Self-Hosting](https://langfuse.com/docs/self-hosting)
- [Lark Developer](https://open.larksuite.com/?lang=en-US)
