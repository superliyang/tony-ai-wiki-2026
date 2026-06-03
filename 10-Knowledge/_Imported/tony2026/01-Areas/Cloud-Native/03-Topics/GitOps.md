---
title: GitOps
type: topic
status: learning
tags:
  - cloud-native/topic
  - cloud-native/gitops
created: 2026-03-24
updated: 2026-03-24
---

# GitOps

## 一句话理解

`GitOps` 是一种把系统期望状态定义在 version control 中，并通过自动化过程持续把 live system 收敛到该状态的工作方式。

## 它为什么重要

GitOps 把 deployment、environment consistency、change history、rollback 和 auditability 连接到了一起。它特别适合和 Kubernetes 这种声明式系统结合。

## 学 GitOps 时要抓什么

- source of truth 是什么
- reconciliation 是怎么发生的
- GitOps 为什么比“脚本式部署”更可追踪
- 它适合哪些场景，不适合哪些场景

## 常见误解

- GitOps 不是“把 YAML 放进 Git 就结束”
- GitOps 也不是只和某个工具绑定，它是一类实践方式
- Argo CD 是高频入口，但不是 GitOps 的全部

## 来源

- [GitOps | CNCF Glossary](https://glossary.cncf.io/gitops/)
- [Argo CD Documentation](https://argo-cd.readthedocs.io/en/latest/)

## 相关

- [[../02-Projects/Argo CD|Argo CD]]
- [[../02-Projects/Kubernetes|Kubernetes]]
- [[平台工程]]
