---
title: CCPM
type: project
status: learning
domain: ai-open-source
category: Claude Code 生态扩展
organization: Automaze
repo: https://github.com/automazeio/ccpm
local_fit: medium
mac_fit: medium
production_fit: medium
learning_fit: high
created: 2026-05-15
updated: 2026-05-15
---

# CCPM

## 它解决什么问题

`CCPM` 是面向 agents 的项目管理 skill system，使用 GitHub Issues 和 Git worktrees 支持并行 agent 执行。

## 为什么现在值得关注

Claude Code 真正进入团队协作后，核心问题会从“写一个任务”变成“多个任务如何拆分、排队、并行、追踪、合并”。CCPM 正好命中这个管理层。

## 它在 stack 的哪一层

- 属于 `agent project management / worktree orchestration`
- 位于 coding agent 与工程协作流程之间

## 核心组件与架构

- GitHub Issues
- Git worktrees
- agent task queues
- shell-based workflow

## 最适合它的场景

- 多个独立任务并行推进
- 用 GitHub Issues 驱动 agent 工作
- 学习如何把 agent 工作流接进项目管理

## 和相邻项目怎么区分

- 和 [[claude-code-action]]：action 更偏 PR/CI 自动化；CCPM 更偏任务分解和 worktree 并行
- 和 [[Ruflo claude-flow]]：CCPM 更贴近 GitHub/worktree 工程协作；Ruflo 更偏 swarm 编排

## 风险与边界

- 并行 agent 容易产生冲突和重复修改
- 必须约定 write set、分支策略和合并策略

## 官方入口

- [automazeio/ccpm GitHub](https://github.com/automazeio/ccpm)

## 关联

- [[项目索引|项目索引]]
- [[../01-Categories/Claude Code 生态扩展|Claude Code 生态扩展]]

