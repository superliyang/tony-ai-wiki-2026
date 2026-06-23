---
title: Agent 能力扩展对比：OpenClaw、Codex、Claude Code、Gemini CLI、Grok、Kimi
type: system
status: learning
tags:
  - ai/system
  - ai/agent
  - ai/comparison
created: 2026-03-28
updated: 2026-03-28
---

# Agent 能力扩展对比：OpenClaw、Codex、Claude Code、Gemini CLI、Grok、Kimi

## 这页解决什么问题

如果只看营销词，很容易把这些系统混成一句话：

“它们都在做 agent。”

但从 `Harness Engineering` 视角看，这些系统的差异非常大。

真正该比的，不是“谁更像 AGI”，而是：

- 动作面怎么长
- 扩展面怎么长
- 自动化面怎么长
- 控制面和 trust boundary 怎么定

## 一张总表

| 系统 | 主入口 | 主要动作面 | 主要扩展面 | 自动化面 | 最像什么 |
| --- | --- | --- | --- | --- | --- |
| `OpenClaw` | gateway + apps + chat channels | typed tools、browser、exec、nodes | skills、plugins、bundle plugins、ClawHub | hooks、heartbeat、cron、webhooks | self-hosted assistant runtime |
| `Codex` | app + CLI + IDE + cloud | shell、computer use、remote MCP、GitHub/cloud tasks | skills、rules、apps / connectors、App Server | automations、background agents、App Server workflows | cloud coding harness |
| `Claude Code` | terminal | shell、MCP、repo tools | slash commands、subagents、hooks、CLAUDE.md | hooks、GitHub Actions、SDK/headless mode | terminal-first coding harness |
| `Gemini CLI` | terminal + GitHub workflows | CLI、extensions、MCP、ADK-adjacent tools | extensions、GEMINI.md、workflow configs | run-gemini-cli、CI / schedules | CLI-to-framework bridge |
| `Grok` Agent Tools | API | web_search、x_search、code_execution、files、remote MCP | tool surface more than app surface | server-side multi-agent loop | tool-rich API harness |
| `Kimi` | playground + open platform | long-context + CLI support + MCP-friendly config | playground configs、third-party MCP | platform workflow, less explicit local automation | open platform agent surface |

## 1. OpenClaw

### 最强的地方

- self-hosted
- 多渠道 assistant
- skills / plugins / ClawHub 完整
- hooks / heartbeat / cron 很强
- apps、nodes、Gateway 一起构成完整 runtime

### 最适合学什么

- long-running assistant runtime
- self-hosted harness
- skills/plugins/automation 如何形成生态

## 2. Codex

### 最强的地方

- `Codex app` 把 multi-agent / worktrees / review 做成了正式体验
- OpenAI 官方已经把 `skills` 和 `automations` 提到产品层
- `App Server` 把 richer task protocol 暴露了出来
- API 侧有 `shell`、`local_shell`、`computer_use`、`remote_mcp`
- ChatGPT developer mode 让 apps / MCP connectors 能带 write actions

### 最适合学什么

- cloud-hosted coding harness
- App Server / task protocol
- apps/connectors 如何变成企业动作面

## 3. Claude Code

### 最强的地方

- terminal-first
- `slash commands` 很成熟
- `subagents` 很适合 delegation
- `hooks` 很适合事件自动化
- `GitHub Actions` 和 `SDK` 让它可嵌入 CI / app

### 最适合学什么

- composable terminal harness
- 如何用 commands / subagents / hooks 形成高效率工作流

## 4. Gemini CLI

### 最强的地方

- CLI 开源入口
- `extensions` 开始形成生态
- `GEMINI.md` 作为项目级指令文件
- `run-gemini-cli` 把它接进 GitHub workflow
- 和 `ADK`、`A2A`、`MCP` 很自然衔接

### 最适合学什么

- CLI 和 framework 如何连起来
- Google 生态里的 agent 工具链

