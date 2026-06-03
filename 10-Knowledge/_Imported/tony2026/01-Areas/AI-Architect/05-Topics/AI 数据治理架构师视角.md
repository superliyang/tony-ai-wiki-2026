---
title: AI 数据治理架构师视角
type: topic
status: active
domain: AI-Architect
created: 2026-05-05
updated: 2026-05-05
---

# AI 数据治理架构师视角

> AI 数据治理的核心不是“有没有数据”，而是数据能否被安全、可信、可追溯、可评测地用于模型、RAG、Agent 和反馈闭环。

## 架构师要回答的问题

- 哪些数据可以进入 prompt、RAG、fine-tuning、eval、日志和反馈？
- 数据的 owner、权限、敏感级别和保留策略是什么？
- 知识库是否有版本和来源？
- 反馈数据能否用于改进模型？
- 用户是否知道数据如何被 AI 使用？

## 数据类型

| 数据 | 治理关注点 |
|---|---|
| 用户输入 | 隐私、敏感数据、保留、审计 |
| 文档知识 | 来源、版本、权限、新鲜度 |
| 业务数据 | 访问控制、最小化、数据血缘 |
| Prompt | 版本、泄露、复用、审批 |
| 检索结果 | 权限、引用、可追溯 |
| 工具输出 | 真实性、审计、缓存 |
| 反馈数据 | 同意、标注质量、偏差 |
| Eval 数据 | 覆盖率、代表性、泄露风险 |
| 日志 Trace | 脱敏、保留、访问控制 |

## 治理链路

```mermaid
flowchart LR
  Source["数据源"]
  Classify["分类分级"]
  Policy["权限与策略"]
  Use["AI 使用场景"]
  Observe["观测与反馈"]
  Improve["改进与回归"]

  Source --> Classify --> Policy --> Use --> Observe --> Improve
  Improve -.回写.-> Policy
```

## 关键设计决策

### 数据能否用于训练

- 用户输入默认不应自动进入训练。
- 企业私有数据要有明确使用边界。
- 反馈数据进入训练前要去标识、授权和质量控制。

### 知识库如何治理

- 每个知识源有 owner。
- 每个文档有版本、更新时间、权限和敏感级别。
- 过期知识要能下线。
- RAG 引用要可追溯。

### Eval 数据如何治理

- eval set 不能泄露给模型或 prompt。
- eval 要覆盖真实业务、边界、失败和攻击样例。
- eval 数据也可能包含敏感信息，需要权限和脱敏。

## 常见失败模式

- 把企业所有文档直接向量化。
- 不区分用户数据、知识数据、训练数据、评测数据。
- 日志里保存完整 prompt 和敏感文件。
- feedback 被直接用于训练，没有同意和质量控制。
- 知识库没有 owner，内容过期无人负责。

## 架构师交付物

- AI data inventory
- AI data usage policy
- RAG knowledge governance plan
- eval data governance plan
- AI logging and retention policy
- data owner matrix

## 关联

- [[./RAG 架构师视角|RAG 架构师视角]]
- [[../../Security/05-Topics/数据安全与隐私保护|数据安全与隐私保护]]
- [[../../AI-Engineering/04-Evaluation/评测索引|评测索引]]

