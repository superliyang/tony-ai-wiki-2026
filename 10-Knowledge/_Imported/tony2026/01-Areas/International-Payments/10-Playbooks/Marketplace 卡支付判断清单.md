---
title: Marketplace 卡支付判断清单
type: playbook
status: learning
tags:
  - finance/payments
  - payments/playbook
  - payments/cards
  - payments/marketplace
created: 2026-03-18
updated: 2026-03-18
---

# Marketplace 卡支付判断清单

## 这页解决什么问题

对 `Marketplace` 来说，卡支付深水区不只是买家刷卡成功率，而是商户主体、平台责任、结算模式、descriptor、争议归因和 `PayFac / MoR / PSP` 模式如何共同决定平台风险边界。

## 最优先看的 6 个判断点

1. 平台到底在支付里扮演什么角色
2. 买家支付和卖家结算是不是被一套清晰主体与责任模型承接
3. descriptor、`MID` 和 merchant identity 是否足够清晰
4. 退款、争议、预争议是否能定位到平台、卖家和履约责任
5. 是否需要更高控制力的 `PayFac` 或 orchestration
6. 当前模式下的合规、资金和运营能力能不能接住

## 逐项判断

### 1. PayFac / MoR / PSP / Orchestration

- 当前模式是否匹配平台规模与责任边界
- 如果平台要深度管理商户、分账、reserve、提现，现有模式是否足够
- 是不是技术想做 orchestration，但法务、财务和运营能力还没跟上

### 2. MCC / Descriptor / MID / 主体

- 买家账单看到的是谁
- 平台主体、卖家主体和收款主体之间是否清楚
- 不同业务线或国家是否需要拆不同 `MID` 与主体

### 3. Authorization / Capture / Reversal

- 订单取消、部分履约、退款回滚时，状态机是否能跟住
- 是否存在 auth 成功但卖家无法履约、最后 reversal 不及时的问题
- 是否把 buyer-side 支付动作和 seller-side 结算动作混在一起理解

### 4. Pre-dispute / 争议治理

- 争议是来自买家不认、卖家问题还是平台规则不清
- 预争议时能否快速判断是退款、找卖家补证据，还是平台承担
- 是否把卖家行为纳入争议治理与 reserve 调整

### 5. Descriptor 与平台体验

- 用户是否知道扣款来自平台还是某个商户
- 卖家服务差是否最后表现为平台拒付问题
- descriptor、客服和订单查询体验是否统一

### 6. 长期模式升级

- 当国家变多、商户变多、资金流变复杂后，是否要从单一 `PSP` 模式升级
- 如果考虑 `PayFac`，是否已经准备好 `KYC / KYB`、reserve、清结算、风控和账本能力

## 最值得盯的指标

- 买家卡支付成功率
- 平台与卖家责任分布下的争议率
- descriptor 相关争议占比
- reserve 覆盖率与提现欺诈损失
- 不同模式下的平台净收入与运营复杂度

## 适合搭配阅读

- [[../05-Topics/PayFac、MoR、PSP 与 Orchestration 模式选择|PayFac、MoR、PSP 与 Orchestration 模式选择]]
- [[../05-Topics/MCC、Descriptor、MID 与主体策略|MCC、Descriptor、MID 与主体策略]]
- [[../05-Topics/Authorization、Capture、Reversal 与 Incremental Auth|Authorization、Capture、Reversal 与 Incremental Auth]]
- [[../05-Topics/Pre-dispute、Ethoca、Verifi 与 RDR|Pre-dispute、Ethoca、Verifi 与 RDR]]
- [[Marketplace 平台支付作战手册]]
