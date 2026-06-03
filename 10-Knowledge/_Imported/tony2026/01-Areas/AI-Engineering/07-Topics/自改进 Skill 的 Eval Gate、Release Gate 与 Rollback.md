---
title: 自改进 Skill 的 Eval Gate、Release Gate 与 Rollback
type: topic
status: learning
tags:
  - ai/engineering
  - ai/memory
  - ai/evaluation
  - ai/reliability
created: 2026-03-29
updated: 2026-03-29
---

# 自改进 Skill 的 Eval Gate、Release Gate 与 Rollback

## 这页想解决什么

真正危险的不是 system 会不会提炼 skill，而是它 **在什么门槛下提炼 skill**。

如果没有 gate，`AutoSkill` 很容易退化成：

- 自动把 noise 永久化
- 自动把局部 workaround 泛化
- 自动把错误扩散到更多任务

## 先把 3 个 gate 分清

### 1. `capture gate`

什么内容允许进 `.learnings/*`。

### 2. `promotion / eval gate`

什么内容允许从 learning 升级成 durable rule 或 skill candidate。

### 3. `release gate`

什么内容允许从 candidate 变成默认启用的 skill / plugin / automation。

## 一个更稳的 7 步门槛

### 第 1 步：schema gate

learning entry 不满足结构要求，就不进入后续流水线。

至少要有：

- source
- provenance
- scope
- recurrence signal
- verification status
- related artifact

### 第 2 步：promotion rubric

只有满足这些条件的条目，才允许 promotion：

- recurring
- verified
- non-obvious
- actionable
- no secret leakage

### 第 3 步：offline eval gate

先在离线任务集上验证，不直接放生产。

最少评估：

- fresh session readability
- task success delta
- over-generalization
- conflict with existing rules / skills

### 第 4 步：shadow / read-only rollout

新 skill 先作为建议，不先作为强默认。

适合的 shadow 模式：

- 只提示 candidate rule
- 只写 draft skill，不自动加载
- 只记录 would-have-fired telemetry

### 第 5 步：canary scope

先放在：

- 单一项目
- 单一 working tree
- 单一 user
- 单一 agent type

不要一开始就全局化。

### 第 6 步：rollback / demotion hook

每次 promotion / release 都必须能回退：

- remove promoted rule
- disable skill version
- demote back to learning ledger
- record rollback reason

### 第 7 步：incident-fed regression

一旦线上出事故，就把事故样本反写进 eval suite。

这一步决定系统会不会真的变稳。

## 什么情况下宁可不上线

- provenance 不清楚
- 只在单次任务中成功
- 依赖项目特定路径或私有命名
- 需要大段上下文才能理解
- 与现有 skill 冲突
- 引入额外安全或权限风险

## release unit 应该怎么划分

### `memory entry`

最小，可回滚成本最低。

### `promoted rule`

中等风险，开始影响默认行为。

### `skill version`

高风险，因为已经被包装成复用方法。

### `plugin / automation`

最高风险，因为它可能自动触发、自动接入工具、自动跨任务运行。

## 几个很值得学的系统信号

- `ChatGPT agent` 在 system card 里明确写了：为了降低 prompt injection 对 memory 的利用，launch 时 memory 被关闭；同时高风险动作需要 user confirmation 和 watch mode。来源：[ChatGPT Agent System Card](https://cdn.openai.com/pdf/6bcccca6-3b64-43cb-a66e-4647073142d7/chatgpt_agent_system_card_launch.pdf)
- `Claude Code` 把 instructions、auto memory、project rules、MCP scope 分开，同时对 project-scoped MCP 配置要求 approval。来源：[Claude Code Memory](https://code.claude.com/docs/en/memory)、[Claude Code MCP](https://code.claude.com/docs/en/mcp)
- `OpenClaw` 的 memory、hooks、compaction flush 都明确落在 workspace files 和 plugin policy 上，这意味着 gate 应该落在文件与插件边界，而不是只靠 prompt。来源：[OpenClaw Memory](https://docs.openclaw.ai/concepts/memory)、[OpenClaw Hooks](https://docs.openclaw.ai/automation/hooks)

## 一句更稳的实践原则

**让 self-improvement 先像 code review，再像自动进化。**

## 关联

- [[Learnings、Promotion 与 Skill Extraction Pipeline]]
- [[自改进记忆的 Incident Library、Poisoning 与 Failure Cases]]
- [[Runtime 发布门槛、灰度与 Blast Radius 控制]]
- [[Eval Harness 与 Regression Suites]]
- [[../06-Projects/Memory Lab/Memory Poisoning、Shared Memory Boundary 与 Release Gates 实验|Memory Poisoning、Shared Memory Boundary 与 Release Gates 实验]]
