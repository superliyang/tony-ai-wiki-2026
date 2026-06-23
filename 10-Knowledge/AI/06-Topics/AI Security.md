---
title: AI Security
type: topic
status: learning
tags:
  - ai/topic
  - ai/security
created: 2026-03-26
updated: 2026-03-26
---

# AI Security

## 它是什么

`AI Security` 关注的是：

- AI 系统会被什么方式攻击
- AI 系统如何扩大传统应用的攻击面
- 如何把安全边界前置到模型、prompt、tool、memory、deployment 和 supply chain

它和 `AI Safety` 有交集，但不一样：

- `AI Safety` 更偏行为、对齐、风险控制和系统可控性
- `AI Security` 更偏攻击面、威胁建模、防护、审计和响应

## 为什么现在一定要单独学

因为 AI 系统的攻击面已经不只是：

- API 被打爆
- 数据泄露
- 权限越权

还包括：

- prompt injection
- jailbreak
- retrieval poisoning
- insecure tool use
- model artifact supply-chain attack
- memory poisoning

## 一条最实用的主线

1. `AI Safety 与 AI Security`
2. `Prompt Injection 与 Jailbreaks`
3. `AI Security Threat Modeling`
4. `Prompt Injection Defense 与 Tool Safety`
5. `Guardrails / Policy Enforcement / Security Gateways`
6. `Model Supply Chain Security`
7. `AI Security Evaluation 与 Red Teaming`

## 这一层最值得记住的系统

- [[../09-Systems/NVIDIA NeMo Guardrails|NVIDIA NeMo Guardrails]]
- [[../09-Systems/Protect AI ModelScan|Protect AI ModelScan]]

## 一句最关键的话

AI 安全不只是“输出别乱说”，而是：

- 不要让模型被诱导
- 不要让模型越权调用
- 不要让不可信 artifact 进入系统
- 不要让不可审计的 agent 进入生产

## 关联

- [[AI Safety 与 AI Security]]
- [[Prompt Injection 与 Jailbreaks]]
- [[AI Safety]]
- [[../07-Maps/AI Security Threat Map|AI Security Threat Map]]
- [[../../AI-Engineering/07-Topics/AI Security Threat Modeling|AI Security Threat Modeling]]
- [[../../AI-Engineering/07-Topics/Prompt Injection Defense 与 Tool Safety|Prompt Injection Defense 与 Tool Safety]]
- [[../../AI-Engineering/07-Topics/Guardrails、Policy Enforcement 与 Security Gateways|Guardrails、Policy Enforcement 与 Security Gateways]]
- [[../../AI-Engineering/07-Topics/Model Supply Chain Security|Model Supply Chain Security]]
- [[../../AI-Engineering/07-Topics/AI Security Evaluation 与 Red Teaming|AI Security Evaluation 与 Red Teaming]]

## 资料

- [OWASP LLM01 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- [NIST Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [Anthropic: Mitigate jailbreaks and prompt injections](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)
