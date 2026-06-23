---
title: Memory Poisoning、Shared Memory Boundary 与 Release Gates 实验
type: project
status: learning
project: Memory Lab
created: 2026-03-29
updated: 2026-03-29
---

# Memory Poisoning、Shared Memory Boundary 与 Release Gates 实验

## 这个实验想验证什么

不是 memory system 能不能“记住更多”，而是：

- 不可信内容能不能被拦在 learnings 层
- project / user / shared memory 边界是否足够清楚
- skill extraction 有没有 eval gate 和 rollback

## 实验 1：poisoned learning entry

构造一个来自 tool output 或网页内容的恶意 instruction，观察系统是否会把它误记成 durable learning。

### 期望结果

- 条目只能进入 quarantine / low-trust ledger
- 不允许直接 promotion

## 实验 2：shared namespace leakage

模拟两个项目或两个 agent 共用粗粒度 namespace。

### 观察点

- 一个项目的 workaround 是否污染另一个项目
- subagent 的局部经验是否误变成 team-wide memory

## 实验 3：promotion review

从 5 条 learning 中挑 1 条真正 recurring 的条目 promotion，另外 4 条全部拦下。

### 观察点

- 有没有清楚的 review rubric
- `why promoted` 是否能被写清楚

## 实验 4：skill extraction eval gate

给候选 skill 跑一个小型 regression suite：

- fresh session readability
- success delta
- false generalization
- conflict with existing skills

### 期望结果

- 至少有一条 candidate 因为 over-generalization 被拦下

## 实验 5：rollback / demotion

把一个已 promotion 的 candidate 回退到 learning ledger。

### 观察点

- 回退是否容易
- provenance 是否完整
- 下游 skill / rule 是否同步失效

## 输出物

- 一份 poisoning 样本清单
- 一份 scope matrix
- 一份 promotion rubric
- 一份 eval checklist
- 一份 rollback runbook

## 推荐前置阅读

1. [[../../07-Topics/记忆评测、污染、遗忘与纠偏|记忆评测、污染、遗忘与纠偏]]
2. [[../../07-Topics/Learnings、Promotion 与 Skill Extraction Pipeline|Learnings、Promotion 与 Skill Extraction Pipeline]]
3. [[../../07-Topics/共享记忆边界：用户、项目、多 Agent 与租户隔离|共享记忆边界：用户、项目、多 Agent 与租户隔离]]
4. [[../../07-Topics/自改进 Skill 的 Eval Gate、Release Gate 与 Rollback|自改进 Skill 的 Eval Gate、Release Gate 与 Rollback]]
5. [[../../07-Topics/自改进记忆的 Incident Library、Poisoning 与 Failure Cases|自改进记忆的 Incident Library、Poisoning 与 Failure Cases]]
