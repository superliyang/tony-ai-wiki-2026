---
title: 大模型与 AI 全景回答母版
type: playbook
status: active
created: 2026-04-29
updated: 2026-04-29
---

# 大模型与 AI 全景回答母版

> 用在所有“你怎么看大模型 / AI 系统 / Agent / RAG / 训练 / 工程 / 落地”的开放题。
> 目标是让回答天然带着从底层到业务的纵深，而不是散点式罗列名词。

## 母版一句话

我会把大模型系统分成四个层次来看：

`能力从哪里来 -> 能力如何被包装成系统 -> 系统如何被验证和治理 -> 最后如何产生业务结果`

展开就是：

`模型原理 / 数据训练 / 后训练 / 推理服务 / RAG 与 Agent / Eval 与 Release / Security 与 Governance / Rollout 与 ROI`

## 30 秒版

“我看大模型不会只看模型本身，而会看完整链路。底层是 Transformer、pretraining、SFT、RLHF/DPO 这些能力形成机制；中间是 inference serving、model routing、RAG、tool use、agent runtime 这些工程系统；再往上是 eval harness、release gate、安全合规和事故回滚；最后是产品 workflow、adoption 和 ROI。面试里如果只讲模型名，很容易漏掉真正决定成败的东西：数据、评测、治理和上线机制。”

## 2 分钟版

“如果从上帝视角看 AI 面试，我会分十层：

第一层是基础原理，比如 token、embedding、attention、loss、sampling，回答模型为什么能工作、为什么会错。

第二层是模型形成，包括 pretraining、数据质量、SFT、RLHF、DPO，回答能力从哪里来，以及为什么同一个 base model 经过后训练后会变成可用助手。

第三层是推理与服务，包括 KV Cache、batching、routing、fallback、SLO 和成本，回答模型如何变成生产服务。

第四层是数据与知识，包括 RAG、context、memory、权限和数据更新，回答模型不知道或不可信时怎么办。

第五层是 Agent 与执行，包括 tool use、workflow、planning、sandbox、approval，回答模型如何安全地做事。

第六层是评测与上线，包括 eval harness、regression、shadow、gray release、A/B、rollback，回答怎么证明系统真的变好。

第七层是安全治理，包括 prompt injection、PII、多租户、审计、合规、red teaming，回答失败边界和责任边界。

最后是产品和组织，包括 workflow fit、ROI、adoption、owner、团队机制。高级面试考的不是你会不会接 API，而是你能不能把这些层串成一个可靠、可维护、可增长的系统。”

## 5 分钟白板版

### 1. 先画能力形成链

```text
Raw Data -> Pretraining -> Base Model -> SFT -> Preference Optimization -> Safety Tuning -> Product Model
```

讲清：

- pretraining 负责通用能力
- SFT 负责指令跟随
- preference optimization 负责偏好、风格和对齐
- safety tuning 负责风险边界
- 数据质量贯穿所有阶段

### 2. 再画系统执行链

```text
User / Workflow
  -> Intent / Policy
  -> Context / RAG / Memory
  -> Model Routing
  -> Tool / Agent / Workflow
  -> Guardrail / Approval
  -> Response / Action / Artifact
```

讲清：

- 用户不是直接面对模型，而是面对一个系统
- RAG、memory、tool use、workflow 都是补模型边界的工程层
- 高风险动作必须有 approval、audit 和 rollback

### 3. 再画评测上线链

```text
Offline Eval -> Regression Suite -> Shadow -> Gray Release -> A/B -> Full Rollout -> Incident Review
```

讲清：

- demo 不能代表生产质量
- bad case 要回灌成 regression
- prompt、model、data、tool 都要版本化
- release gate 是 AI 系统的生命线

### 4. 最后画业务闭环

```text
Problem -> Workflow Fit -> Pilot -> Adoption -> ROI -> Governance -> Team Mechanism
```

讲清：

