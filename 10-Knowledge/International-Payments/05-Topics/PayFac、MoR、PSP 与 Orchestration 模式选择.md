---
title: PayFac、MoR、PSP 与 Orchestration 模式选择
type: topic
status: learning
tags:
  - finance/payments
  - payments/business-model
  - payments/commercial
created: 2026-03-18
updated: 2026-03-18
---

# PayFac、MoR、PSP 与 Orchestration 模式选择

## 这页解决什么问题

支付做大以后，最难的问题之一不是“接不接某个通道”，而是“我们到底要用什么经营模式承接支付”。`PayFac`、`MoR`、传统 `PSP` 接入、payment orchestration，并不是几种技术名词，而是四种完全不同的责任、收益、合规和控制力分配方式。

## 四种模式先抓住什么

- `PSP`：你自己还是 merchant，只是借 PSP 的支付能力接入通道
- `MoR`：`Merchant of Record`，由第三方作为记录商户承接交易与部分合规/税务/退款责任
- `PayFac`：你自己或你的平台作为支付聚合方，承接更强的子商户管理和支付责任
- `Orchestration`：重点不在法律身份，而在通过编排层统一管理多个 PSP / acquirer / payment method

## 真正的差异在哪里

### 1. 控制力

从低到高，大致常见是：`MoR -> PSP -> Orchestration -> PayFac`。但控制力越高，承担的责任通常也越多。

### 2. 上线速度

`MoR` 通常最快，`PSP` 次之，`Orchestration` 和 `PayFac` 往往需要更强的内部能力。

### 3. 合规与运营负担

`MoR` 帮你扛掉一部分，`PayFac` 则会把更多责任拉回到自己这边。

### 4. 费率与经济模型

短期看，`MoR` 可能更贵但更省事；长期做大后，自建更多控制能力或 orchestration 可能更有经济性。

## 什么时候适合哪种模式

### 1. 业务还在验证期

优先看 `MoR` 或标准 `PSP`，先把市场验证跑起来。

### 2. 已经有规模，开始被成本和成功率卡住

这时候通常会考虑 multi-PSP、`orchestration`、多主体与多 `MID` 策略。

### 3. 平台型业务、子商户场景

如果你要深度管理商户入驻、结算、风控和责任分层，`PayFac` 逻辑会更 relevant，但同时意味着更高合规和运营复杂度。

## 业务案例

### 案例 1：SaaS 初期追求全球上线速度

用 `MoR` 可以快速跑多市场，但做到一定规模后，团队会发现费率、descriptor、主体和客户体验控制不够，开始转向自持 merchant + PSP / orchestration。

### 案例 2：Marketplace 想做更细的商户治理

单纯 `PSP` 接入不够，就会开始考虑更深的子商户和资金流能力。但这一步不该只由技术推动，还要看合规、清结算、商务条款与运营能力能不能接住。

## 最值得看的判断维度

- 上线速度 vs 长期控制力
- 费率与总成本
- 合规和牌照压力
- 是否需要多主体 / 多 `MID` / 多市场本地化
- 是否需要更强的子商户和资金流管理
- 内部团队是否有能力运营复杂支付系统

## 常见误区

- 把 orchestration 当成单纯技术中间层
- 以为 PayFac 只是“接更多通道”
- 只看单笔费率，不看长期控制力和合规代价
- 业务和法务、财务、支付技术团队没有一起做模式选择

## 关联

- [[支付系统架构与核心服务]]
- [[收单行、PSP 与通道管理]]
- [[PSP 与 Acquirer 选型框架]]
- [[多实体收款与结算架构]]
- [[支付费率、成本与单位经济]]
- [[MCC、Descriptor、MID 与主体策略]]
