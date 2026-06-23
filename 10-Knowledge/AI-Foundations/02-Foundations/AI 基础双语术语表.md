---
title: AI 基础双语术语表
type: topic
status: learning
tags:
  - ai/foundations
  - ai/glossary
created: 2026-03-27
updated: 2026-04-03
---

# AI 基础双语术语表

> 这页不是完整词典，而是 `AI-Foundations` 最值得先吃透的一批核心术语。

## 先看哪几页

- [[../../怎么用 AI 基础双语术语表：从术语到现代 AI|怎么用 AI 基础双语术语表：从术语到现代 AI]]
- [[../../我想通过作者、论文与时间线理解 AI|我想通过作者、论文与时间线理解 AI]]

## 学法

- 先看中文解释，确认它回答什么问题
- 再记英文 canonical term，方便读论文、文档和技术报告
- 不要死记定义，优先把它放进“历史 / 范式 / 模型 / 工程”主线里理解

## 核心术语

### Agent / 智能体

- 指一个能感知环境、做决策并采取行动的系统
- 在现代语境里，它既可以指 RL agent，也可以指 tool-using LLM agent

### Search / 搜索

- 指在状态空间里寻找一条可行或最优路径
- 它是早期 symbolic AI 的关键主线之一

### Planning / 规划

- 指根据目标、状态和动作规则，生成行动步骤
- 它把“会不会搜”推进到“能不能完成任务”

### Knowledge Representation / 知识表示

- 指如何把世界知识编码成系统可操作的结构
- 这是 rules、graphs、logic 与 symbolic systems 的根

### Representation / 表征

- 指模型内部对输入信息形成的中间表达
- 现代深度学习的关键直觉之一就是：好的学习往往来自好的中间表征

### Feature / 特征

- 指帮助模型区分、预测或决策的输入信息
- 传统 ML 更强调 feature engineering，深度学习更强调 learned features

### Generalization / 泛化

- 指模型在没见过的新样本上仍然表现良好
- 它是“训练好”和“真正有用”之间的分界线

### Overfitting / 过拟合

- 指模型把训练数据记太死，导致对新样本表现变差
- 它提醒我们：优化训练误差不等于学到可迁移规律

### Inductive Bias / 归纳偏置

- 指模型或算法内置的偏好与假设
- 没有 bias，学习往往无法高效进行；关键是 bias 是否合适

### Objective Function / 目标函数

- 指我们真正想优化的量
- 在实践里常常通过 `loss` 来近似或分解

### Loss Function / 损失函数

- 指衡量模型输出和目标差距的函数
- 它是训练时最直接被优化的对象

### Optimization / 优化

- 指通过算法不断调整参数，降低损失或提升目标
- 它把“想学什么”转化成“怎么学得动”

### Gradient / 梯度

- 指函数在某点上变化最快的方向信息
- 深度学习训练几乎离不开它

### Backpropagation / 反向传播

- 指利用链式法则把误差信号从输出层传回各层参数
- 它是现代神经网络真正可训练的关键机制之一

### Probability / 概率

- 指对不确定性的形式化描述
- 统计学习、贝叶斯方法、生成模型都以它为核心语言之一

### Information Theory / 信息论

- 研究信息量、熵、编码与通信边界
- 它帮助我们理解压缩、预测、表示与不确定性

### Causality / 因果

- 关注的不只是相关，而是“如果我干预，会发生什么”
- 它在决策、科学解释与鲁棒泛化里尤其重要

### Reinforcement Learning / 强化学习

- 指 agent 通过与环境交互、根据奖励学习策略
- 它特别适合长期回报、序列决策与行动问题

## 关联

- [[基础索引]]
- [[../05-Topics/Probability and Information Theory|Probability and Information Theory]]
- [[../05-Topics/Optimization Basics|Optimization Basics]]
- [[../05-Topics/Neural Networks Basics|Neural Networks Basics]]
- [[../05-Topics/Representation Learning|Representation Learning]]
- [[../03-Paradigms/范式索引|范式索引]]
- [[../../AI 历史主时间线：从符号主义到大模型|AI 历史主时间线：从符号主义到大模型]]
