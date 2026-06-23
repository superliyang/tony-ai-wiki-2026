---
title: Batch Streaming 判断图
type: map
status: active
domain: Big-Data
updated: 2026-04-25
---

# Batch Streaming 判断图

```mermaid
flowchart TD
  A["业务是否依赖低延迟动作？"] -->|否| B["优先 Batch"]
  A -->|是| C["是否需要连续状态？"]
  C -->|否，只是更快看到| D["Near-real-time / Micro-batch"]
  C -->|是| E["优先 Streaming"]
  E --> F["能否接受复杂状态、迟到数据、回放成本？"]
  F -->|不能| G["重新切业务边界，保留 Batch 校准"]
  F -->|能| H["Streaming + Batch 回补/审计"]
  B --> I["离线口径、历史重算、稳定报表"]
  D --> J["准实时看板、轻量监控"]
  H --> K["实时风控、推荐、告警、事件驱动流程"]
```

## 怎么读这张图

- 如果只是“更快看到数据”，不一定需要完整 streaming 架构
- 如果数据会触发业务动作，才真正进入 streaming 判断
- 如果涉及财务、审计、监管或最终口径，通常仍需要 batch 校准

## 关联

- [[../05-Topics/Batch 与 Streaming 判断框架|Batch 与 Streaming 判断框架]]
- [[../大数据决策导航|大数据决策导航]]

