---
title: Research Agent Workflow
type: workflow
status: learning
tags:
  - ai/workflow
  - ai/research
inputs:
  - research question
  - source constraints
  - output format
steps:
  - scope the question
  - gather sources
  - extract evidence
  - synthesize findings
  - review and refine
tools:
  - browser
  - search
  - file analysis
outputs:
  - structured memo
  - source-backed summary
evaluation:
  - source quality
  - completeness
  - factual consistency
risks:
  - weak sourcing
  - over-summarization
  - fabricated claims
related_products:
  - ChatGPT Agent 产品卡
  - OpenClaw 产品卡
created: 2026-03-22
updated: 2026-03-22
---

# Research Agent Workflow

## 简介

研究型 workflow 是最适合 agent 先创造稳定价值的方向之一，因为它天然是多步、可验证、可阶段性交付的任务。

## 步骤

1. 明确研究问题与边界
2. 搜索与抓取候选来源
3. 提取关键信息与证据
4. 组织结构与形成结论
5. 人类复核、补洞与定稿

## 工具链

- search / browser
- file analysis
- connectors to docs or repositories
- 可能还需要 spreadsheet 或 note-taking output

## 评估

- 来源是否可靠
- 信息覆盖是否完整
- 结论是否真正由证据支持
- 是否节省了人工整理时间

## 风险

- 伪造来源或引用不稳
- 把不确定结论说得太肯定
- 缺少边界控制，最后变成低质量长文

## 最适合的产品

- [[../02-Products/ChatGPT Agent 产品卡|ChatGPT Agent 产品卡]]
- [[../02-Products/OpenClaw 产品卡|OpenClaw 产品卡]]

## 相关

- [[../05-Topics/Research Agents|Research Agents]]
- [[../../AI-Engineering/07-Topics/Agent Evaluation and Reliability|Agent Evaluation and Reliability]]
