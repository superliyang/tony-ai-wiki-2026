---
title: "归因、SKAN 与信号损失"
created: 2026-06-05
updated: 2026-06-21
status: learning
source_status: verified-2026-06-21
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

## 2026-06 判断更新

本页当前以 Apple AdAttributionKit / SKAdNetwork 文档、Google Ads API release notes、Meta Graph API changelog、TikTok Business API blog 作为外部校验来源。

现在的长期判断是：

- 平台 API 和隐私归因框架会持续变化，广告知识库必须保留“API 版本更新”和“数据口径对账”两个 runbook。
- SKAN / AdAttributionKit 类聚合信号更适合做方向性优化和 cohort 校准，不适合拿来单独裁决真实 ROI。
- MMP、平台、BI、财务口径不一致是常态，成熟团队要定义“各自用于什么决策”，而不是追求一个万能真相。
- AI 素材和自动投放会放大数据质量问题：事件错、素材命名乱、归因窗口不清，会直接影响模型学习。

## 服务端信号补全

- Meta CAPI：用于提高事件匹配和服务端转化回传稳定性。
- Google Enhanced Conversions：用于增强转化匹配。
- sGTM：适合多平台、多事件、多地区治理，但要评估工程和合规成本。
- Event schema：事件命名、触发时机、去重键、用户标识必须治理。

## API / 数据变更检查

| 变化类型 | 影响 | 动作 |
|---|---|---|
| Google Ads API 版本变化 | 报表字段、转化、资产、自动化脚本可能变化 | [[10-Knowledge/Advertising/12-Runbooks/平台 API 版本更新 Runbook]] |
| Meta Graph / Marketing API 变化 | 权限、字段、广告对象、事件回传可能变化 | [[10-Knowledge/Advertising/12-Runbooks/平台 API 版本更新 Runbook]] |
| TikTok Business API 变化 | campaign、creative、reporting、event API 可能变化 | [[10-Knowledge/Advertising/12-Runbooks/平台 API 版本更新 Runbook]] |
| MMP / BI 差异扩大 | 预算、ROAS、渠道质量判断失真 | [[10-Knowledge/Advertising/12-Runbooks/MMP 与 BI 对账 Runbook]] |
| AI 素材自动化上线 | 素材质量、品牌风险、实验设计和数据追踪变重要 | [[10-Knowledge/Advertising/12-Runbooks/AI 素材自动化评审 Runbook]] |

## 决策边界

- 日常优化可以使用平台归因和 MMP 趋势。
- 预算战略要用 BI、财务和增量实验校准。
- 奖金与组织目标不要只绑定平台报表。
- 当隐私限制增强时，先治理事件质量，再讨论更复杂的模型。

## 相关

- [[增量测试与 MMM]]
- [[信号损失应对清单|信号损失应对清单]]
- [[来源与校验]]
- [[10-Knowledge/Advertising/12-Runbooks/动作库索引]]

## Sources

- [Apple AdAttributionKit](https://developer.apple.com/documentation/adattributionkit)
- [Apple SKAdNetwork](https://developer.apple.com/documentation/storekit/skadnetwork)
- [Google Ads API release notes](https://developers.google.com/google-ads/api/docs/release-notes)
- [Meta Graph API changelog](https://developers.facebook.com/docs/graph-api/changelog/)
- [TikTok Business API blog](https://business-api.tiktok.com/portal/blog)
