---
title: AI 平台团队采用推进工作流
type: workflow
status: learning
tags:
  - cloud-native/workflow
  - cloud-native/ai
  - cloud-native/platform
created: 2026-03-25
updated: 2026-03-25
---

# AI 平台团队采用推进工作流

## 这个工作流在解决什么

当组织已经确认 AI workload 会长期存在后，平台团队需要回答的不是“给不给 GPU”，而是：如何把分散的 AI 试验，推进成可治理、可复用、可观测的平台能力。

## 推荐工作流

1. 先识别最先平台化的能力
   - 训练集群
   - 推理入口
   - notebook / dev environment
   - artifact / model registry
   - evaluation / approval gate
2. 把 workload 先分层
   - experiment
   - batch training
   - online inference
   - distributed execution
3. 为每类 workload 定义标准入口
   - 哪些团队可以 self-service
   - 哪些要经过平台 review
   - 哪些必须用 approved runtime
4. 定义最小 guardrails
   - quota
   - tenancy
   - storage boundary
   - security policy
   - cost visibility
5. 从 shared service 过渡到 platform product
   - 清楚 catalog 和 workflow
   - 明确 golden path
   - 建立 support / escalation / ownership
6. 用 adoption 和 reliability 复盘
   - 哪些 workload 已经走平台路径
   - 哪些团队仍然绕过平台
   - 哪些环节 friction 最大

## 关键判断

- AI adoption 最容易失败在“平台过早过重”或“平台永远只做人工支持”之间摇摆
- 先标准化最常见 workload，再扩到更复杂路径，通常更稳
- AI 平台能力必须和成本、配额、策略、数据边界一起治理

## 来源

- [Cloud Native Artificial Intelligence Whitepaper](https://www.cncf.io/reports/cloud-native-artificial-intelligence-whitepaper/)
- [Kubeflow Home](https://www.kubeflow.org/)
- [KServe System Architecture Overview](https://kserve.github.io/website/docs/concepts/architecture)
- [Kubeflow 1.11 Release Announcement](https://blog.kubeflow.org/kubeflow-1.11-release/)

## 相关

- [[../03-Topics/AI 时代云原生采用路径|AI 时代云原生采用路径]]
- [[../03-Topics/AI 工作负载平台团队工作方式|AI 工作负载平台团队工作方式]]
- [[../07-Case-Studies/Kubeflow AI Platform Reference Case|Kubeflow AI Platform Reference Case]]
- [[../07-Case-Studies/KServe Enterprise LLM Serving Case|KServe Enterprise LLM Serving Case]]
- [[../04-Maps/AI 时代云原生采用图|AI 时代云原生采用图]]
