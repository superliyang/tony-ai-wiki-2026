---
title: Autodesk Sigstore Compliance Case
type: case-study
status: learning
tags:
  - cloud-native/case-study
  - cloud-native/security
  - cloud-native/supply-chain
created: 2026-03-25
updated: 2026-03-25
---

# Autodesk Sigstore Compliance Case

## 为什么看这个案例

这个案例很适合放在云原生安全主线里，因为它把“供应链安全”从抽象概念拉回到了平台团队必须回答的现实问题：怎么在不明显拖慢开发者速度的前提下，把签名、验证和合规要求接进 CI/CD 和容器交付链路。

## 这个案例最有代表性的点

- Autodesk 的 Developer Enablement 团队把软件供应链安全直接和平台能力建设绑定起来
- FedRAMP 这样的合规要求，放大了“容器镜像必须可验证、可审计”的必要性
- Sigstore 的价值不只是一个签名工具，而是帮助把 build / sign / verify 逐步平台化
- 核心难点不是会不会用工具，而是如何在 freedom 和 security 之间取得平衡

## 你应该从中看到什么

- 供应链安全真正落地时，必须由平台层承接，而不是让每个应用团队各自拼装
- 合规压力经常会推动平台团队把 security workflow 做成默认能力
- `policy-controller`、签名、attestation 这些能力，本质上是在给 Kubernetes admission 加上可验证的前置条件

## 来源

- [Using Sigstore to meet FedRAMP Compliance at Autodesk](https://blog.sigstore.dev/using-sigstore-to-meet-fedramp-compliance-at-autodesk-6f645a920abc/)
- [Kubernetes Policy Controller Overview](https://docs.sigstore.dev/policy-controller/overview/)
- [Sigstore Integration](https://docs.sigstore.dev/cosign/system_config/integration/)

## 相关

- [[../03-Topics/云原生安全|云原生安全]]
- [[../03-Topics/软件供应链安全|软件供应链安全]]
- [[../06-Workflows/策略与供应链安全接入工作流|策略与供应链安全接入工作流]]
- [[../02-Projects/Sigstore|Sigstore]]
- [[../04-Maps/服务网格与安全落地图|服务网格与安全落地图]]
