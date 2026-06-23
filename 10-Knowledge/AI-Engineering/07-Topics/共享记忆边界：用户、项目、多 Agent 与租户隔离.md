---
title: 共享记忆边界：用户、项目、多 Agent 与租户隔离
type: topic
status: learning
tags:
  - ai/engineering
  - ai/memory
  - ai/runtime
  - ai/security
created: 2026-03-29
updated: 2026-03-29
---

# 共享记忆边界：用户、项目、多 Agent 与租户隔离

## 为什么这页重要

很多 memory 设计问题，表面上像检索效果问题，实际上是 scope 问题。

也就是说，系统真正先要回答的不是“记什么”，而是：

- 谁能写
- 谁能读
- 谁能继承
- 谁能推广

## 最稳的 5 层边界

### 1. `session state`

只服务当前 turn / 当前 session。

适合：

- 当前任务的 scratchpad
- 尚未验证的中间结论
- 临时计划与 tool trace

### 2. `project memory`

只服务当前项目或 working tree。

适合：

- build / test / debug 经验
- repo-specific workflow
- 本项目常见坑

### 3. `shared team memory`

服务团队协作，但必须明确 namespace 与 owner。

适合：

- 团队约定
- 公共服务依赖说明
- 常用排障路径

### 4. `durable policy / rule files`

更像可审核的长期规则，而不是自由生长的 memory。

适合：

- 安全要求
- 发布门槛
- 受控 workflow

### 5. `skill / plugin / automation`

这是最高风险的一层，因为一旦进入这里，就意味着“这套方法值得复用”。

## 几个系统给我们的启发

### OpenClaw

`MEMORY.md` 只在 main private session 加载，而 group context 不加载，这是非常典型的 boundary choice。它在提醒我们：**不是所有长期记忆都应该共享。** 另外 daily log 和 curated memory 分层，也说明 append-only log 不等于 durable policy。来源：[OpenClaw Memory](https://docs.openclaw.ai/concepts/memory)

### Claude Code

`CLAUDE.md` 明确区分 project / user / org scope，auto memory 则按 working tree 组织。这种设计在实践里很重要，因为它把“团队共享规则”和“Claude 自己积累的 learnings”分成了两类不同对象。来源：[Claude Code Memory](https://code.claude.com/docs/en/memory)

### LangMem / LangGraph

`namespace` 是核心设计对象。不要把 store 想成一个大桶，而要先定义 `(tenant, project, user, memory_type)` 这类命名空间。来源：[LangMem Memory Tools API](https://langchain-ai.github.io/langmem/reference/tools/)

### ADK

`state`、`artifacts`、`context compaction` 分开，实际上就是在告诉你：不是所有跨 turn 数据都应该进同一种持久层。来源：[ADK State](https://google.github.io/adk-docs/sessions/state/)、[ADK Context Compaction](https://google.github.io/adk-docs/context/compaction/)、[ADK Artifacts](https://google.github.io/adk-docs/artifacts/)

## 多 Agent 场景尤其要防什么

### 1. writer / reader 不对称

一个 background agent 写，另一个 task agent 读，但双方不知道上下文边界。

### 2. subagent 局部经验被主 agent 误当全局经验

局部试验性的发现不应该自动进入 shared memory。

### 3. cross-tenant contamination

多租户系统里，如果 namespace 粗糙，团队 A 的经验可能会成为团队 B 的默认。

## 设计边界时最值得明确的字段

- `scope`: session / project / team / tenant / global
- `writer`: user / foreground agent / background agent / hook
- `review_required`: yes / no
- `expiry`: session / time-based / permanent-until-reviewed
- `promotion_target`: memory / rule / skill / none

## 一个更稳的默认策略

- `session state` 默认不 promotion
- `project memory` 可以自动写，但要有 provenance
- `shared team memory` 默认 require review
- `skill extraction` 默认 require eval + human approval
- `tenant / global scope` 只允许极少数 curated rules 进入

## 关联

- [[记忆架构：State、Memory、Artifact 与 Context]]
- [[Session and Memory Design]]
- [[长期运行 Agent 的记忆系统]]
- [[自改进记忆的 Incident Library、Poisoning 与 Failure Cases]]
- [[自改进 Skill 的 Eval Gate、Release Gate 与 Rollback]]
