---
title: OpenClaw 的分层记忆设计
type: system
status: learning
tags:
  - ai/system
  - ai/openclaw
  - ai/memory
  - ai/agent
created: 2026-03-29
updated: 2026-03-29
---

# OpenClaw 的分层记忆设计

## 为什么这页值得单独拆出来

`OpenClaw` 本身已经讲了 gateway、sessions、skills、plugins、automation。

但如果你想真正研究 `AI memory design`，`OpenClaw` 值得单独拆开的地方是：它把 memory 做成了 workspace 中显式存在、可读可写、可审计的 durable layer。

这在当前 agent 系统里非常有代表性。

## 它的记忆不是“藏在模型脑子里”

官方 memory 文档最值得记住的点就是：

- 文件是 source of truth
- 模型只是在需要时读取、写入和检索这些文件
- durable memory 明确落在 workspace 里

这意味着 `OpenClaw` 的 memory 本质上是：

`workspace-native durable state`

## 一个实用的分层理解

### 1. `session source of truth`

Gateway 维护 session 边界与 routing，这一层更接近 thread / session state，而不是 durable memory 本身。

### 2. `daily append-only memory`

`memory/YYYY-MM-DD.md` 更像 episodic log：

- 今天发生了什么
- 哪些事项值得保留
- 原始经验如何先被追加记录下来

### 3. `MEMORY.md`

这是更接近长期稳定记忆的层：

- 用户偏好
- 持续约束
- 稳定规则
- 已确认事实

### 4. `.learnings`

如果你沿着 `Self-Improving-Agent` 这条线继续看，会发现 `.learnings/LEARNINGS.md`、`ERRORS.md`、`FEATURE_REQUESTS.md` 其实位于一个很关键的中间层：

- 它们还不是稳定 memory
- 也还不是最终 procedural rules
- 更像是等待 triage、promotion、extraction 的 learning ledger

### 5. `workspace rule files`

像 `AGENTS.md`、`SOUL.md`、`TOOLS.md`、`USER.md`、`BOOT.md`、`HEARTBEAT.md` 这些文件，严格说不只是 memory，也是一种 procedural / policy memory。

### 6. `memory_search` / `memory_get`

这类工具说明 recall 不是“模型自己隐式想起来”，而是显式检索 durable files。

## 为什么这套分层很值得学

因为它同时解决了几个工程问题：

- durable memory 可见
- recall 有明确入口
- 背景整理可通过 hooks / heartbeat / cron 推动
- 记忆纠偏可以通过编辑文件完成
- 不必把所有长期状态都塞回 prompt

## 这套设计最像哪类记忆

### semantic memory

- `MEMORY.md`
- 稳定规则和偏好

### episodic memory

- `memory/YYYY-MM-DD.md`
- 每天的经历、片段、事件

### procedural memory

- `AGENTS.md`
- `BOOT.md`
- `HEARTBEAT.md`
- workflow checklist

也就是说，`OpenClaw` 的强项不是只做一层 memory，而是把几种 memory 都做成了 workspace 可操作对象。

## 它和 Claude Code / ADK / LangGraph 的差别

- `Claude Code` 更偏 repo / project rule memory
- `ADK` 更偏 state / compaction / artifacts 的应用框架视角
- `LangGraph` 更偏 execution state + checkpoint
- `OpenClaw` 更偏 durable markdown memory + workspace operating layer

## 为什么它容易被说成“分层记忆”

因为你能很自然地看到：

- session state
- daily logs
- durable memory
- procedural files
- recall tools
- background upkeep

这些层并不是被混成一个上下文窗口，而是被拆成不同对象和不同生命周期。

如果再加上 `.learnings` 这一层，你会更容易理解：OpenClaw 不是只有“记忆”，而是已经很接近一套 `capture -> promote -> recall` 的 durable learning system。

## 推荐继续往下读

- [[OpenClaw]]
- [[OpenClaw 工作原理与架构]]
- [[OpenClaw 的准自进化工作流]]
- [[Self-Improving-Agent（ClawHub Skill）]]
- [[../06-Topics/从 Learnings 到 AutoSkill：技能自提炼|从 Learnings 到 AutoSkill：技能自提炼]]
- [[../06-Topics/AI 记忆设计|AI 记忆设计]]
- [[../06-Topics/自我进化与持续学习的记忆设计|自我进化与持续学习的记忆设计]]
- [[../../AI-Engineering/07-Topics/Session and Memory Design|Session and Memory Design]]
- [[../../AI-Engineering/07-Topics/长期运行 Agent 的记忆系统|长期运行 Agent 的记忆系统]]
- [[../../AI-Engineering/07-Topics/记忆写入、召回、压缩与 Consolidation|记忆写入、召回、压缩与 Consolidation]]

## 官方资料

- [OpenClaw Memory](https://docs.openclaw.ai/concepts/memory)
- [OpenClaw Architecture](https://docs.openclaw.ai/concepts/architecture)
- [OpenClaw Workspace](https://docs.openclaw.ai/agent/workspace)
- [OpenClaw Hooks](https://docs.openclaw.ai/automation/)
- [OpenClaw Heartbeat](https://docs.openclaw.ai/gateway/heartbeat)
- [OpenClaw Cron](https://docs.openclaw.ai/cron/)
