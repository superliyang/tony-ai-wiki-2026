---
title: Regulated Industry Agent Map
type: map
status: learning
tags:
  - ai/maps
  - ai/applications
  - ai/regulation
created: 2026-03-23
updated: 2026-03-24
---

# Regulated Industry Agent Map

```mermaid
graph TD
    A["Regulated Industries"] --> B["Financial Services"]
    A --> C["Healthcare"]
    A --> D["Legal and Compliance"]
    A --> F["Public Sector"]

    B --> B1["Value: advisor productivity, knowledge access, multilingual support"]
    B --> B2["Need: evals, privacy, auditable outputs"]
    B --> B3["Case: Morgan Stanley"]

    C --> C1["Value: documentation relief, claims ops, evidence retrieval"]
    C --> C2["Need: HIPAA, access control, clinician oversight"]
    C --> C3["Case: Oscar, OpenAI for Healthcare"]

    D --> D1["Value: drafting, citation, contract comparison"]
    D --> D2["Need: source grounding, reviewability, low hallucination"]
    D --> D3["Case: Harvey"]

    F --> F1["Value: secure knowledge work, admin support, policy navigation"]
    F --> F2["Need: auditability, deployment fit, policy compliance"]
    F --> F3["Case: ChatGPT Gov"]

    B2 --> E["Common Governance Requirements"]
    C2 --> E
    D2 --> E
    F2 --> E

    E --> E1["Single Source of Truth"]
    E --> E2["Human Approval Gates"]
    E --> E3["Task-Level Evals"]
    E --> E4["Auditability and Evidence"]
```

## 怎么看这张图

- 这张图不是讲行业大小，而是讲“高监管行业里，agent 为什么难，又为什么值”
- 这些行业的共同点是：价值高，但治理要求更高
- 越进入真实生产环境，越要把 eval、审批、证据和审计能力前置
- 如果要继续比较产品层，下一步应配合 [[High-Trust Agent Vendor Selection]] 一起看
- 如果要继续判断组织应该停留在 assistant 还是进入 runtime，也应配合 [[Assistant-to-Runtime Migration in High-Trust Domains]] 一起看

## 关联

- [[../01-Industries/Financial Services Agents|Financial Services Agents]]
- [[../01-Industries/Healthcare Agents|Healthcare Agents]]
- [[../01-Industries/Legal and Compliance Agents|Legal and Compliance Agents]]
- [[Assistant-to-Runtime Migration Map]]
- [[Agent Industry Value Map]]
