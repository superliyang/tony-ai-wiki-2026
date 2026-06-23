---
title: Search and Planning
type: topic
status: learning
tags:
  - ai/foundations
created: 2026-03-13
updated: 2026-04-03
---

# Search and Planning

## 为什么重要

- 很多智能问题可以被描述为“在可能动作中找到最优路径”
- 这是理解早期 AI、经典算法和现代 agent 系统的重要入口

## 核心问题

- 当前状态是什么
- 目标状态是什么
- 系统如何在有限资源下搜索可行路径

## 典型思路

- 暴力搜索
- 启发式搜索
- 规划算法

## 和今天的关系

- 现代 agent、tool use、reasoning workflow 中，很多步骤依然带有 search/planning 的影子

## 今天它以什么形式活着

- planning loop
- task decomposition
- tool-using agent
- workflow orchestration

## 今天最容易误解它的地方

- 很多人会把生成式步骤误当成“天然规划”
- 但一旦任务跨步骤和状态，search / planning 问题就会重新出现

## 建议继续读什么

- [[Symbolic AI]]
- [[Reinforcement Learning Basics]]
- [[../../从 Symbolic AI 到 LLM Agent：旧问题的新形式|从 Symbolic AI 到 LLM Agent：旧问题的新形式]]
