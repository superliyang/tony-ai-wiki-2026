---
title: Harness 工程案例：Codex、Claude Code、OpenClaw、Gemini CLI
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent
  - ai/harness
  - ai/case-study
created: 2026-03-28
updated: 2026-03-28
---

# Harness 工程案例：Codex、Claude Code、OpenClaw、Gemini CLI

## 为什么要看案例，而不只看定义

`Harness Engineering` 说到底不是理论标签，而是不同厂商把 agent 放进不同工作台里的方式。

所以最有价值的问题是：

- 它把什么变成一等公民
- 它牺牲了什么
- 它最适合哪种任务环境

## 案例 1：Codex

`Codex` 最有代表性的地方，是 OpenAI 把 coding agent 从单个工具推进成了：

- `Codex app`
- cloud tasks
- `App Server`
- shell / computer / remote MCP
- skills library
- background work / automations

它的工程启发是：

- 入口不是单一 CLI，而是 multi-surface
- runtime 不是单次调用，而是 richer task session
- automation 不是补充功能，而是工作台的一部分

`Codex` 最像：`cloud-first coding harness`。

## 案例 2：Claude Code

`Claude Code` 把很多能力压进 terminal：

- `CLAUDE.md`
- slash commands
- subagents
- hooks
- MCP
- `GitHub Actions`
- SDK / headless mode

它的工程启发是：

- terminal 可以成为完整 harness，而不只是 prompt shell
- command system 可以成为轻量 skill surface
- hooks + Actions 可以把 repo automation 接进同一套工作流

`Claude Code` 最像：`terminal-first coding harness`。

## 案例 3：OpenClaw

`OpenClaw` 的不同之处在于它不是只服务 coding。

它把下面这些层同时做出来了：

- Gateway runtime
- typed tools / exec / browser / nodes
- skills
- plugins / bundle plugins / community plugins
- ClawHub
- macOS / WebChat / mobile surfaces
- hooks / heartbeat / cron / webhooks

它的工程启发是：

- harness 可以是 `self-hosted assistant operating layer`
- automation plane 不一定附属于 CI，它也可以是 assistant 自己的后台循环
- plugin bundle compatibility 能让不同生态发生“能力兼容”

`OpenClaw` 最像：`self-hosted assistant runtime`。

## 案例 4：Gemini CLI

`Gemini CLI` 现在更像一条从 developer entry 走向 workflow builder 的路线：

- terminal entry
- `GEMINI.md`
- extensions
- `run-gemini-cli` GitHub Action
- 邻接 `ADK` / `A2A` / `Visual Builder`

它的工程启发是：

- CLI 不只是终端工具，也可以是 CI / workflow 的共用入口
- framework、protocol、CLI、workflow builder 可以形成一条完整 Google 路线

`Gemini CLI` 最像：`CLI-first workflow bridge`。

## 典型真实工作流

### `Codex` 最顺的任务

- 多 agent 并行 coding
- review queue 驱动的 cloud backlog
- daily issue triage / CI summary / release brief
- 需要 app、CLI、IDE 和 App Server 共用状态的任务

### `Claude Code` 最顺的任务

- repo-local bugfix / refactor
- review follow-up
- 通过 commands / hooks / subagents 把团队规则沉淀进 terminal loop
- 在 GitHub Actions 里把 repo automation 接进同一条工作流

### `OpenClaw` 最顺的任务

- self-hosted assistant runtime
- channel-first personal assistant
- recurring summaries / daily ops / webhook-driven chores
- 把 skills、plugins、nodes、cron、heartbeat 收成长期在线系统

### `Gemini CLI` 最顺的任务

- CLI 和 GitHub workflow 之间的桥接
- 轻量 issue triage / PR review / workflow automation
- 和 `ADK` / `A2A` / `MCP` 更近的 Google 生态实验

## 一个对照表

| 系统 | 主战场 | 最强点 | 最值得学的地方 |
| --- | --- | --- | --- |
| `Codex` | cloud + app + coding | 多入口、background work、App Server | `cloud-first coding harness` |
| `Claude Code` | terminal + repo | commands / subagents / hooks / MCP | `terminal-first harness` |
| `OpenClaw` | self-hosted assistant runtime | skills / plugins / apps / automation 一体化 | `assistant operating layer` |
| `Gemini CLI` | terminal + GitHub workflow | CLI 与 workflow / framework 衔接 | `CLI -> automation -> framework` |

## 进一步往下读

如果你想从“feature 比较”进入“真实工作流比较”，下一步优先看：

- [[Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel]]
- [[../06-Projects/Harness Lab/Harness Lab 第一轮：Repo 修复、Browser 操作与 Daily Ops|Harness Lab 第一轮：Repo 修复、Browser 操作与 Daily Ops]]

## 这一页最重要的判断

真正成熟的 agent 系统，差异越来越不在“会不会调工具”，而在：

- 入口表面怎么长
- 扩展面怎么长
- 自动化面怎么长
- 信任边界怎么长

也就是说，学习这些系统时，最稳的比较方式不是模型榜单，而是：

`哪一种 harness 工作台被做得最顺、最可治理、最可扩展。`

## 关联

- [[Harness Engineering]]
- [[技能、插件、应用与自动化：Harness 的扩展面]]
- [[Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel]]
- [[Hooks、Cron、CI 与 Background Agents：Harness 自动化闭环]]
- [[../../AI-Learning/09-Systems/Codex|Codex]]
- [[../../AI-Learning/09-Systems/Claude Code|Claude Code]]
- [[../../AI-Learning/09-Systems/OpenClaw|OpenClaw]]
- [[../../AI-Learning/09-Systems/OpenClaw 的技能、插件、应用与自动化生态|OpenClaw 的技能、插件、应用与自动化生态]]
- [[../../AI-Learning/09-Systems/Gemini CLI|Gemini CLI]]
- [[../../AI-Learning/09-Systems/Agent 能力扩展对比：OpenClaw、Codex、Claude Code、Gemini CLI、Grok、Kimi|Agent 能力扩展对比：OpenClaw、Codex、Claude Code、Gemini CLI、Grok、Kimi]]
- [[Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel]]
- [[../08-Maps/Harness 工作流与自动化模式图|Harness 工作流与自动化模式图]]

## 资料

- [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)
- [Unlocking the Codex harness: how we built the App Server](https://openai.com/index/unlocking-the-codex-harness/)
- [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code Hooks](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Claude Code GitHub Actions](https://docs.anthropic.com/en/docs/claude-code/github-actions)
- [OpenClaw Docs](https://docs.openclaw.ai/)
- [OpenClaw Plugins](https://docs.openclaw.ai/plugins)
- [OpenClaw Automation](https://docs.openclaw.ai/automation/)
- [Gemini CLI](https://github.com/google-gemini/gemini-cli)
- [run-gemini-cli](https://github.com/google-github-actions/run-gemini-cli)
