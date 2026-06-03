---
title: OpenClaw
type: system
status: learning
tags:
  - ai/topic
  - ai/system
  - ai/agent
  - ai/assistant
  - ai/openclaw
created: 2026-03-18
updated: 2026-03-29
---

# OpenClaw

## 这个主题是什么

`OpenClaw` 是一个自托管 `self-hosted` 的个人 AI assistant / agent gateway。你可以把它理解成：它不是单纯的聊天产品，也不只是一个“会调工具的 prompt”，而是一套长期在线、跨消息渠道、带工具、带会话、带记忆、带自动化的 agent 运行时系统。

官方 GitHub README 把它描述为“你运行在自己设备上的 personal AI assistant”，而官方文档强调它通过一个长期运行的 `Gateway` 连接 WhatsApp、Telegram、Discord、iMessage 等消息渠道，并把这些入口接到 AI agent 上。

## 为什么它值得学

如果你已经理解了 `Agent`、`AI Assistant`、`Coding Agents` 这些概念，那么 `OpenClaw` 值得学的地方在于：它把这些概念推进到了“真正可运行的系统层”。

它让你看到：

- agent 不只是模型调用循环，而是一个长期在线的 control plane
- assistant 不只是聊天界面，而是跨渠道、跨设备的工作入口
- coding agent 不只是 IDE 插件，而可以嵌入更大的消息与自动化系统中
- 真正的 agent 系统必须处理会话、记忆、工具权限、设备能力和远程接入
- `skills + plugins + apps + automation` 可以一起构成完整 harness

## 如果你想继续挖“它到底怎么跑起来”

建议直接接着看：

- [[OpenClaw 的分层记忆设计]]
- [[OpenClaw 的分层记忆设计]]
- [[OpenClaw 工作原理与架构]]
- [[OpenClaw 的准自进化工作流]]
- [[Self-Improving-Agent（ClawHub Skill）]]
- [[OpenClaw 的技能、插件、应用与自动化生态]]
- [[OpenClaw、ChatGPT 与 Claude Code 的定位差异]]
- [[../07-Maps/OpenClaw Architecture Map|OpenClaw Architecture Map]]
- [[../07-Maps/OpenClaw 准自进化工作流图|OpenClaw 准自进化工作流图]]

## 先抓住它的 7 个关键点

### 1. Gateway 是核心

官方架构文档里，`Gateway` 是单个长期运行的控制平面。它负责拥有消息渠道、维护 provider 连接、处理控制端客户端、以及接收节点能力。

### 2. 它是“渠道化 assistant”而不只是网页聊天

它不是把 agent 限制在一个网页里，而是接到用户本来就在用的消息和设备入口里。

### 3. 工具系统是第一公民

官方 tools 文档里，`OpenClaw` 暴露的是 typed、first-class tools，而不是临时 prompt 拼接。

### 4. 会话和记忆是系统能力，不是附属功能

Gateway 维护 session source of truth；memory 默认落在 Markdown 文件里。

### 5. 技能面已经被产品化

官方 `Skills` 与 `ClawHub` 说明：

- skill 有明确加载位置和优先级
- 可以 per-agent，也可以 shared
- 可以通过 registry 搜索、安装、更新、发布

### 6. 插件与 bundle 让它变成生态系统

官方 `Plugins` 与 `Plugin Bundles` 页面说明：

- 有 native plugins
- 有 community plugins
- 还能读取 `Codex`、`Claude`、`Cursor` bundle 并映射到 native surfaces

### 7. 自动化面很强

`hooks`、`heartbeat`、`cron`、`webhooks` 一起把它推成了长期运行 runtime，而不是只会同步回答的聊天机器人。

## 典型工作流

- self-hosted personal assistant runtime
- channel-first assistant
- recurring summaries / daily ops / webhook chores
- skills、plugins、nodes、cron、heartbeat 组合出来的长期运行系统

## 推荐继续往下读

- [[../../AI-Engineering/07-Topics/Harness 工程案例：Codex、Claude Code、OpenClaw、Gemini CLI|Harness 工程案例：Codex、Claude Code、OpenClaw、Gemini CLI]]
- [[../../AI-Engineering/07-Topics/Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel|Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel]]
- [[../06-Topics/上下文工程|上下文工程]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
- [[OpenClaw 的分层记忆设计]]
- [[OpenClaw 的分层记忆设计]]
- [[OpenClaw 工作原理与架构]]
- [[OpenClaw 的准自进化工作流]]
- [[OpenClaw 的技能、插件、应用与自动化生态]]
- [[../07-Maps/OpenClaw Architecture Map|OpenClaw Architecture Map]]
- [[../07-Maps/OpenClaw 准自进化工作流图|OpenClaw 准自进化工作流图]]
- [[Agent 能力扩展对比：OpenClaw、Codex、Claude Code、Gemini CLI、Grok、Kimi]]

## 它最适合拿来学什么

- self-hosted agent runtime
- long-running assistant systems
- skills / plugins / app surfaces / automation 如何组成 harness
- 分层 durable memory、workspace files、memory recall 如何协同
- self-improving learnings、promotion、skill extraction 如何形成“准持续进化”
- memory / workspace / hooks / schedules 如何形成“准持续进化”效果

## 它和别的系统怎么区分

- `ChatGPT Agent` 更像 cloud-hosted general-purpose agent product
- `Claude Code` 更像 terminal-first coding harness
- `Codex` 更像 cloud coding harness + app server + multi-agent workbench
- `OpenClaw` 更像 self-hosted personal agent runtime + gateway ecosystem

## 相关

- [[OpenClaw 的分层记忆设计]]
- [[OpenClaw 的分层记忆设计]]
- [[OpenClaw 工作原理与架构]]
- [[OpenClaw 的准自进化工作流]]
- [[OpenClaw 的技能、插件、应用与自动化生态]]
- [[OpenClaw、ChatGPT 与 Claude Code 的定位差异]]
- [[Agent 能力扩展对比：OpenClaw、Codex、Claude Code、Gemini CLI、Grok、Kimi]]
- [[../07-Maps/OpenClaw Architecture Map|OpenClaw Architecture Map]]
- [[../07-Maps/OpenClaw 准自进化工作流图|OpenClaw 准自进化工作流图]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]

## 官方资料

- [OpenClaw Docs](https://docs.openclaw.ai/)
- [Gateway Architecture](https://docs.openclaw.ai/concepts/architecture)
- [Tools](https://docs.openclaw.ai/tools)
- [Session Management](https://docs.openclaw.ai/sessions)
- [Memory](https://docs.openclaw.ai/concepts/memory)
- [Skills](https://docs.openclaw.ai/skills)
- [Plugins](https://docs.openclaw.ai/plugins)
- [Plugin Bundles](https://docs.openclaw.ai/plugins/bundles)
- [ClawHub](https://docs.openclaw.ai/tools/clawhub)
- [Hooks](https://docs.openclaw.ai/automation/)
- [Heartbeat](https://docs.openclaw.ai/gateway/heartbeat)
- [Cron Jobs](https://docs.openclaw.ai/cron/)
- [Platforms](https://docs.openclaw.ai/platforms)
