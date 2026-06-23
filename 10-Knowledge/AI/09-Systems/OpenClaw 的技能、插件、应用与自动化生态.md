---
title: OpenClaw 的技能、插件、应用与自动化生态
type: system
status: learning
tags:
  - ai/system
  - ai/agent
  - ai/openclaw
  - ai/plugins
  - ai/automation
created: 2026-03-28
updated: 2026-03-29
---

# OpenClaw 的技能、插件、应用与自动化生态

## 这页解决什么问题

很多人提到“各种 OpenClaw 版本”，其实混在一起说了几种不同东西：

- core gateway/runtime
- macOS companion / WebChat / mobile nodes
- skills
- plugins
- bundle plugins
- hooks / cron / heartbeat
- 社区技能与社区插件

所以这页不把它神化成“很多 fork 的混战”，而是把它整理成：

`OpenClaw 到底提供了哪些正式扩展面。`

## 一句话判断

`OpenClaw` 最值得学的，不只是 Gateway，而是它把 `skills + plugins + apps + automation` 组合成了一个非常完整的 self-hosted agent operating layer。

## 1. Skills：工作方法层

官方 `Skills` 文档说明，OpenClaw 使用 `AgentSkills` 兼容的 skill folder，每个 skill 本质上就是一个带 `SKILL.md` 的目录。

最值得记住的点：

- skills 有明确加载位置与优先级
- `workspace skills`、`~/.openclaw/skills`、bundled skills 分层加载
- plugins 可以自带 skills
- skills 不是“聊天提示词集合”，而是带 supporting files 的能力包

这意味着 OpenClaw 的 skill system 很适合做：

- 团队方法沉淀
- agent-specific workflow
- per-workspace capability packs

## 2. ClawHub：公共技能注册表

官方 `ClawHub` 文档表明，OpenClaw 已经把技能生态做成了 public registry：

- 可搜索
- 可安装
- 可更新
- 可发布
- 有版本历史、stars、comments、moderation

所以它不是“本地乱放几个技能目录”，而是：

`skill distribution and discovery` 已经被产品化了。

这点很重要，因为它让 OpenClaw 很接近一个真正的 agent ecosystem，而不只是单个 runtime。

## 3. Plugins：受信扩展层

官方 `Plugins` 文档把 OpenClaw plugin 描述成 TypeScript runtime modules，并明确说插件是 in-process trusted code。

插件可以注册：

- Gateway RPC methods
- Gateway HTTP routes
- agent tools
- CLI commands
- background services
- context engines
- skills
- auto-reply commands

这意味着 OpenClaw 插件不是简单“接个 API”，而是真正能改系统行为边界的一等公民。

## 4. Bundle Plugins：兼容 Codex / Claude / Cursor 生态

官方 `Plugin Bundles` 页面是最近特别值得学的地方。

OpenClaw 明确支持一类 shared external package：`bundle plugins`。

而它特别有意思的一点是：

- `Codex`
- `Claude`
- `Cursor`

这些 bundle 足够相似，OpenClaw 会把它们当成一个 normalized model 处理，再把可支持的部分映射进 OpenClaw 的 native surfaces，例如：

- skills
- hook packs
- MCP config
- embedded settings

这里最关键的 trust boundary 是：

- native plugin：runtime code in-process 执行
- bundle：更多是 metadata / content pack，被 selective mapping

这意味着 OpenClaw 不只是自己的生态，还在主动做不同 agent ecosystem 的“兼容层”。

## 5. Community Plugins：社区接入层

官方 `Community plugins` 页面说明：

- 社区插件通过 npm 安装
- 要求 public repo、文档、issue tracker、维护信号
- 官方维护一个 quality bar

这说明 OpenClaw 不是只有官方扩展，而是在逐步形成 community plugin marketplace 的形态。

## 6. Companion Apps / Nodes：应用承载层

官方 `Platforms`、`macOS App`、`iOS App` 页面说明：

- 有 `macOS` menu-bar companion
- 有 `WebChat`
- 有 `iOS / Android` nodes
- Gateway 可以本地或远程
- companion app 可以暴露 native capabilities 给 agent 作为 node

这很关键，因为它把 OpenClaw 从“CLI runtime”推进成：

