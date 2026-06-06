---
title: "RTB 与程序化广告链路"
created: 2026-06-05
updated: 2026-06-05
status: seed
tags:
  - knowledge
  - advertising
  - adtech
---

# RTB 与程序化广告链路

## 一句话

程序化广告是把广告位、用户信号、出价策略、预算约束和素材匹配压缩到毫秒级交易里的系统。

## 核心链路

1. 用户打开媒体页面或 App。
2. 媒体通过 SSP 发起广告请求。
3. Exchange / ADX 汇聚请求，并把 bid request 发给多个 DSP。
4. DSP 根据用户、上下文、预算、频控、预估转化率和出价策略决定是否竞价。
5. 交易市场选出胜出广告。
6. 广告曝光、点击、安装、转化等事件回传到平台、MMP 和 BI。
7. 后续数据进入优化模型、预算决策和复盘系统。

## 关键问题

- 这次曝光是真实用户看到的吗？
- DSP 拿到的信号够不够判断价值？
- 出价是为了赢曝光，还是为了买到高 LTV 用户？
- 中间链路抽成、重复供给、低质媒体是否侵蚀了效率？
- 转化回传是否足够快、准、稳定？

## 交易模式对比

- Open Exchange：量大、便宜、透明度和质量波动更大。
- PMP：供应更可控，适合在质量和规模之间折中。
- Programmatic Guaranteed：量和价格更确定，适合品牌安全、确定性供给和大型合作。
- Direct Deal：谈判成本高，但可获得更明确的资源、数据和协同。

## 专家关注点

- Supply Path Optimization：减少重复拍卖和无效中间层。
- Auction dynamics：一价/二价拍卖、floor price、bid shading 对成本的影响。
- Frequency capping：避免过度触达同一用户。
- Brand safety：避免广告出现在不合适内容旁边。
- Post-bid vs pre-bid filtering：投前过滤通常比投后补救更重要。

## 相关

- [[广告欺诈与品牌安全]]
- [[广告投放链路架构图|广告投放链路架构图]]
- [[渠道评估模板|渠道评估模板]]

