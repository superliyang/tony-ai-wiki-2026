---
title: MCP（Model Context Protocol）
type: topic
status: learning
tags:
  - ai/topic
  - ai/agent
  - ai/mcp
created: 2026-03-25
updated: 2026-04-13
---

# MCP（Model Context Protocol）

## 这个主题是什么

`MCP` 是一个开放协议，目标是让 AI 应用以更标准化的方式连接外部系统。

它想解决的问题不是“模型怎么推理”，而是“模型怎样稳定接入工具、资源和可复用能力”。

## 为什么它会在 agent 领域变热

因为 agent 一旦要接入真实世界，就会遇到这些问题：

- 每个工具接法都不一样
- 不同 host / client 很难复用同一套集成
- 权限、返回格式、连接方式不统一
- 本地工具和远程服务都需要统一入口

MCP 的价值，就是把“外部能力接入”从一次性 adapter，推进到协议层。

## 2025-2026 最值得补的新判断

这条线最近最大的变化，不是协议定义本身，而是 MCP 已经开始进入主流产品和 API surface。

一个特别值得记住的官方信号来自 OpenAI 的 MCP 文档：

- remote MCP servers 可以接到 `ChatGPT apps`
- 也可以接到 `deep research`
- 还可以接到 `API integrations`

而且 OpenAI 文档还明确写到 `2025-12-17`，ChatGPT 把 connectors 改名成 apps。

这说明 MCP 已经不只是“工程师圈子里的协议讨论”，而是开始变成真正的产品接入面。

## 你先要抓住什么

- MCP 是协议，不是 agent 本身
- 它更像 tool / resource integration layer
- 有了 MCP，不代表系统就更智能；它只是让能力接入更标准

## 基本角色

一个典型 MCP 体系里，通常会有：

- `host`：真正使用外部能力的 AI 应用
- `client`：host 内部与 server 通信的连接方
- `server`：暴露 tools / resources / prompts 的能力端

## 它适合做什么

- 标准化团队内部工具集成
- 把数据库、文档系统、SaaS API 封成统一能力
- 同一套 server 被多个 agent host 复用
- 把本地脚本能力或远程系统能力，通过统一协议暴露出去

## 它不直接解决什么

- 不直接解决规划问题
- 不直接解决记忆问题
- 不直接决定 approval 和 governance
- 不直接等于“最好用的 agent tool 模式”

所以在工程上，MCP 往往只是 agent harness 的一层，而不是全部系统。

## 为什么会和 CLI 模式被放在一起争论

因为在实践中，很多人面对的是同一个选择：

- 我要不要直接给 agent 一个 `shell / CLI` 动作面
- 还是把能力封成 `MCP server`

这个争论表面上是 `MCP vs CLI`，本质上其实是在比较：

- 直接动作能力
- 协议化工具边界
- 可复用性
- 安全边界
- 团队协作方式

更细的工程判断，继续读 [[../../AI-Engineering/07-Topics/MCP 与 CLI 模式|MCP 与 CLI 模式]]。

## 什么时候 MCP 很合适

- 你要把能力做成跨 host 复用的标准接口
- 你要连接远程系统或共享服务
- 你想把工具暴露边界做得比 shell 更清晰
- 你希望团队把集成沉淀成“服务能力”，而不是一次性脚本

## 什么时候它尤其值得重视

- 你在做 company knowledge、deep research、data app 这类 read-heavy agent
- 你需要把一组内部系统做成可复用的标准接入面
- 你希望多个 host / client 复用同一套能力，而不是每个产品都手搓 adapter

## 什么时候不要把 MCP 神化

- 本地单机场景里，直接 shell / CLI 可能更简单
- 如果任务需要极强的工作目录、进程、文件系统控制，CLI 往往更直接
- 更复杂的 agent session、diff、approval、task object，有时并不适合只靠 MCP 来承载

## 推荐继续往下读

- [[提示词工程]]
- [[上下文工程]]
- [[Tool Use]]
- [[../../AI-Engineering/07-Topics/MCP 与 CLI 模式|MCP 与 CLI 模式]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
- [[../11-Recent-Supplements/2025-2026 AI 新路线补线：Deep Research、Memory 与 Agent Runtime|2025-2026 AI 新路线补线：Deep Research、Memory 与 Agent Runtime]]

## 相关

- [[Agent]]
- [[Tool Use]]
- [[上下文工程]]
- [[Deep Research 与 Research Agents]]
- [[../07-Maps/Agent Prompt-Context-Harness Map|Agent Prompt-Context-Harness Map]]
