---
title: AI Security Evaluation 与 Red Teaming
type: topic
status: learning
tags:
  - ai/engineering
  - ai/security
  - ai/evaluation
created: 2026-03-26
updated: 2026-03-26
---

# AI Security Evaluation 与 Red Teaming

## 为什么这层不能省

因为 AI 安全不是只靠静态设计就能保证的。

你必须持续验证：

- prompt injection 是否会绕过系统
- jailbreak 是否能突破限制
- tool safety 是否真正生效
- model artifact gate 是否足够严

## 常见评测层

- prompt injection test set
- jailbreak suites
- tool misuse scenarios
- retrieval poisoning scenarios
- model artifact scan results

## 为什么红队和普通 eval 不一样

普通 eval 关注“表现好不好”，红队更关注“系统能不能被利用”。

## 关联

- [[Evaluation and Benchmarks]]
- [[Prompt Injection Defense 与 Tool Safety]]
- [[Guardrails、Policy Enforcement 与 Security Gateways]]
- [[../../AI-Learning/09-Systems/Promptfoo|Promptfoo]]
- [[../../AI-Learning/09-Systems/Protect AI ModelScan|Protect AI ModelScan]]
