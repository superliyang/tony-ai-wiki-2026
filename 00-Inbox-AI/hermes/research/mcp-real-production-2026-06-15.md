# MCP 真实落地调研 — 2026-06-15

> 调研原则：追求真实案例、工程细节、可落地方案。不堆砌概念，不画饼。

---

## 一、MCP 到底是什么（30 秒讲清楚）

**MCP (Model Context Protocol) = LLM 的"USB-C 接口"**

- 定义了 LLM 客户端如何**发现**工具、**调用**工具、**接收**结果
- 是 **tool-calling 层的标准化协议**，不是 Agent 框架，不是编排引擎
- 核心抽象：Client（AI 应用/Agent）通过 MCP 协议与 Server（封装工具/数据）通信
- 传输层：JSON-RPC 2.0 over stdio / Streamable HTTP（HTTP+SSE 已被 deprecated）

**MCP 不是：**
- ❌ API 网关（虽然可以构建在网关之上）
- ❌ Agent 编排器（那是 A2A 的事）
- ❌ 安全框架（安全需要你自己建）
- ❌ 万能胶（只解决 tool-calling 标准化这一个问题）

---

## 二、生态现状（2026 年 6 月数字说话）

| 指标 | 数据 | 来源 |
|------|------|------|
| 活跃公网 MCP Server | 10,000+ | Linux Foundation, 2026.04 |
| Python SDK 月下载 | 1.64 亿 | LF 确认 |
| 社区注册 Server 总数 | PulseMCP 15,930 / Smithery 7,300 / 官方 2,000 | 多头碎片化 |
| 企业第一方 Server 供应商 | Salesforce, ServiceNow, Workday, Snowflake, Databricks, SAP, Atlassian, Stripe, GitHub, Slack, Linear, Sentry, Figma, Cloudflare... | 2025.10–2026.03 密集发布 |
| 客户端支持 | Claude Desktop, ChatGPT, Gemini, GitHub Copilot, Cursor, Windsurf, VS Code, Zed | 全主流覆盖 |
| 月活 Server 实例 | Pinterest 一家 66,000 tool calls/月，844 MAU | Pinterest 官方数据 |

**关键信号：生态已从"Anthropic 一家的事"变成全行业基础设施。**

---

## 三、谁在生产环境真正用（5 个真实案例）

### 3.1 Pinterest — MCP 平台化（最成熟的案例）

**规模**：66,000 tool calls/月，844 MAU（2025.01），节省 ~7,000 小时/月

**架构决策**：
1. **全云托管**：不允许本地 stdio Server 进生产环境，所有 MCP Server 部署到云
2. **多小 Server 而非单体**：Presto、Spark、Knowledge 各一个 Server，避免上下文窗口膨胀和安全策略混杂
3. **统一部署管线**：团队只写业务逻辑，平台处理部署/扩缩/基础设施 — 这是整个策略能跑通的关键

**治理层**：
- **Central Registry**（Web UI + API）：生产准入的唯一权威，未注册 = 不可用
- **双层鉴权**：
  - Layer 1: Envoy 代理做 JWT 验证 + 粗粒度策略（"生产 AI Chat 能访问 Presto Server"）
  - Layer 2: Server 内 `@authorize_tool(policy='...')` 装饰器做工具级细粒度授权
- **可观测性内建**：共享库提供日志/调用计数/异常追踪，每个 Server 天然可观测

**核心教训**：
> "MCP protocol gave Pinterest a shared language... That was necessary but far from sufficient. The registry, auth layers, deployment pipeline, and measurement framework are what turned a promising protocol into a production system."

---

### 3.2 leboncoin（法国最大分类广告平台）— MCP 上 ChatGPT Store

**规模**：3000 万月活用户，1500 员工，700+ 工程师参与实验

