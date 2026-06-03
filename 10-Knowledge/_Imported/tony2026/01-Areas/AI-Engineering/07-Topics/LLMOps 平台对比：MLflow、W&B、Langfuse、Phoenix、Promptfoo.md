---
title: LLMOps 平台对比：MLflow、W&B、Langfuse、Phoenix、Promptfoo
type: topic
status: learning
tags:
  - ai/engineering
  - ai/llmops
  - ai/observability
  - ai/comparison
created: 2026-04-03
updated: 2026-04-03
---

# LLMOps 平台对比：MLflow、W&B、Langfuse、Phoenix、Promptfoo

## 这页解决什么问题

很多团队会把这些平台放进同一张采购清单里比较，但它们其实并不都在回答同一个问题。

真正更有用的比较方式是：

- 你的控制点想放在哪里
- 你现在最缺的是哪一层
- 这些平台是互斥替代，还是可以组合

## 一张先抓住差异的表

| 平台 | 最强控制点 | 最像什么 | 最适合解决什么 | 最容易补不上的地方 |
| --- | --- | --- | --- | --- |
| `MLflow` | tracking + registry + lifecycle governance | 实验与资产治理底座 | 模型、prompt、版本、registry、deployment 统一管理 | agent trace 与交互诊断不算它最强项 |
| `Weights & Biases` | experiment workbench + team collaboration | 实验台和团队工作台 | 训练实验、评测看板、协作分析 | LLM app 里的 prompt trace 和 release 对比不一定最顺手 |
| `Langfuse` | prompt / trace / dataset / release comparison | LLM app 观测与版本闭环 | LLM / agent 应用的 prompt、trace、score、release | 更底层的模型资产治理不是主战场 |
| `Phoenix` | observability + eval debugging | trace 调试台 | trace 可视化、OTel-friendly 观测、失败诊断 | 不是最完整的 lifecycle governance 平台 |
| `Promptfoo` | pre-release eval + CI + red team | 发布前门禁 | 回归测试、红队、离线评测、CI gate | 生产 trace 与长期运营观测不是主轴 |

## 最重要的一句判断

这 5 个平台不是严格的一选一关系。

更常见的现实是：

- `MLflow / W&B` 负责实验与资产层
- `Langfuse / Phoenix` 负责运行时观测与诊断层
- `Promptfoo` 负责发布前门禁层

## 它们分别最值得学什么

### MLflow

最值得学的是：

- tracking
- registry
- lifecycle governance
- 把实验、版本和部署对象收在同一治理面里

它更像“平台底座”，不是单点 agent trace 工具。

### Weights & Biases

最值得学的是：

- 实验协作
- 团队 workbench
- metrics / run 对比
- 面向训练和评测的工作流组织方式

它更像“实验工作台”。

### Langfuse

最值得学的是：

- prompt 版本
- trace
- dataset
- score
- release comparison

它特别适合回答：

- 这个 prompt / agent 版本上线后表现有没有变好
- 哪类 trace 在回归

### Phoenix

最值得学的是：

- trace debugging
- eval diagnosis
- OTel-friendly integration

它特别适合“已经有执行数据，但不知道为什么系统在失败”。

### Promptfoo

最值得学的是：

- 发布前回归
- 红队
- CI gate
- prompt / model / config 的离线比较

它很强，但更偏“上线前门禁”，不是整个运营平台。

## 更实用的选型思路

### 如果你最缺的是治理底座

先看：

- [[../../AI-Learning/09-Systems/MLflow|MLflow]]
- [[Enterprise MLOps 与 LLMOps Vendor Tradeoffs]]

### 如果你最缺的是 LLM app / agent trace 可见性

先看：

- [[../../AI-Learning/09-Systems/Langfuse|Langfuse]]
- [[../../AI-Learning/09-Systems/Arize Phoenix|Arize Phoenix]]
- [[LLMOps、AgentOps 与 Observability]]

### 如果你最缺的是发布前 eval gate

先看：

- [[../../AI-Learning/09-Systems/Promptfoo|Promptfoo]]
- [[Prompt Registry、Datasets 与 Evals]]
- [[Online Evals、Human Feedback 与 Annotation]]

### 如果你已经有实验平台，但没有线上 agent diagnosis

常见组合会更像：

- `MLflow + Langfuse`
- `W&B + Langfuse`
- `W&B + Phoenix + Promptfoo`

## 最常见的 4 个误区

### 误区 1：只买 observability，不建 eval set

这样你能看到 trace，但很难真正做 release decision。

### 误区 2：只做 offline eval，不看线上 trace

这样你知道谁在理论上更好，但不知道线上为什么坏。

### 误区 3：把 Promptfoo 当成完整 LLMOps 平台

它更像门禁层，不是全栈治理面。

### 误区 4：把 Langfuse / Phoenix 当成 registry 平台

它们更偏观测与诊断，不是模型资产治理的完整底座。

## 读完这页后你应该能自己回答

- 你现在到底缺的是 `tracking`、`registry`、`trace`、`release` 还是 `eval gate`
- 哪些平台是互补，而不是互斥
- 你当前阶段最应该先补哪一个控制点

## 推荐继续往下读

1. [[LLMOps、AgentOps 与 Observability]]
2. [[Experiment Tracking]]
3. [[Evaluation and Benchmarks]]
4. [[Prompt Registry、Datasets 与 Evals]]
5. [[Online Evals、Human Feedback 与 Annotation]]
6. [[Enterprise MLOps 与 LLMOps Vendor Tradeoffs]]
7. [[../08-Maps/MLOps 与 LLMOps 工程图|MLOps 与 LLMOps 工程图]]

## 关联

- [[../../AI-Learning/09-Systems/MLflow|MLflow]]
- [[../../AI-Learning/09-Systems/Weights & Biases Platform|Weights & Biases Platform]]
- [[../../AI-Learning/09-Systems/Langfuse|Langfuse]]
- [[../../AI-Learning/09-Systems/Arize Phoenix|Arize Phoenix]]
- [[../../AI-Learning/09-Systems/Promptfoo|Promptfoo]]
- [[LLMOps、AgentOps 与 Observability]]
- [[Enterprise MLOps 与 LLMOps Vendor Tradeoffs]]
