---
title: Tokenization
type: topic
status: learning
tags:
  - ai/engineering
  - ai/tokenization
created: 2026-03-13
updated: 2026-03-28
---

# Tokenization

## 为什么它比很多人想的更重要

`Tokenization` 决定的不只是“怎么把文本切开”，而是：

- context window 的真实利用率
- 推理成本
- 多语言公平性
- 代码与文档场景的表达效率
- 训练数据被模型看见的方式

所以 tokenizer 不是模型前面的一个小工具，而是模型资产的一部分。

## tokenizer 实际上是一条 pipeline

一个现代 tokenizer 往往不只是“词表 + encode”，而是至少包括：

1. normalization：大小写、空白、Unicode 规范化
2. pre-tokenization：先切出粗粒度片段
3. model：`BPE`、`Unigram`、`WordPiece` 等子词模型
4. post-processing：加入 special tokens、pair 结构
5. decoding：把 token 序列还原为文本

理解 tokenizer 时，不能只盯着词表大小，而要看这整条 pipeline。

## 为什么 tokenizer 会影响整个生命周期

### 对训练的影响

- 决定相同语料最终变成多少 token
- 决定长序列训练时的 token budget 压力
- 决定领域术语是否被稳定保留

### 对推理的影响

- 相同输入 token 数不同，直接改变延迟和价格
- 上下文窗口的实际容量不是按字符算，而是按 token 算

### 对产品的影响

- 多语言用户可能天然承受不同 token 成本
- 代码、表格、日志等结构化文本如果切分差，会影响工具和 agent 使用体验

## 几种主流方法该怎么理解

### `BPE`

- 通过合并高频子串建立词表
- 工程上常见，兼顾效率和实用性

### `WordPiece`

- 早期 transformer 生态常见
- 更偏概率视角下的子词构造

### `Unigram`

- 从更大候选集合中裁剪出合适词表
- 通常更适合做灵活的子词建模

### `SentencePiece`

- 既是一种工具链，也常作为 tokenizer 训练与应用的统一方式
- 优点是对空格和原始文本边界处理更系统，特别适合多语言场景

## 大模型时代最值得关注的 5 个点

### 1. token density

不同语言和模态的 token 密度差异非常大。

例如：

- 中文
- 日文
- 代码
- JSON / logs
- OCR 文本

都可能在“同样字符数”下产生完全不同的 token 数。

### 2. domain vocabulary

如果 tokenizer 对关键领域术语切分过碎，会影响：

- 学习效率
- 检索效果
- 下游微调质量

### 3. special tokens 和 control tokens

system、tool、role、multimodal placeholder 等 special tokens 已经是系统设计的一部分。

### 4. tokenizer 兼容性

tokenizer 一旦变了，通常意味着：

- 老 checkpoint 不兼容
- prompt 和 dataset 的统计失真
- 评测结果不可直接对比

### 5. packing 与 truncation

很多训练与推理问题，本质不是模型不行，而是：

- packing 策略不合理
- truncation 过早发生
- 边界信息被破坏

## 实践中应该怎么判断 tokenizer 好不好

### 看效率

- 平均每条样本的 token 数
- 长尾样本的 token 膨胀情况

### 看表达质量

- 关键术语是否被切得过碎
- 代码标识符是否被切得无法保留结构
- 特殊格式文本是否被异常破坏

### 看兼容性

- 与现有 checkpoint、dataset、eval set 是否一致
- tokenizer 版本是否被稳定记录

## 常见误区

- 只比较词表大小，不看 normalization 和 pre-tokenization
- 看到“更少 token”就以为一定更好
- 忽略多语言和代码场景的 token 成本差异
- 把 tokenizer 当作可以随便换的小部件

## 学习这页时最该记住什么

- tokenization 是成本问题、能力问题，也是产品问题
- 不理解 tokenizer，就很难真正理解 context window、推理价格和数据准备

## 推荐怎么往下读

1. [[Data Pipelines]]
2. [[Training Stack Overview]]
3. [[Inference Optimization]]
4. [[KV Cache、Prefill-Decode 与 Continuous Batching]]

## 关联

- [[Data Pipelines]]
- [[Training Stack Overview]]
- [[Inference Optimization]]
- [[KV Cache、Prefill-Decode 与 Continuous Batching]]

## 资料

- [Hugging Face Tokenizers](https://huggingface.co/docs/tokenizers/main/en)
- [Transformers Tokenizer API](https://huggingface.co/docs/transformers/main/main_classes/tokenizer)
- [SentencePiece](https://github.com/google/sentencepiece)
