---
title: AI 五条主干关键问题
type: topic
status: active
tags:
  - ai/topic
  - ai/workbench
  - ai/questions
created: 2026-04-13
updated: 2026-04-13
---

# AI 五条主干关键问题

> 这页不是知识清单，而是判断清单。
> 当你在回顾、评估、设计或面试时，先问对问题，往往比先背答案更重要。

## 1. 模型形成线

对应主干：

- [[模型形成线：Pretraining、Transformer、Foundation Models、Reasoning 与 Multimodal]]

关键问题：

- 现代模型能力的底座究竟来自 pretraining、architecture 还是 post-training？
- 当前能力提升更主要来自 scaling、reasoning 训练，还是 multimodal 扩展？
- 这项能力是“模型原生会”，还是“系统包装后看起来会”？
- 当前讨论的是能力边界，还是产品边界？
- long context、reasoning、multimodal 分别解决了什么，不解决什么？

## 2. 能力升级线

对应主干：

- [[能力升级线：Prompt、Context、RAG、Tool Use、Agent、Memory 与 Multi-Agent]]

关键问题：

- 当前瓶颈是 prompt 不够清楚，还是 context 不够好？
- 事实问题应该靠 RAG、memory，还是靠更强模型解决？
- 什么情况下需要 tool use，什么情况下不该让模型直接行动？
- 这是单 agent 问题，还是显式 workflow 更合适？
- multi-agent 是真的提高了任务完成率，还是只是把复杂度前置？

## 3. 运行时工程线

对应主干：

- [[运行时工程线：Inference、Serving、Evaluation、Release Gate 与 Security]]

关键问题：

- 当前线上问题的瓶颈在模型能力、路由、serving 还是 eval 缺失？
- 成本、延迟、吞吐量三者哪个是当前主约束？
- 系统是否具备可回归比较的 eval 基线？
- release gate 是基于真实风险，还是只是人为流程？
- 事故发生后能否快速区分是模型退化、工具问题还是运行时问题？

## 4. 安全治理线

对应主干：

- [[安全治理线：AI Safety、AI Security、Prompt Injection、Approval、Audit 与 Release Gate]]

关键问题：

- 当前讨论的是 safety 问题还是 security 问题？
- 风险是来自输出误导，还是来自动作越权与权限泄露？
- 哪些动作必须经过 approval，哪些动作可以自动化？
- 是否具备足够的 audit trace 来做追责和复盘？
- security control 是停在 guardrail 层，还是已经进入 release gate 和 incident loop？

## 5. 产品落地线

对应主干：

- [[产品落地线：Model、Workflow、Case Study、Rollout、ROI 与 Governance]]

关键问题：

- 这个能力更适合做 assistant、copilot，还是 workflow automation？
- 产品表面看起来是聊天，但真正的价值落在哪个 workflow？
- 这个 case 的成功来自模型能力，还是流程重构与组织改造？
- rollout 的关键阻力在技术、组织、权限还是行为改变？
- ROI 真正体现在哪些经营指标上，谁是 owner？

## 怎么用这页

- 如果你在学习：先用这页判断每条线最值得追的方向
- 如果你在做设计：用这页防止系统讨论一上来就跑偏
- 如果你在准备面试：把这些问题变成你讲项目时主动抛出的 framing

## 关联

- [[AI 五条主干专家工作台]]
- [[AI 五条主干核心指标]]
- [[AI 五条主干易混边界]]
- [[AI 五条主干面试表达要点]]
