---
title: TDD Guard
type: project
status: learning
domain: ai-open-source
category: Claude Code 生态扩展
organization: nizos
repo: https://github.com/nizos/tdd-guard
local_fit: high
mac_fit: high
production_fit: medium
learning_fit: high
created: 2026-05-15
updated: 2026-05-15
---

# TDD Guard

## 它解决什么问题

`TDD Guard` 为 Claude Code 提供自动化 TDD enforcement，约束 agent 在新增行为时先补测试或遵守测试驱动流程。

## 为什么现在值得关注

AI Coding 最大的质量风险之一是“改得很快，但没有验证”。TDD Guard 是把测试纪律从软提示变成 hook / policy 的代表样本。

## 它在 stack 的哪一层

- 属于 `quality gate / TDD policy hook`
- 位于 agent 代码修改和验证闭环之间

## 核心组件与架构

- hooks
- policy enforcement
- test runner integration
- session activity validation

## 最适合它的场景

- 要求新功能先有测试
- 阻止 agent 绕过验证
- 给团队建立 AI Coding 质量门禁

## 和相邻项目怎么区分

- 和 [[Claude Code Safety Net]]：TDD Guard 管测试纪律；Safety Net 管危险命令
- 和 [[claude-code-security-review]]：TDD Guard 管质量；security-review 管安全风险

## 风险与边界

- 对 legacy 项目可能过重
- 需要结合项目真实测试命令，否则容易形成形式主义 gate

## 官方入口

- [nizos/tdd-guard GitHub](https://github.com/nizos/tdd-guard)

## 关联

- [[项目索引|项目索引]]
- [[../01-Categories/Claude Code 生态扩展|Claude Code 生态扩展]]

