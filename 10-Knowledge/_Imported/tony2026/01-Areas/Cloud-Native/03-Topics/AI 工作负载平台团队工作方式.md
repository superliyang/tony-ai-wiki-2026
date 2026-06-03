---
title: AI 工作负载平台团队工作方式
type: topic
status: learning
tags:
  - cloud-native/topic
  - cloud-native/ai
  - cloud-native/platform-engineering
created: 2026-03-25
updated: 2026-03-25
---

# AI 工作负载平台团队工作方式

## 一句话理解

当平台团队开始承接 AI workload 时，它的职责会从“维护 Kubernetes 基础设施”扩展成“维护一组带 guardrails 的训练、推理、数据与加速器平台能力”。

## 为什么这和普通平台团队不完全一样

AI workload 会额外带来几类问题：

- GPU / accelerator scheduling
- 大规模对象存储与 checkpoint
- 训练、评估、推理三类 workload 的差异化资源形态
- 多租户与 quota
- 成本治理
- 模型与 artifact 生命周期

所以 AI 平台团队不会只管：

- cluster
- ingress
- CI/CD

它还会逐步接管：

- approved training runtime
- approved inference runtime
- model registry / metadata plane
- data / artifact access pattern
- policy / cost / tenancy guardrails

## 更成熟的职责边界

平台团队通常负责：

- runtime setup
- cluster-level policy and quota
- shared observability
- artifact and model lifecycle 基础设施
- standard deployment path

应用 / ML 团队通常负责：

- business logic
- model selection and tuning
- prompt / eval logic
- workflow-specific application integration

安全 / 合规团队通常负责：

- data boundary
- workload approval class
- supply chain and policy requirements

## 你应该从中看到什么

- AI 平台团队更像 `platform engineering + MLOps + infra governance` 的交叉体
- 真正成熟的 operating model，一定会把“平台负责什么、应用团队负责什么”切清楚
- 如果团队边界不清，AI adoption 往往会卡在临时支持模式，无法产品化

## 来源

- [Kubeflow Home](https://www.kubeflow.org/)
- [Kubeflow 1.11 Release Announcement](https://blog.kubeflow.org/kubeflow-1.11-release/)
- [KServe Control Plane](https://kserve.github.io/website/docs/concepts/architecture/control-plane)
- [Ray on Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes/)
- [Cloud Native Artificial Intelligence Whitepaper](https://www.cncf.io/reports/cloud-native-artificial-intelligence-whitepaper/)

## 相关

- [[平台团队工作方式]]
- [[AI 时代云原生采用路径]]
- [[../06-Workflows/AI 平台团队采用推进工作流|AI 平台团队采用推进工作流]]
- [[../04-Maps/AI 时代云原生采用图|AI 时代云原生采用图]]
