---
title: LLM Training Stack
type: stack
status: learning
tags:
  - ai/engineering
  - ai/training-stack
created: 2026-03-13
updated: 2026-03-28
---

# LLM Training Stack

## 简介

`LLM Training Stack` 说的不是某一个框架或某一个集群，而是大模型训练所依赖的一整套层次结构。

## 为什么要单独学它

因为训练系统的真实难点几乎都发生在“跨层交互”上：

- 数据慢，表现为 GPU 利用率低
- tokenizer 不合适，表现为上下文成本飙升
- 并行策略不当，表现为扩卡效率差
- checkpoint 和实验记录薄弱，表现为结果不可信
- post-training 设计不当，表现为产品体验和安全边界不稳定

所以训练栈必须按层拆开看，但又不能割裂地看。

## 关键层次

### 1. 数据层

- 采集
- 清洗
- 过滤
- 去重
- mixture
- 版本控制

### 2. tokenizer 层

- normalization
- subword modeling
- special tokens
- token density

### 3. 框架层

- `PyTorch`
- `JAX`
- `TensorFlow`

### 4. 分布式训练层

- `DDP`
- `FSDP`
- `ZeRO`
- tensor parallel
- pipeline parallel

### 5. 基础设施层

- GPU / TPU
- 网络
- 存储
- 调度
- checkpoint

### 6. post-training 层

- `SFT`
- `RLHF`
- `DPO`
- constitutional / preference optimization

### 7. synthetic data 与 eval 层

- instruction synthesis
- preference data generation
- red-team data
- benchmark / safety eval

### 8. 发布层

- registry
- release gate
- deployment handoff
- feedback loop

## 用这页时最该形成的判断

- 训练栈不是单次 job，而是端到端系统。
- 任何“模型训练效果差”的问题，都应该先定位到层，而不是先怪模型。
- post-training、synthetic data、safety eval 已经是现代 LLM 训练栈的一部分，不再是附属品。

## 相关主题

- [[../07-Topics/Training Stack Overview|Training Stack Overview]]
- [[../07-Topics/Data Pipelines|Data Pipelines]]
- [[../07-Topics/Tokenization|Tokenization]]
- [[../07-Topics/Distributed Training|Distributed Training]]
- [[../07-Topics/Infrastructure (GPU-TPU)|Infrastructure (GPU-TPU)]]
- [[../07-Topics/RLHF and Preference Optimization|RLHF and Preference Optimization]]
- [[../07-Topics/Synthetic Data|Synthetic Data]]
- [[../07-Topics/Safety Evaluation|Safety Evaluation]]
- [[../07-Topics/Experiment Tracking|Experiment Tracking]]
- [[../07-Topics/Evaluation and Benchmarks|Evaluation and Benchmarks]]
- [[../07-Topics/Model Registry and Deployment|Model Registry and Deployment]]
