---
title: Puppet Relay Knative Workflow Platform Case
type: case-study
status: learning
tags:
  - cloud-native/case-study
  - cloud-native/serverless
  - cloud-native/knative
created: 2026-03-25
updated: 2026-03-25
---

# Puppet Relay Knative Workflow Platform Case

## 为什么看这个案例

这个案例很适合把 `Knative` 从“serverless on Kubernetes”拉回到更真实的组织价值：不是为了追求一个时髦运行时，而是为了把事件驱动 workflow 和自动化平台做成可扩展的产品。

## 这个案例最有代表性的点

- Puppet 团队用 Knative 构建 `Relay` 这样的 cloud workflow automation platform
- `Knative Serving` 提供了 webhook 和服务按需扩缩容、甚至 scale-to-zero 的底层能力
- 这让他们能把跨 SaaS、云服务和运维动作的 workflow，组织成事件驱动平台，而不是一堆分散脚本

## 你应该从中看到什么

- serverless 在云原生里真正值钱的地方，是把 sporadic、event-driven workload 的平台成本降下来
- `Knative` 的意义不只是“函数平台”，更是帮助团队把 workflow automation 变成标准平台能力
- 这类案例说明 runtime 层选择会直接影响平台产品形态

## 来源

- [Puppet Case Study](https://knative.dev/docs/about/case-studies/puppet/)
- [Knative Home](https://knative.dev/)

## 相关

- [[../03-Topics/Serverless 与事件驱动|Serverless 与事件驱动]]
- [[../02-Projects/Knative|Knative]]
- [[../04-Maps/运行时与状态案例图|运行时与状态案例图]]
