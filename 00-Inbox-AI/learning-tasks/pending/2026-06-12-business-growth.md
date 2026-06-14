# 2026-06-12 商业/经营/战略 — SaaS定价模式的结构性转变

> 学习方向：**商业主题 / 为什么值得学 / 3个核心概念 / 1个真实案例 / 1个反直觉点 / 和Tony工作连接 / 可实践小动作 / 是否建议Codex深挖 / 来源URL**

---

## 主题：从"卖座位"到"卖结果"——AI时代SaaS定价模型的范式迁移

### 为什么这个主题值得学

SaaS行业正在经历20年来最深刻的定价模式重构。这不是渐进优化，而是**成本结构冲击**驱动的范式转移——AI让软件交付首次引入了可变成本，Per-Seat模型的结构性天花板正在被拆除。

几个信号：
- **微软 CEO Satya Nadella** 在2026年4月财报会上明确："Any per-user business of ours will become a per-user and usage business."（我们任何一个按用户收费的业务，都将变成按用户+用量的业务。）
- **Salesforce** 刚在6月8日收购了伦敦的用量计费平台 m3ter，为自己的 AI Agent 产品 Agentforce 构建消费型计费基础设施。
- **Gainsight**（年收入数亿美元）宣布从 SaaS 转向"AI-Native Services"（AI原生服务），成立独立事业部、独立P&L。
- **Adobe** 在今天的财报会上宣布加速 Freemium AI 策略，主动放弃约5亿美元短期ARR以换取漏斗顶部扩张。

这不是"AI公司的事"，而是**所有技术公司的定价逻辑在重写**。对Tony来说，这意味着：
1. 基础架构/平台团队的内部"定价"和ROI论证方式也需要跟着进化
2. 理解这些商业模型有助于判断哪些技术趋势有长期商业可持续性
3. 第一性原理决策框架可以用来审视自己团队的定位和度量

---

## 3个核心概念

### 概念一：Multi-Modal Monetization (M3) — 多模式变现

**来源**：MGI Research

传统SaaS只有一个收费维度：人头 × 单价。M3框架要求企业同时支持：
- **订阅**（recurring）
- **用量**（usage-based: API调用次数、Agent动作数、消息数）
- **结果**（outcome-based: 解决一个工单、完成一个交易）
- **平台费**（platform fee）
- 以及以上所有组合

核心发现：**计费系统 = AI时代的控制面板**。如果无法计费，就无法治理；如果无法治理，财务就会关停。60%以上的软件公司计划在12个月内部署用量计费，但只有不到10%有足够的能力。

### 概念二：Seat-Plus-Consumption — 座位+消费混合模型

**来源**：Microsoft实践 + Bytewaves分析

这是2026年主流的落地形态：
- 保留Per-Seat作为"地板"（给客户可预测的预算底线）
- AI功能叠加Usage计量（让厂商从用量增长中获益）
- 微软M365 Copilot已部署到2000万付费Seat，同时Copilot Credit消费型offer环比增长2倍
- GitHub Copilot从6月1日起全面转为消费型定价

**关键洞察**：纯Seat模型的天花板 = 价格 × 人数。Seat+Consumption模型下，同一个客户的收入可以随用量增长而扩大，不需要新签合同。

### 概念三：第一性原理定价——从"行业惯例"到"物理/经济真相"

**来源**：The Strategy Engine 第2章

第一性原理思考在定价中的应用：
1. **拆解成本结构**：哪些是物理不可约成本（原材料、基础劳动力），哪些是行业惯例（渠道加价、历史溢价）？
2. **SpaceX案例**：火箭原材料成本仅占售价2%，其余98%是惯例和低效——SpaceX通过攻击这个间隙实现了53%成本削减
3. **Zerodha案例**：印度券商传统上收0.5-1%佣金，Zerodha发现单笔交易技术成本仅₹2-5，推出零佣金模式，现在拥有1300万客户、56.5%净利润率

**应用在当前SaaS定价转变**：Per-Seat定价本身就是"惯例"而非"第一性原理"。软件交付的物理成本是什么？Compute、存储、带宽。这些是按用量计的。那为什么按人头收费？因为这是行业惯例——但这个惯例正在被AI的可变成本结构瓦解。

