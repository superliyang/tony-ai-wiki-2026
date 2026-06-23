---
title: AI Agent Systems Map
type: map
status: learning
tags:
  - ai/map
  - ai/agent
created: 2026-03-18
updated: 2026-03-22
---

# AI Agent Systems Map

```mermaid
flowchart TD
  A["Agent"] --> A1["Tool Use"]
  A --> A2["Agent Memory"]
  A --> A3["Planning and Control"]
  A --> B["AI Assistant"]
  A --> C["Coding Agents"]
  A --> A4["Multi-Agent Systems"]
  B --> D["OpenClaw"]
  B --> E["ChatGPT Agent"]
  C --> C1["Claude Code"]
  C --> C2["Codex"]
  C --> C3["Cursor"]
  C --> C4["Devin"]
  C --> D

  D --> D1["Gateway / Control Plane"]
  D --> D2["Channels / Messaging Surfaces"]
  D --> D3["Typed Tools"]
  D --> D4["Sessions / Memory"]
  D --> D5["Canvas / Browser / Nodes / Cron"]
  D --> D6["Local-first / Self-hosted"]

  E --> E1["visual browser / app connectors / take over"]
  C1 --> F1["terminal-first + MCP"]
  C2 --> F2["CLI + App Server / cloud tasks"]
  C3 --> F3["IDE-native + background agents"]
  C4 --> F4["autonomous software engineer"]
```

## 怎么读这张图

- `Agent` 是抽象能力层：模型 + 工具 + 状态 +执行循环
- 如果你想先把抽象能力骨架看清，再打开 [[AI Agent Capability Map]]
- `AI Assistant` 是产品层：面向用户的任务完成入口
- `Coding Agents` 是高价值垂直场景：代码理解、修改、测试、反馈循环
- 这条线现在可以继续拆成 `Claude Code / Codex / Cursor / Devin` 四种不同产品形态
- `OpenClaw` 值得学的地方，是它把 agent/assistant/coding-agent 推进到了“系统运行层”
- 如果你想看更宽的产品定位差异，再看 [[AI Agent Product Positioning Map]] 和 [[AI Coding Agent Positioning Map]]

## 推荐顺序

1. [[../06-Topics/Agent|Agent]]
2. [[../06-Topics/AI Assistant|AI Assistant]]
3. [[../06-Topics/Coding Agents|Coding Agents]]
4. [[../09-Systems/Claude Code|Claude Code]]
5. [[../09-Systems/Codex|Codex]]
6. [[../09-Systems/Cursor|Cursor]]
7. [[../09-Systems/Devin|Devin]]
8. [[../09-Systems/OpenClaw|OpenClaw]]
9. [[../09-Systems/OpenClaw 工作原理与架构|OpenClaw 工作原理与架构]]
10. [[../09-Systems/OpenClaw 的准自进化工作流|OpenClaw 的准自进化工作流]]
11. [[AI Coding Agent Positioning Map]]
12. [[OpenClaw Architecture Map]]
13. [[OpenClaw 准自进化工作流图]]
14. [[AI Agent Product Positioning Map]]

## 关联

- [[../06-Topics/AI 主题索引|AI 主题索引]]
- [[../06-Topics/Agent|Agent]]
- [[../06-Topics/AI Assistant|AI Assistant]]
- [[../06-Topics/Coding Agents|Coding Agents]]
- [[../09-Systems/OpenClaw|OpenClaw]]
- [[../09-Systems/OpenClaw 工作原理与架构|OpenClaw 工作原理与架构]]
- [[../09-Systems/OpenClaw 的准自进化工作流|OpenClaw 的准自进化工作流]]
- [[../09-Systems/OpenClaw、ChatGPT 与 Claude Code 的定位差异|OpenClaw、ChatGPT 与 Claude Code 的定位差异]]
- [[../09-Systems/ChatGPT Agent|ChatGPT Agent]]
- [[../09-Systems/Claude Code|Claude Code]]
- [[../09-Systems/Codex|Codex]]
- [[../09-Systems/Cursor|Cursor]]
- [[../09-Systems/Devin|Devin]]
- [[../09-Systems/Manus|Manus]]
- [[../09-Systems/AI Agent Systems 对比：OpenClaw、ChatGPT Agent、Claude Code、Manus|AI Agent Systems 对比：OpenClaw、ChatGPT Agent、Claude Code、Manus]]
- [[../09-Systems/AI Coding Agent Systems 对比：Claude Code、Codex、Cursor、Devin|AI Coding Agent Systems 对比：Claude Code、Codex、Cursor、Devin]]
- [[AI Coding Agent Positioning Map]]
- [[AI Agent Capability Map]]
- [[OpenClaw Architecture Map]]
- [[OpenClaw 准自进化工作流图]]
- [[AI Agent Product Positioning Map]]
- [[AI Ecosystem Map]]
