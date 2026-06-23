---
title: Semgrep
type: project
status: learning
domain: Security
category: DevSecOps 与供应链安全
organization: Semgrep
repo: https://github.com/semgrep/semgrep
local_fit: high
mac_fit: high
production_fit: high
learning_fit: high
updated: 2026-05-05
---

# Semgrep

## 它是什么

Semgrep 是面向多语言代码的轻量静态分析工具，用“像代码一样”的模式写规则。

## 为什么现在值得关注

- 对安全工程很友好：规则可读、容易和 code review/CI/CD 集成。
- 适合把组织内常见漏洞模式沉淀成规则。

## 它在 stack 的哪一层

- 更像 `子系统`：AppSec SAST 和自定义规则引擎。

## 核心对象模型 / 核心抽象

- rule：pattern、message、severity、metadata。
- ruleset：团队或语言维度的规则集合。
- finding：具体代码位置和修复建议。

## 最适合它的场景

- PR 安全检查。
- 组织内自定义安全规则。
- 漏洞复盘后写回归规则。

## 风险与边界

- 不等于完整代码审计。
- 规则需要持续调噪，否则会被开发团队绕过。

## 关联

- [[../01-Categories/DevSecOps 与供应链安全|DevSecOps 与供应链安全]]
- [[../../05-Topics/安全工程与 DevSecOps|安全工程与 DevSecOps]]

