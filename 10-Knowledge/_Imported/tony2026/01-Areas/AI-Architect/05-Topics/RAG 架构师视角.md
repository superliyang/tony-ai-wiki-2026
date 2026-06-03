---
title: RAG 架构师视角
type: topic
status: active
domain: AI-Architect
created: 2026-05-05
updated: 2026-05-05
---

# RAG 架构师视角

> RAG 不是“向量库 + 大模型”，而是一个知识可信度、权限边界、检索质量和答案责任的架构问题。

## 架构师要回答的问题

- 这个系统回答的是“公开知识”还是“企业内部权限知识”？
- 知识来源是否可信、新鲜、可追溯？
- 用户是否有权限看到被检索出来的内容？
- 检索错了、引用错了、模型编了，怎么发现和修正？
- RAG 是产品功能、内部能力，还是企业知识平台底座？

## RAG 架构分层

| 层 | 架构关注点 |
|---|---|
| 数据源层 | 文档、数据库、工单、代码、Wiki、邮件、知识图谱 |
| 处理层 | 解析、清洗、切分、metadata、版本、敏感信息处理 |
| 索引层 | embedding、hybrid search、向量库、倒排、图关系 |
| 检索层 | query rewrite、filter、rerank、权限过滤 |
| 生成层 | prompt、citation、grounding、structured answer |
| 评测层 | retrieval eval、faithfulness、coverage、人工评审 |
| 治理层 | 数据权限、保留删除、审计、反馈闭环 |

## 关键设计决策

### chunking 怎么做

- 按段落、标题、语义、页面、代码块还是业务对象切？
- chunk 太小会丢上下文，太大会干扰召回。
- metadata 往往比 embedding 更决定生产质量。

### 检索怎么做

- 只用向量检索通常不够，企业场景常需要 keyword、metadata filter、rerank。
- 对结构化业务问题，SQL/搜索/知识图谱可能比向量更可靠。
- query rewrite 可以提升召回，也可能引入错误意图。

### 权限怎么做

- 权限过滤必须发生在检索阶段，而不是只在生成后过滤。
- 多租户、部门、项目、文档级、段落级权限要提前设计。
- RAG 输出要能解释引用来源和权限依据。

### 评测怎么做

- 评测不能只看“答案像不像”，还要看检索是否命中正确来源。
- 需要 golden question、expected source、expected answer、forbidden source。
- 线上反馈要回写到数据、chunk、retrieval、prompt 和 eval。

## 常见失败模式

- 把所有文档丢进向量库，权限和版本都不管。
- 召回错了，却只调 prompt。
- 只看答案满意度，不看引用和可追溯。
- 没有数据 owner，知识过期没人管。
- 没有 eval set，每次改 chunk 或 embedding 都靠感觉。

## 架构师交付物

- RAG 数据源清单
- 知识处理和索引设计
- 权限过滤方案
- Retrieval eval set
- RAG 架构图
- RAG 线上质量指标

## 关联

- [[../07-Templates/AI 架构设计模板|AI 架构设计模板]]
- [[../../AI-Engineering/07-Topics/Mac 上的 RAG、Agent 与本地应用开发|Mac 上的 RAG、Agent 与本地应用开发]]
- [[../../AI-Engineering/04-Evaluation/企业知识库 Agent Eval Pack：检索、归因与权限边界|企业知识库 Agent Eval Pack：检索、归因与权限边界]]

