---
title: Session、Memory 与 Artifact 分层实验
type: project-doc
status: learning
project: Agent Runtime Lab
created: 2026-03-28
updated: 2026-03-28
---

# Session、Memory 与 Artifact 分层实验

## 目标

练会区分：

- request state
- invocation state
- session state
- durable memory
- artifacts

## 最小实验

选一个 agent 场景，例如：

- repo bugfix assistant
- browser task assistant
- recurring daily ops assistant

然后把它的状态分成五层。

## 输出模板

- 什么信息只活在一次调用里
- 什么信息要活在整个任务 session 里
- 什么信息可以成为 durable memory
- 哪些结果应该单独存成 artifact
- 哪些写入需要人工确认
