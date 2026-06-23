---
title: Representation Learning
type: topic
status: active
tags:
  - ai/foundations
  - ai/deep-learning
  - ai/representation
created: 2026-03-13
updated: 2026-05-16
---

# Representation Learning

## 一句话定位

`Representation Learning` 研究模型如何把原始数据变成对任务有用的内部表示，例如 embedding、hidden state、latent space 和 multimodal representation。

它是从“人工设计特征”走向“模型自动学习抽象”的关键转折，也是深度学习、大模型、RAG、多模态和推荐系统的共同底座。

## 它解决什么问题

- 减少对人工特征工程的依赖
- 把复杂原始信号压缩成更可计算、更可迁移的结构
- 让相似对象在表示空间中更接近，让无关差异被弱化
- 支持分类、检索、生成、聚类、推荐、对齐和迁移学习
- 为模型跨任务、跨模态、跨场景复用能力提供基础

## 核心概念

### Feature

- feature 是对原始数据的某种有用刻画
- 传统机器学习经常依赖人工特征
- 深度学习倾向于让模型在训练中自己学出多层特征

### Embedding

- embedding 是把离散对象映射到连续向量空间
- token、用户、商品、图片、文档、代码片段都可以有 embedding
- embedding 的价值在于让语义相似、行为相似或任务相关的对象在向量空间中呈现结构

### Latent Space

- latent space 是模型内部学到的隐含表示空间
- 它不一定直接对应人类可命名概念，但会承载对任务有用的结构
- 生成模型、变分模型、多模态模型都高度依赖 latent representation

### Hidden State

- hidden state 是模型在中间层保存的信息状态
- 在 Transformer 中，每一层的 hidden state 都可以看作 token 经过上下文融合后的表示
- LLM 的很多能力来自逐层构建和重写 hidden representations

### Invariance / Equivariance

- invariance 指对某些变化保持不变，例如图片轻微平移后类别不变
- equivariance 指表示随输入变化而有规律地变化，例如空间位置变化带来特征位置变化
- 好的归纳偏置会帮助模型学到更稳健的表示

### Contrastive Learning

- contrastive learning 通过拉近正样本、推远负样本来学习表示
- 它常用于图文对齐、检索、语义匹配和自监督学习
- CLIP 这类多模态模型的直觉，就可以从表示空间对齐来理解

## 和现代 AI 的关系

- `Token Embedding`：把离散 token 变成连续向量，是 LLM 的入口
- `Contextual Representation`：同一个词在不同上下文中有不同 hidden state
- `Foundation Model`：通过大规模训练学到可迁移的通用表示
- `RAG`：检索质量高度依赖 query/document embedding 的语义结构
- `Multimodal Alignment`：把图像、文本、音频等模态映射到可对齐空间
- `Memory / Personalization`：用户画像、长期记忆和偏好建模都依赖表示组织

## 好表示的判断标准

- `Task-useful`：对目标任务有帮助
- `Compact`：保留关键结构，过滤无关噪声
- `Robust`：对无关扰动不敏感
- `Transferable`：可以迁移到相近任务或新场景
- `Aligned`：与真实语义、用户意图或业务目标尽量一致
- `Interpretable enough`：至少能通过可视化、探针任务或案例分析做一定诊断

## 典型失败模式

- `Shortcut Learning`：模型学到表面捷径，而不是真正能力
- `Spurious Correlation`：表示中混入错误相关性，换场景就失效
- `Representation Collapse`：不同输入被压成过于相似的表示，失去区分度
- `Distribution Shift`：训练分布和线上分布不同，表示不再可靠
- `Bias Amplification`：表示空间放大数据中的偏见
- `Over-specialization`：只对单一任务有效，迁移能力差

## 学习目标

学完这一页，你应该能：

- 解释 embedding、latent space、hidden state 的区别
- 用表示空间理解检索、推荐、分类、生成和多模态对齐
- 判断一个模型问题是不是“表示没有学好”
- 理解为什么 RAG、向量数据库和多模态模型都离不开 representation learning
- 在面试中把表示学习连接到现代大模型工程

## 常见误区

- 误区一：embedding 只是一个向量
  embedding 的关键不是向量形式，而是向量空间里承载了什么语义、行为或任务结构。

- 误区二：维度越高表示越好
  维度提高可能增加容量，也可能带来噪声、成本和过拟合。

- 误区三：可视化好看就代表表示好
  t-SNE/UMAP 只能帮助观察，最终要看任务效果、鲁棒性和泛化能力。

- 误区四：大模型表示天然可靠
  表示仍然受训练数据、目标函数、对齐策略和分布变化影响。

## 最小练习

1. 选 10 个词或商品，想象它们在 embedding 空间里应该如何靠近或远离。
2. 用一句话解释“为什么向量检索能找到语义相近文档”。
3. 找一个推荐系统或 RAG 案例，分析它的表示可能学到了什么、漏掉了什么。
4. 列出一个 representation failure 可能导致的线上问题。

## 面试表达

> Representation Learning 的核心是让模型把原始数据转成对任务有用的内部表示。好的表示能压缩噪声、保留关键结构、支持相似性计算和跨任务迁移。现代 LLM 的 token embedding、Transformer hidden state、RAG 向量检索、多模态对齐和个性化记忆，本质上都可以从表示学习角度理解。

## 相关

- [[Neural Networks Basics]]
- [[Linear Algebra for ML]]
- [[Probability and Information Theory]]
- [[Optimization Basics]]
- [[Statistical Learning]]
- [[../../AI-Learning/06-Topics/Foundation Models|Foundation Models]]
- [[../../AI-Learning/06-Topics/Multimodal Models|Multimodal Models]]
- [[../../AI-Learning/06-Topics/RAG|RAG]]
