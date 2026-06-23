---
title: Harness Engineering
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent
  - ai/harness
created: 2026-03-25
updated: 2026-03-28
---

# Harness Engineering

## 为什么这个词现在值得深学

`Harness Engineering` 已经不只是一个 coding agent 圈内热词了。

如果你把最近这一波 agent 产品放在一起看：

- `OpenAI` 在讲 `Codex harness`、`App Server`、`Shell`、`Computer Use`、`Remote MCP`
- `Anthropic` 在讲 `Claude Code` 的 `slash commands`、`subagents`、`hooks`、`MCP`、`GitHub Actions`
- `Google` 在讲 `Gemini CLI`、`ADK`、`Visual Builder`、`MCP`、`A2A`、`Computer Use`
- `OpenClaw` 在讲 `Gateway`、`skills`、`plugins`、`nodes`、`heartbeat`、`cron`、`ClawHub`
- `xAI` 在讲 `Agent Tools API`、`Remote MCP`、`code execution`、`x_search`、`multi-agent`

你会发现：竞争重点已经不只是“模型强不强”，而是“模型被放进了什么工作台”。

而这个工作台，就是 `harness`。

## 一句话定义

最实用的理解是：

`Harness = agent 被放进去工作的受控环境 + 动作面 + 扩展面 + 控制面 + 反馈回路。`

如果只看 prompt，你只能理解模型说了什么。

如果看 harness，你才能理解：

- agent 在哪里工作
- 能碰什么
- 能被谁扩展
- 什么时候需要审批
- 结果怎样被验证、回放、升级和回滚

## 现在一个成熟 harness 往往有 6 层

### 1. 任务环境层 `task environment`

- repo / workspace / branch / diff
- browser session / desktop session / app state
- external data sources
- user / org memory

### 2. 动作面 `action surfaces`

- `CLI / shell`
- `browser / computer use`
- `MCP servers`
- internal HTTP / SDK tools
- app-specific actions

### 3. 扩展面 `extension surfaces`

- `skills`
- `slash commands`
- `plugins`
- `apps / connectors`
- `subagents`
- `tool bundles`

### 4. 控制面 `control plane`

- sessions / threads / task identity
- permissions / approval / trust boundary
- budgets / timeouts / retries
- policies / allowlists / deny-lists

### 5. 自动化面 `automation plane`

- hooks
- cron / schedules
- GitHub Actions / CI
- background jobs
- heartbeat / keep-alive / watch loops

### 6. 反馈与治理层 `feedback and governance`

- tests / lint / evals
- regression suites
- artifact review
- trace / timeline / replay
- promotion gates / release gates

## 为什么 prompt engineering 不够了

只要 agent 开始：

- 改文件
- 跑命令
- 打浏览器
- 点桌面 UI
- 用插件或连接器调外部系统
- 在后台周期运行

决定质量的主要因素就不再是 prompt 本身，而是 harness 是否：

- 可观察
- 可恢复
- 可约束
- 可扩展
- 可治理

这也是为什么 `Context Engineering` 和 `Harness Engineering` 必须连起来看：

- `prompt` 决定你怎么说
- `context` 决定模型看见什么
- `harness` 决定系统如何让它工作、犯错、被纠正、被审计

## 如何看“厂商的 Agent 能力扩展”

最近半年最值得学的不是某一家又多了一个按钮，而是大家都在往类似方向收敛。

### OpenAI

更像：`cloud coding harness + App Server + apps/connectors`

代表能力：

- `Codex app`：多 agent、worktrees、skills、automations
- `Shell / Local Shell / Computer Use / Remote MCP`
- `ChatGPT developer mode`：apps 与 full MCP connectors
- `App Server`：把 task、event、approval、artifact 暴露给客户端

### Anthropic

更像：`terminal-first harness + composable automation`

代表能力：

