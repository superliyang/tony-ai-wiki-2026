---
title: OpenClaw 的准自进化工作流
type: topic
status: learning
tags:
  - ai/topic
  - ai/openclaw
  - ai/agent
  - ai/memory
  - ai/automation
created: 2026-03-22
updated: 2026-03-29
---

# OpenClaw 的准自进化工作流

## 这页解决什么问题

很多人第一次听 `OpenClaw`，会被一个很抓人的说法吸引：它是不是一种会“自进化”的 agent？

更准确地说，`OpenClaw` 官方并没有把自己定义成 `self-evolving agent`。但它确实提供了一组很适合形成“准自我迭代”行为的机制：

- workspace 文件可持续修改
- memory 默认落到 Markdown
- hooks 可以在事件上自动触发
- heartbeat 可以周期性主动检查
- cron 可以按时间调度 agent turn

所以这页的重点不是神化它，而是把它的“准自进化工作流”拆开来看。

## 一句话理解

`OpenClaw` 的“准自进化”不是模型自己长出新能力，而是 agent 可以通过 memory、workspace、hooks、heartbeat、cron 持续修改自己的工作环境，并在后续运行里读取这些变化。

## 官方明确存在的 5 个积木

### 1. Workspace 是可持续修改的运行时环境

官方 workspace 文档把这些文件当成 agent 运行时的一部分，而不是普通说明文档：

- `AGENTS.md`
- `SOUL.md`
- `TOOLS.md`
- `BOOT.md`
- `HEARTBEAT.md`
- `MEMORY.md`
- `memory/YYYY-MM-DD.md`

这意味着 agent 的很多“行为边界”和“长期偏好”，都可以通过文件而不是模型参数来调整。

### 2. Memory 的 source of truth 是文件

官方 memory 文档里最关键的一点是：

- memory 是 plain Markdown
- files are the source of truth
- 模型只会“记住”被真正写下来的东西

这非常重要，因为它让“经验沉淀”从抽象概念，变成了可检查、可编辑、可回放的文件系统状态。

### 3. Hooks 可以把事件变成自动动作

官方 hooks 文档里，OpenClaw 自带几类很关键的 bundled hooks：

- `session-memory`
- `bootstrap-extra-files`
- `command-logger`
- `boot-md`

这些 hook 的意义在于：系统状态变化后，不一定要靠用户再次手动提醒 agent，某些动作可以自动发生。

### 4. Heartbeat 让 agent 定期“醒来”

heartbeat 是最容易被人误听成“自进化”的部分。官方机制其实很清楚：

- 按周期触发 turn
- 读取 `HEARTBEAT.md`
- 没事就返回 `HEARTBEAT_OK`
- 有事才真正输出提醒或动作结果

所以 heartbeat 更像：

- 主动巡检
- 低打扰 check loop
- 对长期任务的保活机制

### 5. Cron 让 agent 能在明确时间点执行任务

和 heartbeat 不同，cron 更适合明确任务：

- 定时整理某类信息
- 按日/周跑例行检查
- 周期性唤醒特定工作流

如果说 heartbeat 更像“看看有没有事”，cron 更像“到点就做这件事”。

## “准自进化工作流”到底怎么形成

你可以把它理解成一个循环：

1. 用户消息、外部事件、heartbeat 或 cron 触发一次 turn
2. Gateway 维护 session 作为事实来源
3. Agent runtime 读取 workspace、memory、session 上下文
4. Agent 调用工具执行动作
5. 结果被写回 memory 或其他工作文件
6. hooks 在特定事件上进一步补充或整理状态
7. 下一次 turn 再读取这些变化后的文件

这就形成了一种非常像“持续自我修正”的效果。

但要注意，它修正的不是模型权重，而是：

- 工作记忆
- 操作规则
- 例行检查清单
- 长期上下文
- 自动化触发条件

## 一个现在很具体的样本：Self-Improving-Agent

如果只停在 `memory + hooks + cron` 这些抽象积木，这条线还容易显得有点概念化。

现在 `ClawHub` 上已经有了一个很具体的样本：[[Self-Improving-Agent（ClawHub Skill）]]。

这条 skill 做的事情非常典型：

- 把 learnings、errors、feature requests 先写进 `.learnings/`
- 把高价值经验 promotion 到 `AGENTS.md`、`TOOLS.md`、`SOUL.md` 等 durable workspace files
- 再把极少数 recurring、verified、non-obvious、broadly applicable 的模式抽成 reusable skill

这让 `OpenClaw` 的“准自进化”从抽象理念变成了一条很具体的升级路径：

`learning log -> durable workspace rule -> extracted skill`

## 更准确地说，它“进化”的是什么

如果一定要借用“自进化”这个词，那么 OpenClaw 更接近是在进化这些东西：

