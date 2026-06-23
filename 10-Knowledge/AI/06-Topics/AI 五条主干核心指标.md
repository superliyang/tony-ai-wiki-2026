---
title: AI 五条主干核心指标
type: topic
status: active
tags:
  - ai/topic
  - ai/workbench
  - ai/metrics
created: 2026-04-13
updated: 2026-04-13
---

# AI 五条主干核心指标

> 这页的目标不是列全所有 KPI，
> 而是帮你知道：`每条主干最值得盯住的衡量维度是什么。`

## 1. 模型形成线

对应主干：

- [[模型形成线：Pretraining、Transformer、Foundation Models、Reasoning 与 Multimodal]]

最关键的衡量维度：

- 通用能力上限：知识覆盖、泛化能力、跨任务稳定性
- 推理能力：复杂任务成功率、步骤稳定性、长任务完成率
- 多模态能力：跨模态理解准确率、图文语音协同质量
- 长上下文能力：长文档任务完成率、上下文保持能力、信息利用率

更值得追问的不是单个 benchmark 分数，而是：

- 这些指标是否能迁移到真实系统任务
- 能力提升来自训练变化还是测试集偏好

## 2. 能力升级线

对应主干：

- [[能力升级线：Prompt、Context、RAG、Tool Use、Agent、Memory 与 Multi-Agent]]

最关键的衡量维度：

- 任务完成率
- 工具调用成功率
- retrieval 命中率 / 引用质量
- agent 步骤数与失败率
- memory 命中质量与污染率
- multi-agent 协作收益是否大于复杂度成本

更应该看的不是“输出好不好看”，而是：

- 系统是否真的更稳定完成任务
- 新增模块是否带来了确定性的增益

## 3. 运行时工程线

对应主干：

- [[运行时工程线：Inference、Serving、Evaluation、Release Gate 与 Security]]

最关键的衡量维度：

- latency
- throughput
- token / request cost
- availability / error rate
- regression pass rate
- rollout success / rollback frequency

这条线里，很多 senior 判断都来自一个平衡：

- 能力够不够
- 成本扛不扛得住
- 风险可不可控

## 4. 安全治理线

对应主干：

- [[安全治理线：AI Safety、AI Security、Prompt Injection、Approval、Audit 与 Release Gate]]

最关键的衡量维度：

- unsafe output rate
- prompt injection success rate
- tool misuse / unauthorized action rate
- approval bypass rate
- audit completeness
- incident detection / escalation time

这条线的指标不是“有没有风险”，而是：

- 风险能否被发现
- 风险能否被阻断
- 出事后能否被归因和收敛

## 5. 产品落地线

对应主干：

- [[产品落地线：Model、Workflow、Case Study、Rollout、ROI 与 Governance]]

最关键的衡量维度：

- adoption rate
- retained usage
- workflow cycle-time reduction
- error / rework reduction
- business conversion / revenue lift
- owner clarity 与 governance cadence

这条线最容易被忽视的一点是：

- ROI 不该只盯人效
- 很多真实价值来自更快、更稳、更少出错、更少风险

## 怎么用这页

- 学习时：先知道每条线为什么不该只看一个指标
- 设计时：拿它检查你的讨论是否停留在抽象层
- 面试时：用指标语言把“我懂”变成“我做过系统判断”

## 关联

- [[AI 五条主干专家工作台]]
- [[AI 五条主干关键问题]]
- [[AI 五条主干易混边界]]
- [[AI 五条主干面试表达要点]]