- `Claude Code` lives in terminal
- `CLAUDE.md` / memory
- `slash commands`
- `subagents`
- `hooks`
- `MCP`
- `GitHub Actions` / `SDK`

### Google

更像：`CLI + framework + workflow builder`

代表能力：

- `Gemini CLI`
- `GEMINI.md`
- `extensions`
- `run-gemini-cli` GitHub Action
- `ADK`
- `A2A`
- `MCP`
- `Visual Builder`
- `Computer Use Toolset`

### OpenClaw

更像：`self-hosted assistant runtime + gateway + skill/plugin ecosystem`

代表能力：

- `Gateway`
- typed tools
- `skills`
- `ClawHub`
- `plugins`
- `plugin bundles`
- `macOS app / iOS / Android nodes`
- `hooks`
- `heartbeat`
- `cron`
- `webhooks`

### xAI

更像：`API-first server-side agent tools`

代表能力：

- `web_search`
- `x_search`
- `code_execution`
- `collections_search`
- `files`
- `Remote MCP tools`
- `multi-agent` model mode

### Moonshot / Kimi

更像：`open platform + CLI/playground + MCP-friendly ecosystem`

代表能力：

- `Kimi Playground`
- third-party `MCP` config
- `kimi CLI support`
- 围绕 `OpenClaw`、coding 和 long-context 的生态文章与落地姿态

## 这说明了什么

### 1. 动作面正在从单一 tool call 走向多表面

今天的 agent 系统，已经不只是“调一个 function calling tool”。

而是越来越常见地同时拥有：

- `CLI`
- `browser / computer`
- `MCP`
- `apps / connectors`
- `SDK / HTTP tools`

### 2. 扩展面正在产品化

以前很多所谓扩展，本质只是“给 prompt 多塞一点说明”。

现在越来越多厂商把扩展面做成正式产品对象：

- `skills`
- `plugins`
- `subagents`
- `commands`
- `connectors`
- `extensions`

### 3. 自动化面正在成为真正分水岭

真正拉开差距的，不只是 agent 会不会做一件事，而是它能不能：

- 定时跑
- 在事件发生后自动跑
- 在 CI 里跑
- 在后台持续跑
- 出错后留痕并可恢复

### 4. harness 视角下，OpenClaw 特别值得学

因为 `OpenClaw` 不是只做一个聊天入口，而是把：

- assistant
- runtime
- skills
- plugins
- apps / nodes
- automation
- long-running loops

收成了一个非常完整的系统样本。

所以如果你想深学 harness，`OpenClaw` 是很好的 `runtime case`；
如果你想理解 coding harness 的前沿，`Codex` 和 `Claude Code` 是很好的 `product case`；
如果你想看 framework 与 protocol 收敛，`Gemini CLI + ADK` 很有代表性。

## 学这一支时，最稳定的比较维度

比较厂商时，建议一直用同一套维度：

- `任务环境`：repo、browser、desktop、workspace、session
- `动作面`：CLI、MCP、computer use、HTTP/SDK、connectors
- `扩展面`：skills、plugins、commands、subagents、apps
- `自动化面`：hooks、cron、CI、background jobs、heartbeat
- `控制面`：permissions、approvals、budgets、sessions、resume
- `反馈面`：tests、evals、artifacts、replay、release gates
- `部署面`：cloud-hosted、terminal-first、self-hosted、framework-first

## 推荐学习顺序