---

## 1个真实案例：Microsoft的收入模型重写

### 背景
微软在2026年4月29日发布了"多年来最干净的季度"——营收$829亿超预期，EPS $4.27超预期，Azure增长40%，AI ARR达$370亿（YoY +123%）。股价还是跌了3.93%，因为CFO指引了$1900亿年度资本开支。

### 真正重要的故事
市场盯错了数字。Nadella在电话会上宣布的是微软**收入架构的结构性变化**：

> "Any per-user business of ours, whether it's productivity, coding, security, will become a per-user and usage business."

三条产品线同时在拆掉Seat天花板：

| 产品线 | 变化 | 数据 |
|--------|------|------|
| **GitHub Copilot** | 6月1日起全量转为消费型定价 | 14万组织使用，企业订阅YoY翻3倍 |
| **Dynamics 365** | 近60%客服客户已在Seat基础上购买用量Credit | HSBC部署后问题解决时间缩短30%+ |
| **M365 Copilot** | Copilot Credit消费型offer环比增长2倍 | 付费Seat超2000万，周活跃度与Outlook持平 |

### 财务影响
TIKR模型估算：到FY2030年营收可达$6070亿（FY2025为$2820亿），驱动引擎正是**Seat+Consumption模式的深化**——在2000万Copilot Seat基础上叠加消费收入层。

### 反直觉的细节
2026年5月13日，微软与OpenAI修订了合作协议。表面上是OpenAI获得了向竞争对手云分发的权利（被解读为失去独占性）。实际上：
- 微软**取消了对OpenAI的Azure收入分成**——原来每卖一次OpenAI模型要给OpenAI分成，现在不给了
- Azure AI工作负载的**利润率即时改善**
- Wedbush分析师因此上调MSFT目标价至$575

**教训**：商业信号经常藏在细节里。市场盯着亏损的CapEx，却忽略了正在建立的、不需要新合同就能扩大的收入引擎。

---

## 1个反直觉点

### "产品能力不再是决定性竞争优势——变现系统才是"

**来源**：MGI Research

> "AI features are replicated rapidly across the industry. Model access is broadly available. Product capability is no longer the decisive competitive differentiator. It is the monetization system."

在AI时代：
- **产品** → 必要但可快速复制
- **数据** → 重要但正在快速商品化
- **变现系统**（计费基础设施、定价变更速度、买家信任）→ **新的护城河**

这对技术团队意味着什么？你构建的不只是"一个功能"，你需要同时思考**如何计量、如何计费、如何让客户信任这个计量**。这就是为什么Salesforce愿意花未披露的金额收购m3ter，为什么微软在重写整个计价体系。

**反直觉之处**：我们通常认为"更好的产品会赢"。但在AI时代，当模型能力和产品功能趋于同质化时，**更快的定价迭代速度**和**更精准的计费能力**反而成为差异化来源。这不是技术竞赛，是商业基础设施竞赛。

---

## 和Tony工作的连接

### 连接点1：平台工程的"内部定价"问题

Tony的基础架构/平台团队面临相同的挑战：
- 如何度量平台的价值？按人头分摊？按资源用量？按交付结果（如部署速度、事故减少）？
- 如果平台真正提高了工程师效率，传统的人头分摊模型会**惩罚高效团队**（更少的人用更少的资源却承担同样多的分摊成本）
- 应该考虑类似"混合定价"的内部计量：基础服务按人头，弹性/高级服务按用量

参考：Forrester对Cortex Internal Developer Platform的TEI研究发现224% ROI、$441万NPV、6个月回本——但这些数字的前提是平台被**真正采纳**（自愿而非强制）。

### 连接点2：第一性原理审视团队定位

对平台/基础架构团队提几个第一性原理问题：
- "工程师花18%的时间与基础设施搏斗"——这个假设在你的团队成立吗？如果成立，损失是多少？
- 平台团队的"物理不可约成本"是什么？哪些活动是"惯例"（比如人手一个审批工单）？
- 如果从零开始设计内部平台，你会保留什么？放弃什么？

### 连接点3：为AI时代的计量能力做准备

