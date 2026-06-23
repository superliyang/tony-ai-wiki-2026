---
title: OpenAI In-House Data Agent
type: case
status: learning
tags:
  - ai/case-study
  - ai/data-agent
industry: enterprise-operations
problem: make internal analytics faster while preserving trust and correctness
solution: bespoke in-house data agent with reusable workflows and systematic evaluation
stack:
  - OpenAI internal tools
results:
  - covers discovery, SQL, notebook and report publishing
  - packages recurring analyses into reusable workflows
lessons:
  - internal agents need context, workflow reuse, and strong evaluation
related_topics:
  - Enterprise Agent Workflows
  - Operations Agents
  - Analytics Operations Agent Workflow
created: 2026-03-22
updated: 2026-03-24
---

# OpenAI In-House Data Agent

## 背景

内部数据分析往往既重复又高价值，但分析师大量时间花在找表、改 SQL、追上下文，而不是做真正的业务判断。

## 做了什么

- OpenAI 为内部数据分析构建了 bespoke in-house AI data agent
- 覆盖数据发现、SQL 执行、notebook 与 report 发布的完整链路
- 把反复出现的分析任务封装成可复用 workflow
- 用系统化 evaluation 来防止质量漂移和信任崩塌

## 为什么这个案例重要

- 它说明企业内部 agent 的价值，不只是“问答更方便”，而是把重复分析工作产品化
- 它也说明 always-on agent 最怕的是 drift，所以评测和验证必须是系统组成部分，而不是上线后的附加项

## 迁移启发

- 内部 agent 最适合先从高频重复分析和标准化报表切入
- 把 recurring analyses 做成 reusable workflows，往往比单次问答体验更值钱
- 可信的内部 agent 必须和 evaluation、clarification、defaults 一起设计

## 来源

- 官方文章：[Inside OpenAI’s in-house data agent](https://openai.com/index/inside-our-in-house-data-agent/)

## 相关

- [[../03-Workflows/Analytics Operations Agent Workflow|Analytics Operations Agent Workflow]]
- [[../01-Industries/Enterprise Operations Agents|Enterprise Operations Agents]]
- [[../05-Topics/Operations Agents|Operations Agents]]
- [[../../AI-Engineering/07-Topics/Agent Evaluation and Reliability|Agent Evaluation and Reliability]]