- `工作环境`
- `操作规则`
- `任务清单`
- `长期记忆`
- `触发节律`

而不是：

- 模型底层参数
- 推理引擎本身
- 核心系统自动改写自身代码并安全验证

## 一个很典型的例子

假设你让 OpenClaw 帮你做长期研究助理，它可能形成这样的链路：

1. 你先在 `AGENTS.md` 里写研究原则
2. 在 `HEARTBEAT.md` 里写“定期检查未完成研究问题”
3. 它在日常会话里把关键结论写进 `MEMORY.md`
4. 用 `session-memory` 在 `/new` 时沉淀上下文
5. heartbeat 定时检查是否有待推进事项
6. cron 在每天固定时段触发一次整理
7. 你再根据结果调整 `AGENTS.md` 或 `TOOLS.md`

这样跑几轮后，你会感觉它越来越“懂这个长期任务怎么做”。  
这种体验很像自我迭代，但本质上是：

- 文件沉淀
- 自动化触发
- 下次读取旧成果继续工作

## 为什么这很值得学

因为这件事揭示了一个很重要的 AI Agent 现实：

**很多所谓“agent 会成长”，其实不是模型神秘地学会了新东西，而是系统给了它可持续写入、可持续读取、可持续触发的环境。**

这比单纯追问“模型是不是更聪明”更接近真实产品系统。

## 它不等于什么

这里要刻意踩一下刹车，避免把概念说飞：

- 它不等于自动训练新模型
- 它不等于真正意义上的自我改写内核
- 它不等于完全自主、安全可控的持续优化系统
- 它也不保证“写得越多越聪明”，坏 memory 同样会污染后续行为

## 真正的风险点

如果你想把这种机制用在真实系统里，风险通常在这里：

- memory 污染：把错误结论写成长期事实
- checklist 漂移：`HEARTBEAT.md` 越写越乱
- hook 误触发：自动动作在错误时机执行
- cron 过多：系统变得 noisy、昂贵或不可控
- 角色混淆：assistant、agent、automation 责任边界不清

所以“准自进化”要成立，前提不是更多自动化，而是更好的治理。

## 推荐怎么理解它

我建议用这组词来替代“自进化”：

- `可持续自运转`
- `可配置自调整`
- `可积累的 agent 工作流`
- `event-driven self-maintenance`

如果你想把这些说法进一步翻译成工程问题，可以继续读：

- [[../../AI-Engineering/07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]
- [[../../AI-Engineering/07-Topics/Session and Memory Design|Session and Memory Design]]
- [[../../AI-Engineering/07-Topics/Long-Running Agent Operations|Long-Running Agent Operations]]

这几种说法都比“它会自己进化”更准确。

## 推荐阅读顺序

1. [[OpenClaw]]
2. [[OpenClaw 工作原理与架构]]
3. [[Self-Improving-Agent（ClawHub Skill）]]
4. [[../07-Maps/OpenClaw Architecture Map|OpenClaw Architecture Map]]
5. [[../07-Maps/OpenClaw 准自进化工作流图|OpenClaw 准自进化工作流图]]

## 关联

- [[OpenClaw]]
- [[OpenClaw 工作原理与架构]]
- [[Agent]]
- [[AI Assistant]]
- [[Coding Agents]]
- [[../07-Maps/OpenClaw Architecture Map|OpenClaw Architecture Map]]
- [[../07-Maps/OpenClaw 准自进化工作流图|OpenClaw 准自进化工作流图]]
- [[Self-Improving-Agent（ClawHub Skill）]]
- [[../06-Topics/从 Learnings 到 AutoSkill：技能自提炼|从 Learnings 到 AutoSkill：技能自提炼]]
- [[../../AI-Engineering/07-Topics/Learnings、Promotion 与 Skill Extraction Pipeline|Learnings、Promotion 与 Skill Extraction Pipeline]]
- [[../../AI-Engineering/07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]
- [[../../AI-Engineering/07-Topics/Session and Memory Design|Session and Memory Design]]
- [[../../AI-Engineering/07-Topics/Long-Running Agent Operations|Long-Running Agent Operations]]

## 官方资料

- GitHub README: [openclaw/openclaw](https://github.com/openclaw/openclaw)
- Memory: [OpenClaw Memory](https://docs.openclaw.ai/concepts/memory)
- Agent Workspace: [OpenClaw Agent Workspace](https://docs.openclaw.ai/concepts/agent-workspace)
- Hooks: [OpenClaw Hooks](https://docs.openclaw.ai/automation/hooks)
- Heartbeat: [OpenClaw Heartbeat](https://docs.openclaw.ai/gateway/heartbeat)
- Cron vs Heartbeat: [Cron vs Heartbeat](https://docs.openclaw.ai/automation/cron-vs-heartbeat)
