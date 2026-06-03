---
title: Golden Path
type: topic
status: learning
tags:
  - cloud-native/topic
  - cloud-native/platform-engineering
  - cloud-native/golden-path
created: 2026-03-24
updated: 2026-03-24
---

# Golden Path

## 一句话理解

`Golden Path` 指的是平台团队为开发者提供的一条默认推荐路径：让“正确的做法”同时也是“最容易的做法”。

## 为什么它重要

云原生平台的问题通常不是“没有能力”，而是能力太多、入口太散、标准不统一。Golden Path 的价值在于：

- 降低认知负担
- 减少重复脚手架工作
- 把最佳实践内置进模板和 workflow
- 在不完全剥夺灵活性的情况下提高一致性

## 它通常怎么落地

- 用 `software templates` 生成服务骨架
- 用 catalog 管理 owner 和依赖
- 用 docs / examples 降低学习成本
- 用 policy 和 approvals 约束高风险动作

## 学习重点

- Golden Path 不是“只能走一条路”，而是先给出最优默认路径
- 它需要和平台产品入口、模板、文档、治理一起工作
- 它的成败常常取决于 adoption，而不只是技术实现

## 来源

- [Announcing Backstage Software Templates](https://backstage.io/blog/2020/08/05/announcing-backstage-software-templates)
- [Backstage Software Templates](https://backstage.io/docs/next/features/software-templates/)
- [Getting started with Backstage adoption](https://backstage.io/docs/next/golden-path/adoption/getting-started)

## 相关

- [[平台工程]]
- [[Internal Developer Platform]]
- [[平台团队工作方式]]
- [[../02-Projects/Backstage|Backstage]]
