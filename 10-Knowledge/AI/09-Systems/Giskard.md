---
title: Giskard
type: system
status: learning
tags:
  - ai/system
  - ai/evals
  - ai/security
created: 2026-04-14
updated: 2026-04-14
---

# Giskard

## 它是什么

`Giskard` 是一个偏 `quality testing + vulnerability testing` 的开源评估工具链。

它特别值得注意的两块是：

- `RAG Evaluation Toolkit`
- `LLM scan / test suite / CI/CD` 这条上线前质量门禁路线

## 为什么它重要

很多团队会把 agent 评估理解成“能不能完成任务”，但真实系统还要关心：

- 有没有安全脆弱性
- 有没有 prompt / retrieval / generation 的系统性缺陷
- 能不能把测试套件接进工程流水线

`Giskard` 很适合补这层。

## 它最值得抓住的 4 个点

### 1. 它是 test-suite-first

这意味着它很适合：

- 明确测试用例
- 组合测试套件
- 接入 CI/CD

### 2. 它把 RAG evaluation 单独产品化了

这使它不只是泛泛的 LLM 测试，而是对知识型系统更友好。

### 3. 它很适合质量和安全边界一起看

很多时候：

- 质量问题
- 鲁棒性问题
- 安全问题

并不是三张完全分离的表。

### 4. 它更像上线前门禁和测试层，不是 tracing 平台

所以它经常更适合搭配：

- `Promptfoo`
- `Phoenix`
- `Langfuse`

而不是单独承担完整 AgentOps。

## 在 Agent 效果评估这条线上怎么放它

- 用它补 `security / robustness / test-suite` 视角
- 用它把质量检查前移到 CI
- 对 RAG / tool-using agent 做更系统的脆弱性测试

## 它不解决什么

- 它不是完整 runtime tracing 平台
- 它不是主要的 registry / release comparison 平台
- 它不等于长期在线反馈闭环

## 推荐继续往下读

- [[../../AI-Engineering/07-Topics/Agent 效果评估：方法论、开源工具与判断框架|Agent 效果评估：方法论、开源工具与判断框架]]
- [[../../AI-Engineering/07-Topics/AI Security Evaluation 与 Red Teaming|AI Security Evaluation 与 Red Teaming]]
- [[../../AI-Engineering/07-Topics/Agent 上线门槛与安全 Release Gates|Agent 上线门槛与安全 Release Gates]]
- [[Promptfoo]]
- [[Arize Phoenix]]

## 关联

- [[../06-Topics/AI Security|AI Security]]
- [[../06-Topics/MLOps 与 LLMOps|MLOps 与 LLMOps]]
- [[../../AI-Engineering/07-Topics/AI Security Evaluation 与 Red Teaming|AI Security Evaluation 与 Red Teaming]]
- [[../../AI-Engineering/07-Topics/Agent 效果评估：方法论、开源工具与判断框架|Agent 效果评估：方法论、开源工具与判断框架]]

## 资料

- [Giskard OSS Docs](https://docs.giskard.ai/oss/sdk/index.html)
