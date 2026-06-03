---
title: Calculus for ML
type: topic
status: active
tags:
  - ai/foundations
  - ai/math
created: 2026-03-13
updated: 2026-05-16
---

# Calculus for ML

## 一句话定位

`Calculus for ML` 解释模型如何通过误差反向调整参数。你不需要一开始推完所有公式，但必须理解导数、梯度和链式法则，否则很难真正理解训练、backpropagation、optimization 和 fine-tuning。

## 它解决什么问题

机器学习训练需要回答：

- 模型现在错在哪里
- 哪些参数应该变大或变小
- 每个参数对 loss 的影响有多大
- 深层网络的误差信号如何传回前面层

微积分提供“变化率”和“方向”的语言。

## 核心概念

### 导数

导数描述一个变量变化时，另一个变量变化有多快。

直觉：

- 导数为正：往右走，函数变大
- 导数为负：往右走，函数变小
- 导数绝对值大：变化很敏感

### 偏导数

模型参数很多，每个参数都可能影响 loss。

偏导数回答：

> 只改变某一个参数时，loss 会怎么变？

### 梯度

梯度是所有偏导数组成的向量，指出函数增长最快的方向。

训练时通常沿着梯度反方向走，让 loss 下降。

### 链式法则

链式法则解释复合函数的导数如何计算。

神经网络是层层复合的函数：

```text
input -> layer1 -> layer2 -> ... -> loss
```

backpropagation 本质上就是高效使用链式法则。

### Jacobian 与 Hessian

初学不必深挖，但要知道：

- Jacobian 描述多输入多输出的局部变化
- Hessian 描述二阶曲率
- 曲率影响优化稳定性和收敛速度

## 和现代 AI 的关系

### Backpropagation

Backpropagation 不是神秘算法，而是链式法则在神经网络上的系统应用。

它从 loss 开始，把梯度逐层传回，更新每层参数。

### Gradient Descent

Gradient descent 使用梯度决定参数更新方向。

直觉：

```text
new parameter = old parameter - learning rate × gradient
```

### Fine-tuning

Fine-tuning 仍然依赖梯度，只是训练目标、数据和可更新参数范围不同。

例如：

- full fine-tuning：更新全部参数
- LoRA：只更新低秩适配参数
- prompt tuning：更新较少的软提示参数

### Vanishing / Exploding Gradient

深层网络中，梯度可能逐层变小或变大。

这解释了为什么现代网络需要：

- normalization
- residual connection
- careful initialization
- optimizer tricks

## 学习目标

达到可用水平时，你应该能：

- 解释导数、偏导数、梯度
- 解释为什么训练要沿梯度反方向走
- 解释链式法则和 backpropagation 的关系
- 理解 learning rate 为什么重要
- 解释梯度消失 / 爆炸的直觉
- 看懂训练曲线异常时可能和梯度有关

## 常见误区

- 误区 1：以为必须先会完整数学推导才能学深度学习
- 误区 2：把 backpropagation 当黑盒，不理解链式法则
- 误区 3：只看 loss，不看梯度稳定性
- 误区 4：不知道 learning rate 太大会震荡，太小会慢
- 误区 5：忽略 normalization 和 residual 对训练稳定性的作用

## 最小练习

1. 画一个简单二次函数，标出梯度方向
2. 手算一个简单复合函数的链式法则
3. 解释 `loss -> output -> hidden -> weight` 的反向传播路径
4. 对比 learning rate 太大和太小时训练曲线会怎样
5. 用一句话解释为什么 residual connection 有助于训练深层网络

## 面试表达

如果被问“为什么微积分对神经网络重要”，可以这样答：

> 神经网络训练要知道每个参数对 loss 的影响，导数和梯度提供了这个变化方向；网络是多层复合函数，链式法则让误差信号能从 loss 逐层传回前面的参数，这就是 backpropagation 的核心。

## 相关

- [[Optimization Basics]]
- [[Neural Networks Basics]]
- [[Linear Algebra for ML]]
- [[../../AI-Learning/06-Topics/Transformer|Transformer]]
- [[../../AI-Engineering/07-Topics/Training Stack Overview|Training Stack Overview]]
