---
title: 从提示词到 Harness：Agent 能力的渐进式主线
type: topic
status: learning
tags:
  - ai/topic
  - ai/agent
  - ai/harness
  - ai/context
created: 2026-03-31
updated: 2026-04-03
---

# 从提示词到 Harness：Agent 能力的渐进式主线

## 这个主题为什么值得单独拉出来

如果只零散看 `提示词工程`、`上下文工程`、`Tool Use`、`MCP`、`CLI`、`skills`、`plugins`、`Harness Engineering`，很容易产生一种错觉：

- 今天流行 prompt
- 明天流行 context
- 后天又变成 harness
- 再过一阵大家开始谈 skills、tools、plugins、computer use

但更稳的理解不是“热点替换”，而是：

`Agent 工程在沿着一条渐进主线不断外扩。`

也就是从“怎么跟模型说话”，逐步走向“怎么把模型放进一个可执行、可扩展、可治理的工作台”。

## 一条最实用的渐进式主线

### 1. 提示词层 `prompt layer`

这里回答的是：

- 任务到底怎么说清楚
- 输出格式怎么约束
- 角色、边界、few-shot example 怎么表达

这是最内层控制面，所以你会先读 [[提示词工程]]。

### 2. 上下文层 `context layer`

这里回答的是：

- 模型到底看到了什么
- 文件、历史、检索结果、状态、记忆怎么进上下文
- 什么该进，什么不该进

这一步开始从“说清楚”走向“把模型放进正确环境”，所以你会接着读 [[上下文工程]]。

### 3. 工具层 `tool layer`

这里回答的是：

- 模型如何不只输出文本，而是真正去执行动作
- 工具如何被选择、调用、回读、重试和验证

这时系统开始从“会理解”走向“会行动”，所以你会接着读 [[Tool Use]]。

### 4. 动作面层 `action surfaces`

当工具不再只是抽象 function calling，而开始变成具体工作表面时，就会出现：

- `CLI / shell`
- `MCP`
- `browser / computer use`
- app-specific actions

这一层最重要的不是“谁更先进”，而是“不同动作面各自解决什么问题”，所以这里要连着看：

- [[Agent 动作面：Tools、CLI、MCP、Browser 与 Apps]]
- [[MCP（Model Context Protocol）]]
- [[Browser Agents 与 Computer Use]]
- [[../../AI-Engineering/07-Topics/MCP 与 CLI 模式|MCP 与 CLI 模式]]
- [[../../AI-Engineering/07-Topics/Computer Use Runtime and Safety|Computer Use Runtime and Safety]]

### 5. 扩展面层 `extension surfaces`

当 agent 真开始进入产品和团队环境，问题又会升级成：

- 能力如何被安装
- 工作方法如何被沉淀
- 哪些经验应该变成 skill
- 哪些外部能力应该变成 plugin / app / connector
- 哪些事情应该交给 hook、automation、background agent

这时就不只是“能调用工具”，而是“能被扩展、复用和运营”，所以这里要接着看：

- [[Agent 扩展面：Skills、Plugins、Hooks 与 Automations]]
- [[../../AI-Engineering/07-Topics/技能、插件、应用与自动化：Harness 的扩展面|技能、插件、应用与自动化：Harness 的扩展面]]
- [[../09-Systems/Codex Skills 与 Plugins|Codex Skills 与 Plugins]]
- [[../09-Systems/OpenClaw 的技能、插件、应用与自动化生态|OpenClaw 的技能、插件、应用与自动化生态]]

### 6. Harness 层 `workbench layer`

到这里，系统已经不再只是模型 + prompt + tools，而是完整工作台：

- task environment
- action surfaces
- extension surfaces
- control plane
- automation plane
- feedback / eval / release gates

这也是为什么最后会落到 [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]。

### 7. Runtime / Governance 层 `operate the system`

当 harness 真进入生产，你还会自然走到更深层：

- runtime architecture
- session / memory / artifact
- approval / sandbox / release gates
- eval harness / regression suites
- incident library / rollback / blast radius

也就是“会搭一个 agent”继续走向“会运营一个 agent system”。

## 一个更稳的总判断

不要把它理解成：

`Prompt 被 Context 替代，Context 又被 Harness 替代。`

更准确的理解应该是：

- `prompt` 是最内层控制
- `context` 是工作集装配
- `tools` 是动作能力
- `CLI / MCP / browser` 是不同动作面
- `skills / plugins / apps / automation` 是扩展与持续化能力
- `harness` 是把上面这些一起收起来的工作台
- `runtime / governance` 是系统长大之后的运营层

## 你应该怎么学这条线

### 如果你刚起步

先读：

1. [[提示词工程]]
2. [[上下文工程]]
3. [[Tool Use]]
4. [[Agent 动作面：Tools、CLI、MCP、Browser 与 Apps]]
5. [[MCP（Model Context Protocol）]]

### 如果你已经开始做 agent

接着读：

1. [[Agent 动作面：Tools、CLI、MCP、Browser 与 Apps]]
2. [[Browser Agents 与 Computer Use]]
3. [[Agent Memory]]
4. [[../../AI-Engineering/07-Topics/MCP 与 CLI 模式|MCP 与 CLI 模式]]
5. [[../../AI-Engineering/07-Topics/Prompt、Context、Tools、CLI、Skills、Plugins 与 Harness 的工程分层|Prompt、Context、Tools、CLI、Skills、Plugins 与 Harness 的工程分层]]

### 如果你已经开始搭系统

再读：

1. [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
2. [[../../AI-Engineering/07-Topics/动作面设计：Tools、CLI、MCP、Browser、Desktop 与 Channel|动作面设计：Tools、CLI、MCP、Browser、Desktop 与 Channel]]
3. [[../../AI-Engineering/07-Topics/扩展面设计：Skills、Plugins、Hooks、Apps 与 Automation|扩展面设计：Skills、Plugins、Hooks、Apps 与 Automation]]
4. [[../../AI-Engineering/07-Topics/技能、插件、应用与自动化：Harness 的扩展面|技能、插件、应用与自动化：Harness 的扩展面]]
5. [[../../AI-Engineering/07-Topics/Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel|Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel]]
6. [[../../AI-Engineering/07-Topics/Hooks、Cron、CI 与 Background Agents：Harness 自动化闭环|Hooks、Cron、CI 与 Background Agents：Harness 自动化闭环]]

## 推荐配套地图

- [[../07-Maps/Agent Prompt-Context-Harness Map|Agent Prompt-Context-Harness Map]]
- [[../07-Maps/Prompt、Context、Tools 与 Harness 渐进图|Prompt、Context、Tools 与 Harness 渐进图]]
- [[../07-Maps/Agent 子域学习图|Agent 子域学习图]]
- [[../../AI-Engineering/08-Maps/Harness Engineering 与 Agent 扩展生态图|Harness Engineering 与 Agent 扩展生态图]]
- [[../../AI-Engineering/08-Maps/Harness 工作流与自动化模式图|Harness 工作流与自动化模式图]]

## 相关

- [[提示词工程]]
- [[上下文工程]]
- [[Tool Use]]
- [[Agent 动作面：Tools、CLI、MCP、Browser 与 Apps]]
- [[MCP（Model Context Protocol）]]
- [[Browser Agents 与 Computer Use]]
- [[Agent Memory]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
