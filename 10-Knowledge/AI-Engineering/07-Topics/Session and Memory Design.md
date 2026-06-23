---
title: Session and Memory Design
type: topic
status: learning
tags:
  - ai/engineering
  - ai/session
  - ai/memory
created: 2026-03-22
updated: 2026-03-29
---

# Session and Memory Design

## 为什么这一页是 runtime 成败的分水岭

很多 agent 的稳定性问题，本质上不是模型差，而是 session 和 memory 设计差。

如果这两层没有分开，系统通常会出现两种问题：

- 不该记住的也记住了
- 该长期保留的却丢了

## 先把几个层次分开

### `request state`

一次请求或一次 step 内的局部变量。

### `invocation state`

一次完整执行链路内共享的中间状态。很多系统的 subagent / callback / tool chain 都会共享这一层。

### `session state`

一次连续对话或任务的主状态容器。

### `durable memory`

跨 session 持续保留的信息，例如：

- 用户偏好
- 已确认事实
- 项目约定
- 稳定规则

### `artifacts`

不是“记忆”，而是产物：

- 文件
- 截图
- 报告
- patch
- 结构化输出

很多系统把 artifacts 错放进 memory，后面会越来越乱。

## 为什么 session 和 memory 经常被混淆

因为对用户来说它们都叫“记住了”。

但对系统来说：

- session 更像任务容器
- memory 更像长期知识层

比如 `ADK` 把 `session.events` 和 `session.state` 区分开；`Claude Code` 也明确区分会话上下文和 `CLAUDE.md` / auto memory；这正说明成熟系统不会把所有状态混成一团。

## 设计 session 时最该想清楚的事

### 1. 边界按什么切

- 用户
- 渠道
- 任务
- repo / working tree
- tenant

### 2. 生命周期怎么结束

- 自动超时
- 手动关闭
- 交付完成自动封存
- 转入后台任务继续

### 3. checkpoint 放在哪

如果没有 checkpoint，复杂任务失败后就很难接着做。

## 设计 memory 时最该想清楚的事

### 1. 什么是事实，什么只是临时猜测

只有被确认过、可追溯的内容才适合进入 durable memory。

### 2. 谁能写入 memory

- 模型直接写
- 人工确认后写
- hooks / tools 写
- 某些系统层回调写

这件事决定 memory 是否可信。

### 3. recall 怎么做

- 直接注入固定文件
- 检索召回
- summary / compaction
- per-user / per-project memory filter

## 一个更稳的分层策略

### 短期上下文

- 直接随 session 传递
- 适合当前任务内部连续工作

### 工作记忆

- 适合多步任务推进
- 可以 checkpoint
- 不应该自动升级为长期记忆

### 长期记忆

- 偏好、规则、稳定事实
- 需要更强的 write policy

### 产物层

- 文件、图像、日志、报告、diff
- 应放进 artifact store，而不是混进记忆文本

## 为什么现在越来越多系统强调 compaction 和 artifact separation

因为长任务里，真正要解决的不是“记得更多”，而是：

- 哪些历史要压缩
- 哪些状态要保留结构化形式
- 哪些产物要单独存
- 哪些内容绝不能直接写进长期记忆

## 典型失败模式

### 1. memory 污染

模型的猜测、错误结论、临时假设被误写成长期事实。

### 2. session 膨胀

所有历史都塞进上下文，导致成本高、延迟高、还不稳定。

### 3. recall 不可审计

系统拿回了什么历史、为什么拿回来、是否过期，没人说得清。

### 4. artifacts 和 memory 混在一起

长文、日志、结果文件全部塞回 memory，后面 recall 会越来越糟。

## 学这一页最该形成的判断力

### 判断 1：这是 session 问题，还是 durable memory 问题

很多系统故障只要先分清这层，就会好处理很多。

### 判断 2：当前内容该被压缩、提取、结构化，还是根本不该保留

不是所有历史都值得保存。

### 判断 3：哪些写入必须经过确认

长期记忆写入应该比 session 更新更保守。

## 推荐怎么连着读

1. [[记忆架构：State、Memory、Artifact 与 Context]]
2. [[记忆写入、召回、压缩与 Consolidation]]
3. [[记忆评测、污染、遗忘与纠偏]]
4. [[Agent Runtime Architecture]]
5. [[Background Agents]]
6. [[Delegation and Task-Oriented Agents]]
7. [[Long-Running Agent Operations]]
8. [[长期运行 Agent 的记忆系统]]

## 相关主题

- [[记忆架构：State、Memory、Artifact 与 Context]]
- [[记忆写入、召回、压缩与 Consolidation]]
- [[记忆评测、污染、遗忘与纠偏]]
- [[Agent Runtime Architecture]]
- [[Background Agents]]
- [[Delegation and Task-Oriented Agents]]
- [[Long-Running Agent Operations]]
- [[长期运行 Agent 的记忆系统]]
- [[Tool Calling and Action Execution]]

## 资料

- [Claude Code memory](https://code.claude.com/docs/en/memory)
- [ADK State](https://google.github.io/adk-docs/sessions/state/)
- [ADK Context Compaction](https://google.github.io/adk-docs/context/compaction/)
- [ADK Artifacts](https://google.github.io/adk-docs/artifacts/)
