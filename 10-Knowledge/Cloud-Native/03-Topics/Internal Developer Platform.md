---
title: Internal Developer Platform
type: topic
status: learning
tags:
  - cloud-native/topic
  - cloud-native/platform-engineering
  - cloud-native/idp
created: 2026-03-24
updated: 2026-03-24
---

# Internal Developer Platform

## 一句话理解

`Internal Developer Platform`（IDP）不是某一个工具，而是平台团队为开发者提供的一组自助能力、标准化工作流和治理边界的组合产品。

## 为什么它会出现

当组织进入 Kubernetes、GitOps、observability、security、service mesh 这些复杂体系后，开发者如果每次都直接接触底层，效率和一致性都会下降。IDP 的目标就是：

- 把复杂性收敛到平台层
- 把高频操作抽象成 self-service 能力
- 让平台治理不靠口头约定，而是靠产品化入口和 guardrails

## IDP 通常包含什么

- developer portal
- software catalog
- software templates
- golden paths
- deployment and environment workflows
- policy and approval boundaries

## 学习重点

- IDP 不是“堆工具”，而是把开发者体验、平台治理和交付效率放到一起设计
- portal 是入口，catalog 是认知层，templates 是执行层，guardrails 是治理层
- 一个成熟 IDP 往往要同时解决 discoverability、self-service 和 standardization

## 来源

- [What is Backstage?](https://backstage.io/docs/overview/what-is-backstage)
- [Getting started with Backstage adoption](https://backstage.io/docs/next/golden-path/adoption/getting-started)
- [Developer self-service | Humanitec](https://humanitec.com/developer-self-service)

## 相关

- [[平台工程]]
- [[Golden Path]]
- [[平台团队工作方式]]
- [[../02-Projects/Backstage|Backstage]]
