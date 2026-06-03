---
title: Frameworks (PyTorch-JAX-TensorFlow)
type: topic
status: learning
tags:
  - ai/engineering
  - ai/frameworks
created: 2026-03-13
updated: 2026-03-28
---

# Frameworks (PyTorch-JAX-TensorFlow)

## 为什么框架选型不是“语法偏好”

框架决定的不只是代码长什么样，还决定：

- 研究试验速度
- 编译和优化空间
- 分布式训练路线
- 调试难度
- 部署与生产衔接方式
- 团队招聘与知识积累方式

所以框架选型本质上是在选一整套工程生态。

## 它在训练栈里的位置

框架连接三层：

- 上层：模型表达、实验、研究迭代
- 中层：自动求导、编译、并行、checkpoint
- 下层：CUDA / XLA / TPU / Metal / runtime / deployment stack

这也是为什么同一个模型，在不同框架里的工程体验差异会很大。

## 三个主流框架的粗粒度判断

### `PyTorch`

最适合：

- 快速研究迭代
- 大模型训练主线
- 和开源生态深度配合

优势：

- 研究与工程平衡最好
- 社区最大
- distributed、FSDP、TorchTitan、生态工具都很强

代价：

- 工程自由度高，也意味着团队更需要规范
- 复杂系统里容易积累“隐式习惯”

### `JAX`

最适合：

- 编译导向优化
- 函数式、变换式表达
- TPU / XLA 导向的系统优化

优势：

- `jit`、`vmap`、`pmap`、`pjit` 这类变换能力很强
- 很适合系统化做并行和编译优化

代价：

- 团队心智门槛通常更高
- 上手和调试体验对很多工程团队不如 PyTorch 直觉

### `TensorFlow`

最适合：

- 既有 TensorFlow 资产很重的组织
- 特定生产部署链路已经成熟的团队

优势：

- 历史生产化经验深
- tooling 和 serving 体系成熟度高

代价：

- 在当前前沿大模型训练主线上存在感较弱
- 新一代 LLM 研究和训练生态没有 PyTorch 活跃

## 真正值得比较的 6 个维度

### 1. 研究友好性

- 改模型方便吗
- 调试中间状态方便吗
- 新实验迭代快吗

### 2. 编译与优化能力

- 能不能自动做图优化
- 是否容易把 Python 代码压进高性能执行路径

### 3. 分布式训练生态

- 和 `DDP`、`FSDP`、ZeRO、TP、PP 等路线衔接如何
- 社区里有没有成熟实践和模板

### 4. 部署与生产化能力

- 训练和推理是否能顺畅衔接
- artifacts、export、serving 生态是否成熟

### 5. 调试与可解释性

- 出错时是否容易定位
- 中间张量和执行路径是否容易看清

### 6. 团队与生态成本

- 新人是否容易上手
- 文档、教程、社区支持是否充足
- 团队现有代码资产是否能延续

## 今天的大模型工程为什么大多偏向 PyTorch

因为它在几个关键点上形成了组合优势：

- 研究表达足够灵活
- 大模型训练生态最成熟
- 和 Hugging Face、DeepSpeed、Megatron、vLLM 等外部生态衔接紧
- 社区案例最丰富

这不代表 `PyTorch` 在所有维度都赢，而是它在“研究 + 训练 + 生态联动”上最均衡。

## 什么时候应该认真考虑 JAX

- 你非常重视编译优化和系统化 parallel transforms
- 你所在组织对 TPU / XLA 生态很熟
- 你愿意接受更高的框架心智门槛来换更统一的变换体系

## 什么时候 TensorFlow 仍然有价值

- 组织已经有重资产沉淀
- serving、部署、训练工具链都围绕 TensorFlow 建好了
- 当前目标不是追赶最新 LLM 训练主线，而是稳定继承已有生产体系

## 常见误区

- 只看 benchmark，不看组织成本
- 只看训练，不看推理与部署衔接
- 只看 API 语法，不看编译和分布式生态
- 以为“框架选型错了”就一定要全量迁移

## 一个更成熟的选型心智

先问：

- 你更像研究团队、平台团队还是产品团队
- 你更在意实验速度、系统优化还是生产继承
- 你是否已经有大量现成代码和人才路径

再问：

- 框架是否能和你的 distributed、eval、deployment 路线自然接起来

## 学习这页时最该记住什么

- 框架选型是团队工程能力的放大器
- 真正重要的不是“谁最好”，而是谁更适合当前团队、硬件和训练路线

## 推荐怎么往下读

1. [[Training Stack Overview]]
2. [[Distributed Training]]
3. [[Open-Source Ecosystem]]
4. [[Model Registry and Deployment]]
5. [[../02-Frameworks/PyTorch|PyTorch]]
6. [[../02-Frameworks/JAX|JAX]]
7. [[../02-Frameworks/TensorFlow|TensorFlow]]

## 相关主题

- [[Training Stack Overview]]
- [[Distributed Training]]
- [[Open-Source Ecosystem]]
- [[Model Registry and Deployment]]

## 相关实体

- [[../02-Frameworks/PyTorch|PyTorch]]
- [[../02-Frameworks/JAX|JAX]]
- [[../02-Frameworks/TensorFlow|TensorFlow]]
- [[../02-Frameworks/Hugging Face Ecosystem|Hugging Face Ecosystem]]

## 资料

- [PyTorch](https://docs.pytorch.org/docs/main/)
- [JAX Documentation](https://docs.jax.dev/en/latest/)
- [TensorFlow](https://www.tensorflow.org/)
