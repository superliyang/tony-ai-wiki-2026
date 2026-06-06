---
title: "归因、SKAN 与信号损失"
created: 2026-06-05
updated: 2026-06-05
status: seed
source_status: needs-url-verification
tags:
  - knowledge
  - advertising
  - attribution
---

# 归因、SKAN 与信号损失

## 核心观点

隐私变化后的广告测量，不是寻找一个“绝对正确”的归因工具，而是在平台归因、MMP、SKAN、BI、实验和财务数据之间建立校准关系。

## 为什么会不一致

- 平台归因窗口不同。
- click-through 和 view-through 的定义不同。
- 多平台会重复 claim 同一个转化。
- iOS、Safari、Firefox 等环境限制用户级追踪。
- SKAN 提供的是聚合、延迟、受限信号。
- 服务端回传事件可能存在缺失、延迟或重复。
- BI 往往以真实订单、收入、退款和用户生命周期为准。

## SKAN 下的思路

- 不要只等长期收入信号，先设计早期 proxy：注册、激活、教程完成、关键行为、首日留存。
- 把 coarse value 和 fine value 设计成可解释的业务分层，而不是随意编码。
- 让产品事件、MMP 映射、BI 口径和平台优化目标对齐。
- 用 cohort 和 holdout 校准早期信号对 LTV 的预测能力。

## 服务端信号补全

- Meta CAPI：用于提高事件匹配和服务端转化回传稳定性。
- Google Enhanced Conversions：用于增强转化匹配。
- sGTM：适合多平台、多事件、多地区治理，但要评估工程和合规成本。
- Event schema：事件命名、触发时机、去重键、用户标识必须治理。

## 决策边界

- 日常优化可以使用平台归因和 MMP 趋势。
- 预算战略要用 BI、财务和增量实验校准。
- 奖金与组织目标不要只绑定平台报表。
- 当隐私限制增强时，先治理事件质量，再讨论更复杂的模型。

## 相关

- [[增量测试与 MMM]]
- [[信号损失应对清单|信号损失应对清单]]
- [[来源与校验]]

