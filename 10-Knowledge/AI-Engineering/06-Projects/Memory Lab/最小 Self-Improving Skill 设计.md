---
title: 最小 Self-Improving Skill 设计
type: project
status: learning
project: Memory Lab
created: 2026-03-29
updated: 2026-03-29
---

# 最小 Self-Improving Skill 设计

## 为什么先做 skill，不先做 plugin

对我们当前这条线，`skill-first` 是更稳的 thin slice：

- skill 更接近方法层
- 风险比自动化 plugin 小
- 更容易先验证 `learning -> promotion -> extraction` 这条链
- 真验证通了，再打包成 plugin 不晚

## 这版最小实现想解决什么

不是让 agent 自动修改自己的全局规则，而是提供一个 **bounded workflow**：

1. 把 learnings 记到 `.learnings/*`
2. 给高价值条目生成 promotion candidate
3. 给少数稳定模式生成 skill stub
4. 强制经过 eval / rollback discipline

## 我们的落点

- 本地可执行 skill：`/Users/tony/.codex/skills/self-improving-learning-ledger`
- 仓库镜像：`/Users/tony/Documents/vault/tony2026/obsidian-skills/skills/self-improving-learning-ledger`
- 这版已经实际落地了最小脚手架：`SKILL.md`、promotion rubric、eval gate checklist，以及 3 个 helper scripts

## 最小文件结构

- `SKILL.md`
- `references/promotion-rubric.md`
- `references/eval-gate-checklist.md`
- `scripts/append_learning.py`
- `scripts/propose_promotion.py`
- `scripts/generate_skill_stub.py`

## 这版刻意不做什么

- 不自动修改全局 `AGENTS.md` / `TOOLS.md`
- 不自动启用新 skill
- 不自动跨项目共享 learnings
- 不把未评测 candidate 直接 promotion

## 先验安全边界

- log first, promote later
- promotion before extraction
- every durable write needs provenance
- every skill candidate needs eval gate
- every promotion needs rollback path

## 后续如果要进化成 plugin

最自然的下一步不是“自动写更多”，而是：

- 把 skill 包成带 UI / hooks 的 plugin
- 把 promotion candidate review 做成可交互流程
- 把 incident-fed regression 持续接进 release gate

## 关联

- [[Self-Improving-Agent 与 AutoSkill 实验]]
- [[Memory Poisoning、Shared Memory Boundary 与 Release Gates 实验]]
- [[../../07-Topics/Learnings、Promotion 与 Skill Extraction Pipeline|Learnings、Promotion 与 Skill Extraction Pipeline]]
