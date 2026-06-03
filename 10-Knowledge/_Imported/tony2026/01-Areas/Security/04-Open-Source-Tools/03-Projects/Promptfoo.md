---
title: Promptfoo
type: project
status: learning
domain: Security
category: AI 安全与 LLM 红队
organization: Promptfoo
repo: https://github.com/promptfoo/promptfoo
local_fit: high
mac_fit: high
production_fit: medium
learning_fit: high
updated: 2026-05-05
---

# Promptfoo

## 它是什么

Promptfoo 是用于 prompt、agent 和 RAG 测试的开源工具，也支持 AI 红队和漏洞扫描式评测。

## 为什么现在值得关注

- AI 产品安全需要从一次性人工测试变成可回归的 eval gate。
- Promptfoo 适合作为 AI 安全评测的工程入口。

## 它在 stack 的哪一层

- 更像 `子系统`：AI eval、red teaming 和 CI gate 组件。

## 最适合它的场景

- Prompt injection、jailbreak、RAG 泄露和 agent 工具滥用测试。
- AI 产品上线前安全回归。

## 风险与边界

- 评测集需要结合业务场景，不应只用通用 jailbreak 样例。
- AI 安全还要覆盖权限、数据、日志和人工复核。

## 关联

- [[../01-Categories/AI 安全与 LLM 红队|AI 安全与 LLM 红队]]
- [[../../03-Industry-Controls/AI 产品安全控制清单|AI 产品安全控制清单]]

