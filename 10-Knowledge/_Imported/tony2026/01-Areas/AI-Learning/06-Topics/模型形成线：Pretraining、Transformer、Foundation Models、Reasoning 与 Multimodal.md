---
title: 模型形成线：Pretraining、Transformer、Foundation Models、Reasoning 与 Multimodal
type: topic
status: active
tags:
  - ai/topic
  - ai/model-line
created: 2026-04-12
updated: 2026-04-13
---

# 模型形成线：Pretraining、Transformer、Foundation Models、Reasoning 与 Multimodal

> 这条线回答的不是“模型名词有哪些”，而是：
> `现代 AI 模型为什么会形成今天这套能力结构，它是怎样一步步长出来的。`

## 这条线为什么重要

如果这条线不清楚，很多判断都会变成碎片：

- 为什么 `Pretraining` 会成为现代模型能力底座
- 为什么 `Transformer` 能成为统一架构
- 为什么少数 [[Foundation Models]] 会变成上层系统的公共能力层
- 为什么后来会出现 [[Reasoning Models]]、[[Multimodal Models]]、[[Long Context]]
- 为什么很多差异并不只是“参数更多”，而是训练目标、后训练、数据结构和 product surface 发生了变化

这条线更像 `能力形成史 + 架构演化史 + 产品边界史`。

## 一条最简主线

`历史/范式 -> Pretraining -> Transformer -> Scaling -> Foundation Models -> Post-training / Alignment -> Reasoning -> Multimodal -> Long Context`

## 一、Pretraining：底座能力从哪里来

核心页：

- [[Pretraining]]
- [[Foundation Models]]
- [[../../AI-Foundations/专题总览|AI-Foundations]]

Pretraining 解决的是：

- 让模型先获得广义世界知识
- 让模型学会语言/代码/符号模式的统计结构
- 给后续 instruction-following、tool use、reasoning 留出能力底盘

如果没有这一步，很多“会话中的聪明”都无从谈起。

要点：

- 它先学的是 `distribution`，不是任务清单
- 它带来的是 `通用表征能力`，不是可靠产品能力
- 它解释了为什么 foundation model 往往能一模多用

最容易混淆的边界：

- `预训练学到能力` 不等于 `用户可以直接稳定使用`
- `知识记住了` 不等于 `推理可靠`
- `benchmark 强` 不等于 `上线即稳`

## 二、Transformer：为什么现代模型能力会收敛到这类架构

核心页：

- [[Transformer]]
- [[Foundation Models]]

Transformer 的关键意义不是一个“模型名词”，而是它统一了：

- 大规模并行训练
- 长序列建模
- 文本、图像、语音等 token 化后的统一处理方式
- 后续 scaling、instruction tuning、multimodal 扩展的公共骨架

你可以把它理解为：

`不是它单独创造了智能，而是它给大规模学习提供了一个足够通用、足够可扩展的容器。`

## 三、Foundation Models：为什么能力集中到少数底层模型

核心页：

- [[Foundation Models]]
- [[Alignment]]
- [[Synthetic Data]]

当 `Pretraining + Transformer + Scaling` 结合起来后，会出现一个重要结构变化：

- 少数基础模型成为上层产品和系统的通用能力供应层
- 大量应用不再自己训练模型，而是在基础模型上做 `post-training / alignment / productization`

这一步改变了整个产业组织方式：

- 模型厂商负责底座
- 产品团队负责 workflow、tool、UX 和运营边界
- 平台团队负责 API、serving、evaluation、cost 和治理

这也是为什么你在看公司时，经常要区分：

- 它是在做 `model company`
- 还是在做 `model-native product`
- 还是在做 `AI infrastructure / platform`

## 四、Post-training / Alignment：从“会”到“可用”

相关页：

- [[Alignment]]
- [[Evaluation]]
- [[AI Safety]]

Pretraining 得到的是“原始能力”，但人真正能用的系统通常还需要：

- instruction-following
- preference shaping
- safety shaping
- domain adaptation
- style/control alignment

