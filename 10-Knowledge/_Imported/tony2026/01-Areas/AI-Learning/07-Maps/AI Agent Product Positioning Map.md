---
title: AI Agent Product Positioning Map
type: map
status: learning
tags:
  - ai/map
  - ai/agent
  - ai/comparison
created: 2026-03-22
updated: 2026-03-22
---

# AI Agent Product Positioning Map

```mermaid
flowchart TD
  A["AI Agent Systems"] --> B["Cloud General Agent"]
  A --> C["Developer Workflow Agent"]
  A --> D["Autonomous Task / Software Agent"]
  A --> E["Runtime / Gateway"]

  B --> B1["ChatGPT Agent"]
  C --> C1["Claude Code"]
  C --> C2["Codex"]
  C --> C3["Cursor"]
  D --> D1["Manus"]
  D --> D2["Devin"]
  E --> E1["OpenClaw"]

  E1 --> E2["self-hosted"]
  E1 --> E3["multi-channel"]
  E1 --> E4["sessions / memory / hooks / heartbeat"]

  B1 --> B2["ChatGPT main entry"]
  B1 --> B3["cloud-hosted"]

  C1 --> C4["terminal / repo / commands"]
  C2 --> C5["cloud tasks / GitHub / parallelism"]
  C3 --> C6["editor / background agents"]

  D1 --> D3["sandbox execution"]
  D2 --> D4["autonomous software engineering"]
```

## 怎么读这张图

- 这不是“谁更强”的图，而是“谁主要在解决什么问题”的图
- `ChatGPT Agent` 更偏通用入口型
- `Claude Code`、`Codex`、`Cursor` 更偏 developer workflow，但入口和执行方式不同
- `Manus`、`Devin` 更偏更高自治的任务 / 软件工程代理
- `OpenClaw` 更偏运行时基础设施型

## 关联

- [[../09-Systems/ChatGPT Agent|ChatGPT Agent]]
- [[../09-Systems/Claude Code|Claude Code]]
- [[../09-Systems/Codex|Codex]]
- [[../09-Systems/Cursor|Cursor]]
- [[../09-Systems/Devin|Devin]]
- [[../09-Systems/Manus|Manus]]
- [[../09-Systems/OpenClaw|OpenClaw]]
- [[../09-Systems/AI Agent Systems 对比：OpenClaw、ChatGPT Agent、Claude Code、Manus|AI Agent Systems 对比：OpenClaw、ChatGPT Agent、Claude Code、Manus]]
- [[AI Coding Agent Positioning Map]]
- [[../09-Systems/AI Coding Agent Systems 对比：Claude Code、Codex、Cursor、Devin|AI Coding Agent Systems 对比：Claude Code、Codex、Cursor、Devin]]
