---
title: Coding Agent Workflow
type: workflow
status: learning
tags:
  - ai/workflow
  - ai/coding
inputs:
  - task definition
  - codebase context
  - tests or acceptance criteria
steps:
  - inspect codebase
  - plan changes
  - edit files
  - run validation
  - handoff for review
tools:
  - terminal
  - git
  - IDE
  - tests
outputs:
  - code changes
  - validation results
  - review-ready patch
evaluation:
  - task completion
  - regression rate
  - human takeover rate
risks:
  - unsafe execution
  - hidden regressions
  - task drift
related_products:
  - Claude Code 产品卡
  - Cursor 产品卡
  - Codex 产品卡
created: 2026-03-22
updated: 2026-03-22
---

# Coding Agent Workflow

## 简介

coding workflow 的关键不是“模型会不会写代码”，而是 agent 能不能在真实工程环境里安全地读、改、跑、验、交付。

## 步骤

1. 读取任务与仓库上下文
2. 拆解任务与制定实现路径
3. 修改代码与补充测试
4. 运行验证与修复问题
5. 交给人 review、接管或合并

## 工具链

- repository access
- terminal
- tests / lint / build
- issue tracker / PR workflow

## 评估

- task completion rate
- review acceptance rate
- regression rate
- developer handoff quality

## 风险

- 命令自动执行带来的安全与泄露风险
- agent 改动看似可行但不符合工程规范
- 长链任务里状态漂移和误解需求

## 最适合的产品

- [[../02-Products/Claude Code 产品卡|Claude Code 产品卡]]
- [[../02-Products/Cursor 产品卡|Cursor 产品卡]]
- [[../02-Products/Codex 产品卡|Codex 产品卡]]

## 相关

- [[../../AI-Learning/06-Topics/Coding Agents|Coding Agents]]
- [[../../AI-Engineering/07-Topics/Multi-Agent Coding Workflow|Multi-Agent Coding Workflow]]
- [[../../AI-Engineering/07-Topics/Task Success and Failure Recovery|Task Success and Failure Recovery]]