这一步的关键不是“让模型更大”，而是“让模型更可控、更可用、更适配产品面”。

常见误区：

- 把 alignment 理解成单纯安全过滤
- 把 post-training 理解成小修小补
- 忽略 eval 在 post-training 之后的角色

实际上，`post-training 决定产品气质，eval 决定上线边界。`

## 五、Reasoning：为什么行业会从“会说”转向“会想”

核心页：

- [[Reasoning Models]]
- [[Evaluation]]
- [[Coding Agents]]

Reasoning 这一段的关键变化是：

- 大家不再只追求 fluent output
- 而是追求更好的任务分解、步骤稳定性、复杂问题求解能力

这会影响很多上层判断：

- benchmark 怎么看
- latency / cost 怎么权衡
- coding / planning / tool-use 场景应该选什么模型
- 什么时候该把更多控制权交给 runtime，而不是交给模型本身

这一步让面试里一个很重要的问题变得清晰：

`模型能力增强，不一定意味着系统复杂度下降；很多时候反而要求更强的 eval、route 和 release gate。`

## 六、Multimodal：为什么 foundation model 开始统一更多输入输出

核心页：

- [[Multimodal Models]]
- [[Voice、Realtime 与语音工作流]]
- [[OCR 与 Document AI]]
- [[Browser Agents 与 Computer Use]]

Multimodal 的真正含义不是“模型能看图了”，而是：

- 能力边界从文本扩展到图像、语音、视频、界面、文档
- 产品 surface 从 chat 扩展到实时交互、文档流、computer use、agentic workflow
- 评测维度和安全边界变得更复杂

一旦你理解了这点，就会知道：

- [[OCR 与 Document AI]] 不是边缘分支，而是多模态落地的重要形态
- [[Voice、Realtime 与语音工作流]] 是更自然的人机接口方向
- [[Browser Agents 与 Computer Use]] 则把视觉理解和动作执行接到一起

## 七、Long Context：为什么“记得更多”不等于“理解更深”

核心页：

- [[Long Context]]
- [[RAG]]
- [[上下文工程]]

Long Context 让模型处理更长输入，但它不自动解决：

- 检索精度
- 事实一致性
- 上下文污染
- 工具调用决策
- 长任务状态管理

所以它常常不是替代 [[RAG]]，而是重新定义：

- 什么该放进上下文
- 什么该保留在外部系统
- 什么应交给 memory / retrieval / tool

## 八、这条线最容易混淆的边界

### 1. 模型能力 vs 系统能力

- 模型会推理，不代表系统会交付结果
- 模型会看图，不代表产品已具备稳定 multimodal workflow

### 2. 架构统一 vs 产品统一

- Transformer 统一了底层表示方式
- 但产品层仍然会按任务边界分化

### 3. 能力增强 vs 运营简化

- 模型越强，往往越需要更精细的 route、eval、cost 和安全设计

## 九、建议学习顺序

1. [[../../AI-Foundations/专题总览|AI-Foundations]]
2. [[Pretraining]]
3. [[Transformer]]
4. [[Foundation Models]]
5. [[Alignment]]
6. [[Reasoning Models]]
7. [[Multimodal Models]]
8. [[Long Context]]
9. [[OCR 与 Document AI]]
10. [[Voice、Realtime 与语音工作流]]
11. [[Browser Agents 与 Computer Use]]

## 十、这条线在面试里能回答什么

- 为什么 foundation models 会成为 AI 产业的能力底座
- 你如何理解 reasoning、multimodal、long context 之间的关系
- 为什么模型能力升级后，系统工程反而更重要
- 你如何判断一个 AI 产品是在“模型红利”还是“系统红利”

## 关联

- [[AI 五条主干专家工作台]]
- [[AI 领域知识点总纲：点、线、面与层]]
- [[AI 主题索引]]
- [[../07-Maps/AI 知识点点线面图|AI 知识点点线面图]]
- [[Foundation Models]]
- [[Reasoning Models]]
- [[Multimodal Models]]
- [[Long Context]]
