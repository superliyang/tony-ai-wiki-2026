---
date: 2026-06-10
track: 管理能力
type: growth-learning-package
status: pending-review
sources: exa-search
---

# 管理能力：从"分配任务"到"设计责任系统"

## 今日管理主题

**「你的角色不是做所有决定的人，而是设计让好决定自然发生的系统的人」——三条并行的管理能力跃迁线**

技术管理者从一线 TL 到 Director/VP 的演化，本质上不是管更多人的线性放大，而是三次角色定性：

1. **任务分配 → 责任系统设计**：停止做"最聪明的人解所有问题"，转向设计让团队在你不介入时仍能高质量决策的系统
2. **回避冲突 → 校准直接度文化**：建立信息充分流动的反馈文化，既不是"太礼貌导致问题烂掉"，也不是"太直接导致人闭嘴"
3. **管人执行 → 管 Human + AI Agent 混合团队**：当 AI agent 吃掉执行层工作，管理者的稀缺能力变成判断力、边界设计、治理架构

---

## 为什么值得学

Tony 当前正在构建的 AI First 知识操作系统涉及三个维度的管理挑战，恰好被今天三篇文章覆盖：

- **Hermes/OpenHuman/ECC/Codex 多 agent 协作**：你已经有一个多 agent 系统（4 个 agent + Tony 作为人类判断节点）。如何设计 agent 决策边界、所有权、human-on-the-loop 治理——正是 Augment Code 文章的核心
- **团队反馈文化建设**：你和 Hermes 之间、Hermes 和其他 agent 之间的"反馈"如何既保持直接性又不破坏协作关系——直接度刻度盘的框架可以直接映射到 agent 间通信协议设计
- **从执行者到系统设计者**：Tony 正在从"自己做所有事情"过渡到"设计一个 agent 系统来做事"——这正是 delegation 框架从 Level 1 (Tell) 进化到 Level 7 (Delegate) 的过程

---

## 3 个核心概念

### 概念 1：七级委托谱系（Seven Levels of Delegation）

**来源**：Engineering Manager Tools, "Delegation: Stop Being the Bottleneck on Your Own Team"

委托不是二元的（做/不做），而是七个级别组成的谱系：

| 级别 | 名称 | 含义 |
|------|------|------|
| L1 | Tell | 你做决定，通知团队 |
| L2 | Sell | 你做决定，解释原因 |
| L3 | Consult | 你征求意见，然后你决定 |
| L4 | Agree | 讨论后共同决定 |
| L5 | Advise | 你给建议，他们决定 |
| L6 | Inquire | 他们决定后通知你 |
| L7 | Delegate | 他们全权决定和处理 |

**关键操作规则**：
- 匹配级别到 stake 和 readiness：高风险不可逆决策 → L3/L4；常规决策 → L6/L7
- **明确告知级别**：最破坏信任的行为是假装 L7 实际 L3（征求意见但保留否决权）
- **委托结果而非任务**：不是"帮我做这个 JIRA ticket"，而是"你负责确保部署流水线的可靠性，这意味着你拥有监控、runbook 和改进路线图"

> 核心洞察：真正好的委托不是"把活给出去"，而是"设计一个分布式决策系统，让整个组织比任何单一领导者更快、更聪明、更有韧性"。

### 概念 2：直接度刻度盘（The Directness Dial）

**来源**：Joel Dickson (Agoda Director of Engineering), "The Directness Dial: Teaching Engineers to Be Honest Without Being Brutal"

每一个工程团队都在直接度谱系上有一个默认位置，且两种极端都导致同一个结果：**信息不流动**。

- **Dial-at-10（太直接）**：技术上正确，社交上摧毁——人会闭嘴，设计评审变成表演
- **Dial-at-2（太礼貌）**：社交上优雅，信息上空转——问题持续存在，技术债务累积，没人说真话

**核心框架——校准因子**：

| 上调拨盘的因素 | 下调拨盘的因素 |
|---------------|---------------|
| 安全风险（生产事故、安全漏洞） | 新人/首次互动（信任未建立） |
| 重复模式（已给过反馈无变化） | 跨文化语境 |
| 受众能承受（资深工程师、已有信任） | 公开场合（当众批评放大情绪风险） |
| 时间压力（需立即决策） | 对方正经历困难周 |
| 沉默成本高（不指出会导致项目上线失败） | 品味问题而非对错问题 |

