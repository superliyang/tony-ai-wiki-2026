---
title: Neural Networks Basics
type: topic
status: active
tags:
  - ai/foundations
  - ai/deep-learning
created: 2026-03-13
updated: 2026-05-16
---

# Neural Networks Basics

## 一句话定位

`Neural Network` 是一种可学习的参数化函数族：它通过多层变换，把输入数据映射成输出结果，并在训练中自动调整参数，让这种映射越来越符合目标。

这页的重点不是背公式，而是建立一个判断框架：神经网络到底在学什么、怎么学、为什么会有效、什么时候会失败。

## 它解决什么问题

- 从原始数据中自动学习有用特征，而不是完全依赖人工特征工程
- 用多层非线性组合表达复杂函数
- 通过 [[Optimization Basics]] 把误差反馈转成参数更新
- 把图像、文本、语音、行为序列等不同数据统一成可学习的表示
- 为 Transformer、LLM、多模态模型和 Agent 系统提供底层模型能力

## 核心组件

### Input / Output

- input 是模型看到的外部信号，例如 token、像素、音频帧、用户行为、结构化特征
- output 是模型要产生的结果，例如分类、回归、下一个 token、embedding、动作决策
- 真实项目里，输入输出设计往往比模型结构本身更影响效果上限

### Layer

- layer 是信息变换模块，可以理解为“把一种表示变成另一种表示”
- 多层结构让模型逐步从低级特征走向高级抽象
- CNN、RNN、Transformer 的差别，本质上是 layer 的归纳偏置不同

### Weight / Bias

- weight 和 bias 是模型可学习参数
- 训练过程就是不断调整这些参数，使输出更接近目标
- 参数越多不等于能力越强，还要看数据、结构、训练目标和评估约束

### Activation

- activation 提供非线性能力
- 没有非线性，多层线性网络仍然等价于一个线性变换
- ReLU、GELU 等激活函数是现代深度网络表达能力的重要组成

### Loss

- loss 把模型输出与期望结果之间的差距变成可优化数字
- 分类、回归、语言建模、对比学习、偏好学习会使用不同 loss
- 选错 loss 会让模型学会“指标上的捷径”，而不是你真正想要的能力

### Backpropagation

- backpropagation 用链式法则把输出层误差传回前面各层
- 它回答“每个参数对最终错误贡献了多少”
- 它让深层网络可以被端到端训练

### Optimizer

- optimizer 决定参数如何根据梯度更新
- 常见优化器包括 SGD、Momentum、Adam、AdamW
- 优化器不是万能药，必须和数据、loss、学习率、batch size、模型结构一起看

## 训练主流程

1. `Forward`：输入经过网络，得到预测或生成结果
2. `Loss`：把输出和目标比较，计算损失
3. `Backward`：反向传播，计算各参数梯度
4. `Update`：优化器根据梯度更新参数
5. `Evaluate`：用验证集、业务指标或人工评估检查泛化能力

这个循环看起来简单，但现代 AI 工程的很多复杂性都藏在数据、目标、训练稳定性和评估闭环里。

## 和现代 AI 的关系

- `Transformer` 是一种神经网络架构，只是它用 attention 组织信息流
- `LLM` 是在海量文本和代码上训练出来的大规模神经网络
- `Multimodal Model` 是把文本、图像、音频、视频等模态映射到可共同处理的表示空间
- `RAG` 通常不是替代神经网络，而是给模型外接知识检索与上下文组织能力
- `Agent` 的规划、工具调用和记忆系统，底层仍经常依赖模型的表示、推理和生成能力

## 能力边界

神经网络很强，但不是魔法：

- 它需要足够覆盖目标分布的数据
- 它学习的是 objective 下的统计规律，不天然理解业务价值
- 它可能学到 spurious correlation，也可能对分布外输入失效
- 它的内部表示通常不完全可解释
- 它的输出需要评估、安全、监控和产品约束共同兜底

## 学习目标

学完这一页，你应该能：

- 用“可学习函数”解释神经网络
- 讲清楚 layer、activation、loss、backprop、optimizer 的关系
- 看懂一个训练循环的基本结构
- 解释神经网络和 Transformer、LLM、多模态模型之间的继承关系
- 在工程问题中区分模型能力、数据质量、目标设计和评估闭环

## 常见误区

- 误区一：神经网络就是模拟人脑
  它借用了神经元隐喻，但现代深度学习更应该被理解为可微分函数逼近与表示学习系统。

- 误区二：层数越深越好
  深度带来表达能力，也带来训练、泛化、稳定性和成本问题。

- 误区三：模型会自动学到正确知识
  模型只会在训练目标和数据分布下学习有效模式，不保证事实性、价值对齐或安全性。

- 误区四：会调用模型就懂神经网络
  真正理解神经网络，需要知道输入表示、训练目标、优化过程、泛化风险和部署约束。

## 最小练习

1. 画出一个三层神经网络，标注 input、layer、activation、loss、backprop、optimizer。
2. 用业务语言解释“模型训练”而不是只说“调参数”。
3. 比较 CNN、RNN、Transformer 分别更擅长处理什么结构的信息。
4. 找一个模型效果差的案例，分别从数据、loss、结构、优化、评估五个角度列可能原因。

## 面试表达

> 神经网络可以理解为一个可学习的多层函数。训练时，输入经过 forward 得到输出，loss 衡量输出和目标的差距，backprop 计算每个参数的梯度，optimizer 更新参数。现代 LLM、Transformer 和多模态模型都是在这个框架上扩展出来的，真正的工程难点通常在数据、目标、优化稳定性、评估和部署闭环。

## 相关

- [[Connectionism]]
- [[Representation Learning]]
- [[Optimization Basics]]
- [[Linear Algebra for ML]]
- [[Calculus for ML]]
- [[Probability and Information Theory]]
- [[../../AI-Learning/06-Topics/Foundation Models|Foundation Models]]
- [[../../AI-Learning/06-Topics/Transformer|Transformer]]
- [[../../AI-Learning/06-Topics/Multimodal Models|Multimodal Models]]
