---
title: Optimization Basics
type: topic
status: active
tags:
  - ai/foundations
  - ai/math
  - ai/training
created: 2026-03-13
updated: 2026-05-16
---

# Optimization Basics

## 一句话定位

`Optimization` 研究如何让模型参数从“当前很差”一步步移动到“对目标更好”，它是训练神经网络、大模型微调、偏好优化和成本控制背后的共同底层机制。

如果说 [[Calculus for ML]] 告诉你“往哪里变”，那么 optimization 关心的是“怎么变、变多快、会不会崩、成本能不能接受”。

## 它解决什么问题

- 把一个模糊的学习目标变成可优化的 `loss/objective`
- 决定参数如何根据梯度、学习率和优化器更新
- 让训练过程在有限算力、有限数据、有限时间内稳定收敛
- 在欠拟合、过拟合、震荡、发散和平台期之间做诊断
- 把“模型效果问题”转译成可执行的训练策略问题

## 核心概念

### Objective / Loss

- `objective` 是优化目标，定义系统到底想让什么变好
- `loss` 是目标的可计算代理，衡量当前预测、生成或决策与期望之间的差距
- 工程上很多问题不是“模型不聪明”，而是 objective 没有对齐真实业务目标

### Gradient Descent

- `gradient` 指向 loss 增长最快的方向
- 训练通常沿着负梯度方向更新参数
- 梯度下降的本质不是“找全局最优”，而是在复杂高维空间里持续寻找更好的区域

### Learning Rate

- `learning rate` 决定每一步走多大
- 太大会震荡甚至发散；太小会训练慢、卡平台期
- 现代训练常配合 warmup、decay、cosine schedule 等策略控制训练节奏

### Batch / Mini-batch / SGD

- `batch gradient descent` 每次用全量数据，稳定但成本高
- `mini-batch` 是深度学习主流选择，在稳定性和效率之间折中
- `SGD` 的随机性会带来噪声，但噪声有时反而帮助模型跳出差的局部区域

### Momentum / Adam / AdamW

- `Momentum` 利用历史更新方向，减少来回震荡
- `Adam` 自适应调整不同参数的步长，是深度学习常用优化器
- `AdamW` 把 weight decay 与梯度更新解耦，在 Transformer 和大模型训练中非常常见

### Regularization

- regularization 不是单纯“惩罚模型”，而是在控制模型不要只记住训练数据
- 常见方式包括 weight decay、dropout、data augmentation、early stopping
- 在大模型时代，regularization 也包括数据质量、训练配方、评估闭环和安全约束

## 和现代 AI 的关系

- `Pretraining`：优化稳定性直接影响大规模训练能否跑完、是否浪费巨额算力
- `Fine-tuning`：学习率、batch size、训练轮数决定模型是适配任务还是灾难性遗忘
- `RLHF / Preference Optimization`：把人类偏好变成可优化目标，本质上仍是 objective 设计与优化稳定性问题
- `LoRA / PEFT`：不是更新全部参数，而是在受限参数空间里优化低秩适配层
- `Cost Engineering`：训练成本、收敛速度、实验次数，都会被优化策略放大或压缩

## 训练不稳定的常见信号

- loss 突然爆炸：可能是 learning rate 太大、梯度爆炸、数据异常或混合精度问题
- loss 长期不降：可能是目标设计、学习率、数据质量、模型容量或实现 bug
- 训练集变好但验证集变差：典型过拟合，需要检查数据、正则、评估切分
- 指标反复震荡：可能是 batch 太小、学习率太高、数据分布不稳
- 线上效果差于离线评估：可能不是优化器问题，而是 objective 与真实场景错位

## 学习目标

学完这一页，你应该能：

- 解释 loss、gradient、learning rate、optimizer 的关系
- 看懂一次训练曲线里最基本的异常信号
- 区分“模型结构问题”“数据问题”“优化问题”和“评估目标问题”
- 理解为什么大模型训练不是简单地“数据越多、参数越大就行”
- 在面试中用优化视角解释训练稳定性、微调策略和成本控制

## 常见误区

- 误区一：优化就是调 learning rate
  实际上 optimization 同时涉及 objective、数据、梯度、参数空间、训练配方和评估闭环。

- 误区二：loss 越低线上效果一定越好
  如果 loss 不是业务目标的好代理，离线 loss 下降可能会伤害真实用户体验。

- 误区三：优化器越高级越好
  优化器只是训练系统的一部分，数据质量、模型结构和目标设计经常更关键。

- 误区四：大模型训练只靠算力
  算力让实验可行，优化策略决定算力是否被有效转化为能力。

## 最小练习

1. 找一张训练曲线，标注 `loss 下降 / 平台期 / 震荡 / 过拟合` 四类信号。
2. 用一句话解释 learning rate 太大和太小分别会发生什么。
3. 比较 `SGD / Momentum / AdamW` 的直觉差异，不需要推公式。
4. 选一个业务任务，写出它的真实目标与可训练 loss 之间可能存在的偏差。

## 面试表达

> Optimization 是把学习目标转成参数更新过程的机制。它不只是调优化器，而是围绕 objective、loss、gradient、learning rate、batch、regularization 和评估反馈构建一个稳定训练系统。现代大模型里的预训练、微调、RLHF、LoRA 和成本控制，本质上都离不开优化问题。

## 相关

- [[Calculus for ML]]
- [[Linear Algebra for ML]]
- [[Probability and Information Theory]]
- [[Neural Networks Basics]]
- [[Representation Learning]]
- [[../../AI-Engineering/07-Topics/Training Stack Overview|Training Stack Overview]]
- [[../../AI-Engineering/07-Topics/训练与推理成本工程|训练与推理成本工程]]
