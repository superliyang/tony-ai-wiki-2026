---
title: Enterprise LLMOps Vendor Choice Map
type: map
status: learning
tags:
  - ai/maps
  - ai/llmops
  - ai/vendor-selection
created: 2026-03-26
updated: 2026-03-26
---

# Enterprise LLMOps Vendor Choice Map

```mermaid
flowchart TD
  Q["企业 LLMOps 需求"] --> A["Experiment / Registry Governance"]
  Q --> B["LLM / Agent Trace + Scores"]
  Q --> C["Pre-release Eval / Red Team"]
  Q --> D["Self-hosting / Data Residency"]

  A --> MLF["[[../../AI-Learning/09-Systems/MLflow|MLflow]]"]
  A --> WNB["[[../../AI-Learning/09-Systems/Weights & Biases Platform|Weights & Biases Platform]]"]
  B --> LFS["[[../../AI-Learning/09-Systems/Langfuse|Langfuse]]"]
  B --> PHX["[[../../AI-Learning/09-Systems/Arize Phoenix|Arize Phoenix]]"]
  C --> PFO["[[../../AI-Learning/09-Systems/Promptfoo|Promptfoo]]"]
  D --> LFS
  D --> PHX
  D --> MLF
  D --> WNB

  MLF --> OSS["open-source lifecycle"]
  WNB --> COL["research-to-app collaboration"]
  LFS --> APP["LLM / agent app workbench"]
  PHX --> OBS["trace-first observability"]
  PFO --> GATE["CI / regression / red team gate"]
```

## 怎么读

- 先不要问“谁最好”
- 先问“我们现在最缺哪一层控制点”
- 再看 deployment 模式和数据边界是否允许

## 关联

- [[../07-Topics/Enterprise MLOps 与 LLMOps Vendor Tradeoffs|Enterprise MLOps 与 LLMOps Vendor Tradeoffs]]
- [[../07-Topics/Open-Source、Self-Hosting 与 Managed LLMOps|Open-Source、Self-Hosting 与 Managed LLMOps]]
- [[../06-Projects/Enterprise LLMOps/项目总览|Enterprise LLMOps]]
