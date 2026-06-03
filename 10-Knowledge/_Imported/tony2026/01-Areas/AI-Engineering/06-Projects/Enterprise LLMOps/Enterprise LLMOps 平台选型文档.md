---
title: Enterprise LLMOps 平台选型文档
type: project-doc
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# Enterprise LLMOps 平台选型文档

## 目标

为一个企业级 LLM / agent 团队选择第一阶段平台组合。

## 典型需求

- 跟踪 experiment / prompt / dataset / eval evidence
- 建立 release gate
- 支持 production traces 与 regression diagnosis
- 满足 self-hosting / privacy / audit 约束

## 选型维度

- lifecycle coverage
- production observability
- prompt / dataset / score management
- self-hosting maturity
- platform assembly cost
- policy / audit compatibility

## 推荐路线

### 路线 A：open-source-first

- `MLflow`
- `Promptfoo`
- `Phoenix`
- `OpenTelemetry`

适合：有平台团队、合规要求高、愿意自己整合。

### 路线 B：LLM app workbench-first

- `Langfuse`
- `Promptfoo`
- `KServe / Argo CD`

适合：LLM app / agent 团队，需要 prompt + trace + score + dataset + release comparison。

### 路线 C：research-to-app collaboration-first

- `Weights & Biases Platform`
- `Weave`
- 补充 deployment / serving 平台

适合：训练实验和应用 eval 都很重的团队。

## 不推荐的误区

- 指望单一平台覆盖全部生命周期
- 过早追求“平台大一统”
- 没有 release gate 却先做 production observability
- 只有 traces 没有稳定 dataset / scorer

## 关联

- [[Enterprise LLMOps 落地路径]]
- [[../../07-Topics/Enterprise MLOps 与 LLMOps Vendor Tradeoffs|Enterprise MLOps 与 LLMOps Vendor Tradeoffs]]
