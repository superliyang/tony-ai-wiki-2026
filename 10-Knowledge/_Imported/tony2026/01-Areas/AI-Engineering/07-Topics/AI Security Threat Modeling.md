---
title: AI Security Threat Modeling
type: topic
status: learning
tags:
  - ai/engineering
  - ai/security
created: 2026-03-26
updated: 2026-03-26
---

# AI Security Threat Modeling

## 为什么 threat modeling 在 AI 里更重要

因为 AI 系统的攻击面不仅来自代码和接口，还来自：

- prompt
- context window
- retrieval data
- tools
- memory
- model artifact

## 一条最实用的拆法

把 AI 系统拆成 6 个面：

1. input surface
2. context assembly surface
3. model / policy surface
4. tool/action surface
5. state / memory surface
6. artifact / deployment surface

## 每一层要问什么

- 谁能注入不可信内容
- 谁能改变执行路径
- 谁能看到敏感数据
- 谁能持久化污染状态
- 谁能把不安全 artifact 放进生产

## 关联

- [[Security and Privacy]]
- [[Prompt Injection Defense 与 Tool Safety]]
- [[Model Supply Chain Security]]
- [[AI Security Evaluation 与 Red Teaming]]
