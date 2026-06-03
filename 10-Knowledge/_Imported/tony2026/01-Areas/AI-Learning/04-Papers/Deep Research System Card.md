---
title: Deep Research System Card
type: paper
status: learning
authors:
  - OpenAI
year: 2025
organization: "[[OpenAI]]"
created: 2026-04-13
updated: 2026-04-13
---

# Deep Research System Card

## 这篇资料是什么

这是 OpenAI 在 `2025-02-25` 发布的 deep research system card。它不是单纯介绍一个模型，而是在解释一种新的 `agentic capability`：

- 多步互联网研究
- 浏览网页、图像、PDF
- 读用户文件
- 写并执行 Python 做分析
- 最终整合成带引用的报告

## 为什么它重要

它把 `research agent` 从概念推进成了正式产品与治理对象。

这里最值得记住的不是“模型会搜网了”，而是：

- deep research 是 `multi-step research on the internet for complex tasks`
- 它由一个为 web browsing 优化的 early `OpenAI o3` 版本驱动
- 它把 browsing、reasoning、file reading、python analysis 和 synthesis 放进同一个能力面

## 它真正补上的路线

### 1. research agent 不等于 search

它强调的是：

- 多步
- 动态转向
- 长任务
- 证据整合
- 报告生成

这和“搜一下网页再总结”不是一个层级。

### 2. deep research 会自然带出新的风险面

system card 里特别强调了：

- prompt injection
- personal information / privacy
- disallowed content
- browsing-specific risks

也就是说，research agent 一旦能主动读外部内容，安全问题会自然升级。

### 3. 评测方式也必须跟着改

这篇卡里一个很重要的信号是：

- 长答案更难自动评估
- citation 和 synthesis 会让 grading 更复杂
- 传统单步安全评测不够，需要新的 browsing / privacy / prompt injection eval

## 读这篇时最该抓住什么

- deep research 是 `agentic capability`，不是单个 benchmark 名词
- 它会把 `RAG`、`browser use`、`python sandbox`、`report synthesis` 拉进同一条主线
- 它也是 `research agent`、`deep research product` 和 `governed long-horizon agent` 的代表锚点

## 应该接回哪些主题

- [[../06-Topics/Deep Research 与 Research Agents|Deep Research 与 Research Agents]]
- [[../06-Topics/Agent|Agent]]
- [[../06-Topics/Browser Agents 与 Computer Use|Browser Agents 与 Computer Use]]
- [[../06-Topics/上下文工程|上下文工程]]
- [[../06-Topics/AI Safety 与 AI Security|AI Safety 与 AI Security]]

## 关联系统

- [[../09-Systems/ChatGPT Agent|ChatGPT Agent]]
- [[../09-Systems/OpenAI API|OpenAI API]]

## 原文

- [Deep Research System Card (OpenAI, 2025-02-25)](https://cdn.openai.com/deep-research-system-card.pdf)
