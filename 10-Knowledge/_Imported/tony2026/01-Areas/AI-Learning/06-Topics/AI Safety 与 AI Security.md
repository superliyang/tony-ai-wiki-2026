---
title: AI Safety 与 AI Security
type: topic
status: learning
tags:
  - ai/topic
  - ai/safety
  - ai/security
created: 2026-03-26
updated: 2026-04-13
---

# AI Safety 与 AI Security

## 为什么这两个词总被混用

因为它们都在谈“风险”，但关注点不同。

### `AI Safety`

更关注：

- 行为是否可控
- 模型是否会造成广义风险
- 对齐、能力提升、滥用与治理

### `AI Security`

更关注：

- 谁能攻击系统
- 攻击面在哪里
- 权限边界是否会被突破
- 如何防护、检测、审计与响应

## 最实用的区分方法

- 如果你在问“系统会不会做出危险行为”，更偏 `safety`
- 如果你在问“别人能不能利用它、绕过它、污染它”，更偏 `security`

## 为什么在 agent 时代两者更容易缠在一起

因为 agent 系统不仅会输出文本，还会：

- 调用工具
- 读取外部内容
- 写入系统状态
- 长期运行

于是一个原本像 `safety` 的问题，很快就会变成 `security` 问题。

比如：

- prompt injection 既是行为操纵问题，也是攻击问题
- jailbreak 既是对齐问题，也是防护绕过问题

## 学习这页最该记住什么

- `safety` 和 `security` 不该互相替代
- 真正成熟的系统，需要同时把两条线接上
- 到了 `2025-2026`，还必须再补一条更上层的 `model behavior governance` 线：行为准则、preparedness、transparency 和外部监管义务

## 关联

- [[AI Safety]]
- [[AI Security]]
- [[Prompt Injection 与 Jailbreaks]]
- [[模型行为治理：Model Spec、Preparedness、Transparency 与 AI Act]]
- [[../11-Recent-Supplements/2025-2026 AI 治理补线：Model Spec、Preparedness、Transparency 与 AI Act|2025-2026 AI 治理补线：Model Spec、Preparedness、Transparency 与 AI Act]]
