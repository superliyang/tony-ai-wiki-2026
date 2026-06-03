---
title: Argo CD
type: project
status: learning
tags:
  - cloud-native/project
  - cloud-native/argocd
  - cloud-native/gitops
created: 2026-03-24
updated: 2026-03-24
---

# Argo CD

## 定位

`Argo CD` 是 Kubernetes 世界里最有代表性的 GitOps CD 系统之一。它把 Git 里的期望状态持续对齐到集群实际状态。

## 它解决什么问题

- 让 Git 成为 deployment source of truth
- 可视化 live state 与 desired state 的差异
- 自动或手动把 `OutOfSync` 的系统重新收敛

## 为什么它重要

Argo CD 是把 GitOps 从理念落到平台实践的关键项目之一。学懂它，有助于理解为什么 GitOps 不只是“把 YAML 放进 Git”，而是一套围绕 reconciliation、审计、回滚和环境一致性的工作方式。

## 学习重点

- GitOps controller 在持续做什么
- desired state 与 live state 的关系
- 为什么 GitOps 适合和 Kubernetes 这种声明式系统结合

## 来源

- [Argo CD Documentation](https://argo-cd.readthedocs.io/en/latest/)
- [Argo CD Getting Started](https://argo-cd.readthedocs.io/en/release-2.14/getting_started/)
- [GitOps | CNCF Glossary](https://glossary.cncf.io/gitops/)

## 相关

- [[../03-Topics/GitOps|GitOps]]
- [[Kubernetes]]
