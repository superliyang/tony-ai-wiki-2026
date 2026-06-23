---
title: AI Agent Capability Map
type: map
status: learning
tags:
  - ai/map
  - ai/agent
created: 2026-03-22
updated: 2026-03-25
---

# AI Agent Capability Map

```mermaid
flowchart TD
  A["Agent"] --> P["提示词工程"]
  A --> Q["上下文工程"]
  A --> B["Tool Use"]
  A --> C["Agent Memory"]
  A --> D["Planning and Control"]
  A --> E["Multi-Agent Systems"]
  A --> H["A2A"]
  A --> F["AI Assistant"]
  A --> G["Coding Agents"]

  P --> P1["instruction / examples / format / role"]
  Q --> Q1["state / retrieval / files / tools / memory"]
  B --> B1["search / browser / exec / API / MCP / computer use"]
  C --> C1["thread / semantic / episodic / durable memory"]
  D --> D1["plan / act / observe / decide"]
  E --> E1["planner / worker / reviewer / coordinator"]
  H --> H1["agent card / task / events / artifacts / trust"]
  G --> G1["Claude Code / Codex / Cursor / Devin"]
  F --> F1["ChatGPT Agent / OpenClaw / Manus"]
```

## 怎么读这张图

- `Agent` 是总概念
- `提示词工程` 决定任务说明是否清晰
- `上下文工程` 决定系统是否把对的信息、状态和工具带给模型
- `Tool Use` 决定系统是否真正能行动
- `Agent Memory` 决定系统能否跨回合和跨时间持续工作
- `Planning and Control` 决定系统是否能在多步任务中保持稳定
- `Multi-Agent Systems` 解决内部角色分工
- `A2A` 解决跨 agent / 跨 runtime 的协作边界
- `AI Assistant` 和 `Coding Agents` 是两个高价值产品化方向

## 推荐顺序

1. [[../06-Topics/Agent|Agent]]
2. [[../06-Topics/提示词工程|提示词工程]]
3. [[../06-Topics/上下文工程|上下文工程]]
4. [[../06-Topics/Tool Use|Tool Use]]
5. [[../06-Topics/Agent Memory|Agent Memory]]
6. [[../06-Topics/Planning and Control|Planning and Control]]
7. [[../06-Topics/AI Assistant|AI Assistant]]
8. [[../06-Topics/Coding Agents|Coding Agents]]
9. [[../06-Topics/Multi-Agent Systems|Multi-Agent Systems]]
10. [[../06-Topics/A2A（Agent-to-Agent）与协作协议|A2A（Agent-to-Agent）与协作协议]]
11. [[AI Agent Systems Map]]
12. [[AI Agent Product Positioning Map]]
13. [[AI Coding Agent Positioning Map]]
14. [[Agent Prompt-Context-Harness Map]]

## 关联

- [[../06-Topics/AI 主题索引|AI 主题索引]]
- [[../06-Topics/Agent|Agent]]
- [[../06-Topics/提示词工程|提示词工程]]
- [[../06-Topics/上下文工程|上下文工程]]
- [[../06-Topics/Tool Use|Tool Use]]
- [[../06-Topics/Agent Memory|Agent Memory]]
- [[../06-Topics/Planning and Control|Planning and Control]]
- [[../06-Topics/Multi-Agent Systems|Multi-Agent Systems]]
- [[../06-Topics/A2A（Agent-to-Agent）与协作协议|A2A（Agent-to-Agent）与协作协议]]
- [[AI Agent Systems Map]]
- [[AI Agent Product Positioning Map]]
- [[AI Coding Agent Positioning Map]]
- [[Agent Prompt-Context-Harness Map]]
- [[../../AI-Engineering/07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]
- [[../../AI-Engineering/07-Topics/MCP 与 CLI 模式|MCP 与 CLI 模式]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
