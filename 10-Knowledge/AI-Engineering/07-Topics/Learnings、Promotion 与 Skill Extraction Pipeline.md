---
title: Learnings、Promotion 与 Skill Extraction Pipeline
type: topic
status: learning
tags:
  - ai/engineering
  - ai/memory
  - ai/skills
  - ai/harness
  - ai/runtime
created: 2026-03-29
updated: 2026-03-29
---

# Learnings、Promotion 与 Skill Extraction Pipeline

## 为什么这页值得单独拆出来

很多 agent memory 设计最终都会碰到一个问题：

- 哪些东西只是日志
- 哪些东西该变成长期规则
- 哪些东西值得抽成 skill

如果没有这条 pipeline，系统要么完全不成长，要么把所有 noise 都升级成永久 guidance。

## 一条工程上更稳的流水线

### 1. `capture`

输入源包括：

- 用户纠正
- tool failure
- debugging discovery
- repeated task friction
- feature request
- postmortem conclusion

输出先进入 learning log，而不是直接修改核心规则。

### 2. `normalize`

最少要带这些字段：

- id
- area
- source
- priority
- status
- related files
- recurrence signal
- provenance
- resolution state

如果这层不规范，后面的 promotion 和 extraction 会越来越乱。

### 3. `promotion`

先把高价值经验推广成长期规则或 durable workspace memory：

- `AGENTS.md`
- `TOOLS.md`
- `SOUL.md`
- `CLAUDE.md`
- `MEMORY.md`

这一步强调的是：

- concise rule
- stable fact
- actionable checklist

而不是把整段事故原文照抄进去。

### 4. `skill extraction`

只有当一个模式同时具备复用价值和独立可教性时，才适合变成 `SKILL.md`。

典型判断维度：

- recurring
- verified
- non-obvious
- broadly applicable
- easy to teach in isolation

### 5. `evaluation gate`

提炼后的 skill 要回答：

- 新 session 里是否能独立理解
- 是否真能减少同类问题
- 是否和已有 skill 冲突
- 是否引入过度泛化或错误默认值

### 6. `release / rollback`

skill 不是只增不减。

真正成熟的系统需要：

- versioning
- deprecation
- conflict resolution
- rollback / demotion
- audit trail

## 这条 pipeline 里最容易被混淆的对象

### `memory`

更适合放：

- 稳定偏好
- durable facts
- recurring guidance

### `artifact`

更适合放：

- transcript excerpt
- stack trace
- issue reproduction
- screenshot
- diff

### `rule file`

更适合放：

- task checklist
- workflow default
- tool gotcha
- behavioral constraint

### `skill`

更适合放：

- 一套跨任务可复用的方法论
- 带明确使用条件的操作包

## OpenClaw 在这条线上的代表性

`OpenClaw` 特别适合学这条 pipeline，因为它几乎把每一层都具象化了：

- `.learnings/*` 做 capture
- workspace files 做 promotion
- `skills` / `ClawHub` 做 extraction 与 distribution
- `hooks` / `sessions_*` 做 automation 与传播

## 为什么这一页和 Harness Engineering 有直接关系

因为一旦开始提炼 skill，你就不只是在做 memory design，而是在设计 harness 的扩展面。

也就是说，这条 pipeline 同时连接：

- memory engineering
- runtime governance
- skill ecosystem
- automation discipline

## 风险清单

### 1. `learning poisoning`

恶意输入或错误结论被当成经验保存下来。

### 2. `premature promotion`

尚未验证的 workaround 被升级成长期规则。

### 3. `skill bloat`

任何小经验都被抽成 skill，最后导致 skill ecosystem 噪声化。

### 4. `context collision`

多个 skill 或 rule 文件表达重复、冲突甚至相互抵消。

### 5. `false generalization`

单项目有效的技巧被包装成“广泛适用方法”。

## 更稳的工程原则

- log first, promote later
- promote before extracting skills
- keep provenance
- evaluate before broad rollout
- allow rollback and demotion
- separate memory, rules, and skills

## 推荐继续读

- [[记忆架构：State、Memory、Artifact 与 Context]]
- [[记忆写入、召回、压缩与 Consolidation]]
- [[记忆评测、污染、遗忘与纠偏]]
- [[Harness Engineering]]
- [[技能、插件、应用与自动化：Harness 的扩展面]]
- [[../../AI-Learning/09-Systems/Self-Improving-Agent（ClawHub Skill）|Self-Improving-Agent（ClawHub Skill）]]
- [[../../AI-Learning/09-Systems/OpenClaw 的准自进化工作流|OpenClaw 的准自进化工作流]]
- [[../06-Projects/Memory Lab/Self-Improving-Agent 与 AutoSkill 实验|Self-Improving-Agent 与 AutoSkill 实验]]
