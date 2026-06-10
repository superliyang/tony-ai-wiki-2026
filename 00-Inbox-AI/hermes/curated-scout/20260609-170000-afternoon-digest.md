# 🌤️ 核心雷达扫描 · 下午增量版 — 2026-06-09 17:00

> 扫描窗口: 15:30 → 17:00 (增量覆盖上午/15:30 digest 未捕获的信号)
> 方法: Exa 多维度搜索 → 去重上午(09:00) + 下午(15:30) digest → 识别的 7 条增量
> 状态: 26 pending + 4 in-progress learning tasks，无新增学习任务

---

## 增量高信号摘要 (7 条)

### 🔥🔥🔥 1. Anthropic 正式呼吁全球 AI 放缓——递归自我改进已非理论

Anthropic 发布详细警告报告，呼吁建立多边协调机制以暂停前沿 AI 开发。关键内部数据首次公开：Claude 撰写了 Anthropic 自身 80%+ 的生产代码（2 月前为低个位数）；工程师日均合并代码量是 2024 年的 8 倍；Claude 完全自主完成了一项 AI 安全研究项目（97% 性能恢复，人类研究员仅达 23%）。OpenAI 同周在公共政策议程中提出相同关切。双实验室独立预警，时间点高度一致——政策信号级别远高于上午 digest 中「Claude Opus 4.8 系统卡」的追踪级覆盖。
[来源](https://aistify.com/anthropic-calls-industry-pause-ai-recursive-self-improvement-risk/) | 06-08/09

### 🔥🔥🔥 2. Perplexity Search as Code——AI 自己写搜索管道

Perplexity 推出 Search as Code (SaC) 架构：AI 模型不再调用固定搜索 API，而是用 Python 编写自定义搜索管道并在沙箱中执行。200 个高危 CVE 追踪任务中：100% 准确率，42,900 tokens（标准管道的 15%）。WANDR 基准上提升 45% (绝对值)，DSQA 提升 29%。核心范式转变：搜索基础设施从黑盒 API 变成可编程原语层，模型从「调参」变成「设计策略」。
[来源](https://opentools.ai/news/perplexity-search-as-code-ai-models-write-search-pipelines) | 06-06/08

### 🔥🔥 3. Agent Memory 双响炮——今日 arXiv 新论文深化线程 A

**(a) Mage** (arXiv 2606.06090): 执行状态管理框架。将记忆组织为层级状态树，通过 Grow/Compress/Maintain/Revise 四种操作维护。在 MemoryArena 上任务成功率 +7.8~20.4pp，Token 消耗 -55.1%。核心论点：长期 Agent 记忆不是「检索相似内容」而是「维护执行状态」。

**(b) MRAgent** (arXiv 2606.06036): 图记忆 + 主动重建。Cue-Tag-Content 关联图，Agent 在推理过程中动态探索和修剪检索路径。LoCoMo +23%，LongMemEval +12.4%。口号：「记忆是重建的，不是检索的」——与 Mage 互补且独立验证同一方向。
[来源](https://arxiv.org/abs/2606.06090) [来源](https://arxiv.org/abs/2606.06036) | 06-09

### 🔥🔥 4. Agentic Monte Carlo——黑盒 Agent 也能做强化学习

Layer 6 AI (TD Bank 子公司) 提出 AMC 方法：通过贝叶斯推断等价性 + 序列蒙特卡洛，在不访问模型参数的情况下对黑盒 Agent（如 GPT-5.1）进行 RL 级优化。在 AgentGym 三个环境中一致超越 prompting baseline，随测试时计算增加可超越 GRPO（需要完整参数访问）。仅需 2×RTX 6000 Ada 即可训练价值函数，GRPO 需要 8×A100。对 Proprietary API + RL 交叉点有方法论意义。
[来源](https://arxiv.org/abs/2606.05296) | 06-09

### 🔥🔥 5. Lacuna——类型检查的 Agent 安全编程

将 Agent 动作设计为「类型化程序空洞」：LLM 填充的代码在运行前被类型检查，8.6% 的生成在编译阶段被拒绝（零副作用），平均 0.7 次重试即可修正。τ²-bench 上解决 76% 任务，与 baseline agent 持平但保证了安全性。将 Agent 安全从运行时守卫移到编译时——新范式。
[来源](https://arxiv.org/abs/2605.28617) | 05/28+ (arXiv)

### 🔥🔥 6. SparDA——稀疏解耦注意力推动长上下文推理

MIT HAN Lab (Song Han 组) 提出 Sparse Decoupled Attention：引入第四个投影层 Forecast，预测下一层需要的 KV block，实现 CPU→GPU 预取与当前层计算的流水线重叠。在 MiniCPM4.1-8B / NOSA-8B 上 decode 提速 1.7×，启用更大 batch 后吞吐提升 5.3×。仅增加 <0.5% 参数，无需重新训练基础模型。
[来源](https://arxiv.org/abs/2606.04511) | 06-09

### 🔥 7. LLM 情感轴与人类脑电波对齐

KAUST 团队的 arXiv:2606.00129 论文：LLM 内部的情感坐标轴（valence axis）与人类观看情感视频时的 EEG 信号在数学上指向同一方向 (r=+0.80, p<10⁻⁵)。FACED 情感分类新 SOTA (0.6948, +10.5%)。虽然不是实用技术突破，但对 AI 意识/情感讨论有客观数据支撑。
[来源](https://blog.pebblous.ai/report/llm-eeg-valence-axis/en/) | 05/28 arXiv

---

## 学习任务候选

**无新增。** 当前 26 pending + 4 in-progress 已足够饱和。本轮增量中的新信号：
- Anthropic 放缓呼吁 → 纳入 `ai-safety-governance-stack` tracking
- Search as Code → 追踪级，可纳入 `mcp-protocol-evolution` 的「Agent 搜索范式」子线程
- Agent Memory 论文 (Mage/MRAgent) → 强化已存在的 P1 `agent-memory-architecture-package`
- AMC / Lacuna / SparDA → 追踪级，偏学术方法论

---

## 与上午版 / 15:30 版的交叉验证

| 主线 | 上午状态 | 15:30 强化 | 下午增量 |
|------|---------|-----------|---------|
| A: Agent 记忆 | 🔥🔥🔥 | — | 🔥 Mage + MRAgent 双响 |
| B: AI 经济学 | 🔥🔥🔥 | 🔥🔥 MANGOS | 🔥🔥🔥 Anthropic 放缓 (政策面强化) |
| C: MCP 协议 | 🔥🔥 | 🔥🔥 GitHub 1.2.0 + 可观测性 | 🔥 Search as Code (搜索范式，远亲) |
| D: 推理基础设施 | 🔥🔥 | 🔥 TensorRT FP8 | 🔥 SparDA (注意力优化) |
| E: AI 平台战争 | 🔥🔥🔥 (Apple) | 🔥🔥 Claude Fable 5 | — |
| 🆕 Agent 方法论 | — | — | 🔥🔥 AMC (黑盒 RL) + Lacuna (安全编程) |

---

## 值得关注的跨故事主题

1. **Agent 记忆从「检索」到「重建」**：今日两篇论文独立论证同一转向——这不是巧合，是范式级共识信号。Mage 关注执行状态管理，MRAgent 关注图结构重建，方向互补。
2. **Anthropic 的双重角色**：一边在 AIstify 呼吁全球放缓，一边向 SEC 秘密提交 IPO。资本化与安全论叙的可能冲突——值得持续观察政策与市场反应。
3. **「编码即接口」趋势**：Perplexity Search as Code 和 Lacuna 的类型化程序空洞，均将「代码」作为 AI Agent 与基础设施之间的新接口层，替代传统 API 调用范式。

---

*Hermes 核心雷达 | 下午增量版 | 基于上午+15:30 digest 增量补齐 | 无新增学习任务*
