---
title: "Memory Candidate: 合并添加广告投放 + LLM推理优化到学习主题"
created: 2026-06-15
status: pending-review
source: memory-review-scout
type: add (batch)
target: "00-Inbox-AI/agent-memory/learning-themes.md"
---

# Candidate: 合并添加「广告投放」和「LLM 推理优化工程」到学习主题

## 建议操作

**add (batch)** — 在 `learning-themes.md` 的 Active Themes 中添加：

> - Advertising technology (广告投放技术): programmatic advertising, RTB, DSP/SSP/ADX architecture, mobile game UA, SKAN signal engineering, incrementality testing, UA/product/finance KPI alignment. 已产出 ~60K 字领域全貌图 + MOC，待 source verification。
> - LLM inference optimization (LLM 推理优化工程): vLLM / SGLang / TensorRT-LLM / llama.cpp 推理引擎对比, Prefill vs Decode 瓶颈分析, KV Cache 管理策略, 量化/剪枝/Speculative Decoding, 语义缓存与成本控制, 消费级硬件部署优化。Phase 1 全貌图已完成（24KB），Phase 2-3 待继续。

## 变更理由

1. **合并两个 pending candidate 以减少积压**: 
   - 广告投放 candidate 创建于 06/05（pending 10 天）
   - LLM 推理 candidate 创建于 06/09（pending 6 天）
   - 两者的证据和模式高度相似——合并处理减少 Tony 决策负担

2. **两者均满足 canonical memory 写入标准**:
   - 广告投放: Tony 确认"方向没问题"，产出 5 个 vault 文件（~60K 字），06/14 batch review 已将广告投放标记为 accept-with-verification
   - LLM 推理: Tony 主动发起（"搞搞LLM推理优化工程"），Phase 1 领域全貌图已写入 vault

3. **与 Tony 角色高度相关**: 广告投放对应 skill gaming 行业，LLM 推理对应基础架构团队技术栈（K8s/AWS/网关→推理基础设施是自然延伸）

4. **learning-themes.md 最后更新 06/03**: 此后两个重大领域学习未被反映——canonical memory 与实际学习状态割裂 12 天

## 关联发现

memory-review-2026-06-15 的 F3

## 对已有 candidates 的影响

- 如接受本 candidate，pending `2026-06-05-add-advertising-to-learning-themes.md` 和 `2026-06-09-add-llm-inference-to-learning-themes.md` 可标记为 absorbed
- 广告投放的 source verification 任务已在 06/14 batch review 的 P3 中安排

## 备注

- 本 candidate 是合并提交，不是两个独立 candidate 的替代——这是有意为之以减少 Tony 的逐条决策负担
- 如果 Tony 只接受其中一个主题，可 split 后重新提交
