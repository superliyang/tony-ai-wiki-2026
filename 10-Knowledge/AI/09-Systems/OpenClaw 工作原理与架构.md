---
title: OpenClaw 工作原理与架构
type: topic
status: learning
tags:
  - ai/topic
  - ai/agent
  - ai/openclaw
  - ai/architecture
created: 2026-03-18
updated: 2026-03-22
---

# OpenClaw 工作原理与架构

## 这页解决什么问题

如果 `OpenClaw` 只是被理解成“另一个 AI agent 项目”，那你很容易低估它。它真正值得学的，是它把 agent 做成了一个长期运行的系统：有 `Gateway`、有 session source of truth、有 workspace memory、有 hooks / heartbeat / cron，还有 channels、nodes 和 control UI。

这页重点回答三个问题：

1. `OpenClaw` 到底是怎么工作的
2. 它的架构设计为什么和普通聊天产品不一样
3. 你听到的“自进化”在这个体系里最接近什么机制

## 一句话架构

最短的一句话是：

`OpenClaw = 一个长期运行的 Gateway + 一个嵌入式 agent runtime + 一套基于 workspace 文件、sessions、memory、tools、hooks、heartbeat、cron 的 personal agent operating layer`。

官方文档反复强调的核心点是：`Gateway is the single source of truth for sessions, routing, and channel connections.` 这几乎就是它整个系统设计的中心。

## 1. Gateway 是控制平面，不只是代理进程

根据官方架构文档，`OpenClaw` 采用的是单个长期运行的 `Gateway` 模式：

- 一个 long-lived Gateway 持有所有消息渠道
- CLI、Web UI、macOS app、automation 都通过 WebSocket 连它
- nodes（macOS / iOS / Android / headless）也连同一个 Gateway
- 它是 session、routing、channel connection 的唯一事实来源

这和很多“网页对话 + 后台调用模型”的产品不一样。`OpenClaw` 更像一个 agent control plane。

你可以把它理解成：

- 渠道层：负责接住 WhatsApp、Telegram、Discord、iMessage 等入口
- 协调层：负责把输入路由到正确的 agent / session
- 运行层：负责把请求送进 agent runtime，再把结果发回去
- 运维层：负责 health、heartbeat、cron、pairing、remote access

## 2. 它是多入口 assistant，而不是单一聊天框

`OpenClaw` 的一个核心设计是“multi-channel gateway”。官方首页明确把多渠道列成第一层能力：一个 Gateway 可以同时承接 WhatsApp、Telegram、Discord、iMessage 等入口。

这意味着它在产品形态上更接近：

- 一个长期在线的 personal assistant
- 一个消息驱动的 agent runtime
- 一个用户已经习惯在各处叫它的系统

而不是：

- 单一网页聊天窗口
- 只有“你打开它时它才存在”的 assistant

## 3. Agent Runtime 不是抽象概念，而是嵌入式运行时

官方 `Agent Runtime` 文档明确说：`OpenClaw runs a single embedded agent runtime derived from pi-mono.`

也就是说，agent 并不是一个模糊概念，而是一个明确的 runtime：

- 有固定 workspace
- 有 bootstrap files
- 有 tools
- 有 session 管理
- 有 memory 管理

这很值得学，因为它把“AI Agent”从论文概念推进到了工程运行层。

## 4. Workspace 文件就是系统行为的一部分

官方 workspace 文档里，agent workspace 不只是普通目录，而是运行时上下文的一部分。里面有几类关键文件：

- `AGENTS.md`：操作规则 + 行为约束 + 工作记忆
- `SOUL.md`：人格、边界、语气
- `TOOLS.md`：本地工具说明与约定
- `USER.md`：用户信息
- `IDENTITY.md`：agent 身份
- `HEARTBEAT.md`：主动巡检清单
- `BOOT.md`：启动时 checklist
- `BOOTSTRAP.md`：首次启动 ritual
- `MEMORY.md` 与 `memory/YYYY-MM-DD.md`：长期 / 日常记忆

