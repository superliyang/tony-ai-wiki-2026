---
title: 记忆架构：State、Memory、Artifact 与 Context
type: topic
status: learning
tags:
  - ai/engineering
  - ai/memory
  - ai/context
  - ai/runtime
created: 2026-03-29
updated: 2026-03-29
---

# 记忆架构：State、Memory、Artifact 与 Context

## 为什么这一页要单独存在

很多 agent 系统一出问题，表面上像是模型错了，实际上是这四层混了：

- `state`
- `memory`
- `artifact`
- `context`

只要这四层没有分清，系统通常会出现：

- 不该长期保留的被长留了
- 应该结构化存放的被塞进 prompt 了
- 应该由 artifact store 承担的被误写进 memory 了
- context window 膨胀，成本和噪声一起上升

## 四层最稳的定义

### 1. `state`

当前 request / step / session / workflow 内需要共享的可变状态。

它强调：

- 生命周期有限
- 常跟 checkpoint 绑定
- 更像运行时容器

### 2. `memory`

跨 session 仍有价值的稳定事实、偏好、经验、规则。

它强调：

- durable
- 可检索
- 需要 provenance、权限和纠偏

### 3. `artifact`

任务产物，例如：

- diff
- 文档
- 图像
- screenshot
- structured result
- trace excerpt

artifact 不一定是 memory，但经常会成为 memory 的依据。

### 4. `context`

本轮送进模型窗口的信息总和。

它可能来自：

- 当前消息
- state summary
- recalled memory
- artifact summary
- external retrieval

## 为什么 context 不是 memory

这是最常见的误解。

`context` 是这轮模型调用看到什么；`memory` 是系统长期保留什么。

换句话说：

- memory 可能被召回进 context
- 但 memory 本身不等于 context

## 一个常见的更稳分层

### `request / step state`

- 当前 step 计算需要
- 生命周期最短

### `thread / session state`

- 一个连续任务的主状态
- 更适合 checkpoint / resume

### `durable memory`

- 偏好、规则、已确认事实、经验模式

### `artifact store`

- 文件、图像、日志、结果对象

### `context assembly`

- 每次调用前，动态决定要把哪部分 state / memory / artifact summary 装配进模型窗口

## 为什么 artifact separation 很重要

因为很多系统的问题不是“记不住”，而是“什么都往记忆里塞”。

如果 artifact 和 memory 不分，后面会出现：

- recall 噪声激增
- provenance 不清
- cost 高
- 过期策略失效

## 这层最该形成的判断力

### 判断 1

这是 `state mutation`，还是 `durable memory write`？

### 判断 2

这段内容该保留 `raw artifact`，还是提炼成 memory？

### 判断 3

这次模型调用真正需要多少 recalled memory，多少 artifact summary？

### 判断 4

有没有把 artifact、memory、context 三层混成一个大 prompt？

## 典型系统映射

- `LangGraph`：更强在 state / checkpoint / durable execution
- `Google ADK`：更强在 state、compaction、artifacts 的应用框架视角
- `Claude Code`：更强在 repo / project memory 与 terminal harness 的项目规则面
- `OpenClaw`：更强在 workspace-native durable memory 与 procedural files
- `LangMem`：更强在 long-term memory pipeline 抽象

## 推荐继续往下读

- [[Session and Memory Design]]
- [[长期运行 Agent 的记忆系统]]
- [[记忆写入、召回、压缩与 Consolidation]]
- [[记忆评测、污染、遗忘与纠偏]]
- [[../08-Maps/AI Memory Engineering Map|AI Memory Engineering Map]]
- [[../../AI-Learning/06-Topics/AI 记忆设计|AI 记忆设计]]
