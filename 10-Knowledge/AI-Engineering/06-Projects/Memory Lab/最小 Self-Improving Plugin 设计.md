---
title: 最小 Self-Improving Plugin 设计
type: project
status: learning
project: Memory Lab
created: 2026-03-29
updated: 2026-03-29
---

# 最小 Self-Improving Plugin 设计

## 为什么 plugin 是下一步，不是起点

`plugin` 更适合承载：

- hooks
- review handoff
- background promotion jobs
- wrapper scripts
- maybe later UI

但在我们这条线上，它应该建立在已经有的 `skill-first` 薄切片之上，而不是跳过 skill 直接上自动化。

## 这版最小 plugin 想做什么

不是自动帮 agent 改全局行为，而是把这几个动作收成一个更稳定的壳：

1. 捕获 learnings
2. 生成 promotion review
3. 触发 candidate skill stub
4. 把 shadow rollout / rollback discipline 包成固定流程

## 当前本地落点

- local plugin scaffold：`/Users/tony/plugins/self-improving-memory-lab`
- local executable skill：`/Users/tony/.codex/skills/self-improving-learning-ledger`

## 这版 plugin 应该包含什么

- `.codex-plugin/plugin.json`
- `skills/`：承接或镜像现有 bounded self-improving skill
- `hooks/`：记录哪些事件上该 capture learning
- `scripts/`：运行 promotion review、candidate generation、shadow rollout helper

## 不应该做什么

- 不自动修改全局 durable rules
- 不跨项目自动共享 memory
- 不绕开 eval gate 直接 enable 新 skill
- 不让 background task 静默 promotion

## 更合理的插件职责

plugin 负责：

- orchestration
- hook points
- bounded automation
- review handoff

skill 负责：

- methodology
- promotion rubric
- eval gate
- skill extraction discipline

## 这版的判断

plugin-first 很容易过度自动化。更稳的方式是：

- 先有 skill
- 再有 incident-fed eval
- 再有 plugin wrapper
- 最后才考虑更自动的 rollout

## 关联

- [[最小 Self-Improving Skill 设计]]
- [[Incident-Fed Eval 与 Shadow Rollout 实验]]
- [[../../07-Topics/Incident-Fed Evals、Shadow Rollout 与 Promotion Regression|Incident-Fed Evals、Shadow Rollout 与 Promotion Regression]]
