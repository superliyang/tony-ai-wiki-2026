---
title: awesome-claude-code-subagents
type: project
status: learning
domain: ai-open-source
category: Claude Code 生态扩展
organization: VoltAgent
repo: https://github.com/VoltAgent/awesome-claude-code-subagents
local_fit: high
mac_fit: high
production_fit: medium
learning_fit: high
created: 2026-05-15
updated: 2026-05-15
---

# awesome-claude-code-subagents

## 它解决什么问题

`awesome-claude-code-subagents` 收集大量面向 Claude Code 的 specialized subagents，覆盖核心开发、语言专家、基础设施、质量安全、数据 AI、开发者体验等类别。

## 为什么现在值得关注

如果要理解 subagent 该如何分层和命名，这个项目非常适合做 taxonomy 参考。

## 它在 stack 的哪一层

- 属于 `subagent catalog`
- 是专家角色库，不是完整 agent runtime

## 核心组件与架构

- `.claude/agents/`
- category-based subagent files
- plugin installation path
- interactive installer

## 最适合它的场景

- 快速找 code-reviewer、security-auditor、test-automator、cloud-architect 等角色
- 为团队设计 subagent 命名规范和角色边界
- 学习什么角色适合沉淀成 subagent

## 和相邻项目怎么区分

- 和 [[wshobson-agents]]：它更像 subagent awesome list；wshobson 更像插件化工作流系统
- 和 [[anthropics-skills]]：subagent 解决角色分工，skill 解决方法沉淀

## 风险与边界

- subagent 质量不等，需要逐个审查提示词和权限
- 不要把“角色很多”误认为“协作更强”，核心仍是任务边界和验证

## 官方入口

- [awesome-claude-code-subagents GitHub](https://github.com/VoltAgent/awesome-claude-code-subagents)

## 关联

- [[项目索引|项目索引]]
- [[../01-Categories/Claude Code 生态扩展|Claude Code 生态扩展]]

