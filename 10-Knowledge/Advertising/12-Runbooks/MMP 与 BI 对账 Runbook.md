---
title: "MMP 与 BI 对账 Runbook"
created: 2026-06-21
updated: 2026-06-21
status: learning
tags:
  - knowledge
  - advertising
  - runbook
  - measurement
---

# MMP 与 BI 对账 Runbook

## 适用场景

平台报表、MMP、BI、财务收入或产品事件出现明显差异时使用。

## 对账维度

| 维度 | 要核对什么 |
|---|---|
| 时间 | install time、event time、attribution time、timezone |
| 事件 | 事件定义、触发时机、去重键、延迟和重传 |
| 渠道 | campaign、adset、ad、creative、placement 映射 |
| 收入 | gross revenue、net revenue、refund、tax、FX |
| 用户 | 新老用户、跨设备、匿名 ID、登录 ID、隐私限制 |

## 操作步骤

1. 先确定一个统一观察窗口，例如过去 7 天安装 cohort。
2. 固定主口径：预算复盘用 BI / finance，日常优化用平台 + MMP 趋势。
3. 抽样 20-50 个订单或事件，串起平台、MMP、BI、订单系统。
4. 标出差异来源：归因窗口、时区、去重、延迟、退款、事件丢失。
5. 把结论写回指标字典和渠道复盘。

## 相关

- [[10-Knowledge/Advertising/05-Topics/归因、SKAN 与信号损失]]
- [[10-Knowledge/Advertising/05-Topics/指标体系与口径治理]]
