---
title: Incident-Fed Evals、Shadow Rollout 与 Promotion Regression
type: topic
status: learning
tags:
  - ai/engineering
  - ai/memory
  - ai/evals
created: 2026-03-29
updated: 2026-03-29
---

# Incident-Fed Evals、Shadow Rollout 与 Promotion Regression

## 这页想解决什么

当一个 self-improving system 开始从 `learnings -> promotion -> skill extraction` 走向 durable behavior，最大风险不再只是“记不住”，而是：

- 把错误经验学会
- 把 tenant boundary 学坏
- 把一次事故写成长期规则
- 把曾经修过的问题重新放回来

所以 `incident-fed eval` 的意义，不是多做一点测试，而是让过去真实出过的问题，反过来成为 release gate 的输入。

## 为什么 incident-fed 比普通 eval 更重要

普通 eval 更像静态题库。

incident-fed eval 更像运行经验驱动的回归系统，它要求我们把这些东西系统化：

- poisoning case
- shared-memory leakage case
- bad promotion case
- rollback failure case
- background task silent write case
- plugin / MCP contamination case

如果没有这一层，`self-improving` 很容易只剩下“越来越会写”，却没有“越来越不犯旧错”。

## 推荐的评测包结构

一个更稳的 promotion regression pack，至少拆成 4 类：

1. Positive cases
- 候选规则确实帮助了目标任务
- 行为更稳定、更少重复错误

2. Negative cases
- 不该触发时不能乱触发
- 不该共享的上下文不能被写进 durable memory

3. Incident replay cases
- 直接回放之前真实出现过的事故模式
- 例如 prompt injection、memory poisoning、scope leakage

4. Rollback validation cases
- 验证一旦 promotion 失败，系统能否快速降级
- 验证 demotion 后是否恢复到已知稳定状态

## Shadow Rollout 是什么

`shadow rollout` 不是半上线，而是：

- candidate 已经参与 decision
- 但暂时不拥有真正写入权或最终执行权
- 我们先看它“本来会怎么做”
- 再和基线行为做对照

对 self-improving skill 来说，shadow rollout 特别适合：

- promotion candidate review
- new skill suggestion
- memory consolidation policy
- plugin-generated durable writes

## 一条更稳的发布链

1. learning captured
2. promotion candidate proposed
3. incident-fed eval pack 通过
4. shadow rollout
5. scoped canary
6. explicit release
7. ongoing regression watch
8. rollback / demotion if needed

关键点不是把门槛堆高，而是每一层都回答一个不同问题：

- 候选值不值得看
- 候选会不会重演已知事故
- 候选在真实流量里会不会偏
- 候选失败时能不能退

## Promotion Regression 最容易漏掉什么

### 1. 只测成功样例

如果评测包全是正向题，candidate 往往会被高估。

### 2. Incident 没有结构化沉淀

事故只写在聊天里，后面就不会进入 regression pack。

### 3. Shadow 只看输出，不看写入

很多问题不是输出错，而是 memory write 错了。

### 4. Rollback 没有 owner

真正出问题时，没有人知道该删哪个 rule、降哪个 skill、停哪个 background job。

## 推荐的最小 gating 规则

一个 self-improving candidate 在进入 scoped release 前，至少要满足：

- provenance 完整
- scope 清晰
- incident replay 至少 1 个通过
- poisoning / boundary 负例至少 1 个通过
- rollback path 明确
- rollout owner 明确

## 和这条 AI memory 主线怎么接

- `Learnings、Promotion 与 Skill Extraction Pipeline` 讲的是管道
- `自改进记忆的 Incident Library、Poisoning 与 Failure Cases` 讲的是事故来源
- `自改进 Skill 的 Eval Gate、Release Gate 与 Rollback` 讲的是门槛
- 这页讲的是：**怎么把事故真正喂回评测和灰度发布**

## 关联

- [[Learnings、Promotion 与 Skill Extraction Pipeline]]
- [[自改进记忆的 Incident Library、Poisoning 与 Failure Cases]]
- [[自改进 Skill 的 Eval Gate、Release Gate 与 Rollback]]
- [[共享记忆边界：用户、项目、多 Agent 与租户隔离]]
- [[../06-Projects/Memory Lab/Incident-Fed Eval 与 Shadow Rollout 实验|Incident-Fed Eval 与 Shadow Rollout 实验]]
- [[../06-Projects/Memory Lab/最小 Self-Improving Plugin 设计|最小 Self-Improving Plugin 设计]]
- [[../08-Maps/AI Memory Engineering Map|AI Memory Engineering Map]]
