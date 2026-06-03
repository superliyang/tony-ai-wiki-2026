---
title: claude-code-security-review
type: project
status: learning
domain: ai-open-source
category: Claude Code 生态扩展
organization: Anthropic
repo: https://github.com/anthropics/claude-code-security-review
local_fit: medium
mac_fit: medium
production_fit: medium
learning_fit: high
created: 2026-05-15
updated: 2026-05-15
---

# claude-code-security-review

## 它解决什么问题

`claude-code-security-review` 是 Anthropic 的安全审查 GitHub Action，用 Claude 分析代码变更中的潜在安全漏洞。

## 为什么现在值得关注

Claude Code 生态不只要提效，也要防止 agent 把漏洞写进代码。这个项目适合作为 AI-assisted security review 的官方样本。

## 它在 stack 的哪一层

- 属于 `security review / PR gate`
- 位于 coding agent 输出与 merge gate 之间

## 核心组件与架构

- GitHub Action trigger
- diff / changed files input
- Claude-based security analysis
- PR comment / review output

## 最适合它的场景

- PR 安全审查
- 高风险模块变更提醒
- 与 SAST / dependency scan 组合形成 defense-in-depth

## 和相邻项目怎么区分

- 和 [[Claude Code Safety Net]]：它审查代码风险；Safety Net 阻断危险命令
- 和 [[TDD Guard]]：它关注安全；TDD Guard 关注测试纪律

## 风险与边界

- LLM security review 不能替代 SAST、依赖扫描和人工审查
- 需要控制注释噪音和误报
- 对安全敏感仓库要关注代码数据发送边界

## 官方入口

- [anthropics/claude-code-security-review GitHub](https://github.com/anthropics/claude-code-security-review)

## 关联

- [[项目索引|项目索引]]
- [[../01-Categories/Claude Code 生态扩展|Claude Code 生态扩展]]

