---
title: Memory 分层与写入策略实验
type: project-note
status: learning
created: 2026-03-29
updated: 2026-03-29
---

# Memory 分层与写入策略实验

## 实验目标

给一个小型 agent / assistant demo 明确拆出：

- request state
- session state
- durable memory
- artifact store
- context assembly

并且为每一层制定：

- 生命周期
- 写入主体
- recall 方式
- 过期或撤销方式

## 你应该产出什么

- 一张 memory architecture 表
- 一套 write policy
- 一套 recall policy
- 一套 artifact separation 规则

## 最值得观察的点

- 哪些信息最容易被误写成长期 memory
- 哪些 artifacts 其实只该保留 raw object，不该提炼成 summary
- 哪些信息应该先记日志，再后台 consolidation

## 推荐配套阅读

- [[../../07-Topics/记忆架构：State、Memory、Artifact 与 Context|记忆架构：State、Memory、Artifact 与 Context]]
- [[../../07-Topics/记忆写入、召回、压缩与 Consolidation|记忆写入、召回、压缩与 Consolidation]]
