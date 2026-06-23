---
title: 技能、插件、应用与自动化：Harness 的扩展面
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent
  - ai/harness
  - ai/plugins
  - ai/automation
created: 2026-03-28
updated: 2026-03-28
---

# 技能、插件、应用与自动化：Harness 的扩展面

## 为什么要把这层单独拿出来

很多人研究 agent 时，只盯着：

- 模型
- prompt
- tool calling

但现在真正把产品做出差异的，往往是这些“看起来像周边”的东西：

- skills
- plugins
- apps / connectors
- slash commands
- subagents
- hooks
- cron / schedules
- GitHub Actions / CI automation

这些东西如果只零散看，会像很多不同 feature。

从 harness 视角看，它们其实都属于：

`让 agent 的能力被安装、复用、组合、调度和治理的扩展面。`

## 4 种最常见的扩展面

### 1. 技能面 `skill surface`

它解决的是：

- 如何把一段稳定工作方法沉淀下来
- 如何让 agent 在需要时自动选用
- 如何让团队共享“这个任务怎么做”

典型形态：

- `OpenClaw skills`
- `Codex skills`
- `Claude Code` 的 project commands / memory / reusable prompts
- `Gemini CLI` 的 `GEMINI.md`

### 2. 插件面 `plugin surface`

它解决的是：

- 如何把外部能力装进系统
- 如何通过 manifest / config 进行发现和启用
- 哪些扩展能进入 runtime，哪些只能映射成受控能力

典型形态：

- `OpenClaw plugins`
- `OpenClaw bundle plugins`
- `ChatGPT apps / connectors`
- `Claude Code MCP servers`
- `Gemini CLI extensions`

### 3. 应用面 `app surface`

它解决的是：

- 用户从哪里和 agent 交互
- 桌面、终端、IDE、网页、消息通道怎么接起来
- agent 是否只是 API，还是完整产品入口

典型形态：

- `Codex app`
- `Claude Code` terminal + IDE integration
- `ChatGPT` app / connectors / agent mode
- `OpenClaw` macOS app / WebChat / iOS / Android nodes
- `Gemini CLI` + GitHub Action + ADK Visual Builder

### 4. 自动化面 `automation surface`

它解决的是：

- agent 如何在没有人盯着的时候继续跑
- 怎么基于事件触发工作流
- 怎么定时巡检、批量执行、背景运行

典型形态：

- `OpenClaw hooks / heartbeat / cron / webhooks`
- `Claude Code hooks / GitHub Actions / headless SDK`
- `Codex automations / background agents / app server`
- `Gemini CLI` GitHub Action / scheduled workflows
- `xAI` server-side multi-agent tool loops

## 这 4 层在工程上各自负责什么

### 技能

负责沉淀：

- instructions
- playbook
- scripts
- reusable workflow fragments

### 插件

负责接入：

- tools
- provider auth
- channels
- native capabilities
- bundle metadata

### 应用

负责承载：

- UX
- sessions
- human supervision
- diff / artifact review
- multi-surface interaction

### 自动化

负责持续化：

- scheduled work
- event-driven work
- monitoring loops
- CI/CD integration
- long-running background tasks

## 为什么这层和 `MCP` 不冲突

很多人一看到插件，就会问：

“那是不是所有东西都该变成 MCP server？”

不是。

从 harness 角度看：

- `MCP` 是协议化接入层
- `skills` 是工作方法层
- `plugins` 是安装与映射层
- `apps` 是交互承载层
- `automation` 是持续执行层

它们解决的不是同一个问题。

## OpenClaw 为什么特别适合学这层

`OpenClaw` 在这块的结构非常完整：

- `skills`：workspace、shared、bundled、ClawHub
- `plugins`：native plugins、community plugins、bundle plugins
- `apps`：CLI、WebChat、macOS companion、mobile nodes
- `automation`：hooks、heartbeat、cron、webhooks

它几乎把“扩展面”这个概念做成了一门系统设计课。

## Claude Code 为什么也很有代表性

`Claude Code` 虽然不是 self-hosted gateway，但它把另一种扩展形态做得很清楚：

- `slash commands`：很像轻量 skill
- `subagents`：很像任务级 specialization pack
- `hooks`：很像事件自动化
- `MCP`：很像 protocolized integration
- `GitHub Actions` + `SDK`：很像 automation / embedding layer

也就是说，Claude Code 代表的是：

`terminal-first harness 如何在不做“大平台”的情况下，仍然拥有强扩展性。`

## Codex / ChatGPT 为什么代表“应用化扩展”

OpenAI 这一侧很有意思，因为它把扩展面同时放进了：

- `Codex app`
- `CLI`
- `IDE extension`
- `App Server`
- `ChatGPT apps / MCP connectors`

这里最值得学的点是：

- skills 不再只是 repo 内文件，而成了 app-level capability
- automations 不再只是脚本，而变成 cloud/background task
- connectors 不再只是读数据，而开始支持 write/modify action

## Google 为什么代表“框架化扩展”

Google 这一侧更像：

- `Gemini CLI`：开发者入口
- `extensions`：装能力
- `GEMINI.md`：项目约束
- `run-gemini-cli`：CI automation
- `ADK`：framework / protocol layer
- `Visual Builder`：workflow UI layer

所以它代表的是：

`从 CLI 到 framework，再到 visual workflow builder 的一整条扩展链。`

## 一个最实用的判断框架

当你看到任何 agent 产品的“新能力”时，先问：

1. 它属于哪一层？
   - skill
   - plugin
   - app
   - automation
2. 它扩展的是：
   - action surface
   - task surface
   - context surface
   - deployment surface
3. 它落在什么 trust boundary 内？
   - in-process trusted plugin
   - content bundle
   - remote MCP server
   - cloud app / connector
4. 它是否可审计、可关闭、可回放？

## 推荐继续往下读

- [[Harness Engineering]]
- [[MCP 与 CLI 模式]]
- [[App Server 与 Rich Agent Protocols]]
- [[Tool Gateway、MCP Servers 与 SDK Tools]]
- [[../../AI-Learning/09-Systems/OpenClaw 的技能、插件、应用与自动化生态|OpenClaw 的技能、插件、应用与自动化生态]]
- [[../../AI-Learning/09-Systems/Agent 能力扩展对比：OpenClaw、Codex、Claude Code、Gemini CLI、Grok、Kimi|Agent 能力扩展对比：OpenClaw、Codex、Claude Code、Gemini CLI、Grok、Kimi]]
- [[../08-Maps/Harness Engineering 与 Agent 扩展生态图|Harness Engineering 与 Agent 扩展生态图]]

## 相关

- [[Harness Engineering]]
- [[Eval Harness 与 Regression Suites]]
- [[Long-Running Agent Operations]]
- [[Agent Security、Sandbox 与 Approval Architecture]]
- [[../../AI-Learning/09-Systems/OpenClaw|OpenClaw]]
- [[../../AI-Learning/09-Systems/Claude Code|Claude Code]]
- [[../../AI-Learning/09-Systems/Codex|Codex]]
- [[../../AI-Learning/09-Systems/Gemini CLI|Gemini CLI]]
- [[../../AI-Learning/09-Systems/Grok Agent Tools API|Grok Agent Tools API]]
