---
title: Block Internal Knowledge Agent Platform
type: case
status: learning
tags:
  - ai/case-study
  - ai/internal-knowledge
industry: internal-knowledge-work
problem: employees across functions struggle to access internal data and tools quickly without SQL or engineering support
solution: internal open-source agent platform using Claude in Databricks to connect tools, analyze data, and automate workflows
stack:
  - Claude
  - Databricks
results:
  - 75% of engineers save 8 to 10+ hours per week
  - adoption doubled in one month
  - 4,000 active users across 10,000 employees
lessons:
  - internal knowledge agents create outsized value when they connect tools, permissions, and data workflows
  - non-technical access to data is a major leverage point
related_topics:
  - Internal Knowledge Work Agents
created: 2026-03-23
updated: 2026-03-23
---

# Block Internal Knowledge Agent Platform

## 背景

很多企业内部知识问题并不是“没有 AI”，而是员工拿不到、用不好、串不起来内部数据和工具。

## 做了什么

- Block 用 Claude 和 Databricks 构建内部 agent 平台 `goose`
- 让员工可以连接内部工具、分析数据、生成 SQL、自动化工作流
- 通过 MCP server 把更多内部系统接进 agent 工作流

## 结果

- Anthropic 官方披露：75% engineers 每周节省 8-10+ 小时
- 官方披露：一个月内 adoption 翻倍
- 官方披露：约 4,000 名员工在使用，覆盖 15 种不同职能画像

## 为什么值得学

- 这个案例很适合说明，internal knowledge work agent 的核心不是聊天，而是 data access + tool connectivity
- 它也说明平台化能力一旦建立，会迅速扩展到多个职能而不只是工程团队
- 对很多企业来说，这类场景是 agent platform 真正能沉淀长期价值的地方

## 迁移启发

- 优先做能打通工具和数据权限的内部 assistant
- 让非技术员工也能安全解决自己的数据问题，价值会非常大
- 把 benchmark、tool success rate 和 adoption 一起看，比只看聊天满意度更有意义

## 来源

- 官方案例：[Block improves employee productivity and data access with Claude in Databricks](https://www.anthropic.com/customers/block)

## 相关

- [[../01-Industries/Internal Knowledge Work Agents|Internal Knowledge Work Agents]]
- [[../04-Case-Studies/OpenAI In-House Data Agent|OpenAI In-House Data Agent]]
- [[../../AI-Engineering/07-Topics/Tool Calling and Action Execution|Tool Calling and Action Execution]]
