---
title: MLOps 与 LLMOps 生态图
type: map
status: learning
tags:
  - ai/map
  - ai/mlops
  - ai/llmops
created: 2026-03-26
updated: 2026-03-26
---

# MLOps 与 LLMOps 生态图

```mermaid
flowchart TD
  T["[[../06-Topics/MLOps 与 LLMOps|MLOps 与 LLMOps]]"] --> ET["[[../../AI-Engineering/07-Topics/Experiment Tracking|Experiment Tracking]]"]
  T --> EV["[[../../AI-Engineering/07-Topics/Evaluation and Benchmarks|Evaluation and Benchmarks]]"]
  T --> PR["[[../../AI-Engineering/07-Topics/Prompt Registry、Datasets 与 Evals|Prompt Registry、Datasets 与 Evals]]"]
  T --> MR["[[../../AI-Engineering/07-Topics/Model Registry and Deployment|Model Registry and Deployment]]"]
  T --> OE["[[../../AI-Engineering/07-Topics/Online Evals、Human Feedback 与 Annotation|Online Evals、Human Feedback 与 Annotation]]"]
  T --> OB["[[../../AI-Engineering/07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]]"]

  subgraph systems["平台 / 系统"]
    MLF["[[../09-Systems/MLflow|MLflow]]"]
    WNB["[[../09-Systems/Weights & Biases Platform|Weights & Biases Platform]]"]
    LFS["[[../09-Systems/Langfuse|Langfuse]]"]
    PHX["[[../09-Systems/Arize Phoenix|Arize Phoenix]]"]
    PFO["[[../09-Systems/Promptfoo|Promptfoo]]"]
  end

  subgraph cloud["云原生 / 基础设施"]
    OTL["[[../../Cloud-Native/02-Projects/OpenTelemetry|OpenTelemetry]]"]
    KSV["[[../../Cloud-Native/02-Projects/KServe|KServe]]"]
  end

  ET --> MLF
  ET --> WNB
  EV --> PHX
  EV --> PFO
  PR --> MLF
  PR --> WNB
  PR --> LFS
  MR --> MLF
  MR --> WNB
  OE --> LFS
  OE --> PHX
  OB --> LFS
  OB --> PHX
  OB --> OTL
  MR --> KSV
  OE --> OTL
```

## 怎么读这张图

- 左边是生命周期问题
- 中间是平台层
- 右下是承接这些平台的云原生基础设施

真正重要的不是某个工具单点强不强，而是：

- 它在哪个生命周期节点最强
- 它和其它层怎么拼起来
- 它更适合 `experiment system`、`release gate`，还是 `production feedback loop`

## 推荐顺序

1. [[../06-Topics/MLOps 与 LLMOps|MLOps 与 LLMOps]]
2. [[../../AI-Engineering/08-Maps/MLOps 与 LLMOps 工程图|MLOps 与 LLMOps 工程图]]
3. [[../09-Systems/MLflow|MLflow]]
4. [[../09-Systems/Weights & Biases Platform|Weights & Biases Platform]]
5. [[../09-Systems/Langfuse|Langfuse]]
6. [[../09-Systems/Arize Phoenix|Arize Phoenix]]
7. [[../09-Systems/Promptfoo|Promptfoo]]

## 关联

- [[AI Infra 与推理服务生态图]]
- [[Agent 平台生态图]]
- [[../../AI-Engineering/08-Maps/AI Engineering Stack Map|AI Engineering Stack Map]]
