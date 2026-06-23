---
title: Agent Platform
type: project
status: learning
project_stage: design
created: 2026-03-25
updated: 2026-03-25
---

# Agent Platform

## 项目定位

这是一个“可交给 Cursor / Codex / Claude Code 落地实现”的 `Agent 平台` 设计包，不是代码仓库本身。

它的目标不是把所有实现都写在知识库里，而是把下面这些东西沉淀清楚：

- 需求文档
- 架构设计文档
- API 与数据模型
- 实施路线图
- AI 编程助手可执行的任务包

## 当前边界

这个项目默认围绕以下技术判断展开：

- `LangGraph` 作为主 runtime
- `Langfuse` 作为 tracing / eval / prompt / experiment 平台
- `Google ADK` 作为 adapter runtime / A2A / Google 生态兼容层
- `Feishu / Lark` 作为 channel adapter
- `MCP + SDK / HTTP tools + safe CLI` 作为工具面

## 文档清单

- [[Agent Platform V1 需求文档]]
- [[Agent Platform V1 架构设计文档]]
- [[Agent Platform V1 API 与数据模型]]
- [[Agent Platform V1 实施路线图]]
- [[Agent Platform V1 Cursor 实现任务包]]

## 推荐顺序

1. [[Agent Platform V1 需求文档]]
2. [[Agent Platform V1 架构设计文档]]
3. [[Agent Platform V1 API 与数据模型]]
4. [[Agent Platform V1 实施路线图]]
5. [[Agent Platform V1 Cursor 实现任务包]]

## 关联

- [[../../07-Topics/Agent 平台架构（LangGraph、Langfuse、ADK）|Agent 平台架构（LangGraph、Langfuse、ADK）]]
- [[../../07-Topics/Agent SDK 设计|Agent SDK 设计]]
- [[../../07-Topics/Tool Gateway、MCP Servers 与 SDK Tools|Tool Gateway、MCP Servers 与 SDK Tools]]
- [[../../07-Topics/飞书与 Lark 作为 Agent Channel Adapter|飞书与 Lark 作为 Agent Channel Adapter]]
- [[../../08-Maps/Agent 平台技术栈图|Agent 平台技术栈图]]
