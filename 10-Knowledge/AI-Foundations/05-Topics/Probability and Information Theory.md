---
title: Probability and Information Theory
type: topic
status: active
tags:
  - ai/foundations
  - ai/math
created: 2026-03-13
updated: 2026-05-16
---

# Probability and Information Theory

## 一句话定位

`Probability and Information Theory` 是理解 AI 如何处理不确定性、预测下一个 token、评估模型好坏、压缩信息和学习分布的基础语言。

如果线性代数解释“表示怎么计算”，概率和信息论解释“模型到底在预测什么、错在哪里、学到了多少信息”。

## 它解决什么问题

AI 系统经常面对不确定性：

- 这张图最可能是什么类别
- 这个 token 后面最可能接什么
- 检索结果是否可信
- 预测分布和真实分布差多少
- 一个表示保留了多少有用信息

概率论提供不确定性的表达方式，信息论提供信息量和分布差异的度量方式。

## 核心概念

### 概率分布

概率分布描述所有可能结果及其概率。

在 AI 中常见：

- 分类模型输出类别分布
- 语言模型输出 vocabulary 上的 token 分布
- 生成模型学习数据分布

### 条件概率

条件概率描述“已知一些信息后，判断如何变化”。

语言模型的核心就是：

```text
P(next token | previous tokens)
```

也就是在上下文条件下预测下一个 token。

### 似然

似然衡量“在某组参数下，观察到当前数据有多合理”。

训练模型常常等价于让真实数据在模型分布下变得更可能。

### 熵

熵可以理解为不确定性。

- 熵高：分布分散，不确定性大
- 熵低：分布集中，模型更确定

### Cross Entropy

Cross entropy 衡量真实分布和预测分布之间的编码代价。

在分类和语言模型中，它经常就是训练 loss 的核心。

### KL Divergence

KL divergence 衡量两个分布之间的差异。

它常出现在：

- distillation
- RLHF / preference optimization
- variational inference
- policy regularization

### Mutual Information

Mutual information 描述两个变量共享多少信息。

它帮助理解：

- 表示是否保留任务相关信息
- 多模态对齐
- 特征选择
- 数据压缩

## 和现代 AI 的关系

### 语言建模

语言模型不是直接“理解语言”，而是在上下文条件下建模 token 分布。

训练目标通常可以理解为：让模型给真实下一个 token 更高概率。

### Sampling

生成文本时，模型会从概率分布中采样。

常见控制项：

- temperature
- top-k
- top-p
- repetition penalty

这些都在改变输出分布的形状。

### Calibration

模型给出的概率不一定等于真实置信度。

在高风险场景里，需要关心：

- 模型是否过度自信
- 置信度是否和正确率匹配
- 是否需要 abstain / escalation

### Evaluation

很多评测指标都和概率有关：

- log loss
- perplexity
- accuracy with confidence
- uncertainty-aware evaluation

## 学习目标

达到可用水平时，你应该能：

- 解释概率分布、条件概率和似然
- 解释 cross entropy 为什么能作为 loss
- 理解语言模型预测的是条件分布
- 理解 temperature / top-p 对生成的影响
- 知道 KL divergence 在对齐和蒸馏中的作用
- 判断模型置信度是否值得信任

## 常见误区

- 误区 1：把概率输出当成真实可信度
- 误区 2：只看 top-1 答案，不看分布形状
- 误区 3：认为低 loss 一定代表业务效果好
- 误区 4：把 perplexity 和用户体验直接等同
- 误区 5：忽略数据分布变化带来的风险

## 最小练习

1. 手算一个二分类 cross entropy
2. 比较两个 token 分布的熵高低
3. 用 temperature 改变同一个 prompt 的输出风格
4. 解释为什么 top-p 会影响多样性和稳定性
5. 找一个模型错误案例，判断它是“不知道”还是“过度自信”

## 面试表达

如果被问“语言模型为什么和概率有关”，可以这样答：

> 语言模型学习的是在给定上下文下下一个 token 的条件概率分布。训练时通过 cross entropy 让真实 token 的概率更高；推理时再从这个分布中按一定策略采样。因此概率不仅影响模型训练，也影响生成稳定性、多样性、置信度和评测。

## 相关

- [[Statistical Learning]]
- [[Bayesian Methods]]
- [[Neural Networks Basics]]
- [[Representation Learning]]
- [[../../AI-Learning/06-Topics/Evaluation|Evaluation]]
- [[../../AI-Engineering/07-Topics/Evaluation and Benchmarks|Evaluation and Benchmarks]]
