---
title: AI 安全与 LLM 红队
type: category
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# AI 安全与 LLM 红队

## 解决什么问题

- Prompt injection、jailbreak、RAG 泄露、agent 工具滥用、敏感输出和 AI 应用安全评测。
- 把 AI 产品安全从“内容过滤”扩展到数据、权限、工具、评测和治理。

## 代表项目

- [promptfoo](https://github.com/promptfoo/promptfoo)：prompt、agent、RAG 测试和红队。
- [garak](https://github.com/garak-llm/garak)：LLM 漏洞扫描和红队。
- [Counterfit](https://github.com/microsoft/Counterfit)：AI 系统安全测试。
- [LLM Guard](https://github.com/ProtectAI/llm-guard)：LLM 输入输出安全防护。
- [Rebuff](https://github.com/protectai/rebuff)：Prompt injection 检测方向。
- [Anthropic Cybersecurity Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)：面向 AI agent 的安全技能结构。
- [DeepAudit](https://github.com/lintsinghua/DeepAudit)：AI 代码漏洞审计多智能体系统。
- [Shannon](https://github.com/KeygraphHQ/shannon)：AI pentester 方向项目。

## 典型组合

`AI threat model -> promptfoo / garak -> LLM Guard -> 日志与人工复核 -> AI GRC 证据`

## 关联

- [[../../03-Industry-Controls/AI 产品安全控制清单|AI 产品安全控制清单]]
- [[../../../AI-Engineering/08-Maps/AI Security 控制点图|AI Security 控制点图]]

