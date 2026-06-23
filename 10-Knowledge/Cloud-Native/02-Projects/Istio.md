---
title: Istio
type: project
status: learning
tags:
  - cloud-native/project
  - cloud-native/istio
  - cloud-native/service-mesh
created: 2026-03-24
updated: 2026-03-24
---

# Istio

## 定位

`Istio` 是云原生生态里最有代表性的 `service mesh` 项目之一。它关注的不是应用业务逻辑，而是把服务之间的连接、认证、流量控制和 telemetry 统一收拢到一层基础设施能力里。

## 它解决什么问题

- 服务到服务之间的安全通信
- traffic routing、retry、failover、fault injection
- mTLS、identity-based authn/authz
- 为服务间流量统一提供 metrics、logs 和 traces

## 为什么它重要

Istio 让我们更容易理解：当系统变成大量微服务时，网络问题、流量问题和安全问题会逐渐从“应用内部逻辑”转成“平台层治理问题”。

## 学习重点

- service mesh 为什么会出现
- control plane 和 data plane 分别在做什么
- sidecar / ambient 这些模式为什么会影响复杂度与性能
- 为什么 service mesh 既是 networking 话题，也是 security 和 observability 话题

## 来源

- [What is Istio?](https://istio.io/latest/docs/overview/what-is-istio/)
- [Istio Documentation](https://istio.io/latest/docs/)
- [Service Mesh | Cloud Native Glossary](https://glossary.cncf.io/service-mesh/)

## 相关

- [[../03-Topics/服务发现与流量治理|服务发现与流量治理]]
- [[../03-Topics/云原生安全|云原生安全]]
- [[Kubernetes]]
