---
title: Model Supply Chain Security
type: topic
status: learning
tags:
  - ai/engineering
  - ai/security
  - ai/supply-chain
created: 2026-03-26
updated: 2026-03-26
---

# Model Supply Chain Security

## 为什么这一层越来越重要

因为模型文件、adapter、weights、tokenizer、prompt bundles、eval assets 都开始像软件供应链资产一样流动。

如果不把它们纳入安全控制，风险会被低估。

## 典型风险

- model serialization attacks
- 不可信权重来源
- prompt / eval bundle 被篡改
- CI/CD 里缺乏 artifact scan

## 控制点

- artifact provenance
- 签名与校验
- model scan
- registry gate
- deployment admission control

## 关联

- [[Security and Privacy]]
- [[AI Security Threat Modeling]]
- [[../../AI-Learning/09-Systems/Protect AI ModelScan|Protect AI ModelScan]]
- [[../../Cloud-Native/03-Topics/软件供应链安全|软件供应链安全]]
