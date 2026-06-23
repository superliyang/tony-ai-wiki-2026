---
title: AI Security 控制点图
type: map
status: learning
tags:
  - ai/maps
  - ai/security
created: 2026-03-27
updated: 2026-03-27
---

# AI Security 控制点图

```mermaid
flowchart LR
  INPUT["输入与上下文"] --> DETECT["风险检测"]
  DETECT --> POLICY["策略与 Guardrails"]
  POLICY --> ACTION["Tool / Action Gate"]
  ACTION --> STATE["Memory / State"]
  POLICY --> OUTPUT["输出控制"]
  ART["Artifact / Model / Prompt / Image"] --> SUPPLY["Supply Chain Security"]
  DETECT --> RELEASE["Red Team / Regression / Release Gate"]
  ACTION --> RELEASE
  SUPPLY --> RELEASE
  RELEASE --> PROD["Production Rollout"]

  subgraph systems["代表系统"]
    ACS["[[../../AI-Learning/09-Systems/Azure AI Content Safety（Jailbreak Detection）|Azure AI Content Safety（Jailbreak Detection）]]"]
    CFG["[[../../AI-Learning/09-Systems/Cloudflare AI Gateway Guardrails|Cloudflare AI Gateway Guardrails]]"]
    NG["[[../../AI-Learning/09-Systems/NVIDIA NeMo Guardrails|NVIDIA NeMo Guardrails]]"]
    MSCAN["[[../../AI-Learning/09-Systems/Protect AI ModelScan|Protect AI ModelScan]]"]
    PFO["[[../../AI-Learning/09-Systems/Promptfoo|Promptfoo]]"]
  end

  DETECT --> ACS
  POLICY --> CFG
  POLICY --> NG
  SUPPLY --> MSCAN
  RELEASE --> PFO
```

## 怎么读

- 先看威胁从哪里进来
- 再看系统在哪个控制点接入
- 最后看 release gate 是否真的把这些控制点连成闭环

## 关联

- [[AI Security Engineering Map]]
- [[../07-Topics/AI 安全案例与失败模式|AI 安全案例与失败模式]]
- [[../07-Topics/Agent 上线门槛与安全 Release Gates|Agent 上线门槛与安全 Release Gates]]
- [[../../AI-Learning/07-Maps/AI Security Threat Map|AI Security Threat Map]]