**策略**：从"观望"到"自下而上实验"到"生产发布"
- 2024.11：观望模式，不允许动生产
- 2025：允许工程师本地安装 MCP Server 连接 IDE（Cursor, Claude Desktop）
- 2026：发布正式 ChatGPT App，可搜索/筛选/浏览真实商品

**关键教训 — API 不等于 MCP Tool**：
> "We initially made the mistake of wrapping existing REST APIs 1:1 into MCP tools. It failed. REST is designed for deterministic machines; LLMs are 'synthetic humans.'"

- ❌ 错误做法：`get_order_by_id(id)` — LLM 需要先猜 ID，链式调用炸 token
- ✅ 正确做法：`search_user_orders(criteria="red sneakers")` — 语义化工具，符合人类意图

**架构**：**"三明治"模型**
```
Agent (ChatGPT)
  ↓
MCP Layer (语义翻译层 — 新写的)
  ↓
Aggregation API (已有微服务)
  ↓
Databases
```
MCP Server 不是微服务的邻居，而是**坐在它们上面**的语义翻译层。

**生产工程挑战**：
- **长连接管理**：SSE over HTTP，LLM 思考时连接必须保持，这是运维团队的新范式
- **语义可观测性**：200 OK ≠ 成功。用户说"红色车"但 Agent 没传颜色参数 = 语义失败，传统监控看不见
- **Chat-Native UI**：返回不是 JSON，是 React 组件。Agent ↔ UI 双向状态同步

---

### 3.3 Freshworks — MCP Gateway 产品化

**规模**：近 700 个 Marketplace Action 暴露为 MCP Tools，全球多区域部署

**定位**：MCP Gateway = Marketplace 和 AI Agent 之间的桥梁
- 第三方集成从 1-2 周手动工作 → **几小时**自动上线
- 新 App 接入 Action Catalog 的速度大幅增加

**Session 管理创新**：
- MCP 规范假设单机内存 Session → 分布式环境行不通
- **外部 Session Store**（Redis）：任何 Pod 都能处理任何请求
- 水平扩展 + 滚动部署无状态丢失

**三层错误模型**：Protocol errors → Gateway errors → Application errors

---

### 3.4 Salesforce — 企业级 MCP 第一方支持

- 2026 年初发布第一方 MCP Server，覆盖 CRM 核心能力
- 企业级 MCP Server 的三个差异点：
  1. 每个 tool call 都做身份验证
  2. OAuth scope 精确到单个 tool 级别
  3. 审计日志直接对接企业 SIEM

---

### 3.5 AWS — 官方 MCP 战略指南

AWS 2026 年发布了《Model Context Protocol Strategies on AWS》：
- 三个支柱：**Tool Design** + **Server Hosting** + **Governance**
- 推荐三种部署模式：单机 stdio → 远程 HTTP → MCP Gateway
- MCP Gateway 模式：集中注册所有远程 Server，统一鉴权/限流/监控

---

## 四、MCP 部署的 4 种企业拓扑

| 模式 | 适用场景 | 优点 | 代价 |
|------|----------|------|------|
| **单租户 stdio** | 个人开发者/IDE 集成 | 零网络开销，极简 | 无法共享，无治理 |
| **多租户行隔离** | SaaS 多客户 | 强隔离，每租户独立凭证 | 运维复杂，Server 数量 × 租户数 |
| **联邦 Gateway** | 200+ Server 的大型组织 | 统一鉴权/限流/监控，团队自治 | Gateway 是瓶颈和单点 |
| **边缘缓存只读** | 大流量只读查询 | 极低延迟，减轻上游压力 | 只读，缓存失效策略复杂 |

**Pinterest 选的是"联邦 Gateway 变体"**：central registry + Envoy 前置网关 + 团队自治 Server。

---

## 五、安全落地清单（不做的代价是事故）

### 5.1 规范强制要求（2025-11-25 spec）

