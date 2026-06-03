---
title: SaaS 订阅卡支付判断清单
type: playbook
status: learning
tags:
  - finance/payments
  - payments/playbook
  - payments/cards
  - payments/subscription
created: 2026-03-18
updated: 2026-03-18
---

# SaaS 订阅卡支付判断清单

## 这页解决什么问题

当你已经知道 `SaaS` 支付重在续费时，下一步要回答的是：我们到底该从哪些卡支付深水点入手，才能把续费成功率、被动流失和争议一起压住。

## 最优先看的 6 个判断点

1. 首单是否完成了稳定的 `Card-on-File` 建档
2. 后续续费是否被正确标记为 `MIT`
3. 欧洲等监管市场是否把 `SCA`、豁免和补认证路径设计清楚
4. 是否使用 `Network Tokenization` 或 `Account Updater` 提升老卡恢复率
5. 失败重试是否按失败原因分层，而不是粗暴重打
6. 是否对预争议、自动退款和续费提醒做了联动治理

## 逐项判断

### 1. Card-on-File / CIT / MIT

- 首单是不是清晰区分了用户主动发起和后续自动续费
- 首单认证、留卡、授权关系有没有建干净
- 续费重试是否仍被当成普通首单在打

### 2. SCA 与续费豁免

- 重点市场是否区分 `CIT` 与 `MIT`
- 软拒绝后是否有补认证恢复路径
- 是否一味追求少认证，反而损伤发卡行信任

### 3. Network Token / Account Updater

- 到期、换卡、补卡导致的失败占比高不高
- 是否有老客续费恢复率的专门指标
- 是否引入 updater 或 network token 能力

### 4. Descriptor 与主体

- 用户能否在账单上一眼认出这笔续费
- 不同国家是否用了合适的主体与 descriptor
- 是否存在“用户不认识扣款来源”导致的 friendly fraud

### 5. Pre-dispute / RDR

- 是否识别出哪些争议适合自动退款，哪些值得抗辩
- 续费提醒、客服和退款策略是否与争议治理联动
- 是否把 pre-dispute 当成核心续费质量指标之一

### 6. 模式选择

- 你们是自持 merchant + PSP，还是依赖 `MoR`
- 当前模式下是否已经影响 descriptor、主体控制和续费恢复能力
- 如果规模变大，是否需要更高控制力的 `orchestration` 或主体策略

## 最值得盯的指标

- 首单建档成功率
- `MIT` 成功率
- involuntary churn
- 到期/换卡类失败占比
- 预争议率与订阅相关拒付率
- 续费恢复净收入

## 适合搭配阅读

- [[../05-Topics/Card-on-File、CIT、MIT 与 SCA 豁免|Card-on-File、CIT、MIT 与 SCA 豁免]]
- [[../05-Topics/Network Tokenization 与 Account Updater|Network Tokenization 与 Account Updater]]
- [[../05-Topics/Pre-dispute、Ethoca、Verifi 与 RDR|Pre-dispute、Ethoca、Verifi 与 RDR]]
- [[SaaS 订阅支付作战手册]]
