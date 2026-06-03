---
title: AI 架构师 90 天迁移 Playbook
type: playbook
status: active
domain: AI-Architect
created: 2026-05-05
updated: 2026-05-05
---

# AI 架构师 90 天迁移 Playbook

> 目标：让传统互联网架构师在 90 天内形成 AI 架构师的最小可用能力。

## 0-30 天：建立 AI 应用架构坐标

学习重点：

- 模型能力边界、prompt、context、tool calling。
- RAG 基础：embedding、retrieval、rerank、citation。
- AI 应用基本架构：model gateway、RAG、tool gateway、workflow。

产物：

- 一张 AI 应用架构图。
- 一个最小 RAG 原型。
- 一份 AI 系统失败模式清单。

验收：

- 能解释 prompt、RAG、fine-tuning、agent 的选择边界。
- 能画出一个 AI 应用从用户请求到模型、检索、工具和输出的链路。

## 31-60 天：补工程化和生产化

学习重点：

- LLMOps / AgentOps。
- eval、trace、observability。
- cost、latency、cache、fallback。
- release gate、canary、rollback。

产物：

- RAG eval set。
- AI observability 指标表。
- AI 上线门槛清单。
- 一个带 trace 和成本统计的 demo。

验收：

- 能说明 AI 系统如何做质量回归。
- 能设计 prompt/model/dataset 的版本管理。
- 能解释 AI 系统延迟和成本怎么优化。

## 61-90 天：补安全治理和组织落地

学习重点：

- prompt injection、tool abuse、data leakage、memory poisoning。
- AI red team、AI security eval。
- human-in-the-loop、approval、audit。
- use case portfolio、ROI、组织推广。

产物：

- AI 安全威胁模型。
- 工具调用权限矩阵。
- AI 项目从 POC 到生产路线图。
- AI 架构评审模板初稿。

验收：

- 能做一次 AI 架构评审。
- 能判断一个 AI POC 是否具备上线条件。
- 能向管理层解释 AI 项目的价值、风险和治理路径。

## 推荐练习项目

### 项目 1：企业知识库 RAG

- 输入：内部文档、权限、问题集。
- 输出：带引用和权限过滤的问答。
- 重点：retrieval eval、权限边界、citation、hallucination。

### 项目 2：审批型 Agent Workflow

- 输入：一个真实业务流程。
- 输出：agent 调工具、生成建议、人类审批、执行动作。
- 重点：tool permission、audit、rollback、human-in-the-loop。

### 项目 3：AI 上线门槛

- 输入：一个 AI 应用。
- 输出：eval gate、security gate、cost gate、release gate。
- 重点：从 demo 到 production。

## 关联

- [[../05-Topics/AI 时代架构师能力全景|AI 时代架构师能力全景]]
- [[../05-Topics/传统互联网架构师转型 AI 架构师路线|传统互联网架构师转型 AI 架构师路线]]
- [[../06-Maps/AI 架构师迁移地图|AI 架构师迁移地图]]
- [[../../AI-Engineering/09-Templates/Agent 上线门槛模板|Agent 上线门槛模板]]
- [[../../AI-Engineering/09-Templates/AI 安全评审模板|AI 安全评审模板]]

