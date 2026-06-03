---
title: AI 记忆设计图
type: map
status: learning
tags:
  - ai/map
  - ai/memory
created: 2026-03-29
updated: 2026-03-29
---

# AI 记忆设计图

```mermaid
flowchart TD
  M["[[../06-Topics/AI 记忆设计|AI 记忆设计]]"] --> AM["[[../06-Topics/Agent Memory|Agent Memory]]"]
  M --> CM["[[../06-Topics/大模型记忆、项目记忆与 Chat Memory|大模型记忆、项目记忆与 Chat Memory]]"]
  M --> SE["[[../06-Topics/自我进化与持续学习的记忆设计|自我进化与持续学习的记忆设计]]"]

  AM --> OA["[[../09-Systems/OpenClaw 的分层记忆设计|OpenClaw 的分层记忆设计]]"]
  AM --> LM["[[../09-Systems/LangMem|LangMem]]"]
  AM --> LG["[[../09-Systems/LangGraph|LangGraph]]"]
  AM --> CC["[[../09-Systems/Claude Code|Claude Code]]"]
  AM --> ADK["[[../09-Systems/Google Agent Development Kit（ADK）|Google Agent Development Kit（ADK）]]"]

  OA --> ENG1["[[../../AI-Engineering/07-Topics/Session and Memory Design|Session and Memory Design]]"]
  LM --> ENG2["[[../../AI-Engineering/07-Topics/记忆写入、召回、压缩与 Consolidation|记忆写入、召回、压缩与 Consolidation]]"]
  LG --> ENG3["[[../../AI-Engineering/07-Topics/记忆架构：State、Memory、Artifact 与 Context|记忆架构：State、Memory、Artifact 与 Context]]"]
  CC --> ENG1
  ADK --> ENG3
  SE --> ENG4["[[../../AI-Engineering/07-Topics/记忆评测、污染、遗忘与纠偏|记忆评测、污染、遗忘与纠偏]]"]

  ENG1 --> LAB["[[../../AI-Engineering/06-Projects/Memory Lab/项目总览|Memory Lab]]"]
  ENG2 --> LAB
  ENG3 --> LAB
  ENG4 --> LAB
```

## 怎么读

- 上层先区分 memory 的抽象类型
- 中层看各家系统如何把 memory 做成正式能力
- 下层再看 engineering pattern 和实验项目

## 关联

- [[AI Agent Capability Map]]
- [[AI 记忆学习导航.canvas|AI 记忆学习导航（Canvas）]]
- [[AI 记忆学习导航.base|AI 记忆学习导航（Base）]]
- [[../../AI-Engineering/08-Maps/AI Memory Engineering Map|AI Memory Engineering Map]]
