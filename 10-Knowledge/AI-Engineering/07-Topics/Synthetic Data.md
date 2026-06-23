---
title: Synthetic Data
type: topic
status: learning
tags:
  - ai/engineering
  - ai/data
created: 2026-03-13
updated: 2026-03-28
---

# Synthetic Data

## 为什么它已经变成主线问题

当高质量真实数据稀缺、昂贵、敏感或覆盖不足时，合成数据就不再只是“补一点数据”，而会直接决定：

- 指令调优是否能快速启动
- 长尾场景能否被覆盖
- 偏好优化是否有足够样本
- 评测集是否足够丰富

所以 `synthetic data` 是训练与 post-training 之间的重要杠杆。

## 合成数据可以出现在训练链条的哪些位置

### 1. Pretraining augmentation

- 生成结构化文本
- 为低资源语言或特定文体补覆盖
- 做 retrieval / tool / doc-style mixing

### 2. Instruction tuning bootstrap

- 用强模型生成 instruction-response 对
- 启动新领域或新语言的 SFT 数据集

### 3. Preference / critique data

- 生成对比回答
- 生成 critique、revision、self-improvement 样本
- 扩充偏好训练和安全训练集

### 4. Evaluation expansion

- 构造攻击集
- 构造 corner cases
- 构造结构化压力测试数据

## 为什么“有没有 synthetic data”不是关键问题

真正关键的是三件事：

1. 如何生成
2. 如何筛选
3. 如何验证不污染系统

## 几种常见生成路线

### Teacher model generation

- 用更强模型生成 instruction、answer、critique 或 chain
- 优点：启动快、质量通常较高
- 风险：把 teacher 的风格、偏见和盲点整体带进来

### Self-instruct / self-play

- 模型自己生成指令、回答或对抗样本
- 优点：扩张速度快
- 风险：容易 self-feeding，分布逐渐变窄

### Programmatic synthesis

- 用规则、模板、仿真器、执行器生成样本
- 优点：结构清楚、可控性强
- 风险：容易过于干净，不像真实世界数据

## 真实工程里最难的部分

### 1. 多样性不够

看上去数据很多，但其实都在重复同一种任务结构和语言风格。

### 2. 过滤不够

如果没有质量过滤，synthetic data 会把错误、幻觉和模板偏见批量放大。

### 3. 训练评测污染

最危险的不是差一点，而是把 synthetic eval prompt 反向喂进训练集，导致指标虚高。

### 4. 分布错配

模型在 synthetic distribution 上学得很好，但一遇到真实用户数据就失真。

## 合成数据最容易被误用的地方

### 把它当廉价替代品

合成数据是杠杆，不是对高质量真实数据的完整替代。

### 只看数量，不看 mixture

如果 mixture 设计不好，100 万条 synthetic 样本可能还不如 5 万条高质量真实样本。

### 没有独立评测闭环

没有独立 eval 时，很容易误判 synthetic data 的真实收益。

## 学这一页要形成的判断力

### 判断 1：当前问题是缺数据，还是缺更好数据

不是每个问题都靠增加样本量解决。

### 判断 2：synthetic data 是该放在训练集、偏好集，还是 eval 集

不同位置的收益和风险完全不同。

### 判断 3：收益来自覆盖度，还是真实能力提升

如果指标提升只来自模板命中率，价值就很有限。

## 推荐怎么连着读

1. [[Data Pipelines]]
2. [[RLHF and Preference Optimization]]
3. [[Safety Evaluation]]
4. [[Evaluation and Benchmarks]]

## 相关主题

- [[Training Stack Overview]]
- [[Data Pipelines]]
- [[RLHF and Preference Optimization]]
- [[Safety Evaluation]]
- [[Evaluation and Benchmarks]]

## 资料

- [Self-Instruct](https://arxiv.org/abs/2212.10560)
- [Self-Instruct PDF](https://aclanthology.org/2023.acl-long.754.pdf)
- [Anthropic Constitutional AI](https://www.anthropic.com/research/claudes-constitution)
- [Constitutional Classifiers](https://www.anthropic.com/news/constitutional-classifiers)
