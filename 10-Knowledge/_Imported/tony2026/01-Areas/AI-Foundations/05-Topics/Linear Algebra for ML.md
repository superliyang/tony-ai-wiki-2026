---
title: Linear Algebra for ML
type: topic
status: active
tags:
  - ai/foundations
  - ai/math
created: 2026-03-13
updated: 2026-05-16
---

# Linear Algebra for ML

## 一句话定位

`Linear Algebra for ML` 是理解现代 AI 的“表示语言”：样本、token、图片 patch、参数、hidden state、attention 都会被组织成向量、矩阵或张量，然后通过线性变换与非线性组合完成学习和推理。

如果不懂线性代数，你仍然可以调 API，但很难真正理解：

- embedding 为什么是向量
- linear layer 在做什么
- attention 为什么主要是矩阵乘法
- 模型维度、参数量、显存和计算量为什么相关

## 它解决什么问题

机器学习需要把现实世界对象变成可计算对象：

- 文本 -> token id -> embedding vector
- 图片 -> patch / feature map -> tensor
- 用户行为 -> feature vector
- 模型参数 -> matrix / tensor

线性代数提供了描述这些对象和变换的基础工具。

## 必须掌握的核心概念

### 向量

向量是一组有顺序的数，可以表示：

- 一个样本的特征
- 一个 token 的 embedding
- 一个用户画像
- 一个中间 hidden state

关键直觉：向量不是“数字列表”这么简单，它代表一个点、方向或语义位置。

### 矩阵

矩阵可以理解为：

- 一组向量的集合
- 一个线性变换
- 一层模型参数
- batch 数据的组织方式

在神经网络里，最常见的形式是：

```text
output = input × weight + bias
```

### 维度

维度回答“表示空间有多大”。

- embedding dim 越大，表达能力可能越强，但成本也越高
- hidden size 影响参数量、显存和推理成本
- context length 会影响 attention 的计算和内存

### 矩阵乘法

矩阵乘法是信息混合和变换的核心。

在模型里，它常用于：

- feature projection
- token mixing
- attention score
- MLP layer
- classifier head

### 点积与相似度

点积常用来衡量两个向量的相关性。

它帮助你理解：

- embedding similarity
- retrieval / vector search
- attention 中 query 和 key 的匹配
- 推荐系统里的 user-item match

### 特征值、低秩与分解

不必一开始深挖推导，但要知道这些概念解释了：

- 降维
- PCA
- LoRA / low-rank adaptation
- embedding space 的主方向
- 参数压缩和近似

## 和现代 AI 的关系

### Embedding

Embedding 是把离散对象映射到连续向量空间。

理解 embedding 后，你会更容易理解：

- 词向量
- token embedding
- item embedding
- 多模态对齐
- vector database

### Attention

Attention 的核心计算大量依赖矩阵乘法：

```text
Q × K^T -> attention scores
scores × V -> mixed representation
```

直觉：模型用 query 去问 key，得到权重后再汇总 value。

### Linear Layer

Linear layer 是最基础的参数化变换。

它不只是“线性层”，而是神经网络中最常见的信息投影器。

### Batch 与 Tensor

真实训练和推理不是一个样本一个样本算，而是 batch / tensor 并行。

因此你必须习惯看：

```text
[batch, sequence, hidden]
[batch, channel, height, width]
[layers, heads, sequence, head_dim]
```

## 学习目标

达到可用水平时，你应该能：

- 看懂向量、矩阵、张量的形状
- 判断一个矩阵乘法维度是否匹配
- 解释 embedding 和 similarity 的含义
- 解释 attention 为什么需要 `Q/K/V`
- 粗略估算 hidden size / sequence length 对计算成本的影响
- 看懂模型结构图里的 projection、head、MLP、residual

## 常见误区

- 误区 1：把线代当成纯数学课，忽略它在模型里的工程含义
- 误区 2：只背公式，不看 shape
- 误区 3：不知道 batch 维、sequence 维、hidden 维分别代表什么
- 误区 4：以为 embedding 的每个维度都有固定人工语义
- 误区 5：忽略矩阵乘法背后的计算成本

## 最小练习

1. 随便拿一个 transformer 结构图，标出每一步 tensor shape
2. 手算一个小矩阵乘法，确认维度匹配规则
3. 用两个向量计算 dot product / cosine similarity
4. 解释 `Q × K^T` 为什么得到 token-token 相关性
5. 对比 embedding dim 为 384、768、4096 时的成本直觉

## 面试表达

如果被问“为什么线性代数对大模型重要”，可以这样答：

> 大模型本质上把 token、图像 patch、参数和中间状态都表示成高维向量或张量；模型的主要计算由矩阵乘法、投影、相似度和张量变换组成。线性代数不仅解释模型如何表达信息，也直接决定训练和推理的计算成本。

## 相关

- [[Neural Networks Basics]]
- [[Representation Learning]]
- [[Probability and Information Theory]]
- [[Optimization Basics]]
- [[../../AI-Learning/06-Topics/Transformer|Transformer]]
- [[../../AI-Learning/06-Topics/Long Context|Long Context]]
