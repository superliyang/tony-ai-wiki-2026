---
title: Agent 扩展面：Skills、Plugins、Hooks 与 Automations
type: topic
status: learning
tags:
  - ai/topic
  - ai/agent
  - ai/plugins
  - ai/skills
  - ai/automation
created: 2026-04-03
updated: 2026-04-03
---

# Agent 扩展面：Skills、Plugins、Hooks 与 Automations

## 为什么这个子域值得独立

很多 agent 系统在 demo 阶段只需要：

- prompt
- context
- tools

但一旦进入长期使用，真正拉开差距的常常是扩展面：

- 工作方法能不能沉淀成 `skill`
- 能力能不能安装成 `plugin`
- runtime 事件能不能接 `hook`
- 周期任务能不能变成 `automation`

## 四个核心部件

### Skills

`skill` 更像：

- instruction bundle
- references
- helper scripts
- narrow methodology

它适合沉淀：

- 工作方法
- promotion rubric
- eval checklist
- 领域流程

### Plugins

`plugin` 更像：

- packaging layer
- capability shell
- discovery / installation unit
- hook orchestration unit

它适合承载：

- manifest
- hooks
- skills 组合
- scripts
- app / mcp 扩展入口

### Hooks

`hook` 是事件入口。

典型价值：

- 在 `UserPromptSubmit` 记录偏好
- 在 `PostToolUse` 捕获 failure 或 poisoning
- 在 write / edit 之后做 parity check

所以 hook 是连接 runtime 与 learning ledger 的关键桥。

### Automations

`automation` 让系统从单轮对话走向长期执行。

它适合：

- 定时任务
- recurring review
- shadow rollout
- periodic cleanup
- background operations

## 这几个东西之间的关系

更稳的理解不是谁替代谁，而是：

- `skill` 沉淀方法
- `plugin` 提供壳层与安装能力
- `hook` 提供事件入口
- `automation` 提供持续运行

所以一条典型演化路径会是：

`prompt -> tool workflow -> skill -> plugin -> hooks -> automation`

## 自改进系统为什么特别依赖扩展面

像 `Self-Improving-Agent`、`OpenClaw` 的 layered memory、我们的 `self-improving-memory-lab`，都不只是模型能力问题。

真正关键的是：

- 如何捕获信号
- 如何把信号写入 bounded ledger
- 如何 shadow review
- 如何 promotion / rollback

这几步都离不开扩展面。

## 推荐继续读

- [[从 Learnings 到 AutoSkill：技能自提炼]]
- [[Self-Improving Systems]]
- [[../09-Systems/Codex Skills 与 Plugins|Codex Skills 与 Plugins]]
- [[../09-Systems/Self-Improving Memory Lab Plugin|Self-Improving Memory Lab Plugin]]
- [[../09-Systems/OpenClaw 的技能、插件、应用与自动化生态|OpenClaw 的技能、插件、应用与自动化生态]]
- [[../../AI-Engineering/07-Topics/技能、插件、应用与自动化：Harness 的扩展面|技能、插件、应用与自动化：Harness 的扩展面]]
- [[../../AI-Engineering/07-Topics/扩展面设计：Skills、Plugins、Hooks、Apps 与 Automation|扩展面设计：Skills、Plugins、Hooks、Apps 与 Automation]]
- [[从提示词到 Harness：Agent 能力的渐进式主线]]