1. **OAuth 2.1 + PKCE S256** — 远程 Server 的授权必须走这个
2. **RFC 9728 Protected Resource Metadata** — Server 必须暴露 `WWW-Authenticate` 让 Client 自动发现 Auth Server
3. **RFC 8707 Resource Indicators** — Token 必须绑定到特定 MCP Server 的 audience，防止 token 跨 Server 复用
4. **Token Passthrough 明令禁止** — MCP Server **绝对不可以**把 Client Token 转发给上游 API，必须自己获取新 Token

### 5.2 生产环境必须做的 6 件事（来自真实事故）

1. **On-Behalf-Of (OBO) 鉴权**：Agent 请求 = 用户权限，不是 Server 级别的 admin 凭证
2. **Tool 级 RBAC**：不是"能不能连 Server"，而是"能不能调这个具体 Tool"
3. **人工审批流 for 破坏性操作**：删库/改配置/发版 → 必须有人点确认
4. **SSRF/DNS Rebinding 防护**：URL 参数必须验证目的 IP，禁止内网地址
5. **Prompt Injection 防护**：Tool description 本身是攻击面（Tool Poisoning），不良 Server 的 tool description 能诱导 Agent 执行恶意操作
6. **结构化审计日志**：谁、什么时间、调了什么 Tool、参数是什么、结果是什么 → 全部留痕

### 5.3 现实：53% 的 Server 还在用静态 Token

根据审计 6,762 个 MCP Server 的结果：
- 13% 不可达（挂了/废弃了）
- **53% 使用硬编码 Token**（泄露 = 无限访问，无过期，无撤销）
- 大量 Server 无法外部验证安全状态

**结论**：MCP 协议本身不提供安全，安全完全取决于你怎么建。

---

## 六、MCP vs A2A — 一张表说清楚

| 维度 | MCP | A2A |
|------|-----|-----|
| **解决什么问题** | LLM 怎么调 Tool | Agent 之间怎么协作 |
| **类比** | USB-C 接口 | 部门之间的工作流系统 |
| **通信模型** | Client-Server（LLM 是主控） | Peer-to-Peer（Agent 是平等协作者） |
| **调用方式** | 同步 tool call → 返回结果 | 异步任务委托 → 流式进度 → 最终完成 |
| **调用方角色** | LLM 是"大脑"，Server 是"手脚" | 双方都是"大脑" |
| **成熟度（Q2 2026）** | **生产就绪** ✅ | 早期采用，12-18 个月后成熟 |
| **谁在做** | Anthropic 主导，全行业参与 | Google 主导，多厂商工作组 |
| **安全模型** | OAuth 2.1 + scope per tool | OAuth + Agent Card 声明能力 |
| **典型场景** | Agent 查数据库/发邮件/调 API | 编排 Agent 将子任务委派给其他 Agent |
| **并存关系** | ⚠️ 不是竞争，是互补 | Agent 用 A2A 委派任务，被委派的 Agent 用 MCP 调 Tool |

**一句话**：MCP = Agent 的"工具箱标准化"，A2A = Agent 之间的"外包合同标准化"。

---

## 七、落地路线图（从 PoC 到 Production）

### Phase 1：实验期（1-2 周）
- 选 1-2 个高频内部 Tool（Jira/GitHub/Slack），写 MCP Server
- 本地 stdio 模式，连 Claude Desktop / Cursor 给个人用
- **目标**：感受 MCP 是什么，不是评估能不能上生产

### Phase 2：平台化基础（4-6 周）
- 建立 **Central Registry**（类似 Pinterest 的做法）
- 实现 **OAuth 2.1 + PKCE S256** 鉴权
- 部署一个 **MCP Gateway**（统一入口，不要直接暴露裸 Server）
- 选 1 个最安全的内部系统做第一个远程 Server

### Phase 3：生产试点（4-8 周）
- 上线 3-5 个 MCP Server（选低风险，如文档搜索/知识库查询）
- 建立 **可观测性**：tool call 量/延迟/错误率/语义异常
- 建立 **审计日志**：所有 tool call 留痕
- 实行 **Tool 级 RBAC**

