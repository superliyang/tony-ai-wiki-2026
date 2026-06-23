---
title: AI 五条主干易混边界
type: topic
status: active
tags:
  - ai/topic
  - ai/workbench
  - ai/boundaries
created: 2026-04-13
updated: 2026-04-13
---

# AI 五条主干易混边界

> 很多“听起来专业”的表达，其实会在边界处暴露级别。
> 这页的目的就是把最容易说混的概念分清楚。

## 1. 模型形成线

- pretraining vs post-training
  前者决定底座能力，后者决定可用性与产品气质
- reasoning vs fluent generation
  会说得顺不等于会解决复杂任务
- multimodal vs product multimodality
  模型支持多模态不等于系统已经形成稳定多模态 workflow
- long context vs memory
  上下文窗口变长不等于系统有长期记忆能力

## 2. 能力升级线

- prompt vs context
  prompt 是控制指令，context 是任务材料和工作内存
- RAG vs memory
  RAG 偏事实检索，memory 偏长期状态和经验沉淀
- tool use vs agent
  tool use 是单步动作，agent 是多步任务闭环
- agent vs workflow
  agent 更灵活，workflow 更可控；不是所有场景都该交给 agent 自由发挥
- single agent vs multi-agent
  多 agent 不是高级版默认答案，而是复杂度更高的结构选择

## 3. 运行时工程线

- benchmark vs online performance
  测试集表现不等于线上系统表现
- serving vs ops
  serving 解决服务承接，ops 解决长期运行与反馈闭环
- eval vs release gate
  eval 提供判断依据，release gate 决定能否放量
- latency vs throughput
  二者相关但不是一回事，很多系统调优本质是在做权衡

## 4. 安全治理线

- safety vs security
  safety 偏伤害与行为边界，security 偏攻击与控制面
- guardrail vs governance
  guardrail 是单点控制，governance 是整体治理机制
- approval vs audit
  approval 管事前授权，audit 管事后追责和复盘
- policy 写出来 vs policy 真生效
  有 policy 不代表它进入了 runtime、审批和 release 机制

## 5. 产品落地线

- capability vs product
  一个能力不等于一个能被稳定使用的产品
- product surface vs workflow
  交互入口不等于真正创造价值的流程
- rollout vs adoption
  组织推开不等于用户真的持续使用
- ROI vs hype
  热闹的 demo 不等于可持续的经营价值
- case study vs marketing story
  真案例会有约束、失败和权衡，营销故事通常只有结果

## 怎么用这页

- 学习时：先把边界讲清，再追深度
- 讨论时：遇到模糊词，先问它落在哪一侧
- 面试时：能把边界讲清，往往比堆术语更显资深

## 关联

- [[AI 五条主干专家工作台]]
- [[AI 五条主干关键问题]]
- [[AI 五条主干核心指标]]
- [[AI 五条主干面试表达要点]]
