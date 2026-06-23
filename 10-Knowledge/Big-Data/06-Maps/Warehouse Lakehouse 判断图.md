---
title: Warehouse Lakehouse 判断图
type: map
status: active
domain: Big-Data
updated: 2026-04-25
---

# Warehouse Lakehouse 判断图

```mermaid
flowchart TD
  A["核心问题是什么？"] --> B["稳定 BI 与指标口径"]
  A --> C["低成本沉淀多格式原始数据"]
  A --> D["多引擎复用同一份开放数据"]
  B --> E["优先 Warehouse"]
  C --> F["优先 Data Lake，但必须补 Catalog / Quality / Owner"]
  D --> G["考虑 Lakehouse"]
  G --> H["是否有平台能力管理表格式、Catalog、权限与性能？"]
  H -->|没有| I["先托管或简化架构"]
  H -->|有| J["Lakehouse + Governance + 多计算引擎"]
  E --> K["BI / SQL / 审计 / 稳定报表"]
  F --> L["原始数据 / 数据科学 / 探索处理"]
  J --> M["BI + ML + AI + 多团队复用"]
```

## 怎么读这张图

- Warehouse、data lake、lakehouse 不是简单新旧替代关系
- Lakehouse 的核心不是对象存储，而是开放存储上的表管理、catalog、治理和多引擎复用
- 如果团队平台能力不足，过早自建 lakehouse 可能放大复杂度

## 关联

- [[../05-Topics/Warehouse、Data Lake 与 Lakehouse|Warehouse、Data Lake 与 Lakehouse]]
- [[../大数据决策导航|大数据决策导航]]

