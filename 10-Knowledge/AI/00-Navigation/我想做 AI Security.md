---
title: 我想做 AI Security
type: guide
status: active
updated: 2026-04-03
---

# 我想做 AI Security

## 先别把它看成“模型安全”一个点

你先要判断：

- 你在防的是 `prompt injection`、`tool misuse`、`memory poisoning`、`artifact supply chain`，还是组织 rollout 风险
- 你的系统是 chat app、agent runtime、plugin ecosystem，还是高信任行业应用
- 你当前更缺 `threat model`、`runtime control`、`eval`，还是 `operating model`

## 最短阅读路径

1. [[AI 总控制塔|AI 总控制塔]]
2. [[AI-Learning/07-Maps/AI Security Threat Map|AI Security Threat Map]]
3. [[AI-Engineering/07-Topics/Security and Privacy|Security and Privacy]]
4. [[AI-Engineering/07-Topics/AI Security Threat Modeling|AI Security Threat Modeling]]
5. [[AI-Engineering/07-Topics/Prompt Injection Defense 与 Tool Safety|Prompt Injection Defense 与 Tool Safety]]
6. [[AI-Engineering/07-Topics/Guardrails、Policy Enforcement 与 Security Gateways|Guardrails、Policy Enforcement 与 Security Gateways]]
7. [[AI-Engineering/07-Topics/Model Supply Chain Security|Model Supply Chain Security]]
8. [[AI-Engineering/07-Topics/AI Security Evaluation 与 Red Teaming|AI Security Evaluation 与 Red Teaming]]
9. [[AI-Engineering/07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]
10. [[AI-Engineering/08-Maps/AI Security 控制点图|AI Security 控制点图]]
11. [[AI-Engineering/07-Topics/Enterprise AI Security Operating Model|Enterprise AI Security Operating Model]]
12. [[AI-Applications/05-Topics/High-Trust Agent Vendor Selection|High-Trust Agent Vendor Selection]]

## 关键系统样本

- [[AI-Learning/09-Systems/NVIDIA NeMo Guardrails|NVIDIA NeMo Guardrails]]
- [[AI-Learning/09-Systems/Azure AI Content Safety（Jailbreak Detection）|Azure AI Content Safety（Jailbreak Detection）]]
- [[AI-Learning/09-Systems/Cloudflare AI Gateway Guardrails|Cloudflare AI Gateway Guardrails]]
- [[AI-Learning/09-Systems/Protect AI ModelScan|Protect AI ModelScan]]

## 读完这条线后，你应该能自己回答

- 你的 AI 系统最危险的面到底在哪
- 哪些控制该放在 prompt 前，哪些要放在 runtime、tool、artifact 或 release gate
- guardrails 工具、policy gateway、red team、org operating model 各自解决什么问题
- 什么时候该把安全问题上升到 vendor choice 和行业 rollout 层

## 关联

- [[AI 问题导航|AI 问题导航]]
- [[AI-Applications/06-Maps/Regulated Industry Agent Map|Regulated Industry Agent Map]]
- [[AI-Engineering/08-Maps/AI Security Engineering Map|AI Security Engineering Map]]
