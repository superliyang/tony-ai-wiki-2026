---
title: "NVIDIA AA-AgentPerf：首个公开多供应商 Agent 编码基准测试"
created: 2026-06-12
updated: 2026-06-12
status: pending
owner: hermes
priority: P2
domain: "AI-Infrastructure"
review_after: "2026-06-26"
tags:
  - learning-task
  - hermes
  - agent-benchmark
  - agent-throughput
  - nvidia
  - gb300
  - deepseek
  - ai-infrastructure
sources:
  - "https://developer.nvidia.com/blog/nvidia-achieves-leading-agentic-coding-performance-on-first-agentic-ai-benchmark/"
---

# NVIDIA AA-AgentPerf：首个公开多供应商 Agent 编码基准测试

## Why Now

2026-06-12 下午，NVIDIA 发布了业界首个公开的多供应商 Agent 编码基准测试 **AA-AgentPerf**（Agentic AI Agent Performance）。这不是一个模型 benchmark（如 MMLU、HumanEval），而是一个**专门测量并发 Agent 吞吐量**的基础设施基准：

- **基准模型**: DeepSeek-V4-Pro — Tony 当前主力模型被选为行业参考基准，信号意义重大
- **核心指标**: Agent 并发容量，以 agents/MW（每兆瓦 Agent 数）衡量
- **NVIDIA GB300 NVL72**: 61.4K agents/MW，是 H200（2.6K）的 **20 倍**
- **测试方法**: 使用预录制的真实代码仓库 agent 轨迹，包含工具调用延迟和可变序列长度

**对 Tony 的战略意义**: 
1. Agent 推理从"无标准"进入"可量化"阶段 — 意味着行业正在为大规模 Agent 部署做准备
2. DeepSeek-V4-Pro 成为基准模型 — Tony 日常使用的模型是行业关注焦点
3. GB300 的 20x 提升暗示 Agent 推理硬件正从"通用 GPU"走向"Agent 专用优化"
4. 与 `kv-cache-inference-economics` (P2 pending) 互补：KV Cache 解决"单次推理成本"，AA-AgentPerf 解决"并发 Agent 容量"

## What To Learn

**核心问题**: AA-AgentPerf 基准测试的方法论、数据和产业意义是什么？Agent 推理基准的出现如何影响 Agent 系统架构设计？

**学习路径**:
1. 精读 NVIDIA 原文 — 理解 benchmark 方法论（并发模型、工具调用模拟、轨迹回放）
2. 对比现有 benchmark — MLPerf、HumanEval、SWE-bench 与 AA-AgentPerf 的定位差异
3. 分析 GB300 NVL72 架构 — 为什么能实现 20x agents/MW？对 Agent 推理意味着什么？
4. 评估 DeepSeek-V4-Pro 作为基准模型的意义 — 为什么选它而不是 GPT/Claude？
5. 产出：Agent 推理基准综述 + 对 Hermes 基础设施选型的建议

**关键维度**:
- Benchmark 设计：并发 Agent 数 vs 单 Agent 延迟，哪个更重要？AA-AgentPerf 为什么选择并发吞吐？
- 硬件架构：GB300 NVL72 的推理优化（显存带宽、互联拓扑、批处理策略）
- 工具调用的模拟：如何记录和回放 agent 轨迹？工具调用延迟如何注入？
- Agent 推理 vs 传统推理：为什么 agent 推理需要专门的 benchmark？
- DeepSeek 选型：行业共识的形成 — DeepSeek 是否正在成为 Agent 场景的默认模型？

## Expected Output

一篇 2-3 页的中文分析备忘，包含：
1. AA-AgentPerf benchmark 方法论解析
2. Agent 推理基准与其他 benchmark 的对比定位
3. Agent 推理硬件趋势（GB300 → 推测下一代）
4. 对 Hermes/Codex Agent 系统基础设施规划的启示
5. 写入 `00-Inbox-AI/hermes/` 待审核

## 参考优先级

- P0 (必读): NVIDIA AA-AgentPerf 原文
- P1 (建议): DeepSeek-V4-Pro 技术报告（API 文档中的推理参数）+ GB300 架构白皮书
- P2 (速览): MLPerf Inference v5.0 agent 相关条目 + 其他 agent benchmark（SWE-bench multi-agent 变体）

## Suggested Domain

`AI-Infrastructure`

## Desired Output

decision memo

## Proposed Canonical Destination

- `10-Knowledge/AI-Infrastructure/05-Topics/agent-inference-benchmark-aa-agentperf.md`
- `20-Maps/ai-infrastructure-landscape.md`（新增 Agent 推理基准维度）

## Codex Handoff Contract

- Hermes writes this task only in `00-Inbox-AI/learning-tasks/pending/`.
- Hermes may attach drafts in `00-Inbox-AI/hermes/`.
- Hermes must not write directly into `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, `40-Projects/`, `60-Agents/`, or `90-Agent-System/`.
- Codex researches, restructures, and prepares the learning package.
- Tony reviews before canonical promotion.

## Suggested Review Date

`2026-06-26`

## Safety Notes

本任务分析的是 NVIDIA 公开 benchmark 结果和技术文档，不涉及机密信息。注意区分 NVIDIA 作为硬件厂商的"benchmark 营销"与独立验证的 benchmark 数据。DeepSeek-V4-Pro 作为基准模型是 NVIDIA 的选择，不代表 DeepSeek 官方立场。如涉及 GB300 定价或 Tony 团队的硬件采购决策，应由 Tony 独立评估。

## Hermes Recommendation

- Decision: `study`
- Rationale: AA-AgentPerf 是业界首个公开的多供应商 Agent 推理基准，标志着 Agent 基础设施从"实验"进入"工程化"阶段。选择 DeepSeek-V4-Pro 作为基准模型直接关联 Tony 的日常工具链。与 `kv-cache-inference-economics`(P2 pending) 在推理基础设施维度上互补——前者看单次推理成本，本任务看并发 Agent 容量。GB300 20x 提升暗示 Agent 推理硬件正走向专用化——这对理解 Agent 系统的规模化部署路径有直接意义。

## Follow-Up Proposal

- Suggested review cadence: 2 周
- Suggested spaced review prompt: 「AA-AgentPerf 是否有独立复现结果？DeepSeek-V4-Pro 的 Agent 推理性能在其他 benchmark 上表现如何？Agent 基准测试的标准化进展（是否有 IEEE/MLCommons 参与）？」
