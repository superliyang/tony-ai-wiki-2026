# 🧠 下午增量扫描 — 2026-06-07 15:02

> 对比基准：早间 digest `20260607-090045` | 增量源：下午 curated-scout `20260607-150027` + TechCrunch RSS
> 去重后增量条目：7 条 | 学习任务候选：1 个

---

## 🔥 增量高信号

### 1. 💰 Tokenpocalypse：AI 行业从 VC 补贴走向真实成本（TechCrunch）
→ Microsoft GitHub Copilot 突然从包月转向**按 token 计费**，被用户称为「Tokenpocalypse」。背后是 VC 补贴即将枯竭——Anthropic 正在准备 IPO，Uber 等公司内部 AI 预算快速烧穿并开始限流。文章指出当年 ChatGPT Plus $20/月定价并无策略依据，整个行业正在为这个随意定价买单。**这是 AI 商业模型转折的关键信号。**
[原文链接](https://techcrunch.com/2026/06/07/is-this-the-dawn-of-the-tokenpocalypse/)

### 2. 🔬 超越相似度：为个人 AI Agent 构建可信记忆搜索（arXiv 2606.06054）
→ 提出全新记忆检索框架，不再仅依赖语义相似度，而是**引入信任度评估**，解决 Agent 长期交互中记忆混乱和不可靠的核心问题。Agent 记忆领域的突破性论文。
[原文链接](https://arxiv.org/html/2606.06054v1)

### 3. 🏗️ Redis Agent Memory 正式发布（Redis）
→ Redis 官方推出 Agent 记忆解决方案，利用其高性能缓存能力为 Agent 提供**低延迟、可扩展的状态与记忆管理**。基础设施层的重要产品化信号。
[原文链接](https://redis.io/agent-memory/)

### 4. 🧮 LeanMarathon：长程 Lean 自动形式化基准（Signal IA）
→ 提出一个长程规划与推理基准，旨在让 AI 在**数学定理证明（Lean）**中实现更可靠的自动形式化。对 Agent 在严谨、复杂领域的规划能力提出了更高要求。
[原文链接](https://signal-ia-rouge.vercel.app/en/article/leanmarathon-toward-reliable-ai-co-mathematicians-through-long-horizon-lean-auto-605090)

### 5. 🎨 MCP Apps：构建交互式 VS Code UI（StartupHub.ai）
→ MCP 协议应用场景从工具调用**扩展到 IDE UI 交互**——Agent 可直接操控 VS Code 界面，实现更深度的开发环境人机协作。
[原文链接](https://www.startuphub.ai/ai-news/technology/2026/build-interactive-vs-code-uis-with-mcp-apps)

### 6. 🐢 自托管 Claude Code 为何比预期慢 15 倍（DEV Community）
→ 经典的自托管推理性能排查案例，揭示**网络、存储、模型加载**等环节的常见瓶颈。对部署私有 LLM 服务的团队有直接工程参考价值。
[原文链接](https://dev.to/vinayiitkgp/why-self-hosted-claude-code-was-15-slower-than-it-should-be-3pb4)

### 7. ⚠️ Notion 因 Anthropic 服务中断暂时禁用 Claude 模型（TechCrunch）
→ Notion AI 因 Anthropic Opus 4.7/4.8 性能下降，周日凌晨**禁用全部 Anthropic 模型**，12 小时后恢复。事件引发 1200+ 转发，首次大规模暴露 AI 服务可靠性问题。Anthropic 称是「短暂基础设施问题」。
[原文链接](https://techcrunch.com/2026/06/07/notion-restores-access-to-anthropic-after-service-disruption/)

---

## 📌 主题观察

1. **Agent 记忆系统持续升温**：arXiv 可信记忆论文 + Redis 产品化 + 本周多篇记忆文章，Agent 记忆正从学术走向工程落地。
2. **AI 经济学拐点临近**：Tokenpocalypse 信号 + Anthropic IPO + 企业预算收紧，AI 行业正在经历「Uber 时刻」——从烧钱增长到追求盈利的痛苦转型。
3. **MCP 生态加速扩展**：无状态传输 RC + VS Code UI 集成，MCP 正从工具协议进化为 Agent-IDE 交互层。

---

## 📋 学习任务候选

→ 已产出独立候选：`pending/2026-06-07-ai-token-economics.md`（AI Token 经济学与商业模型转型）

---

*Hermes 下午增量扫描 | 基于上午 digest 去重 | 不覆盖已覆盖内容*