## 5. Grok Agent Tools API

### 最强的地方

- `tool-rich API`
- `x_search` 是独特优势
- `code_execution`、`files`、`collections_search` 很适合 data / research / ops
- `remote MCP` 和 `multi-agent` 模式让 API 自身就很 agentic

### 最适合学什么

- server-side tool orchestration
- OpenAI-compatible tool surface 的另一条实现路线

## 6. Kimi / Moonshot Open Platform

### 最强的地方

- long-context 路线仍然独特
- `Kimi Playground` 已支持 third-party MCP
- 官方 changelog 已记录 `kimi CLI support`
- Moonshot 还在主动写 `OpenClaw` 相关生态文章

### 最适合学什么

- 中国模型厂商如何把 open platform 做得更 agent-friendly
- long-context / CLI / MCP / OpenClaw 生态如何组合

## 7. 从 Harness 视角怎么选学习重点

### 如果你想学 runtime 设计

优先看：

- [[OpenClaw]]
- [[OpenClaw 的技能、插件、应用与自动化生态]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]

### 如果你想学 coding harness

优先看：

- [[Codex]]
- [[Claude Code]]
- [[Gemini CLI]]

### 如果你想学 apps / connectors / enterprise action surfaces

优先看：

- [[Codex]]
- [[ChatGPT Agent]]
- [[Kimi]]

### 如果你想学 tool-rich API

优先看：

- [[Grok Agent Tools API]]
- [[Google Agent Development Kit（ADK）]]
- [[../../AI-Engineering/07-Topics/Tool Gateway、MCP Servers 与 SDK Tools|Tool Gateway、MCP Servers 与 SDK Tools]]

## 8. 一句最关键的判断

这些系统不是在回答同一个问题：

- `OpenClaw`：agent runtime 应该怎么长期在线存在？
- `Codex`：怎么把多 agent coding 工作台做成产品？
- `Claude Code`：怎么把 terminal harness 做到高效可组合？
- `Gemini CLI`：怎么把 CLI、workflow automation 和 framework 接起来？
- `Grok`：怎么把 server-side tool orchestration 做成 API 能力？
- `Kimi`：怎么把 open platform、MCP、CLI 和长上下文结合起来？

## 推荐继续往下读

- [[OpenClaw]]
- [[OpenClaw 的技能、插件、应用与自动化生态]]
- [[Codex]]
- [[Claude Code]]
- [[Gemini CLI]]
- [[Grok Agent Tools API]]
- [[Kimi]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
- [[../../AI-Engineering/07-Topics/技能、插件、应用与自动化：Harness 的扩展面|技能、插件、应用与自动化：Harness 的扩展面]]
- [[../../AI-Engineering/08-Maps/Harness Engineering 与 Agent 扩展生态图|Harness Engineering 与 Agent 扩展生态图]]

## 资料

- [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)
- [Developer mode and MCP apps in ChatGPT](https://help.openai.com/en/articles/12584461-developer-mode-and-full-mcp-connectors-in-chatgpt-beta)
- [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Slash commands | Claude Code](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
- [Subagents | Claude Code](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Hooks | Claude Code](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Gemini CLI](https://github.com/google-gemini/gemini-cli)
- [run-gemini-cli](https://github.com/google-github-actions/run-gemini-cli)
- [ADK Overview](https://google.github.io/adk-docs/)
- [OpenClaw Skills](https://docs.openclaw.ai/skills)
- [OpenClaw Plugins](https://docs.openclaw.ai/plugins)
- [Plugin Bundles](https://docs.openclaw.ai/plugins/bundles)
- [Grok 4.1 Fast and Agent Tools API](https://x.ai/news/grok-4-1-fast/)
- [Remote MCP Tools | xAI](https://docs.x.ai/docs/guides/tools/remote-mcp-tools)
- [Kimi Open Platform release log](https://platform.moonshot.ai/blog/posts/changelog)
