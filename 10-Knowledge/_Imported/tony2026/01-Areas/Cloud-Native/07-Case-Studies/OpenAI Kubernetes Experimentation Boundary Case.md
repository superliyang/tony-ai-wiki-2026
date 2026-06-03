---
title: OpenAI Kubernetes Experimentation Boundary Case
type: case-study
status: learning
tags:
  - cloud-native/case-study
  - cloud-native/ai
  - cloud-native/adoption
created: 2026-03-25
updated: 2026-03-25
---

# OpenAI Kubernetes Experimentation Boundary Case

## 为什么看这个案例

这个案例的价值不在“OpenAI 用了 Kubernetes”这件事本身，而在于它非常清楚地展示了 AI 组织在 adoption path 里的一个关键事实：并不是所有 AI workload 都会统一落在 Kubernetes 上，平台边界会根据实验、训练和超大规模生产需求分层。

## 这个案例最有代表性的点

- CNCF case study 明确提到：OpenAI 大量实验 workload 受益于 Kubernetes 的 portability 和 ecosystem
- 同时，最大规模的 workload 仍然会直接管理裸云 VM
- 这说明 Kubernetes 在 AI 组织里的角色，往往先成为实验和大部分通用基础设施的平台，而不是一开始就吞掉所有计算面

## 你应该从中看到什么

- AI 时代云原生 adoption 的一个成熟标志，不是“All-in Kubernetes”，而是清楚哪些 workload 适合 Kubernetes，哪些需要特殊基础设施路径
- 这类边界意识，恰恰说明平台团队已经进入 operating model 思维，而不是工具崇拜
- OpenAI 这样的案例很好地解释了为什么我们前面一直强调 `experimentation -> shared services -> guarded platform -> operating model`

## 来源

- [OpenAI | CNCF Case Study](https://www.cncf.io/case-studies/openai/)

## 相关

- [[../03-Topics/AI 时代云原生采用路径|AI 时代云原生采用路径]]
- [[../03-Topics/AI 工作负载平台团队工作方式|AI 工作负载平台团队工作方式]]
- [[../04-Maps/AI 时代云原生采用图|AI 时代云原生采用图]]
