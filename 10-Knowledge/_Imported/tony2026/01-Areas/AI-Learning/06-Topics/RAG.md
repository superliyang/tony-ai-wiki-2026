---
title: RAG
type: topic
status: draft
tags:
  - ai/topic
  - ai/rag
created: 2026-03-13
updated: 2026-03-13
---

# RAG

## 这个主题是什么

`RAG` 是 retrieval-augmented generation 的简称，指在生成回答前先检索外部信息，再把检索结果交给模型使用。

## 为什么重要

- 它是把通用模型接入企业知识、私有数据和实时信息的常见方法
- 很多真实应用不需要重新训练模型，而是更需要让模型“拿到对的上下文”

## 你先要抓住什么

- RAG 不是让模型变聪明，而是让模型在回答时拥有更相关、更最新的信息
- 它通常由检索、排序、上下文构造和生成四部分组成
- RAG 经常和长上下文、agent、knowledge base 一起出现

## 适合解决什么问题

- 私有知识问答
- 文档检索与总结
- 需要最新信息的场景
- 企业内部 assistant

## 关键问题

- 检索到的信息是否真的相关
- 上下文拼接方式会不会把模型搞乱
- RAG 和长上下文应该怎么搭配

## 相关

- [[Long Context]]
- [[Agent]]
- [[AI Assistant]]
