---
title: 什么时候该上 Langfuse、Phoenix、Promptfoo，什么时候 MLflow 与 W&B 更合适
type: guide
status: active
updated: 2026-04-03
---

# 什么时候该上 Langfuse、Phoenix、Promptfoo，什么时候 MLflow 与 W&B 更合适

## 一句先判断

如果你缺的是 `实验治理底座`，先看 `MLflow / W&B`。

如果你缺的是 `LLM / agent 运行时观测和诊断`，先看 `Langfuse / Phoenix`。

如果你缺的是 `发布前回归和红队门禁`，先看 `Promptfoo`。

## 最实用的判断表

| 你当前最痛的点 | 更该先补什么 | 为什么 |
| --- | --- | --- |
| 实验、版本、registry、生命周期治理乱 | `MLflow / W&B` | 先把资产和实验面收起来 |
| 线上 agent / LLM app 不知道为什么坏 | `Langfuse / Phoenix` | 先把 trace、score、诊断立起来 |
| 上线前没法做回归、红队和 CI gate | `Promptfoo` | 先把门禁补起来 |
| 训练实验和 app 运营都要兼顾 | `MLflow / W&B` + `Langfuse / Phoenix` | 底座和运行时不是同一层 |
| 已经有 observability，但没有 release 纪律 | `Promptfoo` 或 dataset/eval pipeline | trace 不等于 gate |

## 什么时候更该先上 MLflow / W&B

- 你现在最大的问题是实验和资产治理
- 团队还在训练、评测、registry、版本管理阶段
- 你需要一个实验工作台或治理底座

这时候不要误以为：

- `Langfuse` 可以单独承担全部生命周期治理
- `Promptfoo` 可以替代实验底座

## 什么时候更该先上 Langfuse / Phoenix

- 你已经在做 LLM app / agent
- 真正痛点是 prompt、trace、tool call、retrieval、failure diagnosis
- 你需要知道“线上为什么坏”，不是只知道“离线分数多少”

更细一点：

- 更想做 prompt / trace / release comparison：先看 `Langfuse`
- 更想做 trace debugging / observability diagnosis：先看 `Phoenix`

## 什么时候 Promptfoo 就够了

- 你当前最急的是上线前回归
- 想把 prompt / RAG / agent regression 放进 CI
- 团队先需要“别把明显坏版本放出去”

这种阶段，`Promptfoo` 很可能比先搭一整套大平台更划算。

但如果你要解决的是：

- 生产 trace 观测
- 线上 failure diagnosis
- 长周期数据回流

那它就不够了。

## 最常见的 4 个误区

### 误区 1：先买最全的平台

错。

真正更稳的是先补你最缺的控制点。

### 误区 2：有 trace 就等于有治理

错。

trace 解决“看见”，不自动解决“是否该发布”。

### 误区 3：有 offline eval 就等于可以稳定上线

错。

你仍然需要线上观测和失败诊断。

### 误区 4：Langfuse / Phoenix / Promptfoo 是彼此完全替代

也错。

很多团队更像是：

- `MLflow / W&B` 管底座
- `Langfuse / Phoenix` 管运行时
- `Promptfoo` 管发布前门禁

## 读完这页后你应该能自己回答

- 你现在到底最缺底座、观测还是门禁
- `Langfuse`、`Phoenix`、`Promptfoo` 该先上哪个
- 什么时候该回到 `MLflow / W&B` 这种更偏实验治理的平台

## 推荐继续往下读

1. [[./AI-Engineering/07-Topics/LLMOps 平台对比：MLflow、W&B、Langfuse、Phoenix、Promptfoo|LLMOps 平台对比：MLflow、W&B、Langfuse、Phoenix、Promptfoo]]
2. [[./AI-Engineering/07-Topics/Enterprise MLOps 与 LLMOps Vendor Tradeoffs|Enterprise MLOps 与 LLMOps Vendor Tradeoffs]]
3. [[./AI-Engineering/07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]]
4. [[./AI-Engineering/07-Topics/Prompt Registry、Datasets 与 Evals|Prompt Registry、Datasets 与 Evals]]
5. [[./AI-Engineering/07-Topics/Online Evals、Human Feedback 与 Annotation|Online Evals、Human Feedback 与 Annotation]]

## 关联

- [[AI 决策导航|AI 决策导航]]
- [[./AI-Engineering/07-Topics/LLMOps 平台对比：MLflow、W&B、Langfuse、Phoenix、Promptfoo|LLMOps 平台对比：MLflow、W&B、Langfuse、Phoenix、Promptfoo]]
