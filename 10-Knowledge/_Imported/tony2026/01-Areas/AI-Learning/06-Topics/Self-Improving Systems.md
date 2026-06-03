---
title: Self-Improving Systems
type: topic
status: learning
tags:
  - ai/topic
  - ai/memory
  - ai/agent
  - ai/self-improving
created: 2026-03-31
updated: 2026-03-31
---

# Self-Improving Systems

## 这页要回答什么

不是泛泛讨论“agent 会不会自我进化”，而是把更靠谱的系统问题拆开：

- 什么可以学
- 什么不该学
- 经验如何进入 memory
- 什么时候只能 shadow observe
- 什么时候才值得 promotion
- promotion 之后怎么 eval、rollout、rollback

## 为什么这条线值得单独看

`Self-Improving Systems` 不是单一功能，而是四层东西叠在一起：

1. `learning capture`
2. `memory governance`
3. `promotion / skill extraction`
4. `release discipline`

少任何一层，系统就很容易从“会学习”滑到“乱学习”。

## 这一层最容易被误解的地方

### 不是模型自己变强

多数工程系统里的 self-improving，更接近：

- capturing preferences
- logging incidents
- consolidating repeated patterns
- proposing candidate rules or skills

而不是让权重自己在线更新。

### 不是记得越多越好

真正的问题不是“记忆少”，而是：

- polluted memory
- stale memory
- wrong promotion
- cross-project leakage
- blast radius too large

### 不是自动化越多越先进

更成熟的路线通常是：

- capture
- observe
- cluster
- verify
- replay incidents
- candidate shadow rollout
- only then promote

## 当前更值得学的系统样本

- [[../09-Systems/OpenClaw 的分层记忆设计|OpenClaw 的分层记忆设计]]
- [[../09-Systems/OpenClaw 的准自进化工作流|OpenClaw 的准自进化工作流]]
- [[../09-Systems/Self-Improving-Agent（ClawHub Skill）|Self-Improving-Agent（ClawHub Skill）]]
- [[../09-Systems/LangMem|LangMem]]
- [[../09-Systems/Claude Code|Claude Code]]
- [[../09-Systems/Codex Skills 与 Plugins|Codex Skills 与 Plugins]]
- [[../09-Systems/Self-Improving Memory Lab Plugin|Self-Improving Memory Lab Plugin]]
- [[../09-Systems/self-improving-learning-ledger 技能|self-improving-learning-ledger 技能]]

## 工程上应该怎么拆

推荐按这条线读：

1. `state / memory / artifact / context`
2. `write / recall / compression / consolidation`
3. `pollution / poisoning / forgetting / correction`
4. `promotion / skill extraction`
5. `incident-fed eval / shadow rollout`
6. `hook payload / live cache / release gate`

## 我们当前本地实验给出的一个关键认识

本地 `Self-Improving Memory Lab` 插件说明了一件很实际的事：

- 不是把逻辑写进插件源码就算“接到 runtime”了
- 还要关心：
  - live cache
  - installed path
  - real hook payload
  - debug snapshot

这一步经常被忽略，但它决定了系统到底是“实验脚本”，还是“真的接上 agent runtime”。

## 推荐继续读

- [[AI 记忆设计]]
- [[从 Learnings 到 AutoSkill：技能自提炼]]
- [[记忆污染、Memory Poisoning 与自改进风险]]
- [[../07-Maps/Self-Improving Systems 学习图|Self-Improving Systems 学习图]]
- [[../../AI-Engineering/07-Topics/Learnings、Promotion 与 Skill Extraction Pipeline|Learnings、Promotion 与 Skill Extraction Pipeline]]
- [[../../AI-Engineering/07-Topics/Incident-Fed Evals、Shadow Rollout 与 Promotion Regression|Incident-Fed Evals、Shadow Rollout 与 Promotion Regression]]
- [[../../AI-Engineering/07-Topics/Codex Plugin Hook Payload、Live Cache 与 Debug Snapshot|Codex Plugin Hook Payload、Live Cache 与 Debug Snapshot]]
- [[../../AI-Engineering/06-Projects/Memory Lab/Codex Hook Payload 兼容与 Live Cache 调试|Codex Hook Payload 兼容与 Live Cache 调试]]
