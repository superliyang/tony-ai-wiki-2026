---
title: Enterprise AI Security Operating Model Map
type: map
status: learning
tags:
  - ai/maps
  - ai/security
  - ai/operating-model
created: 2026-03-27
updated: 2026-03-27
---

# Enterprise AI Security Operating Model Map

```mermaid
flowchart LR
  APP["产品 / 应用团队"] --> TM["Threat Modeling"]
  PLATFORM["平台 / Agent 平台团队"] --> CTRL["Control Points"]
  SEC["Security / AppSec / GRC"] --> BOARD["Review Board / Exceptions"]
  OWNER["业务 / 风险 Owner"] --> SHIP["Ship / No-Ship"]

  TM --> GATE["Release Gates"]
  CTRL --> GATE
  BOARD --> GATE
  GATE --> PROD["Production"]
  PROD --> TEL["Telemetry / Alerts"]
  TEL --> IR["Incident Response"]
  IR --> REG["Regression / Policy Update"]
  REG --> GATE
```

## 怎么读

- 左边是组织角色
- 中间是控制和审批
- 右边是生产、事件与回流闭环

## 关联

- [[AI Security 控制点图]]
- [[../07-Topics/Enterprise AI Security Operating Model|Enterprise AI Security Operating Model]]
- [[../07-Topics/AI Security Telemetry、Escalation 与 Incident Response|AI Security Telemetry、Escalation 与 Incident Response]]
- [[../06-Projects/AI Security Governance/项目总览|AI Security Governance]]
