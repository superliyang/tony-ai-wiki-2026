---
title: Gemini CLI
type: system
status: learning
tags:
  - ai/system
  - ai/agent
  - ai/google
  - ai/cli
created: 2026-03-28
updated: 2026-03-28
---

# Gemini CLI

## 它是什么

`Gemini CLI` 是 Google 面向开发者的 terminal-first agent/coding tool。官方 GitHub 仓库把它定位成开源命令行工具，而 `run-gemini-cli` GitHub Action 又把它进一步推进到了自动化工作流里。

## 为什么值得单独学

如果你把它只看成“Google 版 Claude Code”，会低估它。

它真正值得学的地方在于：

- 它是 `CLI` 入口
- 又有 `extensions`
- 又有 `GEMINI.md` 这类项目记忆
- 还能进入 `GitHub Actions`
- 它和 `ADK`、`A2A`、`MCP` 之间天然更近

也就是说，它不只是一个聊天命令，而是一条 `CLI -> automation -> framework` 的生态入口。

## 关键能力面

### 1. Terminal-first

它首先是开发者工具，不是网页聊天框。

### 2. 项目记忆 `GEMINI.md`

`run-gemini-cli` 官方 Action 文档明确把 `GEMINI.md` 当成 repository-specific instructions and context 的载体。

这点很重要，因为它说明：

- Google 也在把“项目级规则文件”做成一等公民
- 这条路和 `CLAUDE.md`、`AGENTS.md`、workspace rules 是同类收敛

### 3. Extensions

官方 GitHub Action 和 extensions 组织都显示：Gemini CLI 正在形成 extension ecosystem。

这意味着它不是只靠内建能力，而是允许：

- 安装扩展
- 接入其他 CLI / MCP servers
- 在不同项目里复用能力包

### 4. Automation

`run-gemini-cli` 官方 GitHub Action 很值得学，因为它把 Gemini CLI 变成了：

- issue triage agent
- PR review assistant
- scheduled workflow actor
- `@gemini-cli` comment-driven collaborator

### 5. 和 ADK 的关系

如果说 `Gemini CLI` 更像开发者入口，那么 `ADK` 更像构建 agent system 的 framework 层。

所以可以粗略理解成：

- `Gemini CLI`：入口与工作流工具
- `ADK`：runtime / multi-agent / MCP / A2A layer

## 它和 Claude Code 的差异

- `Claude Code` 更成熟地把 `slash commands + subagents + hooks` 做成了 terminal harness
- `Gemini CLI` 更强地连接 `Google` 自身的 framework 与 workflow builder 生态

## 它和 Codex 的差异

- `Codex` 更偏 cloud task operator + app server + app experience
- `Gemini CLI` 更偏 open CLI + extensions + GitHub workflow automation

## 它和 OpenClaw 的差异

- `OpenClaw` 更像长期在线的 self-hosted runtime / gateway
- `Gemini CLI` 更像 terminal-native workbench + automation entry

## 什么时候优先研究它

- 你关心 Google 生态里的 agent 开发路径
- 你想看 `CLI + extensions + GitHub Actions` 这条线怎么长
- 你想把 `Gemini` 能力和自己的代码仓库 / CI 流程接起来

## 推荐继续往下读

- [[Google Agent Development Kit（ADK）]]
- [[Agent 能力扩展对比：OpenClaw、Codex、Claude Code、Gemini CLI、Grok、Kimi]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
- [[../../AI-Engineering/07-Topics/技能、插件、应用与自动化：Harness 的扩展面|技能、插件、应用与自动化：Harness 的扩展面]]
- [[../../AI-Engineering/07-Topics/Agent 平台架构（LangGraph、Langfuse、ADK）|Agent 平台架构（LangGraph、Langfuse、ADK）]]

## 相关

- [[Google Agent Development Kit（ADK）]]
- [[Kimi]]
- [[Claude Code]]
- [[Codex]]
- [[OpenClaw]]
- [[../../AI-Engineering/07-Topics/MCP 与 CLI 模式|MCP 与 CLI 模式]]
- [[../../AI-Engineering/07-Topics/App Server 与 Rich Agent Protocols|App Server 与 Rich Agent Protocols]]

## 资料

- [Gemini CLI](https://github.com/google-gemini/gemini-cli)
- [run-gemini-cli](https://github.com/google-github-actions/run-gemini-cli)
- [ADK Overview](https://google.github.io/adk-docs/)
- [ADK MCP](https://google.github.io/adk-docs/mcp/)
- [ADK Computer Use Toolset](https://google.github.io/adk-docs/tools/gemini-api/computer-use/)
- [ADK Visual Builder](https://google.github.io/adk-docs/visual-builder/)
