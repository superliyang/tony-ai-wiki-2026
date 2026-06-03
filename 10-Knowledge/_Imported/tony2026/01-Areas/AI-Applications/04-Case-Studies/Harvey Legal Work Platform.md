---
title: Harvey Legal Work Platform
type: case
status: learning
tags:
  - ai/case-study
  - ai/legal
industry: legal-and-compliance
problem: legal work needs complex reasoning, domain knowledge, citations, and low-hallucination output
solution: custom-trained case-law model and legal AI workflows built with OpenAI
stack:
  - custom-trained OpenAI model
results:
  - added 10 billion-token equivalent legal context
  - tested with 10 of the largest law firms
lessons:
  - legal agents need domain grounding beyond prompt engineering and basic RAG
  - citation quality is a product requirement, not a nice-to-have
related_topics:
  - Legal and Compliance Agents
created: 2026-03-23
updated: 2026-03-23
---

# Harvey Legal Work Platform

## 背景

法律工作不是普通问答。它通常要求复杂推理、充分上下文、 jurisdiction 差异理解，以及最重要的：引用和依据必须可靠。

## 做了什么

- Harvey 与 OpenAI 合作构建定制化法律模型
- 不是停留在 prompt engineering 或基础 RAG，而是把案例法语料深度引入模型训练流程
- 目标不是让模型“看起来懂法”，而是支持文书草拟、复杂诉讼问题回答、合同差异识别等真实法律工作

## 结果

- 官方披露：引入了相当于 100 亿 token 的法律上下文
- 官方披露：与 10 家头部律所一起测试
- 官方披露：模型输出中的每一句都能由引用的案例支撑，目标之一就是减少编造案例

## 为什么值得学

- 这个案例很适合说明：在高专业、高风险行业里，通用模型能力往往只是起点
- 真正进入生产环境，需要 domain grounding、citation discipline 和 high-trust review workflow
- 也说明不是所有行业问题都能靠“加一个检索层”解决

## 迁移启发

- 法律和合规 agent 要优先设计来源与引用体系
- 如果任务是开放性、复杂推理型，仅靠通用 prompt 和轻量 RAG 可能不够
- 在这类行业里，输出可审查性往往比回答流畅度更重要

## 来源

- 官方案例：[Harvey](https://openai.com/index/harvey/)
- 官方说明：[Introducing improvements to the fine-tuning API and expanding our custom models program](https://openai.com/index/introducing-improvements-to-the-fine-tuning-api-and-expanding-our-custom-models-program/)

## 相关

- [[../01-Industries/Legal and Compliance Agents|Legal and Compliance Agents]]
- [[../05-Topics/Agent Productization|Agent Productization]]
- [[../../AI-Engineering/07-Topics/Agent Evaluation and Reliability|Agent Evaluation and Reliability]]
