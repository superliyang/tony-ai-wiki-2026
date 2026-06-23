---
title: Claude Code
type: system
status: learning
tags:
  - ai/product
  - organization/anthropic
  - ai/system
  - ai/agent
  - ai/coding-agent
created: 2026-03-01
updated: 2026-05-15
organization: "[[Anthropic]]"
modality:
  - coding
family: Claude
related_papers:
  - "[[Constitutional AI]]"
related_people:
  - "[[Dario Amodei]]"
---

# Claude Code

## 简介

`Claude Code` 是 Anthropic 面向开发者的 terminal-first agentic coding tool。官方 overview 直接说它“lives in your terminal”，并且可以编辑文件、运行命令、创建提交、接 MCP 数据源、在 CI 中自动化执行。

## 为什么重要

- 它代表了 `terminal-first coding harness` 的成熟形态
- 它把 `skills + plugins + commands + subagents + hooks + MCP + GitHub Actions` 收成了一套很完整的开发者工作流
- 它非常适合拿来理解：为什么 coding agent 的竞争点已经从“会不会写代码”变成了“工作台好不好用”

## 2026-05-15 补充：Claude Code 已经是生态系统

最新需要抓住的不是某个单点功能，而是 Claude Code 的能力已经很像一套 `AI Coding Workbench`：

- `CLAUDE.md / memory`：沉淀项目规则和开发者偏好
- `skills`：沉淀可复用专业方法
- `plugins`：把 skills、commands、agents、hooks、MCP 等能力打包分发
- `subagents`：沉淀专门角色和上下文隔离
- `hooks`：把安全、质量、审计和自动化接进事件流
- `MCP`：接外部工具、资料、日志、issue 和知识库
- `GitHub Actions / SDK`：把 Claude Code 嵌进 PR、CI 和后台自动化

所以要用好 Claude Code，重点不是“多装插件”，而是建设一套从个人到团队都能复用的 agent engineering 能力。

## 关键能力面

### 1. 终端就是主入口

Claude Code 明确不是另一个网页聊天窗，而是直接在 terminal 中工作。

### 2. `CLAUDE.md` / memory 是项目规则面

`/init` 与 `/memory` 这条线，本质上是在把项目规则、代码规范、偏好和上下文沉淀成长期可复用的工作文件。

这里很值得注意的一点是：`Claude Code` 的 memory 并不是通用聊天产品那种“记住用户偏好”逻辑，而更像 `repo / project memory`。这让它在 coding harness 场景里非常强，因为它把长期信息压在：

- codebase 规则
- working tree 约定
- command / workflow 偏好
- subagent 可继承的任务边界

这也说明 `project memory` 是 agent engineering 里很重要的一条线。

### 3. Skills / slash commands 是任务方法层

官方 `Slash commands` 文档说明：

- 可以有 built-in commands
- 也可以把 Markdown 文件变成 custom slash commands
- project scope 和 personal scope 都支持
- commands 还能指定 `allowed-tools`、`description`、`model`
- MCP prompts 还能被动态暴露成 slash commands

现在更推荐把可复用方法沉淀为 `skills`：skill 可以带说明、流程、脚本、模板和参考资料；slash command 更适合作为轻量触发入口。

这说明 Claude Code 的扩展面已经从 command system 走向更完整的 skill / plugin ecosystem。

### 4. Subagents 是 specialization surface

官方 `Subagents` 文档说明：

- subagent 有独立 purpose
- 有单独 context window
- 可单独配置工具权限
- 可在任务匹配时被委托执行

这让 Claude Code 很适合研究：

- task decomposition
- delegation
- context preservation

### 5. Hooks 是 automation surface

官方 `Hooks` 文档说明：

- hooks 按事件与 matcher 组织
- 可以在 `PreToolUse`、`PostToolUse`、`UserPromptSubmit`、`Stop` 等节点触发
- 本质上是事件驱动自动化

### 6. MCP 是 integration surface

官方 overview 与 slash commands 都明确提到 `MCP`：

- Claude Code 可以接 Google Drive、Figma、Slack 等外部数据源
- connected MCP server 暴露的 prompts 还能变成 commands
- subagents 也能继承 MCP tools

### 7. GitHub Actions 与 SDK 是 embedding surface

官方 `GitHub Actions` 文档表明：

- `@claude` mention 可以触发 workflow
- Claude Code GitHub Actions 建在 Claude Code SDK 之上
- SDK 提供 headless mode、TypeScript、Python 入口

这说明 Claude Code 不只是最终产品，也能嵌入你自己的自动化系统。

## 典型工作流

- repo-local bugfix / refactor
- review follow-up
- hooks + Actions 串起来的 repo automation
- 通过 commands / subagents 固化团队规则

## 推荐继续往下读

- [[Claude Code 生态全景]]
- [[Claude Code 能力安装清单]]
- [[Claude Code 自定义能力工作台：Skills、Plugins、Hooks、MCP]]
- [[../07-Maps/Claude Code 生态能力图|Claude Code 生态能力图]]
- [[../../AI-Engineering/07-Topics/Claude Code Harness 工程实践|Claude Code Harness 工程实践]]
- [[../../AI-Engineering/07-Topics/Harness 工程案例：Codex、Claude Code、OpenClaw、Gemini CLI|Harness 工程案例：Codex、Claude Code、OpenClaw、Gemini CLI]]
- [[../../AI-Engineering/07-Topics/Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel|Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel]]
- [[Codex]]
- [[OpenClaw]]
- [[LangGraph]]
- [[LangMem]]
- [[Agent 能力扩展对比：OpenClaw、Codex、Claude Code、Gemini CLI、Grok、Kimi]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
- [[../../AI-Engineering/07-Topics/技能、插件、应用与自动化：Harness 的扩展面|技能、插件、应用与自动化：Harness 的扩展面]]
- [[../../AI-Engineering/07-Topics/MCP 与 CLI 模式|MCP 与 CLI 模式]]

## 它最值得学的地方

一句话说：

`Claude Code` 让我们看到，terminal harness 也可以拥有很强的扩展性、自动化能力和团队复用能力。

它最强的不是一个单独 feature，而是这组组合：

- terminal
- skills
- plugins
- commands
- subagents
- hooks
- MCP
- GitHub Actions
- SDK

## 它和 Codex 的差异

- `Claude Code` 更偏 terminal-first、local repo loop、composable commands
- `Codex` 更偏 cloud task operator、app server、app-based multi-agent workbench

## 它和 OpenClaw 的差异

- `Claude Code` 是 coding harness
- `OpenClaw` 是 self-hosted assistant runtime / gateway

## 什么时候优先研究它

- 你主要关心 coding agent
- 你想研究 `commands / subagents / hooks / MCP` 组合
- 你想把 agent 接进 terminal、CI、review flow

## 相关

- [[Claude 系列]]
- [[Coding Agents]]
- [[Developer Tools]]
- [[Codex]]
- [[OpenClaw]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
- [[../../AI-Engineering/07-Topics/App Server 与 Rich Agent Protocols|App Server 与 Rich Agent Protocols]]

## 官方资料

- [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code Memory](https://docs.anthropic.com/en/docs/claude-code/memory)
- [Claude Code skills](https://docs.anthropic.com/en/docs/claude-code/skills)
- [Claude Code plugins](https://code.claude.com/docs/en/plugins)
- [Slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
- [Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Hooks](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [GitHub Actions](https://docs.anthropic.com/en/docs/claude-code/github-actions)
- [Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code/sdk)
- [Claude Code MCP](https://docs.anthropic.com/en/docs/claude-code/mcp)