**媒介补偿法则**：文字（Slack/PR comment）会剥离所有非语言信号——你在脑子里觉得是 dial-6 的话，在屏幕上会被读成 dial-9。**书面反馈需要比当面低 2-3 格**。

**教练操作方法**：
- 教练 Dial-at-10：「那次评审后其他工程师什么反应？为什么他们安静了？」——不告诉结论，引导他自己算成本
- 教练 Dial-at-2：在 1:1 里反复回放「周二那个评审，你有话要说，我看到了。为什么没说？」——每周重复，直到说话变成预期行为而非个性偏好

> 核心洞察：校准直接度不是找"中间值"——是建立**范围**。同一个工程师在讨论生产安全问题时应 dial-9，在讨论命名规范偏好时应 dial-3。始终在某一端的人，是把舒适区当成技能了。

### 概念 3：Agentic Engineering 决策层级（Decision Tiers for Human+Agent Teams）

**来源**：Augment Code, "Agentic Engineering Operating Model" + Anthropic 2026 Agentic Coding Trends Report

当 AI agent 进入工程团队后，管理模式的根本转变：

| 维度 | Pre-Agent 状态 | Agentic 状态 |
|------|---------------|-------------|
| 执行模型 | 人执行，工具辅助 | 人掌舵，agent 执行 |
| 团队规模 vs 范围 | 大团队，有限范围 | 小团队，扩展范围 |
| 主要瓶颈 | 执行产能 | 判断力和 review 产能 |
| 知识持久化 | 文档、wiki | 共享组织记忆基础设施 |
| 治理模型 | 事后合规叠加 | 运行时 policy-as-code 强制 |

**三级决策体系**：

| 层级 | 范围 | 示例 |
|------|------|------|
| Tier A：仅人类 | agent 零自主权 | 架构决策、安全策略、受监管发布的审批、agent 范围定义 |
| Tier B：Agent 辅助 | agent 生成，人批准后生效 | 需求验证、设计评审、代码合并审批、合规评估 |
| Tier C：完全自主 | agent 在策略边界内自主执行 | 单元测试生成、代码脚手架、静态分析、依赖更新（在批准范围内） |

**关键治理原则**：
- 从 human-in-the-loop（人审查每个变更）→ human-on-the-loop（人定义规约和质检的 harness，agent 在 harness 内自主执行）
- 新增角色：Agent Orchestration Engineer、Agent Reliability Engineer、Context Engineer、AI Governance Owner
- **组织记忆作为基础设施**：没有共享记忆，每个 agent session 从零开始，每次事故重新发现已知原因——知识不会 compound

> Anthropic 2026 报告核心数据：开发者约 60% 的工作涉及 AI，但只有 0-20% 的任务可"完全委托"。AI 是持续协作者，但需要主动的设置、监督、验证和人类判断——尤其在高风险工作中。

---

## 1 个真实案例

### 案例：从"人肉决策瓶颈"到"模块所有权系统"——管理 40+ 工程师的 TPM 转型

**来源**：C.B. Mishra, "Agile Leadership: Managing 40+ Engineers Efficiently"

一个管理 40+ 工程师的 TPM 发现自己的日常变成了：
- 每天被问 30+ 次「这个怎么做」
- 每个决策排队等他
- 团队交付速度受限于他的决策速度

**转型动作**：

1. **模块所有权制度**：将项目拆分为独立模块，每个模块指定一个 Module Lead 拥有该领域的上下文、日常决策权、非跨域协调问题自主解决权
2. **你的角色从「做所有决定的人」变成「设计让好决定自然发生的系统的人」**
3. **TPM 成为"压力膜"**——所有外部混乱经过 TPM 过滤、翻译、结构化后以 ticket 形式交给团队，团队不直接承受业务侧噪音
4. **分发决策权而非随机放权**：每个模块有清晰的决策边界、升级触发条件（超过预算阈值、跨模块依赖、涉及关键客户关系）

**结果**：交付速度提升 35%，不是因为团队更努力，而是因为团队不再被阻塞、不再过劳、不再做错事。「系统产生结果。建造系统。」

---

## 1 个反直觉点

### 「太礼貌」和「太直接」造成的损害是一样的

大多数技术管理者的直觉是：直接伤人是问题，礼貌不是问题。但 Joel Dickson 的核心论证是：

> 两种极端造成的结果完全相同：**信息不流动**。

- 太直接 → 人不敢分享想法 → 信息丢失
- 太礼貌 → 人不好意思提问题 → 信息丢失

