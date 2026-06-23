---
title: AI 时代云原生采用路径
type: topic
status: learning
tags:
  - cloud-native/topic
  - cloud-native/ai
  - cloud-native/adoption
created: 2026-03-25
updated: 2026-03-25
---

# AI 时代云原生采用路径

## 一句话理解

AI 时代的云原生 adoption，通常不会一步走到“统一 AI 平台”，而是沿着 `experiments -> shared services -> guarded platform -> operating model` 逐步演进。

## 为什么这是一个独立主题

前面我们已经把：

- runtime
- serverless
- storage
- service mesh
- security
- model serving
- training orchestration

这些能力都放到了结构里。

但真实组织里，最难的往往不是“技术能不能跑”，而是：

- 哪些能力先 centralize
- 哪些能力先由平台团队托管
- 哪些能力还应该保持 team-level autonomy
- 什么时候从 shared service 走到真正的 platform product

## 常见演进阶段

1. `Experimentation`
   - 数据科学、ML、应用团队各自试验
   - 依赖 notebook、单点 GPU、脚本和临时环境
2. `Shared Infrastructure`
   - 开始共享 GPU quota、镜像基线、对象存储、训练集群
   - 平台团队先提供最低限度的共用底座
3. `Guarded Platform Services`
   - 推理、训练、模型注册、策略控制、成本治理逐渐平台化
   - 出现 control plane、profile、quota、policy、approved runtime
4. `AI Platform Operating Model`
   - 平台团队、应用团队、安全团队、数据/ML 团队出现稳定协作边界
   - adoption、cost、reliability、governance 进入固定 operating rhythm

## 你应该从中看到什么

- AI workload 不会自动“变成平台”，中间一定会经历 shared service 阶段
- adoption path 的关键不只是技术成熟度，还包括多租户、安全、成本和组织边界
- 这也是为什么 Kubernetes 上的 AI 项目越来越强调 multi-tenancy、control plane、reference platform 和 standard mode

## 来源

- [Cloud Native Artificial Intelligence Whitepaper](https://www.cncf.io/reports/cloud-native-artificial-intelligence-whitepaper/)
- [Kubeflow Home](https://www.kubeflow.org/)
- [KServe System Architecture Overview](https://kserve.github.io/website/docs/concepts/architecture)
- [Kubeflow 1.11 Release Announcement](https://blog.kubeflow.org/kubeflow-1.11-release/)

## 相关

- [[AI 工作负载平台团队工作方式]]
- [[../06-Workflows/AI 平台团队采用推进工作流|AI 平台团队采用推进工作流]]
- [[../04-Maps/AI 时代云原生采用图|AI 时代云原生采用图]]
- [[AI 时代的云原生]]
