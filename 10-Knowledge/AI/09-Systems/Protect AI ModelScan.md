---
title: Protect AI ModelScan
type: system
status: learning
tags:
  - ai/system
  - ai/security
  - ai/supply-chain
created: 2026-03-26
updated: 2026-03-26
---

# Protect AI ModelScan

## 它是什么

`ModelScan` 是 Protect AI 开源的模型扫描工具，用来检测模型序列化文件里是否含有危险代码或不安全内容。

## 为什么它重要

因为很多团队会认真扫描容器镜像和依赖包，却还没把模型文件当成真正的 supply-chain artifact。

这在 foundation model 时代是危险的。

## 它最值得抓住的点

- 模型文件本身也可能是攻击面
- model serialization attack 是真实问题
- model supply chain security 不应只停留在“来源可信”这种口头判断

## 它更适合放在哪一层

- model supply-chain security
- CI / artifact gate
- pre-deployment scan layer

## 关联

- [[../06-Topics/AI Security|AI Security]]
- [[../../AI-Engineering/07-Topics/Model Supply Chain Security|Model Supply Chain Security]]
- [[../../AI-Engineering/07-Topics/AI Security Evaluation 与 Red Teaming|AI Security Evaluation 与 Red Teaming]]

## 资料

- [ModelScan GitHub](https://github.com/protectai/modelscan)