如果Tony的团队未来需要提供AI服务（RAG、Agent、Copilot类工具），从现在就应该考虑计量基础设施——即使最初只是简单的用量跟踪。等需要的时候再建，可能来不及（参考MGI数据：补救计费系统故障的成本在$100万-$500万以上）。

---

## 可实践小动作（本周可做）

1. **做一次"成本结构分解"**（30分钟）：挑一个你团队提供的服务/平台能力，拆解它的成本结构。标出哪些是"物理不可约"（compute、存储），哪些是"惯例"（人工审批、手动配置）。算一下惯例占了总成本的百分比。

2. **问一个第一性原理问题**（团队周会）："如果我们的平台从今天开始对所有内部用户免费（无分摊），但需要按实际用量全部透明计量——会发生什么？谁会多用？谁会少用？我们会发现什么？"

3. **追踪一个信号**（持续）：关注微软Q4 FY2026财报（预计7月29日）。关键数字不是Azure增长率，而是**M365 Commercial Cloud的ARPU**——如果ARPU加速（超过E5升级能解释的范围），说明消费型收入的飞轮已经开始转动。这将验证整个Seat+Consumption模式的商业可行性。

4. **阅读一篇关键文章**（15分钟）：细读[The End of Per-Seat SaaS Pricing: What Salesforce's m3ter Deal Signals](https://breaktheordinary.com/end-of-per-seat-saas-pricing-2026/)，尤其关注最后的"自由职业者视角"——"如果AI让我用2小时完成原来需要10小时的工作，按小时计费意味着我因为效率提高而给自己降薪80%。"这种思维同样适用于内部平台的价值度量。

---

## 是否建议Codex深挖

**强烈建议**。以下方向适合让Codex做深度研究：

1. **MGI SaaS Pricing Evolution完整报告**：目前只读到摘要，完整报告有更详细的迁移模型和数据。可以让Codex尝试获取完整内容或找到相关的公开分析。

2. **内部平台ROI量化模型**：结合Forrester的TEI框架和Luca Berton的平台工程ROI公式（Developer Hours Saved × Hourly Rate + Infra Savings ÷ Platform Team Cost），让Codex为Tony的团队搭建一个可用的ROI计算模型（填入团队的实际数字）。

3. **竞品定价追踪器**：让Codex做一个自动追踪脚本，监控主要SaaS/AI公司的定价模式变化（Notion AI、Cursor、Figma AI、GitHub Copilot等），定期更新对比表。

4. **第一性原理分析框架实操**：以上文Strategy Engine的Assumption Breakdown Framework为模板，让Codex选择一个Tony团队面对的真实战略问题，完成Step 1-5的完整分析。

---

## 来源URL

| 文章 | URL | 日期 |
|------|-----|------|
| MGI Research: SaaS Pricing Evolution | https://mgiresearch.com/research/saas-pricing-evolution-from-seats-to-usage/ | 2026-03-30 |
| Microsoft Revenue Model Rewiring (TIKR) | https://www.tikr.com/blog/microsoft-is-quietly-rewiring-its-revenue-model-heres-why-that-could-matter-more-than-azure-growth | 2026-05-16 |
| First Principles Thinking in Strategy | https://strategy-engine.pages.dev/chapters/chapter-02-first-principles/ | 2025-11-25 |
| Gainsight Pivot to AI-Native Services | https://www.upstartsmedia.com/p/exclusive-gainsight-pivot-ai-native-services | 2026-05-27 |
| Salesforce m3ter Deal & End of Per-Seat | https://breaktheordinary.com/end-of-per-seat-saas-pricing-2026/ | 2026-06-11 |
| SaaS Pricing Models 2026 (Bytewaves) | https://bytewaves.news/comparisons/saas-pricing-models-per-seat-vs-usage-based-outcome-2026/ | 2026-06-10 |
| Platform Engineering Business Case | https://biztechbridge.com/insights/platform-engineering-business-impact | 2026-04-08 |
| Platform as a Product (InfoQ) | https://www.infoq.com/news/2026/04/platform-product-deliver-value/ | 2026-04-16 |

---

*生成时间: 2026-06-12 | Hermes 商业/经营/战略 轨道 | 评分: ★★★★★ 建议晋升 wiki*
