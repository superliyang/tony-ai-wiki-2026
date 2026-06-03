---
title: 预充值与 Prefunding 管理
type: topic
status: learning
tags:
  - finance/payments
  - payments/treasury
  - payments/prefunding
created: 2026-03-15
updated: 2026-03-15
---

# 预充值与 Prefunding 管理

## 这页解决什么问题

很多跨境收单、代发和本地支付方式都要求你先准备资金。`Prefunding` 管理做不好，会出现两种极端：钱备少了业务掉量，钱备多了现金效率变差。

## 核心问题

- 每个通道和市场要备多少资金
- 哪些国家和方式需要单独的 prefund buffer
- 什么时候补、补多少、谁来批准

## 一个成熟思路

- 按通道、国家、币种和业务场景分池管理
- 为高波动场景设置更高 buffer
- 结合结算节奏、周末、节假日和活动流量做预测

## 常见误区

- 所有通道只看一个总余额
- 只按日常均值备付，不看波峰
- 业务、财务和支付运营对 prefund 没有统一 owner

## 关联

- [[Settlement Calendar 与结算节奏管理]]
- [[多币种资金池管理]]
- [[跨境汇款与代发作战手册]]
- [[通道季度复审清单]]
