---
title: self-improving-learning-ledger 技能
type: system
status: learning
tags:
  - ai/system
  - ai/skill
  - ai/memory
  - ai/self-improving
created: 2026-03-31
updated: 2026-03-31
---

# self-improving-learning-ledger 技能

## 这是什么

这是我们自己做的一个 **Codex skill**，目标不是自动修改全局规则，而是把更安全的自改进流程固化成可复用方法：

- bounded learning capture
- promotion review
- incident-fed observation
- candidate skill generation
- eval gate
- rollback discipline

它是整个 `Self-Improving Memory Lab` 的方法骨架。

## 当前本地位置

- 本地 skill：
  - `/Users/tony/.codex/skills/self-improving-learning-ledger`
- plugin bundled skill：
  - `/Users/tony/plugins/self-improving-memory-lab/skills/self-improving-learning-ledger`
- 仓库镜像：
  - `/Users/tony/Documents/vault/tony2026/obsidian-skills/skills/self-improving-learning-ledger`

## 它负责什么，不负责什么

### 它负责

- 把 learnings 收进 `.learnings`
- 用 rubric 给 promotion 候选打分
- 生成 review-only candidate skill
- 给自改进流程加上 eval gate 和边界说明

### 它不负责

- 直接启用新规则
- 直接改全局 durable memory
- 自动跨项目共享经验
- 绕过人工确认直接 rollout

## 它在整个插件实验里处于哪一层

如果把我们这条实验链拆层，可以这样看：

- `skill`
  - 负责方法与评审标准
- `plugin`
  - 负责 hooks、scripts、orchestration
- `incident pack`
  - 负责 regression replay

也就是说：

- `self-improving-learning-ledger` 是方法层
- `Self-Improving Memory Lab Plugin` 是运行层

## 当前最重要的几个文件

- `/Users/tony/.codex/skills/self-improving-learning-ledger/SKILL.md`
- `/Users/tony/.codex/skills/self-improving-learning-ledger/references/promotion-rubric.md`
- `/Users/tony/.codex/skills/self-improving-learning-ledger/references/eval-gate-checklist.md`
- `/Users/tony/.codex/skills/self-improving-learning-ledger/scripts/append_learning.py`
- `/Users/tony/.codex/skills/self-improving-learning-ledger/scripts/propose_promotion.py`
- `/Users/tony/.codex/skills/self-improving-learning-ledger/scripts/generate_skill_stub.py`

## 这一层为什么有价值

很多所谓“self-improving agent”最大的问题，不是不会学，而是：

- 什么都记
- 什么都升格
- 缺少 rollback
- 缺少安全门禁

这个 skill 的真正价值，是把“学到什么”和“能不能升级成长期规则”分开。

## 推荐继续读

- [[Codex Skills 与 Plugins]]
- [[Self-Improving Memory Lab Plugin]]
- [[Self-Improving-Agent（ClawHub Skill）]]
- [[../../AI-Engineering/07-Topics/Learnings、Promotion 与 Skill Extraction Pipeline|Learnings、Promotion 与 Skill Extraction Pipeline]]
- [[../../AI-Engineering/07-Topics/自改进 Skill 的 Eval Gate、Release Gate 与 Rollback|自改进 Skill 的 Eval Gate、Release Gate 与 Rollback]]
- [[../../AI-Engineering/06-Projects/Memory Lab/Self-Improving Memory Lab 插件实战|Self-Improving Memory Lab 插件实战]]