这套设计非常重要，因为它说明：

`OpenClaw` 的“智能”并不只来自模型，也来自 workspace 文件组织出来的长期上下文。

## 5. Session 模型是它区别于普通 assistant 的关键层

官方 session 文档有两个很重要的点：

### 1. Gateway 是 session 的 source of truth

UI 客户端不能自己本地乱猜 session 状态，必须向 gateway 查询。

### 2. DM 和 group 并不是同一种 session

官方默认 direct chat 会 collapse 到主 session，但又提供 `dmScope` 配置：

- `main`
- `per-peer`
- `per-channel-peer`
- `per-account-channel-peer`

这说明 `OpenClaw` 不是简单把所有消息都喂给一个上下文，而是在认真做“会话边界设计”。

这是 agent 产品化里非常关键的一层：

- 单用户连续性
- 多用户隔离
- 多渠道身份映射
- 多 agent 路由

## 6. Memory 不是“模型脑补”，而是 Markdown files

官方记忆文档里最值得记住的一句话是：

`The files are the source of truth; the model only “remembers” what gets written to disk.`

默认有两层记忆：

- `memory/YYYY-MM-DD.md`：日常 append-only 日志
- `MEMORY.md`：整理后的长期记忆

再配两个工具：

- `memory_search`
- `memory_get`

这个设计非常实用，也非常工程化。它意味着：

- 不把记忆神秘化
- 记忆是文件系统中的 durable state
- recall 通过工具完成
- “记住”这件事，本质上是写盘和检索，而不是指望模型隐式保留

## 7. Tools 是正式能力面，不是临时拼接

`OpenClaw` 官方 tools 文档把工具设计成 typed、first-class tools。文档和首页能力说明里可以看到它强调：

- `browser`
- `exec` / `process`
- `canvas`
- `nodes`
- `cron`
- `memory`
- `sessions`
- `web_search`

这很值得和很多“agent demo”区分开：

- demo 往往是 prompt 里说“你可以调用工具”
- `OpenClaw` 是 runtime 层真的有一套工具系统、profile、allow / deny 机制

所以从架构上看，它更像：

- agent runtime platform
- assistant operating layer
- personal automation control plane

## 8. 主动运行机制：heartbeat、cron、hooks

这是你提到“自进化”时最容易想到、也最接近的部分。

官方文档里，主动运行机制主要有三层：

### Heartbeat

- 默认每 30 分钟一次
- 读取 `HEARTBEAT.md`
- 没事就回 `HEARTBEAT_OK`
- 有事才真正触发对外提醒

它更像一个 agentic poll / proactive check loop。

### Cron

- 是 Gateway 自带的 scheduler
- 任务持久化在 `~/.openclaw/cron/`
- 可以 main-session 方式运行，也可以 isolated job 方式运行
- 可以把 agent 在指定时间点唤醒去干活

### Hooks

官方 hooks 文档里最重要的几个 bundled hooks 是：

- `session-memory`
- `bootstrap-extra-files`
- `command-logger`
- `boot-md`

这些 hook 让 `OpenClaw` 变成一个事件驱动系统，而不只是“来一条消息 -> 回一句话”的系统。

## 9. 你说的“自进化”怎么理解

这里我想帮你把概念说准一点：

**就我查到的官方文档来看，`OpenClaw` 并没有把自己的核心机制正式命名为“自进化 `self-evolution`”。**

我更倾向于把你听到的“自进化”拆成两层理解：

### 官方明确存在的层

这是可以直接从官方文档确认的：

- workspace 文件可编辑
- memory 写入磁盘
- hooks 能在事件上触发自动动作
- heartbeat 能持续主动巡检
- cron 能定时唤醒 agent
- `BOOT.md` / `HEARTBEAT.md` 可以持续调整 agent 的行为 checklist

这一层更准确的名字应该是：

- `可持续自运转`
- `可配置自调整`
- `event-driven self-maintenance`

### 社区常说的“自进化”层

