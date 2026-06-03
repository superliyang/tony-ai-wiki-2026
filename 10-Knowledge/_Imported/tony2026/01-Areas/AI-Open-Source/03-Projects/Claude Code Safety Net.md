---
title: Claude Code Safety Net
type: project
status: learning
domain: ai-open-source
category: Claude Code 生态扩展
organization: kenryu42
repo: https://github.com/kenryu42/claude-code-safety-net
local_fit: high
mac_fit: high
production_fit: medium
learning_fit: high
created: 2026-05-15
updated: 2026-05-15
---

# Claude Code Safety Net

## 它解决什么问题

`Claude Code Safety Net` 是一个安全 hook / plugin，用来在 destructive git 和 filesystem 命令执行前拦截风险操作。

## 为什么现在值得关注

AI Coding 的风险不只在生成代码，也在 agent 能执行命令。这个项目直接命中 `PreToolUse hook`、命令解析和防误删防回退。

## 它在 stack 的哪一层

- 属于 `agent safety hook / command guard`
- 位于 shell 执行前的防护层

## 核心组件与架构

- `PreToolUse` hook
- destructive command detection
- git-aware safety rules
- strict / paranoid / worktree modes
- audit logging / secret redaction

## 最适合它的场景

- 本地 repo 防止 `git reset --hard`、`git checkout --`、危险 `rm`
- 团队给 Claude Code 加基础安全网
- 和 sandbox / permission deny rules 组合使用

## 和相邻项目怎么区分

- 和 [[claude-code-security-review]]：Safety Net 防命令事故；security-review 审查代码漏洞
- 和 [[TDD Guard]]：Safety Net 管安全操作；TDD Guard 管测试纪律

## 风险与边界

- 它不是 OS sandbox，不能替代文件系统和网络隔离
- 它依赖命令分析，未知绕过形式仍需结合 sandbox 和权限策略

## 官方入口

- [claude-code-safety-net GitHub](https://github.com/kenryu42/claude-code-safety-net)

## 关联

- [[项目索引|项目索引]]
- [[../01-Categories/Claude Code 生态扩展|Claude Code 生态扩展]]

