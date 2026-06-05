---
title: "长周期 Agent 的路由与推理优化：会话感知模型选择 + Nemotron 3 Ultra"
created: 2026-06-04
updated: 2026-06-04
status: pending
owner: hermes
priority: P2
domain: Multi-Agent-Orchestration
review_after: 2026-06-18
tags:
  - learning-task
  - hermes
  - agent-routing
  - long-running-agents
  - inference-optimization
---

# 长周期 Agent 的路由与推理优化：会话感知模型选择 + Nemotron 3 Ultra

## Why Now

Agent 正从单轮对话走向长周期任务——这意味着两个核心挑战：

1. **模型选择**：长任务中不同阶段需要不同模型能力（推理/执行/总结），固定模型导致性能衰减或成本浪费
2. **推理效率**：长周期 Agent 的推理延迟和 KV Cache 膨胀是隐藏的成本杀手

两个最新技术方案直接回应这些挑战：

- **vLLM 会话感知 Agent 路由**（2026-06-02）：根据对话历史自动选择最合适的模型，保持上下文连续性
- **NVIDIA Nemotron 3 Ultra**（2026-06-03）：专为 Agent 场景优化推理效率，解决长周期任务中模型性能衰减

同时，EDN 的技术分析揭示了 LLM 推理的隐藏瓶颈（内存带宽、KV Cache 管理），为理解这些优化方案提供了底层视角。

Tony 的 Hermes 在执行长时间 cron job 和多步骤工作流时，面临类似的模型选择和推理成本问题。

## Source

- URL: https://vllm.ai/blog/2026-06-02-session-aware-agentic-routing
- URL: https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-powers-faster-more-efficient-reasoning-for-long-running-agents/
- URL: https://www.edn.com/the-hidden-bottleneck-in-llm-inference-and-the-impact-on-mlperf-benchmarking/
- URL: https://vllm.ai/blog/2026-06-02-vllm-omni-autoround
- Source note: 2026-06-03 ~ 06-04 多批次 curated-scout 中出现路由和推理优化主题
- Captured evidence: `00-Inbox-AI/hermes/curated-scout/20260604-090044-summary.md` (#1, #4, #11), `20260603-210040-summary.md` (#2)

## Suggested Domain

`Multi-Agent-Orchestration` — 路由策略和推理优化是多 Agent 编排的核心工程问题，直接影响系统稳定性和运行成本

## Desired Output

- **learning package**: 会话感知路由的算法原理 + Nemotron 3 Ultra 的架构优势 + LLM 推理瓶颈全景
- **comparison map**: 固定模型 vs 会话感知路由 vs 混合路由 — 延迟/成本/连续性三维对比
- 附带：对 Hermes cron job / delegate_task 的模型选择策略改进建议

## Suggested Review Date

`2026-06-18` — P2 优先级，给 Codex 更多深研时间

## Safety Notes

- 路由策略变更可能影响 Hermes 所有自动化任务的模型选择行为
- Nemotron 3 Ultra 为 NVIDIA 闭源模型，需评估供应商锁定风险
- 推理优化方案的实测性能数据需要独立验证（不依赖厂商白皮书）

## Hermes Recommendation

- Decision: `study`
- Rationale: 这是前两个 P1 任务（MCP + Memory）的自然延伸——Agent 通信和记忆解决后，下一个瓶颈就是"用哪个模型、怎么跑得快"。vLLM 的路由策略和 NVIDIA 的硬件优化代表两种互补路径。P2 优先级，但深研价值高——直接指导 Hermes 的 delegate_task 和 cron job 的模型选择策略。
