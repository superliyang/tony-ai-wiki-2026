---
title: RLHF and Preference Optimization
type: topic
status: learning
tags:
  - ai/engineering
  - ai/alignment
created: 2026-03-13
updated: 2026-03-28
---

# RLHF and Preference Optimization

## 为什么这页现在必须学深

现代大模型不只是靠 pretraining 决定质量，产品体验、拒答风格、推理展开方式、工具调用边界，越来越多来自 post-training。

所以 `RLHF`、`DPO`、constitutional / preference-based optimization 不是“最后加一道工序”，而是行为工程的主战场。

## 一条典型 post-training 链路

可以粗略拆成：

1. `SFT`：先把模型拉到“会按指令回答”的区域
2. preference data collection：收集偏好对比或评分
3. reward modeling 或 direct preference objective：把偏好转成优化信号
4. policy optimization：用 RLHF / PPO，或直接用 `DPO` 一类方法优化
5. safety / product eval：验证 helpfulness、harmlessness、style 和 refusal 行为
6. release gate：决定是否能上线或进入下一轮训练

## `RLHF` 真正在解决什么

`RLHF` 的目标不是让模型更会续写，而是让模型更接近：

- 人类偏好的回答风格
- 产品所需的行为边界
- 可接受的安全和拒答策略
- 更稳定的工具调用与任务完成模式

这也是为什么对齐阶段经常比模型参数量更直接影响“用户觉得好不好用”。

## 从工程上怎么区分几条主路线

### `SFT`

适合：

- 建立基础 instruction-following 能力
- 把 base model 拉进产品可用区间

风险：

- 只会模仿示例分布
- 很难仅靠 SFT 解决复杂偏好权衡

### `RLHF` / PPO-style optimization

适合：

- 需要显式 reward signal
- 希望对行为进行更细控制

代价：

- 训练更复杂
- 对 reward model 质量高度敏感
- 调参成本和不稳定性更高

### `DPO` 等 preference optimization

适合：

- 想绕开显式 reward model 和在线采样复杂度
- 希望更简单地把偏好数据直接转成优化目标

代价：

- 仍然高度依赖 preference data 质量
- 容易把“偏好”误当成“真实性”或“鲁棒性”

### `Constitutional AI` / AI feedback style approaches

适合：

- 想减少纯人工标注负担
- 希望把行为原则显式化

代价：

- constitution 本身会成为产品和价值选择
- 容易形成更“整齐”的风格偏置

## 真正难的不是算法名词，而是数据和评测

### 偏好数据的难点

- 标注主观性强
- 审核标准随时间漂移
- 不同场景偏好冲突
- pairwise 数据容易忽略“差多少”

### reward / preference signal 的难点

- 好回答和安全回答不总一致
- 用户喜欢和组织允许不总一致
- 风格偏好可能压制信息密度或推理透明度

### 评测的难点

post-training 后必须同步评估：

- helpfulness
- instruction following
- over-refusal
- jailbreak robustness
- regression on core capabilities

## 常见失败模式

### 1. Reward hacking

模型学会了讨好 reward，而不是完成真实任务。

### 2. Over-refusal

安全收紧以后，模型在无风险场景也大量拒答。

### 3. Style collapse

模型回答变得过度同质化、模板化、过于官腔。

### 4. Capability regression

alignment 更强了，但代码、推理或 long-form quality 下降。

### 5. Preference overfitting

模型只学会一小群标注者或某批 prompt 的偏好。

## 学这一页要形成的判断力

### 判断 1：这是能力问题还是对齐问题

- 不会解题，是基础能力问题
- 会解题但总以不理想方式回答，往往是 post-training 问题

### 判断 2：这是数据问题还是 objective 问题

- 偏好样本不稳定，再换损失函数也难救
- objective 设计不对，再多数据也可能把模型推歪

### 判断 3：这轮 post-training 有没有把产品变好

不要只看单项 benchmark，要同时看：

- 用户体验
- 关键任务成功率
- 安全门槛
- 拒答与误伤
- regression cost

## 推荐怎么连着读

1. [[Synthetic Data]]
2. [[Safety Evaluation]]
3. [[Evaluation and Benchmarks]]
4. [[Online Evals、Human Feedback 与 Annotation]]
5. [[AI Security Evaluation 与 Red Teaming]]

## 相关主题

- [[Training Stack Overview]]
- [[Synthetic Data]]
- [[Safety Evaluation]]
- [[Evaluation and Benchmarks]]
- [[Online Evals、Human Feedback 与 Annotation]]
- [[AI Security Evaluation 与 Red Teaming]]

## 资料

- [InstructGPT](https://arxiv.org/abs/2203.02155)
- [Direct Preference Optimization](https://arxiv.org/abs/2305.18290)
- [Anthropic Constitutional AI](https://www.anthropic.com/research/claudes-constitution)
- [Constitutional AI Paper](https://www-cdn.anthropic.com/files/4zrzovbb/website/7512771452629584566b6303311496c262da1006.pdf)