一个沉默的、人人点头的评审会比一个充满争论的评审更危险——前者把问题藏到生产环境才暴露，后者至少问题在房间里被处理了。

**对 Tony 的反直觉启示**：Hermes agent 之间的通信如果"太礼貌"（不敢指出其他 agent 的问题），其危害等价于"太直接"导致 agent 互相不信任。agent 间需要设计明确的「问题升级协议」（escalation triggers），让指出问题不是"攻击"而是"协议要求"。

---

## 和 Tony 工作连接

### 直接可迁移的三条线索

1. **Agent 决策层级映射**
   Tony 的 Cognitive OS 已有 4 个 agent 的严格写边界（OpenHuman 不写 wiki、Hermes 不写 wiki、ECC 需 review 后写 wiki）。这套边界设计天然映射到 Tier A/B/C 决策体系——可以显式定义为：
   - **Tier A（仅 Tony）**：wiki 写入、agent 范围变更、安全关键决策
   - **Tier B（Agent 辅助 + Tony 审批）**：OpenHuman 候选 → Tony judge → Codex crystallize
   - **Tier C（Agent 自主）**：Hermes cron scout 搜索、routine 通知、定时维护

2. **直接度校准 → Agent 间通信协议**
   当前 Hermes 对 OpenHuman/ECC/Codex 的通信可以引入"直接度"概念——例如 Hermes 发现 OpenHuman 候选质量下降时，如何既直接指出又不破坏协作？答案：**升级协议（escalation trigger）**——预定义的客观条件（如连续 3 个候选未通过 review）自动触发升级，让"指出问题"变成协议执行而非个人判断。

3. **从执行到系统设计者的跃迁**
   Tony 正在经历从"自己做所有 Vault 操作"到"设计 agent 系统自动维护 Vault"的转变。这和 Delegation Level 1→7 的进化完全对应：当前已经在 L5（Advise——agent 给建议，Tony 决定），目标 L6/L7（agent 在一定范围内自主管理）。关键是像模块所有权制度一样，为每个 agent 定义清晰的**决策边界 + 升级触发条件**。

---

## 可实践小动作

- **本周**：为 Tony Cognitive OS 的 4 个 agent 各写一行"决策边界声明"——什么决定自己能做，什么需要 Tony。格式：`Agent X 可自主决定：__。必须升级给 Tony：__。`
- **本周**：在下一个 Hermes 产生信号时，实验不同的"直接度"——用 dial-5（提问而非判断）替代默认的汇报语气，观察协作效果
- **本月**：审查当前 review-queue 的瓶颈在哪里——是 Tony 的 review 产能（对应 "human-on-the-loop" 瓶颈），还是 agent 输出质量（对应 agent evaluation 瓶颈），还是跨 agent 协调（对应 governance 瓶颈）

---

## 是否建议 Codex 深挖

✅ **强烈建议**。三个方向都可以让 Codex 结晶为 wiki 知识资产：

1. **Agent 决策层级 → `10-Knowledge/工程管理/Agent-决策层级设计.md`**：将 Augment Code 的 Tier A/B/C 映射到 Tony 的 Cognitive OS 架构，形成可复用的治理框架
2. **直接度刻度盘 → `30-Playbooks/Agent-通信协议.md`**：将 Joel Dickson 的框架转化为 agent 间通信的 escalation trigger 协议设计
3. **Delegation 七级 → `30-Playbooks/管理者-委托框架.md`**：作为 Codex 在帮助 Tony 管理 agent 系统时的参考框架

## 来源 URL

- [Delegation: Stop Being the Bottleneck on Your Own Team — Engineering Manager Tools](https://www.em-tools.io/engineering-management-frameworks/delegation-framework)
- [Agentic Engineering Operating Model: Teams + Agents — Augment Code](https://www.augmentcode.com/guides/agentic-engineering-operating-model)
- [The Directness Dial: Teaching Engineers to Be Honest Without Being Brutal — Joel Dickson / Medium](https://medium.com/beer-and-servers-dont-mix/the-directness-dial-teaching-engineers-to-be-honest-without-being-brutal-4e500b3a5fe9)
- [Agile Leadership: Managing 40+ Engineers Efficiently — C.B. Mishra](https://www.cbmishra.com/managing-large-engineering-teams-agile-leadership/)
- [2026 Agentic Coding Trends Report — Anthropic](https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf)
