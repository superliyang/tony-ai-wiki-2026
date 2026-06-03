---
title: WebVoyager：Building an End-to-End Web Agent with Large Multimodal Models
type: paper
status: draft
tags:
  - ai/paper
  - ai/agent
  - ai/browser
aliases: []
authors: []
organization: []
year: 2024
venue: ACL / arXiv
related_models: []
related_people: []
related_topics:
  - "[[Agent]]"
  - "[[Browser Agents 与 Computer Use]]"
  - "[[Tool Use]]"
source: https://arxiv.org/abs/2401.13919
created: 2026-04-03
updated: 2026-04-03
---

# WebVoyager：Building an End-to-End Web Agent with Large Multimodal Models

## 简介

`WebVoyager` 是最近两年 browser agent 论文里很值得记住的一张卡，因为它开始把 web agent 从“能不能操作页面”推进到“能不能在真实网站里端到端完成任务”。

## 核心想法

它把多模态网页理解、动作选择和真实网站环境下的任务完成度放到同一个 agent 闭环里看。

## 为什么重要

- 它说明 browser agent 的难点从来不只是点击，而是 `observe -> reason -> act -> recover`
- 它让 `web agent` 这个方向更接近真实世界，而不是只停留在合成 demo
- 它是理解后来 cloud-hosted browser agent 产品的好入口

## 相关系统 / 产品路线

- [[ChatGPT Agent]]
- [[OpenClaw]]
- [[Browser Agents 与 Computer Use]]

## 相关主题

- [[Agent]]
- [[Browser Agents 与 Computer Use]]
- [[Tool Use]]

## 后续可补充

- 它和 ReAct 路线的关系
- 它对 action grounding、benchmark 和 safety 的要求
- 为什么网页环境会让 agent runtime 变得更脆弱

## 相关

- [[ReAct：Synergizing Reasoning and Acting in Language Models]]
- [[ScreenAI：A Vision-Language Model for UI and Infographics Understanding]]
- [[../../AI-Engineering/07-Topics/Computer Use Runtime and Safety|Computer Use Runtime and Safety]]
