---
title: Claude Code 生态扩展
type: category
status: active
domain: ai-open-source
created: 2026-05-15
updated: 2026-05-15
---

# Claude Code 生态扩展

## 这个分类解决什么问题

`Claude Code 生态扩展` 关注的是围绕 Claude Code 的开源能力层：skills、plugins、subagents、hooks、MCP、GitHub Actions、项目管理、质量门禁、安全防护和多 agent 编排。

它不是“谁 stars 多就装谁”，而是回答：

- 哪些扩展真正改善 Claude Code 的工作流
- 哪些扩展适合个人学习，哪些适合团队落地
- 哪些扩展是能力集合，哪些是治理/安全门禁
- 哪些扩展应该只读、试用、隔离安装

## 分类层次

### 官方与准官方入口

- [[../03-Projects/anthropics-skills|anthropics-skills]]
- [[../03-Projects/claude-plugins-official|claude-plugins-official]]
- [[../03-Projects/claude-code-action|claude-code-action]]
- [[../03-Projects/claude-code-security-review|claude-code-security-review]]

### 能力集合与配置框架

- [[../03-Projects/SuperClaude Framework|SuperClaude Framework]]
- [[../03-Projects/claude-code-templates|claude-code-templates]]
- [[../03-Projects/wshobson-agents|wshobson-agents]]
- [[../03-Projects/awesome-claude-code-subagents|awesome-claude-code-subagents]]
- [[../03-Projects/awesome-claude-plugins|awesome-claude-plugins]]
- [[../03-Projects/awesome-claude-skills|awesome-claude-skills]]

### 工程工作流与团队协作

- [[../03-Projects/CCPM|CCPM]]
- [[../03-Projects/Compound Engineering Plugin|Compound Engineering Plugin]]
- [[../03-Projects/Ruflo claude-flow|Ruflo claude-flow]]

### 安全、质量与门禁

- [[../03-Projects/Claude Code Safety Net|Claude Code Safety Net]]
- [[../03-Projects/TDD Guard|TDD Guard]]

## 选型建议

- 初学者：先看 [[../03-Projects/anthropics-skills|anthropics-skills]]、[[../03-Projects/claude-plugins-official|claude-plugins-official]]、[[../03-Projects/claude-code-templates|claude-code-templates]]
- 想做团队提效：看 [[../03-Projects/Compound Engineering Plugin|Compound Engineering Plugin]]、[[../03-Projects/CCPM|CCPM]]、[[../03-Projects/wshobson-agents|wshobson-agents]]
- 想做安全治理：看 [[../03-Projects/Claude Code Safety Net|Claude Code Safety Net]]、[[../03-Projects/TDD Guard|TDD Guard]]、[[../03-Projects/claude-code-security-review|claude-code-security-review]]
- 想做自定义能力：从 [[../03-Projects/anthropics-skills|anthropics-skills]] 的 skill 结构和 [[../03-Projects/claude-plugins-official|claude-plugins-official]] 的 plugin 结构开始

## 风险边界

- 扩展会拿到命令、文件、MCP 或外部服务权限，必须先看源码、权限和安装脚本
- 第三方 marketplace 不是天然可信；优先在非关键 repo、低权限、无生产密钥环境试用
- hooks / shell wrapper / MCP server 属于高风险扩展面，必须有最小权限和可回滚路径

## 关联

- [[分类索引|分类索引]]
- [[../03-Projects/项目索引|项目索引]]
- [[../../AI-Learning/09-Systems/Claude Code 生态全景|Claude Code 生态全景]]
- [[../../AI-Learning/09-Systems/Claude Code 能力安装清单|Claude Code 能力安装清单]]
- [[../../AI-Learning/09-Systems/Claude Code 自定义能力工作台：Skills、Plugins、Hooks、MCP|Claude Code 自定义能力工作台]]

