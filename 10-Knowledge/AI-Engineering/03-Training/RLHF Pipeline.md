---
title: RLHF Pipeline
type: training
status: seed
tags:
  - ai/training
created: 2026-03-13
updated: 2026-03-13
---

# RLHF Pipeline

## 简介

`RLHF Pipeline` 关注从监督微调到偏好建模再到对齐优化的一整条训练流程。

## 为什么它重要

- 它直接影响模型在真实交互中的行为质量
- 很多用户感觉到的“模型更像助手了”，背后往往不是预训练，而是这条对齐链路

## 关键阶段

- SFT
- preference data collection
- reward modeling / direct preference optimization
- safety and release gating

## 每一步分别在做什么

- SFT：让模型先学会遵循指令和目标格式
- preference data：收集“哪个回答更好”的偏好信号
- reward / DPO：把偏好变成可优化目标
- gating：用安全与质量标准决定是否能进入产品

## 真正要看懂的地方

- RLHF pipeline 是训练系统、标注系统、评测系统和发布系统共同参与的流程
- 它的难点往往不在算法名字，而在数据质量、反馈一致性和门禁设计

## 学习这页时最该记住什么

- 对齐训练是现代助手产品体验的重要来源
- 它不是孤立算法，而是一整条工程 pipeline

## 适用场景

- 对齐优化
- 提升交互质量和行为控制

## 相关

- [[LoRA and PEFT]]
- [[../07-Topics/RLHF and Preference Optimization|RLHF and Preference Optimization]]
- [[../07-Topics/Safety Evaluation|Safety Evaluation]]
