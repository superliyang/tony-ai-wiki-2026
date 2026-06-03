---
title: OpenClaw Architecture Map
type: map
status: learning
tags:
  - ai/map
  - ai/openclaw
  - ai/architecture
created: 2026-03-18
updated: 2026-03-22
---

# OpenClaw Architecture Map

```mermaid
flowchart TD
  A["Channels"] --> B["Gateway"]
  A1["WhatsApp / Telegram / Discord / iMessage"] --> A
  C["Clients"] --> B
  C1["CLI / Web UI / macOS App / Automations"] --> C
  D["Nodes"] --> B
  D1["macOS / iOS / Android / headless"] --> D

  B --> E["Routing"]
  B --> F["Sessions"]
  B --> G["Agent Runtime"]
  B --> H["Heartbeat / Cron / Hooks"]
  B --> I["Health / Presence / Events"]

  G --> J["Workspace"]
  J --> J1["AGENTS.md"]
  J --> J2["SOUL.md"]
  J --> J3["TOOLS.md"]
  J --> J4["HEARTBEAT.md / BOOT.md"]
  J --> J5["MEMORY.md / daily memory"]

  G --> K["Typed Tools"]
  K --> K1["browser / exec / process"]
  K --> K2["canvas / nodes / web"]
  K --> K3["memory / sessions / cron"]

  F --> L["Gateway is source of truth"]
  F --> L1["DM scope / per-peer isolation"]
  F --> L2["group vs DM boundaries"]

  J5 --> M["Memory tools"]
  M --> M1["memory_search"]
  M --> M2["memory_get"]

  H --> N["Proactive loop"]
  N --> N1["heartbeat"]
  N --> N2["cron"]
  N --> N3["session-memory / boot-md / hooks"]
```

## 怎么读这张图

- `Gateway` 是整个系统的控制平面与事实中心
- Channels、Clients、Nodes 都不是各自独立跑 agent，而是接到同一个 Gateway
- Agent runtime 真正吃的是 workspace、tools、sessions、memory
- 主动能力并不是“魔法自进化”，而是 heartbeat、cron、hooks 形成的持续运行机制

## 关于“自进化”

- 官方文档没有把核心机制正式命名为 `self-evolution`
- 更接近的官方机制是：workspace 可编辑、memory 写盘、hooks、heartbeat、cron、boot-md
- 如果 agent 借由这些机制持续改自己的工作文件和记忆，它会表现出一种“准自我迭代”的效果

## 关联

- [[../09-Systems/OpenClaw|OpenClaw]]
- [[../09-Systems/OpenClaw|OpenClaw]]
- [[../09-Systems/OpenClaw 工作原理与架构|OpenClaw 工作原理与架构]]
- [[../09-Systems/OpenClaw 的准自进化工作流|OpenClaw 的准自进化工作流]]
- [[OpenClaw 准自进化工作流图]]
- [[AI Agent Systems Map]]
