---
title: Research Agent Eval Pack：信息整合、引用与冲突处理
type: evaluation
status: learning
tags:
  - ai/evaluation
  - ai/agent
  - ai/research
created: 2026-04-15
updated: 2026-04-15
---

# Research Agent Eval Pack：信息整合、引用与冲突处理

## 这包任务在判断什么

这套包判断的是：

- agent 能不能做出“有证据的研究”，而不是像在写顺滑作文
- 它会不会混淆事实、推断和建议
- 面对时间敏感、来源冲突、长任务上下文漂移时，结论还能不能站住

## 适用对象

- deep research agent
- analyst copilot
- market / policy / competitor research assistant
- report drafting agent

## 环境假设

- 来源质量不一致
- 问题可能带时间敏感性
- 研究任务经常需要多轮搜索与整合
- 最终产物通常是结构化总结或报告

## 主要指标

- `source-grounded answer quality`
- `citation correctness`
- `claim traceability`
- `hallucinated-claim rate`
- `time to completion`
- `report usefulness`

## 发布门槛建议

- `citation correctness >= 0.90`
- `hallucinated-claim rate <= 0.05`
- `claim traceability >= 0.85`
- 时间敏感问题必须显式标时间边界

## Task Family A：定向研究

### Case A1

- 目标：回答一个范围清晰的问题并给出处
- 通过标准：来源够强，结论与来源一致
- grader：citation check + human review

### Case A2

- 目标：给出两个对象的结构化比较
- 通过标准：维度一致，不偷换概念
- grader：rubric-based human review

## Task Family B：多来源整合

### Case B1

- 目标：整合 3 个以上来源形成结论
- 通过标准：能区分核心来源与辅助来源
- grader：claim traceability

### Case B2

- 目标：从长材料里提炼 executive summary
- 通过标准：保留关键事实，不掩盖不确定性
- grader：human review

## Task Family C：冲突与不确定性

### Case C1

- 目标：来源冲突时输出结论
- 通过标准：显式写出冲突，不强行统一
- grader：human review + contradiction handling rubric

### Case C2

- 目标：时间敏感问题研究
- 通过标准：标明日期与适用边界
- grader：time-bound correctness

## Task Family D：边界与风险

### Case D1

- 目标：资料不足问题
- 通过标准：不编造，不装作确定
- grader：unsupported-claim check

### Case D2

- 目标：来源质量很差的问题
- 通过标准：主动降权或提示风险
- grader：source-quality handling

## Task Family E：产物可用性

### Case E1

- 目标：生成给管理者看的 1 页摘要
- 通过标准：短、清楚、可决策，不只是信息堆砌
- grader：human usefulness review

### Case E2

- 目标：生成带行动建议的分析
- 通过标准：把事实和建议显式分开
- grader：fact-vs-advice separation check

## 最容易暴露的失败模式

- 引了来源，但关键结论并不被来源支撑
- 把旧信息当新信息
- 把推断写成事实
- 来源冲突时强行写一个单一结论
- 看起来像研究报告，其实只是流畅摘要

## 适合用什么工具组合

- `Langfuse + Promptfoo`
  - 适合做报告质量回归与线上 trace 对照
- `Inspect AI + Phoenix`
  - 适合更结构化的研究任务与失败诊断

## 关联

- [[Agent Eval 任务包：Repo、Research、RAG、Tool Use]]
- [[Agent 效果评估指标清单]]
- [[../09-Templates/Agent 效果评测模板|Agent 效果评测模板]]
- [[../09-Templates/Agent Eval 任务包模板|Agent Eval 任务包模板]]
