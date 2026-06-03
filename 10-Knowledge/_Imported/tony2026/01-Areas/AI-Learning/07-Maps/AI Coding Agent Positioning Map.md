---
title: AI Coding Agent Positioning Map
type: map
status: learning
tags:
  - ai/map
  - ai/agent
  - ai/coding-agent
  - ai/comparison
created: 2026-03-22
updated: 2026-03-22
---

# AI Coding Agent Positioning Map

```mermaid
flowchart TD
  A["Coding Agent Systems"] --> B["Terminal-first Pairing"]
  A --> C["IDE-native Workflow"]
  A --> D["Cloud Task Delegation"]
  A --> E["Autonomous Software Engineer"]

  B --> B1["Claude Code"]
  C --> C1["Cursor"]
  D --> D1["Codex"]
  E --> E1["Devin"]

  B1 --> B2["repo / commands / tests"]
  C1 --> C2["editor / background agents"]
  D1 --> D2["cloud / parallel tasks / GitHub"]
  E1 --> E2["managed session / long-running engineering work"]
```

## 怎么读这张图

- 这不是能力排行榜，而是入口与工作方式图
- `Claude Code` 最适合拿来理解 terminal-first coding agent
- `Cursor` 最适合拿来理解 IDE-native agent
- `Codex` 最适合拿来理解 cloud-first / delegated coding agent
- `Devin` 最适合拿来理解更强自治的软件工程 agent

## 相关

- [[../09-Systems/Claude Code|Claude Code]]
- [[../09-Systems/Codex|Codex]]
- [[../09-Systems/Cursor|Cursor]]
- [[../09-Systems/Devin|Devin]]
- [[../09-Systems/AI Coding Agent Systems 对比：Claude Code、Codex、Cursor、Devin|AI Coding Agent Systems 对比：Claude Code、Codex、Cursor、Devin]]
- [[AI Agent Product Positioning Map]]
