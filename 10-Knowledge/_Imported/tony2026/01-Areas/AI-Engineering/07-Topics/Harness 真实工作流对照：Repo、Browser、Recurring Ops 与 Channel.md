---
title: Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent
  - ai/harness
  - ai/workflow
created: 2026-03-28
updated: 2026-03-28
---

# Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel

## 为什么这页很重要

很多对 agent 系统的比较，停留在：

- 模型强不强
- tool call 多不多
- 有没有 `MCP`

但真正决定体验和产出差异的，常常不是 feature list，而是 **哪一种工作流被做成了一等公民**。

所以最值得比较的不是“谁功能更多”，而是：

- `repo-local coding loop` 谁最顺
- `browser / desktop takeover` 谁最自然
- `recurring ops` 谁最像长期运转系统
- `channel assistant` 谁最像真正的 personal runtime

## 工作流 1：Repo-local coding loop

典型任务：

- 读代码库
- 改 2 到 5 个文件
- 跑测试
- 看 diff
- 按项目规范迭代

### `Claude Code`

这类任务里，`Claude Code` 往往最顺。

原因不是模型，而是它把下面这些东西做成了同一条 terminal loop：

- terminal entry
- `CLAUDE.md`
- slash commands
- subagents
- hooks
- `MCP`

它特别适合：

- repo-local 修复
- code review follow-up
- 按团队规则做 refactor
- 需要 shell / grep / read / edit 高频来回切换的任务

### `Codex`

`Codex` 也能做 repo 任务，但它更像把 repo task 放进更大的 cloud workbench 里。

当任务开始需要：

- 多 worktrees
- 多 agent 并行
- review queue
- app / IDE / CLI 多入口切换

它会越来越顺。

### `OpenClaw`

`OpenClaw` 不是最典型的 repo-local coding harness。

它能通过：

- typed tools
- exec
- plugin bundles
- 节点能力

进入代码任务，但它更强的不是“单仓库工程循环”，而是长期 assistant runtime。

## 工作流 2：Browser / desktop task

典型任务：

- 打开网页
- 浏览多个页面
- 找信息
- 点按钮
- 读取截图和页面状态

### `Codex / OpenAI computer use`

如果任务是明显的 browser / desktop takeover，`OpenAI` 这一线更像是把它当成正式动作面在做。

尤其是：

- `computer_use`
- `shell / local_shell`
- `remote_mcp`
- App Server 的 event / approval / artifact 视图

这条线最值得学的是：

- 连续动作循环
- 审批和 event stream
- 多表面统一到一个 richer runtime

### `Claude Code / Anthropic computer use`

`Claude Code` 本体更偏 terminal，但 Anthropic 的 `computer use` 说明它在 browser / desktop agent 这一面也很重视。

不过从产品心智上看：

- `Claude Code` 主工作台仍然是 terminal
- `computer use` 更像 Anthropic 的另一类动作面，而不是都收进一个单一 app workbench

### `OpenClaw`

`OpenClaw` 的 browser / device 能力更像“assistant operating layer 的动作面”。

它适合：

- assistant 在长期运行时偶尔调用 browser / device / node command
- 把 desktop / macOS / mobile node 当成外设
- 用 channel + node 组合形成跨设备 runtime

但如果只看“浏览器 takeover 体验本身”，它未必像专门面向 browser agent 的表面那样顺滑。

## 工作流 3：Recurring ops / daily automation

典型任务：

- 每天汇总 issue / CI / alerts
- 定时跑摘要
- 周期分析代码库
- 事件触发后补充上下文和通知

### `OpenClaw`

这是 `OpenClaw` 最强的一类。

因为它把：

- `heartbeat`
- `cron`
- `webhooks`
- `hooks`
- main session / isolated session
- channel delivery

一起做成了长期运行 runtime。

它特别适合：

- daily brief
- recurring summaries
- self-hosted assistant chores
- channel-based notifications
- 既想自动跑，又想保留 session memory 的任务

### `Claude Code`

`Claude Code` 更适合 repo-centric recurring ops：

- GitHub Actions
- hooks
- SDK / headless mode

也就是：

- PR review automation
- issue follow-up
- repo policy checks
- CI 内的 comment-driven loop

