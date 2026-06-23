---
title: Clarizen Kubernetes Runtime Security Case
type: case-study
status: learning
tags:
  - cloud-native/case-study
  - cloud-native/security
  - cloud-native/runtime
created: 2026-03-25
updated: 2026-03-25
---

# Clarizen Kubernetes Runtime Security Case

## 为什么看这个案例

这个案例很适合把运行时安全从“安全理论”拉回到平台工程现实：当组织已经在 EKS 上跑生产 workload 且涉及敏感数据时，运行时安全不再是可选附加项，而会变成平台默认能力的一部分。

## 这个案例最有代表性的点

- Clarizen Go 运行在 `EKS + ECR` 这一套标准云原生环境上
- 他们关心的不只是镜像安全，还包括：
  - runtime visibility
  - drift prevention
  - compliance requirements
  - deployment control
- 这说明 runtime security 在真实组织里，通常是和 admission、compliance、day-2 governance 一起被引入的

## 你应该从中看到什么

- 运行时安全不是孤立产品功能，而是平台治理的一部分
- 敏感数据与合规要求，会显著推动运行时可见性和 drift prevention 成为默认能力
- runtime security 的真实难点，不是能不能告警，而是如何接进默认工作流而不拖垮开发速度

## 来源

- [Clarizen Secures its Kubernetes Development Pipeline with Aqua Security](https://www.aquasec.com/customers/clarizen-case-study-kubernetes-security/)
- [Runtime Protection for K8s Workloads](https://www.aquasec.com/blog/kubernetes-runtime-security/)
- [Linux kernel security constraints for Pods and containers](https://kubernetes.io/docs/concepts/security/linux-kernel-security-constraints/)

## 相关

- [[../03-Topics/运行时安全|运行时安全]]
- [[../06-Workflows/运行时安全响应工作流|运行时安全响应工作流]]
- [[../04-Maps/Day-2 运维与运行时安全图|Day-2 运维与运行时安全图]]
