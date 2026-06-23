---
title: Open Policy Agent
type: project
status: learning
domain: Security
category: 身份、密钥、证书与策略
organization: OPA
repo: https://github.com/open-policy-agent/opa
local_fit: high
mac_fit: high
production_fit: high
learning_fit: high
updated: 2026-05-05
---

# Open Policy Agent

## 它是什么

Open Policy Agent 是通用策略引擎，用 Rego 语言表达访问控制、配置校验和策略决策。

## 为什么现在值得关注

- policy-as-code 是云原生、平台工程和安全治理的核心模式之一。
- OPA 帮助把安全从文档控制变成可执行策略。

## 它在 stack 的哪一层

- 更像 `底座`：策略决策底座。

## 核心抽象

- input：待评估上下文。
- policy：Rego 策略。
- data：外部数据。
- decision：allow、deny、reason 或派生结果。

## 最适合它的场景

- Kubernetes admission policy。
- API 授权和服务间访问。
- IaC / CI/CD policy gate。

## 风险与边界

- 策略语言需要学习成本。
- 策略必须测试、版本化和灰度，否则可能误伤业务。

## 关联

- [[../01-Categories/身份、密钥、证书与策略|身份、密钥、证书与策略]]
- [[../04-Patterns/规则即代码检测模式|规则即代码检测模式]]

