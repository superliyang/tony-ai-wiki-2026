---
title: Agent 平台生态图
type: map
status: learning
tags:
  - ai/map
  - ai/agent
  - ai/platform
created: 2026-03-25
updated: 2026-03-25
---

# Agent 平台生态图

```mermaid
flowchart TD
  A["Agent Platform"] --> T["Topics"]
  A --> S["Systems"]
  A --> E["Engineering"]

  T --> TP["提示词工程"]
  T --> TC["上下文工程"]
  T --> TM["MCP"]
  T --> TA["A2A"]
  T --> TT["Agent 平台"]

  S --> SADK["Google ADK"]
  S --> SLG["LangGraph"]
  S --> SLF["Langfuse"]
  S --> SOC["OpenClaw"]

  E --> ER["Agent Runtime Architecture"]
  E --> EH["Harness Engineering"]
  E --> ESDK["Agent SDK 设计"]
  E --> ETG["Tool Gateway / MCP / SDK Tools"]
  E --> ECH["Feishu / Lark Channel Adapter"]
  E --> EPA["Agent 平台架构"]

  SADK --> TA
  SLG --> ER
  SLG --> EH
  SLF --> EH
  SLF --> EPA
  TM --> ETG
  TA --> EPA
  EH --> EPA
  ESDK --> EPA
  ECH --> EPA
```

## 怎么读这张图

- `Topic` 层回答：平台为什么会出现
- `System` 层回答：具体用哪些 runtime / framework / observability system
- `Engineering` 层回答：怎么把这些东西真正拼成一个平台

## 推荐顺序

1. [[../06-Topics/Agent 平台|Agent 平台]]
2. [[../09-Systems/Google Agent Development Kit（ADK）|Google Agent Development Kit（ADK）]]
3. [[../09-Systems/LangGraph|LangGraph]]
4. [[../09-Systems/Langfuse|Langfuse]]
5. [[../../AI-Engineering/07-Topics/Agent SDK 设计|Agent SDK 设计]]
6. [[../../AI-Engineering/07-Topics/Tool Gateway、MCP Servers 与 SDK Tools|Tool Gateway、MCP Servers 与 SDK Tools]]
7. [[../../AI-Engineering/07-Topics/飞书与 Lark 作为 Agent Channel Adapter|飞书与 Lark 作为 Agent Channel Adapter]]
8. [[../../AI-Engineering/07-Topics/Agent 平台架构（LangGraph、Langfuse、ADK）|Agent 平台架构（LangGraph、Langfuse、ADK）]]

## 关联

- [[AI Agent Systems Map]]
- [[AI Agent Capability Map]]
- [[Agent Prompt-Context-Harness Map]]
- [[../../AI-Engineering/08-Maps/Agent 平台技术栈图|Agent 平台技术栈图]]