### `Codex`

`Codex` 的 `Automations` 更像 cloud workbench 里的 background work。

它适合：

- issue triage
- CI failure summary
- release brief
- background coding chores

但它更偏“team coding workbench 的后台队列”，不是 personal runtime 的 heartbeat 型自动化。

## 工作流 4：Channel assistant / long-lived personal runtime

典型任务：

- 从聊天入口发起任务
- 让 agent 记住长期上下文
- 连接手机、桌面、消息渠道
- 把通知、提醒、外部系统接回来

### `OpenClaw`

这一类基本是 `OpenClaw` 的主战场。

因为它本来就是：

- gateway
- channels
- nodes
- skills / plugins / bundles
- automation plane

一起组成的 assistant runtime。

它最适合研究：

- 自托管 personal agent
- channel-first harness
- 长期在线 control plane

### `Codex`

`Codex` 更像 coding / app / cloud task operator，而不是 channel-first personal assistant runtime。

### `Claude Code`

`Claude Code` 非常强，但主要还是 coding harness，不是 channel-native assistant layer。

## 一个更实用的判断表

| 真实工作流 | 最顺的默认选择 | 为什么 |
| --- | --- | --- |
| repo-local bugfix / refactor | `Claude Code` | terminal loop、commands、subagents、hooks、MCP 收得最紧 |
| 多 agent 并行 coding / review queue | `Codex` | app、cloud tasks、worktrees、background work、App Server |
| browser takeover / desktop task | `Codex` / OpenAI browser-computer line | 多动作面 + approvals + event stream 更像正式 runtime |
| repo-centric automation | `Claude Code` | hooks + GitHub Actions + SDK 最连贯 |
| self-hosted recurring assistant ops | `OpenClaw` | heartbeat + cron + webhook + channel delivery |
| channel-first personal runtime | `OpenClaw` | gateway + channels + nodes + plugins |

## 最重要的结论

`Codex`、`Claude Code`、`OpenClaw` 不是谁全面替代谁，而是分别把不同工作流做成了一等公民：

- `Claude Code`：最像 `repo-local terminal harness`
- `Codex`：最像 `cloud coding workbench`
- `OpenClaw`：最像 `self-hosted assistant operating layer`

所以真正成熟的选择方式应该是：

先判断你的任务属于哪种 workflow，再决定选哪种 harness。

## 推荐顺序

1. [[Harness 工程案例：Codex、Claude Code、OpenClaw、Gemini CLI]]
2. [[Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel]]
3. [[../06-Projects/Harness Lab/项目总览|Harness Lab]]
4. [[../06-Projects/Harness Lab/Harness Lab 第一轮：Repo 修复、Browser 操作与 Daily Ops|Harness Lab 第一轮：Repo 修复、Browser 操作与 Daily Ops]]

## 关联

- [[Harness Engineering]]
- [[Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel]]
- [[Hooks、Cron、CI 与 Background Agents：Harness 自动化闭环]]
- [[Harness 工程案例：Codex、Claude Code、OpenClaw、Gemini CLI]]
- [[../06-Projects/Harness Lab/项目总览|Harness Lab]]
- [[../06-Projects/Harness Lab/多厂商 Harness 对照实验|多厂商 Harness 对照实验]]
- [[../../AI-Learning/09-Systems/Codex|Codex]]
- [[../../AI-Learning/09-Systems/Claude Code|Claude Code]]
- [[../../AI-Learning/09-Systems/OpenClaw|OpenClaw]]

## 资料

- [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)
- [Unlocking the Codex harness: how we built the App Server](https://openai.com/index/unlocking-the-codex-harness/)
- [Computer use](https://platform.openai.com/docs/guides/tools-computer-use)
- [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
- [Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Hooks](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Claude Code GitHub Actions](https://docs.anthropic.com/en/docs/claude-code/github-actions)
- [Cron vs heartbeat](https://docs.openclaw.ai/cron-vs-heartbeat/)
- [Cron Jobs](https://docs.openclaw.ai/cron/)
- [Nodes](https://docs.openclaw.ai/nodes)
- [Plugin Bundles](https://docs.openclaw.ai/plugins/bundles)