- ROI 不能只看 token 调用量
- adoption 不等于长期价值
- AI 项目成熟后要沉淀成团队机制，而不是靠个人英雄主义

## 开放题通用结构

### 问：“你怎么看大模型技术栈？”

回答顺序：

1. 能力形成：pretraining / SFT / RLHF / DPO
2. 能力释放：inference / routing / RAG / agent
3. 生产可靠：eval / observability / release gate
4. 风险治理：security / privacy / audit / compliance
5. 业务闭环：workflow / adoption / ROI

### 问：“你如何设计一个 AI 系统？”

回答顺序：

1. 目标和失败边界
2. 用户和 workflow
3. 模型和数据策略
4. RAG / tool / agent 选择
5. 推理、成本、延迟、容量
6. eval、灰度、回滚
7. 安全、权限、审计
8. rollout、指标、复盘

### 问：“你如何判断一个 AI 候选人是否资深？”

回答顺序：

1. 会不会从业务问题出发
2. 会不会讲底层原理和失败根因
3. 会不会做系统分层
4. 会不会讲 tradeoff
5. 会不会讲 eval / release / incident
6. 会不会把经验机制化

## 回答时最强的连接句

- `我先从底层能力说起，再往工程和业务落地收。`
- `这个问题不能只看模型，要看模型、数据、系统、评测和治理的组合。`
- `如果只是 demo，我会这么做；如果要生产上线，我会多加三层控制。`
- `这里真正的 tradeoff 是质量、成本、延迟和风险，不是单纯哪个方案更高级。`
- `我会把 bad case 变成 regression，而不是只修一次 prompt。`
- `这个方案上线前，我最关心的是门禁指标和回滚路径。`

## 常见掉分表达

- `我们直接用大模型解决。`
- `RAG 可以解决幻觉。`
- `Agent 可以自动完成复杂任务。`
- `多 Agent 更强。`
- `模型换强一点就好了。`
- `上线后看用户反馈再说。`

这些表达的问题是：缺少边界、缺少验证、缺少风险和缺少 owner 感。

## 高级表达替换

- 不说 `RAG 可以解决幻觉`，说 `RAG 只能改善外部事实 grounding，但仍需要检索评测、答案引用、冲突处理和人工兜底。`
- 不说 `Agent 自动执行任务`，说 `Agent 要被放进 workflow、tool gateway、approval、sandbox、audit 和 rollback 里，否则执行能力越强风险越大。`
- 不说 `模型更强就好`，说 `模型升级要经过 task-level regression、成本评估、灰度和 fallback，否则强模型也可能引入新失败模式。`
- 不说 `效果不错`，说 `我会用任务完成率、人工接管率、事实错误率、延迟、成本和安全事件数一起判断。`

## 和其他题库的关系

- 底层与训练：[[../05-Question-Banks/01-LLM基础与训练题库|LLM基础与训练题库]]
- 推理系统：[[../05-Question-Banks/02-推理与系统架构题库|推理与系统架构题库]]
- Agent：[[../05-Question-Banks/03-Agent与工具调用题库|Agent与工具调用题库]]
- RAG：[[../05-Question-Banks/04-RAG与数据工程题库|RAG与数据工程题库]]
- 评测上线：[[../05-Question-Banks/05-评测与上线治理题库|评测与上线治理题库]]
- 安全合规：[[../05-Question-Banks/06-安全与合规题库|安全与合规题库]]
- 产品落地：[[../05-Question-Banks/12-产品落地、Rollout、ROI 与 Governance题库|产品落地、Rollout、ROI 与 Governance题库]]
- 综合题库：[[../05-Question-Banks/14-大模型与 AI 全景题库|大模型与 AI 全景题库]]

## 练法

1. 用 30 秒版回答一次
2. 用 2 分钟版回答一次
3. 用 5 分钟白板版画一次
4. 随机抽一个题库问题，用这套母版强行串回 `原理 -> 工程 -> 治理 -> 业务`
5. 复盘自己有没有只讲技术，没有讲指标和风险
