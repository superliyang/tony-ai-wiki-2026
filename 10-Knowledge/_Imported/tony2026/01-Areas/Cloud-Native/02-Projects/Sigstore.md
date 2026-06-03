---
title: Sigstore
type: project
status: learning
tags:
  - cloud-native/project
  - cloud-native/sigstore
  - cloud-native/supply-chain
created: 2026-03-24
updated: 2026-03-24
---

# Sigstore

## 定位

`Sigstore` 是现代软件供应链安全里非常关键的开源项目族。它关注的是：软件 artifact 如何被签名、验证、审计和建立可信来源。

## 它解决什么问题

- 容器镜像、二进制、SBOM 等 artifact 的签名与验证
- 减少传统 key management 的复杂度
- 为软件供应链提供公开可审计的签名记录

## 为什么它重要

云原生系统高度依赖镜像、依赖包、构建产物和自动化交付链路。Sigstore 让“这个 artifact 能不能信”变成更系统化的问题，而不是只靠人工信任。

## 学习重点

- artifact signing 为什么在云原生里变得重要
- ephemeral keys、identity、public log 分别在解决什么问题
- Sigstore 为什么经常和 provenance、SLSA、policy enforcement 一起出现

## 来源

- [Sigstore Overview](https://docs.sigstore.dev/)
- [What is SLSA?](https://slsa.dev/spec/v1.1/about)

## 相关

- [[../03-Topics/软件供应链安全|软件供应链安全]]
- [[../03-Topics/云原生安全|云原生安全]]
- [[Kyverno]]
