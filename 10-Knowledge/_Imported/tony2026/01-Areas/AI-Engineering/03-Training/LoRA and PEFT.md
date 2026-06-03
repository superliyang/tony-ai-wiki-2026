---
title: LoRA and PEFT
type: training
status: seed
tags:
  - ai/training
created: 2026-03-13
updated: 2026-03-13
---

# LoRA and PEFT

## 简介

LoRA 和更广义的 PEFT 关注如何以更低成本完成模型微调，是应用阶段非常关键的训练方法。

## 为什么它重要

- 不是所有团队都需要从头训练模型，更多团队需要低成本定制现有模型
- LoRA/PEFT 让“可调模型”从少数大团队能力，变成更多团队可用的工程手段

## 关键能力

- parameter-efficient fine-tuning
- low-cost adaptation
- domain customization

## 它主要解决什么问题

- 全量微调太贵
- 领域适配需要更快迭代
- 不同任务需要维护多个轻量适配版本

## 真正要看懂的地方

- LoRA/PEFT 的意义不只是节省算力，更是改变模型定制方式
- 它让模型微调从“改整个模型”转成“附加一层轻量可替换能力”

## 学习这页时最该记住什么

- PEFT 是应用落地阶段最重要的训练方法之一
- 学会它，你会更理解为什么很多团队更看重适配效率而不是训练极限

## 适用场景

- 垂直领域适配
- 资源有限的微调任务

## 相关

- [[../02-Frameworks/Hugging Face Ecosystem|Hugging Face Ecosystem]]
- [[RLHF Pipeline]]
- [[../07-Topics/Cost Optimization|Cost Optimization]]
