---
title: Ruflo claude-flow
type: project
status: watch
domain: ai-open-source
category: Claude Code 生态扩展
organization: ruvnet
repo: https://github.com/ruvnet/ruflo
local_fit: medium
mac_fit: medium
production_fit: low
learning_fit: medium
created: 2026-05-15
updated: 2026-05-15
---

# Ruflo claude-flow

## 它解决什么问题

`Ruflo / claude-flow` 面向 Claude 的多 agent orchestration、swarm workflow、RAG integration 和 Claude Code / Codex 集成。

## 为什么现在值得关注

它代表 Claude Code 生态里“更激进的多 agent / swarm 编排”方向。即使不直接采用，也适合拿来观察社区如何尝试把 coding agent 升级为多 agent 工作平台。

## 它在 stack 的哪一层

- 属于 `multi-agent orchestration / swarm workflow`
- 更偏实验性平台，不是基础插件

## 核心组件与架构

- multi-agent swarm
- workflow coordination
- RAG integration
- Claude Code / Codex integration

## 最适合它的场景

- 研究多 agent 编排思路
- 对比 CCPM、wshobson-agents、SuperClaude 的不同路线
- 做非生产 sandbox 实验

## 和相邻项目怎么区分

- 和 [[CCPM]]：CCPM 更工程项目管理；Ruflo 更偏 swarm orchestration
- 和 [[wshobson-agents]]：wshobson 更偏插件和角色集合；Ruflo 更偏平台化编排

## 风险与边界

- status 标为 `watch`：先观察，不建议直接用于核心生产项目
- 多 agent/swarm 容易放大不可控性、上下文污染和权限风险
- 安装前应重点审查脚本、MCP、网络访问和文件写入行为

## 官方入口

- [ruvnet/ruflo GitHub](https://github.com/ruvnet/ruflo)

## 关联

- [[项目索引|项目索引]]
- [[../01-Categories/Claude Code 生态扩展|Claude Code 生态扩展]]

