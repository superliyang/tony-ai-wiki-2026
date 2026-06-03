---
title: AI Security Engineering Map
type: map
status: learning
tags:
  - ai/maps
  - ai/security
created: 2026-03-26
updated: 2026-03-27
---

# AI Security Engineering Map

```mermaid
flowchart TD
  SP["Security and Privacy"] --> TM["AI Security Threat Modeling"]
  TM --> PI["Prompt Injection Defense 与 Tool Safety"]
  TM --> MS["Model Supply Chain Security"]
  PI --> GR["Guardrails、Policy Enforcement 与 Security Gateways"]
  PI --> AP["Agent Security、Sandbox 与 Approval Architecture"]
  GR --> RT["AI Security Evaluation 与 Red Teaming"]
  MS --> RT
  RT --> CASES["AI 安全案例与失败模式"]
  RT --> GATE["Agent 上线门槛与安全 Release Gates"]
  GATE --> EVAL["Eval Harness 与 Regression Suites"]

  subgraph systems["Systems"]
    ACS["[[../../AI-Learning/09-Systems/Azure AI Content Safety（Jailbreak Detection）|Azure AI Content Safety（Jailbreak Detection）]]"]
    NG["[[../../AI-Learning/09-Systems/NVIDIA NeMo Guardrails|NVIDIA NeMo Guardrails]]"]
    CFG["[[../../AI-Learning/09-Systems/Cloudflare AI Gateway Guardrails|Cloudflare AI Gateway Guardrails]]"]
    MSCAN["[[../../AI-Learning/09-Systems/Protect AI ModelScan|Protect AI ModelScan]]"]
    PFO["[[../../AI-Learning/09-Systems/Promptfoo|Promptfoo]]"]
  end

  PI --> ACS
  GR --> NG
  GR --> CFG
  MS --> MSCAN
  RT --> PFO
```

## 关联

- [[../07-Topics/主题索引|主题索引]]
- [[../07-Topics/AI 安全案例与失败模式|AI 安全案例与失败模式]]
- [[../07-Topics/Agent 上线门槛与安全 Release Gates|Agent 上线门槛与安全 Release Gates]]
- [[../../AI-Learning/07-Maps/AI Security Threat Map|AI Security Threat Map]]
- [[AI Security 控制点图]]
- [[Agent Runtime Engineering Map]]
