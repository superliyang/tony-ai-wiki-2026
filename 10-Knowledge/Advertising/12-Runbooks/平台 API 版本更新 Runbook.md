---
title: "平台 API 版本更新 Runbook"
created: 2026-06-21
updated: 2026-06-21
status: learning
tags:
  - knowledge
  - advertising
  - runbook
  - api
---

# 平台 API 版本更新 Runbook

## 适用场景

Google Ads API、Meta Graph / Marketing API、TikTok Business API 或 MMP API 有版本、字段、权限、报表口径变化时使用。

## 检查步骤

1. 查看官方 release notes / changelog，标出 breaking changes、deprecated fields、new metrics。
2. 盘点内部依赖：拉数脚本、投放自动化、报表、BI、告警、实验看板。
3. 建立字段映射：旧字段、新字段、口径差异、影响报表。
4. 在 sandbox 或小流量账号跑回归，比较过去 7 天数据差异。
5. 更新数据字典和自动化任务，记录切换日期。

## 验收标准

- 关键报表没有静默断数。
- 花费、转化、收入、ROAS、SKAN / MMP 口径变化有说明。
- 自动化投放任务有 rollback 路径。

## Sources

- [Google Ads API release notes](https://developers.google.com/google-ads/api/docs/release-notes)
- [Meta Graph API changelog](https://developers.facebook.com/docs/graph-api/changelog/)
- [TikTok Business API blog](https://business-api.tiktok.com/portal/blog)
