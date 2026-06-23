---
title: Runtime 事故复盘与发布门槛实验
type: project-doc
status: learning
project: Agent Runtime Lab
created: 2026-03-28
updated: 2026-03-28
---

# Runtime 事故复盘与发布门槛实验

## 目标

把 runtime 的失败模式和 rollout 控制从“看懂”变成“会自己拆”。

## 最小实验

选一个你熟悉的 agent 系统场景，例如：

- coding agent with shell + background workers
- browser agent with approvals
- channel gateway with plugins + memory + cron

然后做三件事：

1. 写一个最可能发生的 runtime 事故
2. 定义这个事故的 blast radius
3. 设计上线前应该有的 release gates

## 你应该输出的内容

- 事故属于哪一层：control / execution / state / rollout / observability
- 影响哪些 capability、哪些用户、哪些 session
- 哪些指标本应提前报警
- 哪些 rollout 步骤本应更慢
- 哪些 gates 应从建议变成硬门槛

## 推荐配套阅读

1. [[../../07-Topics/Agent Runtime 失败模式、事故复盘与 Postmortems|Agent Runtime 失败模式、事故复盘与 Postmortems]]
2. [[../../07-Topics/Runtime 发布门槛、灰度与 Blast Radius 控制|Runtime 发布门槛、灰度与 Blast Radius 控制]]
3. [[../../07-Topics/Plugin、Memory 与 Background Task 失效模式|Plugin、Memory 与 Background Task 失效模式]]
