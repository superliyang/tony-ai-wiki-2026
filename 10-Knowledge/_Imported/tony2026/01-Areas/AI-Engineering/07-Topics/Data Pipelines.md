---
title: Data Pipelines
type: topic
status: learning
tags:
  - ai/engineering
  - ai/data
created: 2026-03-13
updated: 2026-03-28
---

# Data Pipelines

## 为什么它是训练系统的起点

很多团队把数据管道理解成“把训练集准备出来”。

但在大模型系统里，`Data Pipeline` 更像一条持续运行的制造链，它同时决定：

- 训练数据质量
- 训练可复现性
- 合规边界
- 成本结构
- 后续评测解释力

所以数据管道不是前置脚本，而是训练系统的质量控制前线。

## 一条成熟数据管道通常有 6 个阶段

### 1. Ingestion

把不同来源接进系统：

- web crawl
- code repository
- 文档和表格
- 对话与业务日志
- 人工标注数据

### 2. Governance

回答这些高风险问题：

- 是否有授权
- 是否需要脱敏
- 是否有版权或隐私限制
- 哪些数据禁止进入训练主集

### 3. Normalization

统一格式和字段：

- schema 统一
- 编码统一
- 文本抽取
- HTML / markup 清理
- 文档切片

### 4. Quality Processing

典型步骤：

- 过滤
- 去重
- 质量评分
- 语言识别
- 毒性 / 敏感内容标记
- 噪声样本剔除

### 5. Mixture and Versioning

这里决定：

- 哪些子集混在一起
- 配比是多少
- 哪一版数据用于哪个实验
- 数据变更如何回溯

### 6. Delivery

最后要能高吞吐、稳定地把数据送到：

- training jobs
- eval jobs
- downstream fine-tuning jobs

## 最重要的几个工程问题

### 数据质量怎么定义

数据质量不能只看“像不像自然语言”，还要看：

- 重复度
- 结构完整性
- 领域覆盖
- 标注一致性
- 是否对目标任务真的有帮助

### 数据版本怎么绑定实验

如果训练结果无法绑定：

- 数据版本
- 过滤规则版本
- mixture 版本
- tokenizer 版本

那实验结论通常不可信。

### 数据量和数据质量怎么取舍

- 更多数据有助于泛化
- 但低质量数据会污染训练，放大 token 和算力浪费
- 在大模型里，“错得很稳定的数据”往往比“少一点但更干净的数据”更危险

## 大模型数据管道里最常见的动作

### 过滤

常见过滤目标：

- 垃圾文本
- 高重复模板内容
- 格式损坏文档
- 明显无语义样本
- 高风险敏感内容

### 去重

去重至少要区分：

- exact dedup
- near dedup
- 文档级去重
- 段落级去重

因为重复度过高会让模型记住模式，而不是学到泛化能力。

### 采样与混合

成熟管道不会把所有数据一锅煮，而会做：

- domain mixture
- language mixture
- quality-tier mixture
- curriculum-style sampling

### 数据交付

如果 delivery 层不稳定，会出现：

- GPU starvation
- host memory 抖动
- 存储 I/O 成为瓶颈
- 分布式节点读到不一致的 shard

## 你应该重点观察的指标

- 重复率
- 过滤前后保留率
- 样本长度分布
- 语言 / 领域分布
- 数据读取吞吐
- dataloader stall 比例
- 不同 mixture 对 eval 的边际贡献

## 数据管道最常见的失败模式

- 只关心“收了多少数据”，不关心“这些数据是否真的有效”
- 数据去重做得太晚，训练时才发现污染严重
- 数据版本不稳定，实验不能复盘
- 训练集和评测集存在污染
- 合规审查滞后，导致可用数据集被临时回收

## 一套更成熟的判断方式

当你看一个数据 pipeline 时，不要只问“它能不能处理数据”，而要问：

- 它能不能解释数据来自哪里
- 它能不能稳定复现上次的数据视图
- 它能不能证明过滤和 mixture 的效果
- 它能不能支持训练与评测同时使用同一套版本语义

## 学习这页时最该记住什么

- 数据不是原料仓库，而是 AI 系统最前面的质量和合规边界
- 很多训练问题最后会回到：数据质量、版本和 mixture 设计

## 推荐怎么往下读

1. [[Tokenization]]
2. [[Training Stack Overview]]
3. [[Distributed Training]]
4. [[Evaluation and Benchmarks]]

## 关联

- [[Tokenization]]
- [[Training Stack Overview]]
- [[Distributed Training]]
- [[Evaluation and Benchmarks]]
- [[Experiment Tracking]]

## 资料

- [Hugging Face Datasets Overview](https://huggingface.co/docs/datasets/en/how_to)
- [Hugging Face Datasets GitHub](https://github.com/huggingface/datasets)
