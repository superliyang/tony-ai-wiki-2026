---
title: Transformer
type: topic
status: draft
tags:
  - ai/topic
  - ai/transformer
created: 2026-03-13
updated: 2026-03-13
---

# Transformer

## 这个主题是什么

`Transformer` 是现代大语言模型和许多多模态模型最核心的架构基础。

## 为什么重要

- 它几乎定义了现代 foundation model 的主流技术路线
- 如果你只记一个现代 AI 关键架构名字，基本就是它

## 你先要抓住什么

- Transformer 解决的不是“让模型更会聊天”，而是让模型更擅长处理序列、建模上下文和扩展规模
- attention 是它的核心机制之一，用来决定输入中哪些部分彼此相关
- 它之所以重要，不只因为理论优雅，更因为它在工程上能扩展

## 关键组成

- token embedding
- positional information
- self-attention
- feed-forward network
- residual connection

## 为什么它改变了行业

- 更适合大规模并行训练
- 更容易利用海量数据进行预训练
- 能从 NLP 扩展到多模态和生成任务

## 相关

- [[Pretraining]]
- [[Foundation Models]]
- [[Long Context]]
