---
title: 记忆写入、召回、压缩与 Consolidation
type: topic
status: learning
tags:
  - ai/engineering
  - ai/memory
  - ai/consolidation
created: 2026-03-29
updated: 2026-03-29
---

# 记忆写入、召回、压缩与 Consolidation

## 为什么 memory 系统真正难在这里

很多团队都能“加一个 memory store”，但成熟系统和 demo 的差距，通常出在：

- 什么时候写
- 写什么
- 什么时候召回
- 召回多少
- 怎么压缩
- 怎么在后台整理成更稳定的长期记忆

## 先把写入分两类

### `hot-path write`

在任务执行过程中即时写入。

优点：

- 立刻可用
- 对当前长任务帮助大

代价：

- latency 增加
- 更容易把猜测写成事实
- 更容易被 prompt injection 或局部错误污染

### `background consolidation`

先保留 trace / transcript / artifacts，再后台抽取 durable memory。

优点：

- 更稳
- 更适合加 provenance、去重、纠偏
- 更容易做 write policy

代价：

- 不是即时生效
- 需要额外队列、作业、治理和评测

## recall 不只是检索，更是预算分配

一个成熟 recall policy 至少要回答：

- 为什么这条 memory 被召回
- 这次召回多少条
- 是把原文召回，还是 summary
- 召回后对 context budget 的影响是什么

也就是说，recall 不只是命中率问题，还是 `context budget allocation` 问题。

## 三种压缩方式

### 1. `summary compaction`

把长 transcript 压缩成短摘要。

### 2. `fact extraction`

抽取稳定事实、偏好、规则。

### 3. `experience consolidation`

不是抽取事实，而是抽取经验模式：

- 什么做法经常成功
- 什么工具顺序更稳
- 什么失败模式应该提前规避

## consolidation 真正的目标

不是把东西压得更短，而是把低价值历史变成高价值结构。

例如把：

- 原始对话
- 原始日志
- 原始工具输出

整理成：

- stable facts
- episodic summaries
- procedural updates
- searchable artifacts

## 一个更稳的 pipeline

1. 执行任务，生成 raw trace 和 artifacts
2. 热路径只更新必要 state，少量写 memory
3. 后台提取 semantic / episodic / procedural candidates
4. 做去重、归并、权限检查、过期检查
5. 将通过的内容写入 durable memory
6. 将高风险变更送进 review / eval gate

## 什么时候该保守

- memory 会影响 tool use
- memory 会影响 routing
- memory 可能跨用户 / 跨项目共享
- memory 会进入长期默认 prompt
- memory 会改变安全或合规行为

这些场景里，background consolidation 往往比 hot-path write 更稳。

## 最容易踩的坑

- 每轮都写，导致 memory 污染
- 召回太多，context 被淹没
- 压缩后丢掉 provenance
- summary 越压越偏，最后变成错误事实
- 没有 forgetting，memory 只增不减

## 推荐继续往下读

- [[记忆架构：State、Memory、Artifact 与 Context]]
- [[记忆评测、污染、遗忘与纠偏]]
- [[长期运行 Agent 的记忆系统]]
- [[Plugin、Memory 与 Background Task 失效模式]]
- [[../../AI-Learning/09-Systems/LangMem|LangMem]]
- [[../../AI-Learning/09-Systems/OpenClaw 的分层记忆设计|OpenClaw 的分层记忆设计]]
