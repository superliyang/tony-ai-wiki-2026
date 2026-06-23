---
title: Hooks、Cron、CI 与 Background Agents：Harness 自动化闭环
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent
  - ai/automation
  - ai/harness
created: 2026-03-28
updated: 2026-03-28
---

# Hooks、Cron、CI 与 Background Agents：Harness 自动化闭环

## 为什么自动化面值得单独学

很多 agent 看起来会用工具，但一到真正生产里，差异就出现在这几个问题上：

- 什么事件触发它
- 它能跑多久
- 它失败后怎样重试、回放、升级和人工接管
- 它怎么把结果发回用户或系统

这就是 `automation plane` 的价值。

## 5 类最常见的自动化触发

### 1. Hook-driven

触发源来自运行时内部事件，例如：

- before / after tool call
- after message
- before commit
- on session lifecycle

代表：

- `Claude Code hooks`
- `OpenClaw hooks`

### 2. Schedule-driven

触发源来自固定节奏：

- cron
- heartbeat
- daily review
- polling / watchdog

代表：

- `OpenClaw cron`
- `OpenClaw heartbeat`
- 各类 background check loops

### 3. Repo / CI-driven

触发源来自工程事件：

- PR opened
- issue comment
- scheduled workflow
- release gate check

代表：

- `Claude Code GitHub Actions`
- `run-gemini-cli` GitHub Action
- `Codex` cloud / app-side automation

### 4. App / Cloud-driven

触发源来自托管平台自身：

- background task
- server-side queue
- long-running session continuation

代表：

- `Codex app` automations / background work
- `App Server` style runtime services
- `xAI` server-side multi-agent loops

### 5. Channel-driven

触发源来自对话入口或 webhook：

- bot mention
- incoming webhook
- external event push

代表：

- `OpenClaw` webhooks / nodes
- apps / connectors / bot adapters

## 各家最值得学的自动化样式

### OpenClaw

`OpenClaw` 的自动化面非常完整：

- hooks
- heartbeat
- cron jobs
- webhooks

它的启发是：

`assistant runtime` 不应该只有“等用户说话”，也应该有自己的节奏、回访和后台循环。

### Claude Code

`Claude Code` 的自动化更偏开发者环境：

- hooks
- `GitHub Actions`
- SDK / headless mode

它的强项是把 repo 工作流直接接进自动化链：

- comment-driven review
- PR automation
- scripted coding loops

### Codex

`Codex` 的自动化更像 cloud-first coding harness：

- app-side automation
- background work
- richer `App Server` runtime
- shell / computer / MCP surfaces 进入同一工作台

它的启发是：

`automation` 不只是 CI job，而是托管 agent work queue。

### Gemini CLI

`Gemini CLI` 最值得学的是：它把 terminal 工具和 `GitHub Action` 直接打通。

这意味着：

- 本地工作流和 CI 工作流可以共用同一入口
- 同一套 `GEMINI.md` / extension thinking 可以进入 repo automation

### xAI

`xAI` 这条线说明，自动化并不一定需要终端或 app 入口。

如果 API 侧已经把：

- search
- code execution
- files
- remote MCP
- multi-agent

做成一套 server-side surfaces，那么自动化 loop 本身就能发生在服务端。

## 一个成熟自动化闭环的 6 个步骤

1. `trigger`
2. `context hydration`
3. `bounded execution`
4. `approval / interruption`
5. `artifact + trace persistence`
6. `replay / escalation / retry`

如果少了后 3 步，很多“自动化 agent”都只是一次性脚本，不是真正可运维的 harness automation。

## 设计自动化面时最容易犯的错

- 只设计触发，不设计回放
- 只设计成功路径，不设计失败路径
- 只设计能力，不设计 budget / approval / cooldown
- 只设计工具，不设计 artifacts 和审计记录

## 学习建议

如果你想真正理解 harness 的自动化层，最好的顺序通常是：

1. 先看 `hooks`
2. 再看 `cron / heartbeat`
3. 再看 `CI / GitHub Actions`
4. 最后看 `background agents / cloud task queues`

这样会更容易看懂不同厂商到底在自动化面押注了什么。

## 关联

- [[Harness Engineering]]
- [[技能、插件、应用与自动化：Harness 的扩展面]]
- [[Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel]]
- [[Harness 工程案例：Codex、Claude Code、OpenClaw、Gemini CLI]]
- [[Eval Harness 与 Regression Suites]]
- [[Long-Running Agent Operations]]
- [[Agent Security、Sandbox 与 Approval Architecture]]
- [[../08-Maps/Harness 工作流与自动化模式图|Harness 工作流与自动化模式图]]

## 资料

- [OpenClaw Automation](https://docs.openclaw.ai/automation/)
- [OpenClaw Heartbeat](https://docs.openclaw.ai/gateway/heartbeat)
- [OpenClaw Cron Jobs](https://docs.openclaw.ai/cron/)
- [Claude Code Hooks](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Claude Code GitHub Actions](https://docs.anthropic.com/en/docs/claude-code/github-actions)
- [Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code/sdk)
- [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)
- [Unlocking the Codex harness: how we built the App Server](https://openai.com/index/unlocking-the-codex-harness/)
- [run-gemini-cli](https://github.com/google-github-actions/run-gemini-cli)
- [Multi Agent | xAI](https://docs.x.ai/developers/model-capabilities/text/multi-agent)