- agent gateway
- multi-surface assistant
- local-first but remotely reachable system

## 7. Automation：长时间运行层

OpenClaw 的自动化面是它最有个人特色的部分之一。

### Hooks

官方 `Hooks` 文档说明：

- hooks 是 event-driven automation system
- 自动发现、可启停、可通过 CLI 管理
- 有 bundled hooks，如：
  - `session-memory`
  - `bootstrap-extra-files`
  - `command-logger`
  - `boot-md`

### Heartbeat

heartbeat 更像低打扰定期唤醒与检查节奏。

### Cron

官方 `Cron Jobs` 文档说明：

- 持久化在 `~/.openclaw/cron/`
- 重启不丢 schedule

### Webhooks

官方 hooks 页面也把 external HTTP webhooks 单独列出。

所以 OpenClaw 的 automation 不是一条线，而是：

- in-gateway event hooks
- scheduled jobs
- keep-alive inspection loops
- external trigger endpoints

## 8. Slash commands / OpenProse 之类的“轻应用”

像 `OpenProse` 这种官方页面展示了另一种很有意思的组合：

- 一个 plugin
- 安装一个 skill pack
- 同时暴露一个 `/prose` slash command

这说明 OpenClaw 不是把 skill、plugin、command 三者拆得特别死，而是允许它们组合成一个更完整的 capability bundle。

## 你现在应该怎么理解“OpenClaw 的各种版本”

更准确的说法不是“OpenClaw 有很多互相替代的版本”，而是：

### 1. Runtime 形态

- gateway core
- local-first deployment
- remote gateway
- VPS / hybrid / VM hosting

### 2. Client / App 形态

- CLI
- WebChat
- macOS app
- iOS / Android nodes

### 3. Extension 形态

- skills
- plugin skills
- native plugins
- bundle plugins
- community plugins
- ClawHub registry

### 4. Automation 形态

- hooks
- heartbeat
- cron
- webhooks

## 为什么这页对学 Harness Engineering 很关键

因为 `OpenClaw` 几乎把 harness 的几个重要层都做成了具体对象：

- task environment：workspace / session / memory
- action surfaces：typed tools / nodes / browser / exec
- extension surfaces：skills / plugins / bundles / ClawHub
- app surfaces：macOS / WebChat / mobile nodes
- automation surfaces：hooks / heartbeat / cron / webhooks

这使它成为一个非常好的 `full-stack agent runtime case study`。

## 推荐继续往下读

- [[OpenClaw]]
- [[OpenClaw 工作原理与架构]]
- [[OpenClaw 的准自进化工作流]]
- [[OpenClaw、ChatGPT 与 Claude Code 的定位差异]]
- [[Agent 能力扩展对比：OpenClaw、Codex、Claude Code、Gemini CLI、Grok、Kimi]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
- [[../../AI-Engineering/07-Topics/技能、插件、应用与自动化：Harness 的扩展面|技能、插件、应用与自动化：Harness 的扩展面]]

## 相关

- [[OpenClaw]]
- [[OpenClaw 工作原理与架构]]
- [[OpenClaw 的准自进化工作流]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
- [[../../AI-Engineering/07-Topics/Long-Running Agent Operations|Long-Running Agent Operations]]
- [[../07-Maps/OpenClaw Architecture Map|OpenClaw Architecture Map]]
- [[../07-Maps/OpenClaw 准自进化工作流图|OpenClaw 准自进化工作流图]]

## 资料

- [OpenClaw Skills](https://docs.openclaw.ai/skills)
- [ClawHub](https://docs.openclaw.ai/tools/clawhub)
- [OpenClaw Plugins](https://docs.openclaw.ai/plugins)
- [Plugin Bundles](https://docs.openclaw.ai/plugins/bundles)
- [Community Plugins](https://docs.openclaw.ai/plugins/community)
- [Hooks](https://docs.openclaw.ai/automation/)
- [Cron Jobs](https://docs.openclaw.ai/cron/)
- [Platforms](https://docs.openclaw.ai/platforms)
- [macOS App](https://docs.openclaw.ai/platforms/macos)
- [OpenProse](https://docs.openclaw.ai/prose)
