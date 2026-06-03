---
title: Prompt Injection 与 Jailbreaks
type: topic
status: learning
tags:
  - ai/topic
  - ai/security
  - ai/prompt-injection
created: 2026-03-26
updated: 2026-03-26
---

# Prompt Injection 与 Jailbreaks

## 它们是什么

### Prompt Injection

攻击者通过输入、网页、文档、检索结果或工具返回内容，把恶意指令塞进模型上下文里，试图改变模型行为。

### Jailbreak

攻击者试图绕过模型或系统已有的限制，让模型输出本来不该输出的内容，或执行本来不该执行的行为。

## 为什么在 agent 时代更危险

因为 agent 不只是回答问题，它还可能：

- 打开网页
- 阅读文档
- 调用工具
- 执行命令
- 长期保存状态

于是 prompt injection 不再只是“让模型说错话”，而是可能：

- 诱导工具调用
- 泄露敏感上下文
- 改变执行流程
- 污染长期 memory

## 一条最实用的判断

- 用户输入不可信
- 外部内容也不可信
- retrieval 结果不可信
- tool output 也不天然可信

如果团队没有这个默认前提，agent 系统很容易被设计错。

## 防御的基本层次

1. 输入和外部内容默认不可信
2. 高风险工具必须走显式审批或 allowlist
3. prompt 里不能假设“系统提示永远优先”
4. 需要运行时监测和输出后检查
5. 高权限环境要最小化、隔离化

## 关联

- [[AI Security]]
- [[../../AI-Engineering/07-Topics/Prompt Injection Defense 与 Tool Safety|Prompt Injection Defense 与 Tool Safety]]
- [[../../AI-Engineering/07-Topics/AI Security Evaluation 与 Red Teaming|AI Security Evaluation 与 Red Teaming]]
- [[../09-Systems/NVIDIA NeMo Guardrails|NVIDIA NeMo Guardrails]]

## 资料

- [OWASP LLM01 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- [Anthropic: Mitigate jailbreaks and prompt injections](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)
- [Anthropic Computer Use Risk Notes](https://docs.anthropic.com/en/docs/build-with-claude/computer-use)