1. [[../../AI-Learning/06-Topics/上下文工程|上下文工程]]
2. [[MCP 与 CLI 模式]]
3. [[Computer Use Runtime and Safety]]
4. [[App Server 与 Rich Agent Protocols]]
5. [[技能、插件、应用与自动化：Harness 的扩展面]]
6. [[Eval Harness 与 Regression Suites]]
7. [[../../AI-Learning/09-Systems/OpenClaw|OpenClaw]]
8. [[../../AI-Learning/09-Systems/OpenClaw 的技能、插件、应用与自动化生态|OpenClaw 的技能、插件、应用与自动化生态]]
9. [[../../AI-Learning/09-Systems/Claude Code|Claude Code]]
10. [[../../AI-Learning/09-Systems/Codex|Codex]]
11. [[../../AI-Learning/09-Systems/Gemini CLI|Gemini CLI]]
12. [[../../AI-Learning/09-Systems/Grok Agent Tools API|Grok Agent Tools API]]
13. [[../../AI-Learning/09-Systems/Agent 能力扩展对比：OpenClaw、Codex、Claude Code、Gemini CLI、Grok、Kimi|Agent 能力扩展对比：OpenClaw、Codex、Claude Code、Gemini CLI、Grok、Kimi]]
14. [[../08-Maps/Harness Engineering 与 Agent 扩展生态图|Harness Engineering 与 Agent 扩展生态图]]
15. [[../08-Maps/Harness Engineering 深度学习导航.canvas|Harness Engineering 深度学习导航（Canvas）]]
16. [[../08-Maps/Harness Engineering 深度学习导航.base|Harness Engineering 深度学习导航（Base）]]

## 相关

- [[MCP 与 CLI 模式]]
- [[Computer Use Runtime and Safety]]
- [[App Server 与 Rich Agent Protocols]]
- [[Tool Gateway、MCP Servers 与 SDK Tools]]
- [[Agent Security、Sandbox 与 Approval Architecture]]
- [[Eval Harness 与 Regression Suites]]
- [[Long-Running Agent Operations]]
- [[../08-Maps/Agent Action Surfaces and Protocols Map|Agent Action Surfaces and Protocols Map]]
- [[../08-Maps/Harness Feedback Loop Map|Harness Feedback Loop Map]]
- [[../08-Maps/Harness Engineering 与 Agent 扩展生态图|Harness Engineering 与 Agent 扩展生态图]]

## 资料

- [OpenAI Harness Engineering](https://openai.com/index/harness-engineering/)
- [Unlocking the Codex harness: how we built the App Server](https://openai.com/index/unlocking-the-codex-harness/)
- [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)
- [Shell | OpenAI API](https://platform.openai.com/docs/guides/tools-shell)
- [Computer use | OpenAI API](https://platform.openai.com/docs/guides/tools-computer-use)
- [Developer mode and MCP apps in ChatGPT](https://help.openai.com/en/articles/12584461-developer-mode-and-full-mcp-connectors-in-chatgpt-beta)
- [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Slash commands | Claude Code](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
- [Subagents | Claude Code](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Hooks | Claude Code](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Claude Code GitHub Actions](https://docs.anthropic.com/en/docs/claude-code/github-actions)
- [Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code/sdk)
- [Gemini CLI](https://github.com/google-gemini/gemini-cli)
- [ADK Overview](https://google.github.io/adk-docs/)
- [ADK Computer Use Toolset](https://google.github.io/adk-docs/tools/gemini-api/computer-use/)
- [OpenClaw Skills](https://docs.openclaw.ai/skills)
- [OpenClaw Plugins](https://docs.openclaw.ai/plugins)
- [OpenClaw Hooks](https://docs.openclaw.ai/automation/)
- [Grok Agent Tools](https://docs.x.ai/developers/tools/x-search)


## 实践入口

- [[Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel]]
- [[Hooks、Cron、CI 与 Background Agents：Harness 自动化闭环]]
- [[Harness 工程案例：Codex、Claude Code、OpenClaw、Gemini CLI]]
- [[../06-Projects/Harness Lab/项目总览|Harness Lab]]


## 推荐继续往下读

- [[Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel]]
- [[Hooks、Cron、CI 与 Background Agents：Harness 自动化闭环]]
- [[Harness 工程案例：Codex、Claude Code、OpenClaw、Gemini CLI]]
- [[Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel]]
- [[../06-Projects/Harness Lab/项目总览|Harness Lab]]
