# 行业理解 Growth Track — AI 基础设施：推理经济学的临界点

**日期:** 2026-06-15（周一）
**方向:** AI 基础设施（推理/训练市场）
**状态:** 待学习

---

## 今日行业

2026 年 AI 基础设施正在经历结构性转折——**推理（inference）已取代训练（training）成为 AI 支出的绝对主力**。Inference 占 AI 优化云基础设施支出的 55%+，预计年底达到 70–80%。这个转变不是渐进的，而是一个临界点。

## 为什么值得学

1. **钱在哪里**: 全球 AI 基础设施支出 $1.37T（2026），推理芯片市场单独 >$50B。推理是持续性的支出而非一次性训练成本，这意味着市场结构完全不同。
2. **和你的工作直接相关**: 如果你的产品使用 AI agent，每一次用户请求可能触发 5-50 次 LLM 调用。理解推理经济学 = 理解你的成本结构和定价模型。
3. **竞争优势窗口**: 大多数公司还在用「训练思维」做 AI 预算，而领先的公司已经在做三层架构（API → 自托管云 → 本地部署）的推理优化。

## 3 个核心概念

### 1. 推理成本悖论（Cost Paradox）
单次推理价格两年降了 280 倍，per-token 成本年降 80%，但总推理支出指数级增长。原因：agentic AI 的调用乘数效应（一个任务 10-20 次 LLM 调用）、RAG 上下文膨胀（每次查询塞几千页内容）、7×24 always-on agent。

### 2. 三层推理架构（Three-Tier Architecture）
- **Tier 1 — Managed API**: $0.15–$15/MTok，适合低量、实验、前沿模型需求
- **Tier 2 — 自托管云**: 自己的模型 + 租 GPU，适合定制模型、合规场景
- **Tier 3 — 本地部署**: 8×–18× 成本优势 vs 按需云价，breakeven 2–5 个月

决策框架：日 token 量、数据主权要求、延迟敏感度、GPU 运维能力。

### 3. GPU 市场从短缺走向「功能性平衡」
H100 现货价已降到 $1.35/hr，lead time 从 50+ 周降到 6-12 周。但 B200 仍有 360 万块积压订单，新芯片依然是卖方市场。AMD MI300X 已进入生产环境（25% 新部署含 AMD GPU），ROCm 已基本等效 CUDA。

## 1 个真实案例

**Lenovo 2026 TCO 分析**：Llama 70B on 8×H100 本地部署 cost $0.11/MTok vs Azure 按需 $0.89/MTok = **8× 成本优势**。五年生命周期：本地 $1.01M vs AWS $6.24M，节省 83.8%。

**Inworld AI 实测**：B200 cost $0.02/MTok vs H100 $0.14 = **7× 提升**。

## 1 个反直觉点

> **私有云正在吃掉生产推理，而非公有云。**

Broadcom 2026 报告显示：56% 企业已在或计划在私有云跑生产推理，而公有云同一工作负载占比从 56% 暴跌到 41%（一年降 15 个百分点）。原因不是云不好，而是推理的规模经济在成本端逆转了——规模越大越应该「回家」（repatriation）。

## 和 Tony 当前工作的连接

- 如果你在用 agent/LLM pipeline 构建产品，**每一次推理调用都在烧钱**。理解 token 经济学直接影响产品定价和利润。
- Inference engine 选型（vLLM vs SGLang）可带来 29% 吞吐量差 = 每月 $15K GPU 节省。这对任何规模化产品都是关键决策。
- 三层架构思维不仅适用于大厂——即使是中小团队也应该知道什么时候从 API 切到自托管。

## 可实践的小动作

1. **算一笔账**: 估算当前/计划中的产品日 token 消耗量，对照 breakeven 表（>10M tokens/day 就该考虑自托管）
2. **关注一个信号**: B200 在 neocloud 的现货价格走势——当 B200 跌破 $2/hr，GPU 市场就真的从卖方转向买方了
3. **试试 SGLang**: 如果你在用 vLLM，跑一个对比 benchmark。29% 的吞吐差可能直接变营收。

## 是否建议 Codex 深挖

**建议。** 方向：
- 写一个推理成本计算器（输入：日请求量、模型、token 量 → 输出：各 tier 月成本对比 + breakeven 时间）
- 调研 SGLang vs vLLM 最新 benchmark 并做一份对比报告到 ECC

---

## 来源

| # | 标题 | 来源 | URL |
|---|------|------|-----|
| 1 | Inference Economics Tipping Point 2026 | Stravoris Research | https://www.stravoris.com/insights/inference-economics-tipping-point-2026 |
| 2 | State of AI Infrastructure 2026: Mid-Year Reality Check | TURION.AI | https://turion.ai/blog/state-of-ai-infrastructure-2026/ |
| 3 | Hyperscaler vs Colocation vs Edge: Where AI Workloads Are Actually Running in 2026 | Value Add VC | https://valueaddvc.com/blog/hyperscaler-vs-colocation-vs-edge-where-ai-workloads-are-actually-running-in-2026 |
| 4 | Broadcom Private Cloud Outlook 2026 | Broadcom (GlobeNewswire) | https://sa.marketscreener.com/news/broadcom-s-private-cloud-outlook-2026 |
| 5 | AI GPU Supply and Pricing 2026 | Presenc AI | https://presenc.ai/research/ai-gpu-supply-and-pricing-2026 |

---

*Hermes Growth Track · 周一行业理解 · 2026-06-15*
