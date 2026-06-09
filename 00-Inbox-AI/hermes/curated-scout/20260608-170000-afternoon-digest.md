# 🌤️ 核心雷达扫描 · 下午增量版 — 2026-06-08 17:00

> 扫描窗口: 2026-06-08 09:00 ~ 17:00 (基于 15:01 curated-scout + 增量分析)
> 上午版已覆盖 12 条信号 (4 主线 + 2 新线)，本版仅收录增量
> 状态: 上午创建 3 个新 learning tasks (causal-world-models / brain-inspired-computing / ai-service-reliability)

---

## 一、下午新增高信号 (8 条，去重上午覆盖)

### 🆕 新主线 E: AI 平台战争 — Apple 正式参战

**1. 🔥🔥🔥 OpenAI 秘密提交 IPO，紧随 Anthropic** (TechCrunch / Wired / The Verge)
→ AI 双巨头接连启动上市。上午版已覆盖 Anthropic IPO 准备 + Tokenpocalypse，OpenAI 的跟进将这一趋势从「信号」升级为「格局」。AI 行业从技术竞赛全面进入资本化阶段，定价模型、业务连续性和监管合规将同时经受公开市场检验。
[来源](https://techcrunch.com/2026/06/08/following-anthropic-openai-files-confidentially-for-ipo/) | 06-08 下午

**2. 🔥🔥🔥 Apple WWDC 2026: Siri AI 平台化 — 「更便宜的 AI」策略** (The Verge / TechCrunch / Wired)
→ Apple 用一场 WWDC 宣告正式进入 AI 平台战争。核心策略：(a) 全新 Siri 基于大模型重构，拥有独立 App；(b) Shortcuts AI 允许自然语言构建工作流 — AI 从「对话」走向「执行」；(c) 「更便宜的 AI」定价策略吸引小开发者，对抗 OpenAI/Google 的高成本路线；(d) Image Playground、Photos AI 编辑等全线 AI 化。Apple 的隐私优先 + 端侧推理 + 低价策略是区别于 OpenAI/Google 的第三条道路。
[来源](https://www.theverge.com/tech/942416/apple-siri-ai-update-wwdc) | 06-08 下午

**3. 🔥🔥 Apple Shortcuts AI：用自然语言构建工作流** (TechCrunch)
→ 这是 Apple AI 策略中最具「Agent 化」的信号。用户描述意图，AI 自动生成多步骤 Shortcuts 工作流。这与 Unisound U2 的「100+ 步 Agent 执行」和 MCP Apps 的「IDE UI 交互」形成三线共振——**AI 正在从对话界面走向工作流编排**。
[来源](https://techcrunch.com/2026/06/08/apple-will-let-you-build-workflows-using-ai-in-its-new-shortcuts-app/) | 06-08 下午

### 🔥🔥 主线 D 强化: 推理基础设施 — 训练 + 推理双线突破

**4. 🔥🔥 NVIDIA NVFP4: 4位浮点精度训练在 Blackwell 上落地** (NVIDIA Developer)
→ 使用 JAX + MaxText 在 Blackwell GPU 上通过 NVFP4（4位浮点）训练模型，显著降低显存占用和训练成本。从 FP16 → FP8 → FP4，每一步都是训练经济学的阶跃。这对「前缀缓存」等推理优化形成互补——训练和推理两端同时在突破成本边界。
[来源](https://developer.nvidia.com/blog/train-models-faster-with-jax-and-maxtext-using-nvfp4-on-nvidia-blackwell/) | 06-08 下午

**5. 🔥🔥 Xiaomi MiMo + TileRT: 1万亿参数模型在普通GPU上突破1000 tokens/s** (MarkTechPost)
→ 极致推理优化的工程成就。万亿参数级模型在 commodity GPU 上达到 1000+ t/s，意味着推理成本的「平民化」正在加速。与上午的「前缀缓存 80%→5% 陷阱」一文形成对照——推理工程化既有陷阱也有突破。
[来源](https://www.marktechpost.com/2026/06/08/xiaomi-mimo-and-tilert-push-a-1-trillion-parameter-model-past-1000-tokens-per-second-on-commodity-gpus/) | 06-08 下午

### 🔥 主线 A 强化: Agent 记忆 — GRAM 论文 + 检索增强学习

**6. 🔥 GRAM: RL 驱动的图结构 Agent 记忆** (OpenReview)
→ 提出通过强化学习让 Agent 主动维护和更新图结构记忆，解决静态记忆无法适应动态任务的问题。与上午 arXiv 2606.06054「信任感知检索」互补——前者解决「信什么」，后者解决「怎么组织」。Agent 记忆研究正在进入「结构化 + 可信 + 自适应」三位一体的深水区。
[来源](https://openreview.net/forum?id=rzGvGnwVC7) | 06-07 发表，06-08 下午 scout 捕获

**7. 🔥 检索增强 Agent：学会从经验中学习** (OpenReview)
→ 提出让 Agent 通过检索过往成功/失败经验来优化未来决策的框架。这与上午 OpenAI Dreaming V3 的「休眠时学习」形成互补——一个靠「做梦」巩固，一个靠「翻旧账」改进。RAG + Agent 的前沿交叉。
[来源](https://openreview.net/forum?id=tVTcYtmHIt) | 06-07 发表，06-08 下午 scout 捕获

### 🔥 新信号: AI 主权 + RAG 产品化

**8. 🔥 英国 10亿美元 AI 主权超算：摆脱对美国技术依赖** (Wired)
→ 英国政府投资建设本土 AI 算力基础设施。与上午 DeepSeek $7B 融资形成中、美、欧三极逐力格局。AI 算力正在成为国家战略资产。
[来源](https://www.wired.com/story/uk-supercomputer-investment-ai-homegrown-semiconductor/) | 06-08 下午

---

## 二、追踪信号 (持续观测，不进入 digest 正文)

- **Google NotebookLM Gemini 3.5 升级：新增「云电脑」+ 来源查找** — RAG 产品形态从文档问答进化为具备计算环境的研究助手。对 Agent 工作环境设计有参考价值。(The Verge) | 06-08
- **MCP SEP-2106: Full JSON Schema 2020-12** — MCP 协议持续标准化。工具 I/O 定义能力增强。(DEV Community) | 06-08
- **GitHub MCP Server 1.2.0** — MCP 生态工具链成熟度提升。(GitHub) | 06-08
- **Multi-Tenant LLM Serving 架构指南** — 面向生产的 LLM 多租户推理完整指南。(Spheron Blog) | 06-07
- **PhysicsX $300M 融资 (AI 物理仿真)** — AI 在垂直科学领域的应用加速。(TNW) | 06-08
- **Meta 智能眼镜移除面部识别代码** — AI 硬件隐私合规挑战。(Wired) | 06-08
- **DeepSeek-V4-Flash 量化恢复 MTP Head 提升 62% 吞吐** — 推理优化。(agentry) | 06-07

---

## 三、与上午版的交叉验证

| 上午主线 | 下午增量 | 方向 |
|---------|---------|------|
| B: AI 经济学/Tokenpocalypse | OpenAI IPO 确认资本化趋势 | 🔥🔥🔥 强化 |
| (新) | Apple WWDC / AI 平台战争 | 🆕 独立浮现 |
| D: 推理基础设施 | NVFP4 训练 + MiMo 推理突破 | 🔥🔥 强化 |
| A: Agent 记忆 | GRAM + 检索增强学习 论文 | 🔥 强化 (结构化方向) |
| C: MCP 协议 | SEP-2106 + GitHub Server 1.2.0 | 追踪级延伸 |
| (新) | 英国 $1B AI 主权超算 | 🆕 AI 算力主权 |

---

## 四、下午核心判断

1. **AI 平台战争正式开打。** Apple WWDC 不是简单的产品更新，它宣告了 AI 竞争的第三极——隐私优先 + 低价 + 端侧推理。与 OpenAI（全能模型）+ Google（搜索+云）形成三国格局。这不再是「谁的模型更强」，而是「谁的平台生态更完整」。

2. **推理基础设施双线突破。** NVFP4 4位训练 + Xiaomi 1T 参数 1000+ t/s 推理，代表训练和推理两端同时从「能用」进入「用得起」。叠加上午前缀缓存工程化，推理基础设施正在经历类似云计算 2014-2016 的「成本悬崖」时刻。

3. **Agent 记忆研究进入深水区。** GRAM (RL + 图) 和检索增强学习与上午 arXiv 论文形成三篇互补——信任、结构、经验，三个维度同时被突破。Agent 记忆正在从「工程 hack」变成「有理论框架的学科」。

---

## 五、学习任务候选

**无新增。** 上午创建的 3 个 learning tasks (causal-world-models / brain-inspired-computing / ai-service-reliability) 覆盖了本轮的全部新领域。下午信号均为已有主线的强化或产品动态追踪，无需独立学习任务。

建议关注：Apple AI 平台策略可纳入 `industry-growth` 或新建「AI 平台竞争格局」tracking note，但当前不适合作为独立 deep-dive learning task。

---

*Hermes 核心雷达 | 下午增量版 | 基于 15:01 curated-scout 增量分析 | 无新增 learning tasks*
