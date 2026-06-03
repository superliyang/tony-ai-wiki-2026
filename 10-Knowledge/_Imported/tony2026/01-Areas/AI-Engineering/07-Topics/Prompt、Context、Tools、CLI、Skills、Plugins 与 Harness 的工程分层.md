---
title: Prompt、Context、Tools、CLI、Skills、Plugins 与 Harness 的工程分层
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent
  - ai/harness
  - ai/context
  - ai/tools
created: 2026-03-31
updated: 2026-04-03
---

# Prompt、Context、Tools、CLI、Skills、Plugins 与 Harness 的工程分层

## 为什么要把这几个词放到一页里

今天谈 agent，最常见的混乱不是“概念太少”，而是“概念太多但层次混在一起”。

常见混淆包括：

- 把 `prompt` 问题当成 `context` 问题
- 把 `tool use` 问题当成 `CLI or MCP` 阵营之争
- 把 `skill` 当成另一种 `plugin`
- 把 `plugin` 当成 `harness`
- 把 `harness` 当成“很多 feature 的集合”而不是一个工作台设计问题

所以这页的目标，是把它们放回同一张工程分层图里。

## 一张最实用的工程分层表

### 1. Prompt

它负责：

- instruction
- role
- examples
- output schema
- behavioral boundaries

它回答的问题是：

- 模型该怎么理解任务
- 输出应该长什么样

典型失败：

- 任务理解偏差
- 格式不稳
- 语气、边界、优先级混乱

### 2. Context

它负责：

- state packing
- file / repo slicing
- retrieval assembly
- memory recall
- tool schema placement

它回答的问题是：

- 模型在这一轮到底看见什么

典型失败：

- 信息缺失
- 信息过载
- 历史步骤丢失
- 工具返回没有被正确结构化

### 3. Tools

它负责：

- 调外部能力
- 执行动作
- 获取结果
- 把结果送回下一步推理

它回答的问题是：

- 模型如何从“会说”变成“会做”

典型失败：

- 选错工具
- 参数构造错误
- 返回不可消费
- 执行失败后没有合适恢复

### 4. CLI / MCP / Browser

它们不是同一层，但都属于动作面：

- `CLI`：本地强动作面
- `MCP`：协议化接入面
- `browser / computer use`：UI 动作面

它们回答的问题是：

- agent 通过什么表面去接触真实世界

典型失败：

- 权限过宽
- 信任边界模糊
- UI 不稳定
- tool surface 太碎或太松

### 5. Skills / Plugins / Apps / Automation

它们属于扩展面：

- `skills`：沉淀工作方法
- `plugins`：安装与接入能力
- `apps / connectors`：提供交互与业务入口
- `automation`：让 agent 在后台或事件驱动下持续运行

它们回答的问题是：

- 能力如何复用、安装、组合、持续执行

典型失败：

- 经验无法沉淀
- 扩展污染 runtime
- 背景任务缺少观测和门禁
- 一次性脚本无法产品化

### 6. Harness

`Harness` 负责把上面几层一起收起来。

它真正负责的是：

- task environment
- action surfaces
- extension surfaces
- control plane
- automation plane
- feedback / release gates

它回答的问题是：

- 这个 agent system 在哪里工作、如何扩展、怎样被约束、如何被评估、出了问题怎么回滚

典型失败：

- 任务环境不可见
- 会话不可恢复
- artifact 不可审计
- blast radius 太大
- rollback / shadow rollout 缺失

## 一个常见误区：把 skill 和 plugin 当成一回事

更稳的区分是：

- `skill` 更像可复用工作方法
- `plugin` 更像可安装运行时能力
- `tool` 更像单次动作能力
- `harness` 更像把这些能力放进工作台的系统设计

所以：

- 不是所有 skill 都该变成 plugin
- 不是所有 plugin 都该直接暴露成 tool
- 不是所有 tool 组合起来就已经是 harness

## 一个常见误区：把 CLI / MCP 当成体系之争

更准确的理解是：

- `CLI` 适合 repo-local / shell-native / developer-first workflow
- `MCP` 适合 protocolized integration / team reuse / shared service
- `browser` 适合 UI-only / SaaS / desktop/web task
- `harness` 解决的是“这些动作面如何在一个系统里共存并被治理”

所以很多成熟系统最后都是混合型：

- shell 做本地动作
- MCP 做共享集成
- browser 做 UI 补面
- skills / plugins 做扩展
- harness / runtime 做控制和反馈

## 在真实项目里，应该先做哪一层

### 如果任务还不稳定

先做好：

- prompt
- context
- tool contract

### 如果任务已经开始反复执行

再补：

- CLI / MCP / browser 的动作面选择
- skill 化的工作方法
- plugin 化的能力接入

### 如果系统已经进入团队和生产环境

必须补：

- harness
- eval / regression
- release gate
- incident / rollback / blast radius

## 一个很实用的诊断问题

当 agent 失败时，先问：

1. 是 `prompt` 没说清楚？
2. 还是 `context` 没喂对？
3. 还是 `tool contract` 不稳定？
4. 还是动作面选错了？
5. 还是扩展面把系统搞复杂了？
6. 还是 harness 本身没有可观察、可恢复、可治理？

这个诊断顺序比“换个模型试试”更有工程价值。

## 推荐配套阅读顺序

1. [[../../AI-Learning/06-Topics/提示词工程|提示词工程]]
2. [[../../AI-Learning/06-Topics/上下文工程|上下文工程]]
3. [[Prompt 到 Context：任务表达、工作集与失败诊断]]
3. [[../../AI-Learning/06-Topics/Tool Use|Tool Use]]
4. [[动作面设计：Tools、CLI、MCP、Browser、Desktop 与 Channel]]
5. [[MCP 与 CLI 模式]]
6. [[扩展面设计：Skills、Plugins、Hooks、Apps 与 Automation]]
7. [[技能、插件、应用与自动化：Harness 的扩展面]]
6. [[Harness Engineering]]
7. [[Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel]]
8. [[Hooks、Cron、CI 与 Background Agents：Harness 自动化闭环]]
9. [[Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel]]

## 关联

- [[Harness Engineering]]
- [[Prompt 到 Context：任务表达、工作集与失败诊断]]
- [[动作面设计：Tools、CLI、MCP、Browser、Desktop 与 Channel]]
- [[扩展面设计：Skills、Plugins、Hooks、Apps 与 Automation]]
- [[MCP 与 CLI 模式]]
- [[技能、插件、应用与自动化：Harness 的扩展面]]
- [[Tool Calling and Action Execution]]
- [[Session and Memory Design]]
- [[Codex Plugin Hook Payload、Live Cache 与 Debug Snapshot]]
- [[../08-Maps/Harness Engineering 与 Agent 扩展生态图|Harness Engineering 与 Agent 扩展生态图]]
- [[../../AI-Learning/07-Maps/Prompt、Context、Tools 与 Harness 渐进图|Prompt、Context、Tools 与 Harness 渐进图]]
