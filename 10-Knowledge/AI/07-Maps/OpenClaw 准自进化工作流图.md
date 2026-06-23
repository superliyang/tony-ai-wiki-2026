---
title: OpenClaw 准自进化工作流图
type: map
status: learning
tags:
  - ai/map
  - ai/openclaw
  - ai/automation
  - ai/memory
created: 2026-03-22
updated: 2026-03-29
---

# OpenClaw 准自进化工作流图

```mermaid
flowchart TD
  A["User Message / External Event"] --> B["Gateway Session"]
  H["Heartbeat"] --> B
  I["Cron Job"] --> B

  B --> C["Agent Runtime"]
  C --> D["Workspace Files"]
  C --> E["Memory Files"]
  C --> L[".learnings/*"]
  C --> F["Typed Tools"]

  D --> D1["AGENTS.md / SOUL.md / TOOLS.md"]
  D --> D2["BOOT.md / HEARTBEAT.md"]
  E --> E1["MEMORY.md"]
  E --> E2["memory/YYYY-MM-DD.md"]
  L --> L1["LEARNINGS.md"]
  L --> L2["ERRORS.md"]
  L --> L3["FEATURE_REQUESTS.md"]

  C --> G["Action / Reply / File Update"]
  G --> E
  G --> D
  G --> L

  J["Hooks"] --> L
  J --> D
  B --> J

  L --> P["Promotion Gate"]
  P --> D
  P --> EG["Eval Gate"]
  EG --> S["Skill Extraction"]
  S --> SK["skills/<name>/SKILL.md"]
  EG --> RB["Rollback / Demotion"]

  D --> K["Next Turn Reads Updated Context"]
  E --> K
  SK --> K
  K --> B
```

## 怎么读这张图

- heartbeat 和 cron 都可以唤醒一次新的 agent turn
- 每次 turn 都不是从零开始，而是读入已经变化过的 workspace 与 memory
- hooks 会在某些事件上自动补充状态
- `.learnings/*` 会先作为 learning ledger 暂存经验
- promotion gate 决定哪些经验升级成 workspace rules，哪些进一步抽成 skill
- eval gate 决定这些升级是不是能真的放开 rollout
- agent 后续行为之所以“越来越像会自我调整”，关键不在模型变了，而在上下文文件、durable rules 和 skill surfaces 变了

## 这张图最想说明什么

OpenClaw 最接近“自进化”的地方，不是神秘的内核成长，而是：

- 可以持续写
- 可以持续读
- 可以持续触发
- 可以在下次运行里利用上次沉淀

## 关联

- [[../09-Systems/OpenClaw|OpenClaw]]
- [[../09-Systems/OpenClaw 工作原理与架构|OpenClaw 工作原理与架构]]
- [[../09-Systems/OpenClaw 的准自进化工作流|OpenClaw 的准自进化工作流]]
- [[../09-Systems/Self-Improving-Agent（ClawHub Skill）|Self-Improving-Agent（ClawHub Skill）]]
- [[Self-Improving Memory 风险与治理图]]
- [[../../AI-Engineering/07-Topics/自改进 Skill 的 Eval Gate、Release Gate 与 Rollback|自改进 Skill 的 Eval Gate、Release Gate 与 Rollback]]
- [[OpenClaw Architecture Map]]
