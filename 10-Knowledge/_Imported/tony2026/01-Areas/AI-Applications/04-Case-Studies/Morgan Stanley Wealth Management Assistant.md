---
title: Morgan Stanley Wealth Management Assistant
type: case
status: learning
tags:
  - ai/case-study
  - ai/finance
industry: financial-services
problem: give financial advisors fast, reliable access to internal knowledge while meeting strict quality expectations
solution: internal assistant plus evaluation framework for retrieval, summarization, and multilingual support
stack:
  - GPT-4
results:
  - 98%+ advisor team adoption
  - internal retrieval scaled from 7,000 questions to a 100,000-document corpus
lessons:
  - evals drive trust in regulated industries
  - reliability and governance are adoption prerequisites
related_topics:
  - Financial Services Agents
created: 2026-03-23
updated: 2026-04-03
---

# Morgan Stanley Wealth Management Assistant

## 背景

金融顾问的日常工作高度依赖内部知识库、研究内容、流程文档和客户上下文。问题不是没有信息，而是信息太多、太散，而且必须在高质量标准下快速调用。

## 做了什么

- Morgan Stanley 与 OpenAI 合作构建内部 assistant
- 把 GPT-4 嵌入财富管理工作流
- 不只是上线一个 chatbot，而是先建立严格的 `eval framework`
- 用摘要评测、翻译评测和检索优化来不断提高质量与一致性

## 结果

- 官方披露：超过 98% 的 advisor teams 主动使用 `AI @ Morgan Stanley Assistant`
- 官方披露：系统从回答约 7,000 个问题，扩展到能够覆盖 100,000 份文档语料
- 官方披露：文档访问比例从 20% 提升到 80%

## 为什么值得学

- 这个案例说明：在金融行业，真正决定 adoption 的不是 demo，而是 evals
- 它也说明 agent 的第一波价值，往往来自“高可信知识访问”和“更快的信息到洞察”
- 金融行业里的好案例，通常都会把 reliability、privacy、governance 放在很靠前的位置

## rollout packet

### pilot

- 先把范围收在高可信知识访问，而不是一上来做自动执行

### gate

- `eval framework` 本身就是 gate，不只是上线前检查

### review

- 持续追踪摘要、翻译、检索质量，而不是只看用户主观感受

### scale

- 信任一旦建立，场景才有机会从知识访问扩展到更多高价值工作流

## 迁移启发

- 在 regulated industry 里，先做“可信助手”往往比先做“自动执行 agent”更现实
- 要把评测框架当作产品的一部分，而不是上线前一次性测试
- 质量和信任一旦建立，应用边界才可能从知识问答扩展到更多场景

## 来源

- 官方案例：[Morgan Stanley uses AI evals to shape the future of financial services](https://openai.com/index/morgan-stanley/)

## 相关

- [[../01-Industries/Financial Services Agents|Financial Services Agents]]
- [[../05-Topics/Agent Adoption and Change Management|Agent Adoption and Change Management]]
- [[../../AI-Engineering/07-Topics/Agent Evaluation and Reliability|Agent Evaluation and Reliability]]
- [[../../AI Rollout Operating Packet：试点、门禁、复盘与规模化|AI Rollout Operating Packet：试点、门禁、复盘与规模化]]
