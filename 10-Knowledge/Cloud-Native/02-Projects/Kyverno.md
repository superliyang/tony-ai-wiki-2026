---
title: Kyverno
type: project
status: learning
tags:
  - cloud-native/project
  - cloud-native/kyverno
  - cloud-native/security
  - cloud-native/policy
created: 2026-03-24
updated: 2026-03-24
---

# Kyverno

## 定位

`Kyverno` 是 Kubernetes 场景里非常重要的 `policy engine`。它把 policy enforcement 放进声明式和 Kubernetes-native 的工作流中。

## 它解决什么问题

- admission-time policy enforcement
- validate / mutate / generate / cleanup 资源
- image verification 和部分软件供应链安全策略
- policy-as-code 与 cluster governance 的连接

## 为什么它重要

Kyverno 很适合帮助初学者理解：云原生安全并不只是“扫描镜像”，而是把 policy 变成可以持续执行、持续审计、持续报告的系统能力。

## 学习重点

- admission controller 在 Kubernetes 安全治理里的位置
- policy-as-code 为什么适合云原生系统
- validate / mutate / generate 各自对应什么治理需求
- Kyverno 如何连接 cluster security 与 supply chain security

## 来源

- [Introduction | Kyverno](https://kyverno.io/docs/introduction/)
- [How Kyverno Works](https://kyverno.io/docs/introduction/how-kyverno-works/)

## 相关

- [[../03-Topics/云原生安全|云原生安全]]
- [[../03-Topics/软件供应链安全|软件供应链安全]]
- [[Kubernetes]]
