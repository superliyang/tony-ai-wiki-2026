---
title: SWIFT 流程图
type: map
status: learning
tags:
  - finance/maps
created: 2026-03-13
updated: 2026-03-14
---

# SWIFT 流程图

```mermaid
flowchart LR
    A[付款人] --> B[付款银行]
    B --> C[SWIFT 报文]
    C --> D[中间行/代理行]
    D --> E[收款银行]
    E --> F[收款人]

    B -.可能持有.-> G[Nostro/Vostro 账户]
    D -.可能检查.-> H[合规筛查]
```

## 怎么看这张图

- 实线是“信息和支付指令的大致流向”
- 虚线提醒你：真正的账户关系和合规检查不一定直接显示在用户前台
- 这张图最重要的结论是：`SWIFT` 是通信和指令层，不是“钱自动飞过去”的那一层

## 关联

- [[../05-Topics/SWIFT 与代理行体系|SWIFT 与代理行体系]]
- [[../05-Topics/Nostro 与 Vostro 账户|Nostro 与 Vostro 账户]]
