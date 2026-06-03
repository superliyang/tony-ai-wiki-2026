---
title: Harness 工作流与自动化模式图
type: map
status: learning
tags:
  - ai/map
  - ai/agent
  - ai/harness
  - ai/automation
created: 2026-03-28
updated: 2026-03-28
---

# Harness 工作流与自动化模式图

```mermaid
flowchart LR
  A["Harness Workflow Modes"] --> B["Terminal-first
repo + shell + diff"]
  A --> C["Desktop / Browser-first
GUI + browser + takeover"]
  A --> D["Cloud-first
server-side tasks + App Server"]
  A --> E["Channel-first
bots + connectors + nodes"]

  B --> B1["Claude Code"]
  B --> B2["Gemini CLI"]
  B --> B3["Codex CLI"]

  C --> C1["ChatGPT agent"]
  C --> C2["OpenAI computer use"]
  C --> C3["Anthropic computer use"]
  C --> C4["OpenClaw apps"]

  D --> D1["Codex app / App Server"]
  D --> D2["Grok Agent Tools API"]
  D --> D3["managed background agents"]

  E --> E1["OpenClaw nodes / webhooks"]
  E --> E2["apps / connectors / MCP connectors"]

  F["Automation Plane"] --> F1["Hooks"]
  F --> F2["Cron / Heartbeat"]
  F --> F3["CI / GitHub Actions"]
  F --> F4["Background Agents"]
  F --> F5["Webhooks / Channel Events"]

  F1 --> G1["Claude Code hooks
OpenClaw hooks"]
  F2 --> G2["OpenClaw cron / heartbeat"]
  F3 --> G3["Claude Code Actions
run-gemini-cli"]
  F4 --> G4["Codex automations"]
  F5 --> G5["OpenClaw nodes
channel adapters"]
```

## 这张图怎么用

- 先看上半部分：任务更自然地属于哪一种工作流模式。
- 再看下半部分：这个模式通常怎样进入自动化闭环。
- 最后再回到具体厂商，判断它的优势是不是刚好匹配你的任务。

## 推荐顺序

1. [[../07-Topics/Harness Engineering|Harness Engineering]]
2. [[../07-Topics/Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel|Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel]]
3. [[../07-Topics/Hooks、Cron、CI 与 Background Agents：Harness 自动化闭环|Hooks、Cron、CI 与 Background Agents：Harness 自动化闭环]]
4. [[../07-Topics/Harness 工程案例：Codex、Claude Code、OpenClaw、Gemini CLI|Harness 工程案例：Codex、Claude Code、OpenClaw、Gemini CLI]]
5. [[Harness Engineering 与 Agent 扩展生态图]]
6. [[../06-Projects/Harness Lab/项目总览|Harness Lab]]

## 关联

- [[Harness Engineering 与 Agent 扩展生态图]]
- [[Harness Feedback Loop Map]]
- [[Agent Action Surfaces and Protocols Map]]
- [[../07-Topics/Harness Engineering|Harness Engineering]]
- [[../07-Topics/技能、插件、应用与自动化：Harness 的扩展面|技能、插件、应用与自动化：Harness 的扩展面]]
