---
title: 我想理解 AI 记忆与自改进
type: guide
status: active
updated: 2026-04-03
---

# 我想理解 AI 记忆与自改进

## 先判断你说的 memory 到底是哪种 memory

- weights / parametric memory
- chat / project memory
- runtime state
- durable memory
- artifacts
- background consolidation

如果这些层不先分开，后面几乎一定会把“记忆”“上下文”“状态”“技能提炼”混成一团。

## 最短阅读路径

1. [[AI 总控制塔|AI 总控制塔]]
2. [[AI-Learning/06-Topics/AI 记忆设计|AI 记忆设计]]
3. [[AI-Learning/06-Topics/Agent Memory|Agent Memory]]
4. [[AI-Learning/06-Topics/大模型记忆、项目记忆与 Chat Memory|大模型记忆、项目记忆与 Chat Memory]]
5. [[AI-Learning/07-Maps/AI 记忆设计图|AI 记忆设计图]]
6. [[AI-Engineering/07-Topics/记忆架构：State、Memory、Artifact 与 Context|记忆架构：State、Memory、Artifact 与 Context]]
7. [[AI-Engineering/07-Topics/记忆写入、召回、压缩与 Consolidation|记忆写入、召回、压缩与 Consolidation]]
8. [[AI-Engineering/07-Topics/记忆评测、污染、遗忘与纠偏|记忆评测、污染、遗忘与纠偏]]
9. [[AI-Engineering/07-Topics/Learnings、Promotion 与 Skill Extraction Pipeline|Learnings、Promotion 与 Skill Extraction Pipeline]]
10. [[AI-Learning/06-Topics/从 Learnings 到 AutoSkill：技能自提炼|从 Learnings 到 AutoSkill：技能自提炼]]
11. [[AI-Learning/09-Systems/OpenClaw 的分层记忆设计|OpenClaw 的分层记忆设计]]
12. [[AI-Learning/09-Systems/OpenClaw 的准自进化工作流|OpenClaw 的准自进化工作流]]
13. [[AI-Engineering/08-Maps/AI Memory Engineering Map|AI Memory Engineering Map]]
14. [[AI-Engineering/06-Projects/Memory Lab/项目总览|Memory Lab]]

## 这条线最值得看的不是“会不会记”

而是：

- 写入边界怎么定义
- recall policy 怎么收敛
- 什么该留下，什么该忘掉
- 什么时候允许 promotion，什么时候必须 shadow review
- 自改进为什么一定要有 eval gate、release gate 和 rollback

## 读完这条线后，你应该能自己回答

- `memory`、`state`、`artifact`、`context` 为什么不能混
- “持续学习”什么时候是能力，什么时候是风险
- 一个 self-improving workflow 最小应该长什么样
- 为什么 incident replay、promotion report 和 candidate skill 是必要中间层

## 关联

- [[AI 问题导航|AI 问题导航]]
- [[AI-Learning/07-Maps/Self-Improving Memory 风险与治理图|Self-Improving Memory 风险与治理图]]