### Phase 4：规模推广（持续）
- **统一部署管线**：团队只管写 tool 定义，平台管部署
- **多租户隔离**：如果 SaaS 场景，external Session Store
- **Prompt Injection 监控**：定期扫描 tool description 注入风险
- **Shadow MCP 治理**：通过快速审批流程让开发者走正路，而不是封堵

---

## 八、常见踩坑（来自真实案例）

| 踩坑 | 正确做法 |
|------|----------|
| 把 REST API 1:1 映射成 MCP Tool | 设计**语义化 Tool**：`searchOrders("red sneakers")` 而非 `getOrderById(id)` |
| 本地 stdio 直接暴露给生产 Agent | 所有生产 Server 必须远程 HTTP + 鉴权 |
| 静态 Token 当鉴权 | OAuth 2.1 + PKCE S256 + audience binding |
| 把 Client Token 转发给上游 API | **严禁**。Server 必须自己获取上游 Token |
| 单体 Server 塞 50 个 Tool | 拆成多个小 Server，每个 3-8 个 Tool |
| MCP Server 当微服务邻居 | MCP Server 是**语义翻译层**，坐聚合 API 上面 |
| 忽略长连接管理 | LLM 调用是长会话，需要 SSE/Streamable HTTP + 运维适配 |
| 只关注 tech metrics 忽略语义 drift | 200 OK ≠ 成功，建立**语义可观测性** |

---

## 九、对 Tony 的推荐

### 如果现在就要动手

1. **从内部工具切入**，不要一上来就连生产数据库
   - Jira/GitHub/Confluence/飞书文档的 MCP Server 已有成熟实现
   - 让团队在 IDE 里先用起来，感受 MCP 的工作模式

2. **Gateway 模式起步**
   - 不要暴露裸 MCP Server，用一个 Gateway 做统一入口
   - Gateway 负责鉴权、限流、审计、路由
   - 你的网关/安全背景在这块有天然优势

3. **安全前置，不要事后补**
   - OAuth 2.1 + PKCE S256 从一开始就做
   - Tool 级 RBAC 不是 nice-to-have，是 must-have
   - Token passthrough = 红线

4. **关注传输层和工具设计，而不是协议本身**
   - MCP 协议已经稳定，工程难点在它周围的东西
   - 最有价值的三件事：**Registry + Auth + Deployment Pipeline**

### 值得持续关注的方向

- **MCP Registry 联邦化**（类似 npm + sigstore）：服务发现和信任链
- **MCP Server 信任评分**（类似 SSL Labs）：独立的安全审计层
- **MCP + A2A 的组合使用**：单个 Agent 用 MCP 调工具 + 多 Agent 用 A2A 协作
- **工具描述工程（Tool Description Engineering）**：这会是新的"Prompt Engineering"

---

## 参考来源

1. Pinterest MCP Ecosystem — ByteByteGo, 2026
2. leboncoin MCP Production Journey — leboncoin tech blog, 2026.02
3. Freshworks MCP Gateway — Freshworks Engineering, 2026.05
4. AWS MCP Strategies — AWS Prescriptive Guidance, 2026
5. MCP Server Ecosystem 2026 — CallSphere / RunLocalAI / DigitalApplied
6. MCP Server Patterns for Enterprise — DigitalApplied, 2026.05
7. MCP Security Risks & Best Practices — TrueFoundry, 2026
8. IETF MCP Security Considerations — draft-mohiuddin-mcp-security, 2026
9. Bridging Protocol and Production (arXiv:2603.13417) — MCP production design patterns paper
10. Enterprise-Grade Security for MCP (arXiv:2504.08623) — security frameworks paper
11. MCP vs A2A — DigitalOcean / VentureBeat / AgentModeAI / TheSpawn, 2026
12. I audited 6,762 MCP servers — DEV Community, 2026
