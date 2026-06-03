---
title: AI 五条主干案例、失败模式与取舍
type: topic
status: active
tags:
  - ai/topic
  - ai/workbench
  - ai/tradeoffs
created: 2026-04-13
updated: 2026-04-13
---

# AI 五条主干案例、失败模式与取舍

> 这页的目标不是再补概念，
> 而是把五条主干进一步压成：`真实案例 -> 常见失败模式 -> 核心取舍方式`。

## 1. 模型形成线

对应主干：

- [[模型形成线：Pretraining、Transformer、Foundation Models、Reasoning 与 Multimodal]]

代表案例：

- `foundation model` 作为公共底座，带动上层产品和平台分工
- `reasoning model` 提升复杂任务完成率，但也抬高 latency 和成本
- `multimodal model` 打开语音、文档、computer use 等新表面

常见失败模式：

- 把 benchmark 提升当成真实系统收益
- 把“模型会了”误当成“产品已经能交付”
- 把 long context 误当成 memory / retrieval 的替代

典型取舍：

- 选更强模型，还是选更可控、更便宜的模型组合
- 把复杂度留在模型里，还是转移到 runtime / workflow
- 先追 reasoning 能力，还是先追 multimodal product fit

## 2. 能力升级线

对应主干：

- [[能力升级线：Prompt、Context、RAG、Tool Use、Agent、Memory 与 Multi-Agent]]

代表案例：

- 企业知识问答从 prompt-only 升级到 RAG
- coding / ops 场景从 tool use 升级到 agent loop
- 长任务系统引入 memory、planning 和 approval

常见失败模式：

- 过度迷信 prompt，忽略 context 组织
- 过早上 multi-agent，导致调试和协同复杂度暴涨
- 把 memory 当成“什么都记住”，结果产生污染和不可控行为

典型取舍：

- RAG、memory、long context 分别该承担多少职责
- workflow 应显式编排，还是交给 agent 自主决策
- 单 agent 做稳更重要，还是多 agent 并行探索更重要

## 3. 运行时工程线

对应主干：

- [[运行时工程线：Inference、Serving、Evaluation、Release Gate 与 Security]]

代表案例：

- 高并发服务下通过 route、cache、降级把成本压住
- 用 eval harness 和 release gate 把模型切换做成可控机制
- 把 incident response 接回 rollout 和 regression 套件

常见失败模式：

- 只看效果，不看 token 成本和延迟
- 没有可回归 eval，导致升级后线上退化才被发现
- 没有 rollback 和 tracing，事故发生时无法快速止血

典型取舍：

- latency、quality、cost 之间怎么平衡
- self-hosted、managed API、hybrid route 怎么选
- 先追上线速度，还是先补 eval / release / rollback 机制

## 4. 安全治理线

对应主干：

- [[安全治理线：AI Safety、AI Security、Prompt Injection、Approval、Audit 与 Release Gate]]

代表案例：

- 有 tool use 的 agent 通过 approval 和 sandbox 限制 side effects
- 通过 audit trace、telemetry 和 incident loop 做闭环治理
- 把 prompt injection 风险从“输出问题”升级为“动作与权限问题”

常见失败模式：

- 只做一层 output filter，就以为安全问题解决了
- 没有 approval 分级，导致高风险动作也默认自动执行
- 有日志但没有 audit trace，复盘时无法归因

典型取舍：

- 安全收得多紧，才不会把用户体验完全压死
- 哪些任务需要 mandatory approval，哪些可以自动放行
- 安全机制是放在产品边缘，还是直接进入 release gate 和 operating model

## 5. 产品落地线

对应主干：

- [[产品落地线：Model、Workflow、Case Study、Rollout、ROI 与 Governance]]

代表案例：

- assistant / copilot 在知识、客服、研发场景进入具体 workflow
- rollout 从小范围试点走向部门或公司级 adoption
- ROI 从“模型很强”转成“流程更快、更稳、错误更少”

常见失败模式：

- 做了一个看起来很强的聊天框，但没有进入真实流程
- rollout 只做宣传，不做 owner、培训和行为改变
- 只会讲人效，不会讲风险下降、吞吐提升和经营价值

典型取舍：

- assistant、copilot、workflow automation 分别适合什么任务边界
- 先做通用平台，还是先做垂直高价值场景
- 先追 adoption，还是先追 ROI 可证明性

## 怎么用这页

- 学习时：用它把抽象主干接到真实案例和真实失败
- 设计时：优先看“常见失败模式”和“典型取舍”
- 面试时：用“案例 -> 失败模式 -> 取舍 -> 指标”这条线讲出 senior 感

## 关联

- [[AI 五条主干专家工作台]]
- [[AI 五条主干关键问题]]
- [[AI 五条主干核心指标]]
- [[AI 五条主干易混边界]]
- [[AI 五条主干面试表达要点]]
