---
title: "Memory Candidate: 添加「LLM 推理优化工程」到学习主题"
created: 2026-06-09
status: pending-review
source: memory-review-scout
type: add
target: "00-Inbox-AI/agent-memory/learning-themes.md"
---

# Candidate: 添加「LLM 推理优化工程」到学习主题

## 建议操作

**add** — 在 `learning-themes.md` 的 Active Themes 中添加：

> - LLM inference optimization (LLM推理优化工程): vLLM / SGLang / TensorRT-LLM / llama.cpp 推理引擎对比，Prefill vs Decode 瓶颈分析，KV Cache 管理策略，量化/剪枝/Speculative Decoding，语义缓存与成本控制，消费级硬件部署优化。

## 变更理由

1. **Tony 主动发起深度领域学习**：2026-06-07，Tony 说"搞搞LLM推理优化工程"，触发了 domain-expert-learning 全流程。Phase 1 全貌图已完成并写入 `00-Inbox-AI/hermes/llm-inference-optimization-领域全貌图-draft.md`（24KB, 12 sections），Phase 2-3 待继续。

2. **符合 precedent**：2026-06-05 的"广告投放"采用完全相同的模式（Tony 说方向没问题 → 产出 vault draft → 候选 → canonical），"LLM推理优化"满足同等条件。

3. **与 Tony 背景高度相关**：
   - Tony 负责基础架构团队，技术栈含 K8s/AWS/Nginx/网关 — 推理基础设施是自然延伸
   - 属于 `AI engineering and agent tooling` 的子方向（已存在于 Active Themes）
   - 与最近 curated-scout 高频出现的推理优化信号（缓存/量化/消费级部署）形成闭环

4. **当前 `learning-themes.md` 缺失**：活跃主题中无推理/基础设施优化相关条目，但 Tony 的技术角色和近期学习行为表明这应是活跃方向。

## 关联发现

memory-review-2026-06-09 的 F5

## 备注

- 学习产出位置：`00-Inbox-AI/hermes/llm-inference-optimization-领域全貌图-draft.md`
- Phase 2 & 3 尚未执行（Tony 未继续），但如果接受本候选，可考虑触发 `build learning map LLM推理优化` 进入正式 domain learning 流程
- 与 F2（广告投放）是同一类问题：Tony 的实际学习行为未反映到 canonical memory