这是我基于官方机制做的**推断**：

如果 agent 能通过工具去修改自己的 `AGENTS.md`、`HEARTBEAT.md`、项目文档、memory 文件，甚至通过 hooks 和 cron 去持续迭代这些工作文件，那么它就会表现出一种“准自进化”的行为。

但严格说，这更像：

- 通过文件系统与自动化机制不断改进自己的操作环境
- 而不是“OpenClaw 内核自己会进化”

所以更准确的表达是：

`OpenClaw 具备做“可持续自我迭代工作流”的能力，但官方核心概念更偏 gateway、sessions、memory、hooks、heartbeat、cron，而不是直接把它定义成 self-evolving agent。`

## 10. 为什么它对学习 AI Agent 很有价值

学 `OpenClaw` 最大的收益，不是学一堆命令，而是你会开始真正区分这些层：

- 模型层：模型本身强不强
- agent 层：会不会拆任务、调工具、循环执行
- assistant 层：用户如何和它交互
- runtime 层：session / memory / workspace / tools 怎么落地
- ops 层：heartbeat / cron / hooks / remote access 怎么维持长期运行

很多 agent 讨论只停在前两层。`OpenClaw` 的价值，是把后面三层也暴露出来给你看。

## 如果你想继续把它抽象成工程问题

当你不再只想理解 `OpenClaw` 本身，而是想提炼出更一般的工程模式时，可以继续读：

- [[../../AI-Engineering/07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]
- [[../../AI-Engineering/07-Topics/Session and Memory Design|Session and Memory Design]]
- [[../../AI-Engineering/07-Topics/Long-Running Agent Operations|Long-Running Agent Operations]]

## 推荐学习顺序

1. [[Agent]]
2. [[AI Assistant]]
3. [[Coding Agents]]
4. [[OpenClaw]]
5. [[OpenClaw 的准自进化工作流]]
6. [[OpenClaw、ChatGPT 与 Claude Code 的定位差异]]
7. [[../07-Maps/OpenClaw Architecture Map|OpenClaw Architecture Map]]
8. [[../07-Maps/OpenClaw 准自进化工作流图|OpenClaw 准自进化工作流图]]
9. [[../07-Maps/AI Agent Systems Map|AI Agent Systems Map]]

## 关联

- [[OpenClaw]]
- [[Agent]]
- [[AI Assistant]]
- [[Coding Agents]]
- [[OpenClaw 的准自进化工作流]]
- [[OpenClaw、ChatGPT 与 Claude Code 的定位差异]]
- [[Developer Tools]]
- [[../07-Maps/OpenClaw Architecture Map|OpenClaw Architecture Map]]
- [[../07-Maps/OpenClaw 准自进化工作流图|OpenClaw 准自进化工作流图]]
- [[../07-Maps/AI Agent Systems Map|AI Agent Systems Map]]
- [[../../AI-Engineering/07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]
- [[../../AI-Engineering/07-Topics/Session and Memory Design|Session and Memory Design]]
- [[../../AI-Engineering/07-Topics/Long-Running Agent Operations|Long-Running Agent Operations]]

## 官方资料

- GitHub README: [openclaw/openclaw](https://github.com/openclaw/openclaw)
- 首页: [OpenClaw Docs](https://docs.openclaw.ai/)
- 架构: [Gateway Architecture](https://docs.openclaw.ai/concepts/architecture)
- Agent runtime: [Agent Runtime](https://docs.openclaw.ai/concepts/agent)
- Workspace: [Agent Workspace](https://docs.openclaw.ai/concepts/agent-workspace)
- Session: [Session Management](https://docs.openclaw.ai/sessions)
- Memory: [Memory](https://docs.openclaw.ai/concepts/memory)
- Hooks: [Hooks](https://docs.openclaw.ai/automation/hooks)
- Heartbeat: [Heartbeat](https://docs.openclaw.ai/gateway/heartbeat)
- Cron: [Cron Jobs](https://docs.openclaw.ai/cron/)
