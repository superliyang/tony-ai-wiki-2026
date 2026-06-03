---
title: Model Registry and Deployment
type: topic
status: learning
tags:
  - ai/engineering
  - ai/deployment
  - ai/llmops
created: 2026-03-13
updated: 2026-03-26
---

# Model Registry and Deployment

## 为什么重要

- 模型从实验结果变成生产资产，需要可管理的版本与发布流程
- 没有注册表和发布纪律，团队很难稳定上线和回滚
- 到 `LLMOps` 阶段，真正要治理的已经不只是模型权重，还包括 prompt、dataset、tool schema 和 eval evidence

## 系统视角

模型注册表和部署流程是实验系统与生产系统之间的交接面。它需要回答：

- 哪个模型版本被谁训练出来
- 它对应什么 tokenizer、配置、评测结果和依赖
- 它绑定了什么 prompt / dataset / scorer
- 它是否满足上线门禁
- 上线后若出问题，如何回滚

## 核心问题

- 哪个版本可以进入生产，依据是什么
- 模型、tokenizer、配置、prompt、评测报告如何作为一个整体被追踪
- 灰度、回滚和兼容性如何设计
- deployment object 到底是 model、app config，还是一个完整 release bundle

## 一个成熟发布流程通常包含

- 训练或应用产物登记
- 自动化评测与门禁
- 人工审批或风险复核
- staging / canary / shadow release
- 线上监控与在线评测
- 回滚与复盘

## 常见平台怎么分工

- `MLflow`：model registry、prompt registry、promotion stages
- `Weights & Biases Platform`：registry、artifacts、release workflow 协作
- `Langfuse`：prompt、scores、dataset run comparison，辅助 release decision
- `KServe`：承接实际 serving / deployment 控制面
- `Argo CD`：交付与 GitOps 层

## 为什么这里经常出事故

- 模型文件和配置没绑定，线上跑的不是评测过的版本
- tokenizer 变了但依赖系统不知道
- prompt 版本没和发布记录绑定
- 只关心模型效果，不关心线上兼容性和回滚路径
- release gate 只看静态 benchmark，不看真实任务集

## 学习这页时最该记住什么

- 部署对象不是一个权重文件，而是一整组受控资产
- 模型治理能力决定团队能不能持续迭代
- `LLMOps` 里注册与发布的对象通常已经是 release bundle，而不是单一 artifact

## 关联

- [[Experiment Tracking]]
- [[Evaluation and Benchmarks]]
- [[Prompt Registry、Datasets 与 Evals]]
- [[Online Evals、Human Feedback 与 Annotation]]
- [[../05-Deployment/部署索引|部署索引]]
- [[../../AI-Learning/09-Systems/MLflow|MLflow]]
- [[../../AI-Learning/09-Systems/Weights & Biases Platform|Weights & Biases Platform]]
- [[../../AI-Learning/09-Systems/Langfuse|Langfuse]]
- [[../../Cloud-Native/02-Projects/KServe|KServe]]
- [[../../Cloud-Native/02-Projects/Argo CD|Argo CD]]
