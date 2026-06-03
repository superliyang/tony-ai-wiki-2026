---
title: AI 面试详细考点地图：从原理到系统与组织
type: checklist
status: active
created: 2026-04-29
updated: 2026-04-29
---

# AI 面试详细考点地图：从原理到系统与组织

> 这页不是题库，而是“面试官可能在哪些点上深挖你”的详细考点地图。
> 用法：先看 [[./AI 面试上帝视角：从底层原理到业务落地|AI 面试上帝视角]]，再用这页逐层查漏。

## 总体心法

每个考点都要准备四层：

1. `一句话定义`：这个东西是什么
2. `为什么重要`：它解决什么问题
3. `工程边界`：它什么时候失效、代价是什么
4. `生产验证`：用什么指标、评测、门禁证明它可用

如果只能背一句：

> AI 面试最怕“只会名词”，最强的是能把每个名词讲回 `原理 -> 取舍 -> 指标 -> 风险 -> 机制`。

## 1. 底层原理考点

### Tokenization

- 要会讲：token 是模型处理文本的离散单位，不等于中文词或英文单词
- 常见追问：为什么 token 数会影响成本、延迟和上下文长度
- 高级回答：tokenization 会影响多语言、代码、表格、长文档和 OCR 输入的成本结构
- 容易掉坑：只说“分词”，不讲成本和上下文预算

### Embedding

- 要会讲：embedding 是把离散 token / 文档 / query 映射到向量空间
- 常见追问：embedding 为什么能做语义检索，为什么也会检错
- 高级回答：embedding 检索适合语义相似，不等于事实一致；需要 hybrid search、rerank、metadata filter 和 eval
- 容易掉坑：把 embedding 当成万能知识理解

### Attention

- 要会讲：attention 让模型在生成时按相关性聚合上下文信息
- 常见追问：attention 为什么导致长上下文成本高
- 高级回答：长上下文不是免费记忆，KV Cache、attention pattern、context packing 都会影响成本和质量
- 容易掉坑：只会背 Q/K/V，不会讲系统代价

### Sampling

- 要会讲：temperature、top-p、top-k 影响输出随机性和多样性
- 常见追问：生产系统 temperature 怎么设
- 高级回答：高风险任务应低随机、强结构化、强校验；创意任务可提高随机性；同一产品不同步骤可用不同 decoding 策略
- 容易掉坑：把 temperature 当成“越高越聪明”

### Hallucination

- 要会讲：hallucination 来自概率生成、训练分布、缺少 grounding、目标函数不等于事实性
- 常见追问：为什么 RAG 不能彻底消灭幻觉
- 高级回答：RAG 只能改善 grounding，还要处理检索漏召、冲突证据、引用校验、答案 abstention 和人工复核
- 容易掉坑：说“加 RAG 就解决”

## 2. 训练与后训练考点

### Pretraining

- 要会讲：pretraining 通过大规模数据学习语言、知识、模式和压缩表示
- 常见追问：高质量数据为什么比单纯数据量重要
- 高级回答：数据覆盖、去重、污染、配比、难例、版权/合规都会影响能力和风险
- 容易掉坑：只说“数据越多越好”

### SFT

- 要会讲：SFT 用高质量示范让模型学会指令跟随和任务格式
- 常见追问：SFT 为什么可能让模型更会“像样回答”，但不一定更真实
- 高级回答：SFT 改变输出分布，但事实性仍受 base model、数据和 grounding 限制
- 容易掉坑：把 SFT 当成注入知识的首选

### RLHF / RLAIF

- 要会讲：RLHF / RLAIF 用偏好信号塑造行为风格、帮助性和安全边界
- 常见追问：reward hacking 是什么
- 高级回答：偏好优化会带来过度迎合、拒答过度、表面安全和 reward model 偏差，需要 eval 和红队
- 容易掉坑：只说“让模型更符合人类偏好”

### DPO / PPO

- 要会讲：PPO 更复杂、控制力强；DPO 更简单稳定，适合工程快速落地
- 常见追问：资源有限团队怎么选
- 高级回答：先看目标是行为微调、偏好对齐还是复杂策略优化；多数应用团队优先 DPO / SFT + eval，不轻易自建 PPO
- 容易掉坑：只比较算法名字，不讲工程成本

### Fine-tuning vs RAG

- 要会讲：fine-tuning 改行为和任务分布，RAG 接外部知识
- 常见追问：企业知识库为什么通常先 RAG
- 高级回答：企业知识更新快、权限复杂、审计要求高；RAG 更容易更新、引用和回滚
- 容易掉坑：把私有知识都拿去微调

## 3. 推理与服务考点

### KV Cache

- 要会讲：KV Cache 复用历史 token 的 key/value，提升自回归生成效率
- 常见追问：多轮对话 KV Cache 爆了怎么办
- 高级回答：滑窗、摘要、context pruning、session 分层、长短请求分池、模型路由、预算控制
- 容易掉坑：只讲缓存，不讲质量回归

### Continuous Batching

- 要会讲：连续批处理提高 GPU 利用率和吞吐
- 常见追问：为什么吞吐上去了尾延迟可能变差
- 高级回答：需要优先级队列、请求分层、timeout、SLO guardrail 和容量预留
- 容易掉坑：只讲省钱，不讲 SLO

### Model Routing

- 要会讲：按任务复杂度、风险、成本、延迟选择模型
- 常见追问：如何防路由震荡
- 高级回答：设置置信度阈值、升级策略、fallback、冷启动保护、路由版本化和回归评测
- 容易掉坑：只说“简单任务小模型，复杂任务大模型”

### Cost Model

- 要会讲：成本来自 input/output token、模型单价、重试、检索、工具、GPU、人工审核和运维
- 常见追问：成本突然翻倍先看什么
- 高级回答：先看 token 长度、重试率、路由命中、缓存命中、异常流量、长上下文占比、供应商价格变化
- 容易掉坑：只看模型 API 单价

### SLO

- 要会讲：AI SLO = 传统可用性 + AI 质量指标
- 常见追问：AI 系统 SLO 包哪些指标
- 高级回答：availability、latency、error rate、task success、faithfulness、human handoff、safety incident、unit cost
- 容易掉坑：只讲 QPS / latency

## 4. RAG 与知识系统考点

### Chunking

- 要会讲：chunk 大小影响召回、上下文噪声、引用准确性和成本
- 常见追问：chunk 太大/太小分别有什么问题
- 高级回答：按文档结构、标题层级、表格、权限边界和任务粒度设计 chunk；用 retrieval eval 验证
- 容易掉坑：固定 500 字切一切

### Query Rewrite

- 要会讲：把用户问题改写成更适合检索的 query
- 常见追问：query rewrite 为什么可能伤害结果
- 高级回答：改写可能丢约束或过度扩展，需要保留原 query、生成多个 query、做对照评测
- 容易掉坑：默认 rewrite 一定提升

### Hybrid Search

- 要会讲：BM25 擅长关键词，vector 擅长语义，hybrid 提升召回稳健性
- 常见追问：什么时候关键词比向量更重要
- 高级回答：专有名词、错误码、合同条款、产品型号、代码符号通常需要 lexical match
- 容易掉坑：只会向量数据库

### Rerank

- 要会讲：rerank 对候选文档重新排序，提高最终上下文质量
- 常见追问：rerank 的代价是什么
- 高级回答：增加延迟和成本；需要按场景决定是否 top-k rerank、是否缓存、是否小模型 rerank
- 容易掉坑：不看端到端 latency

### Permission-Aware RAG

- 要会讲：检索必须尊重用户权限，不能先召回再靠模型不说
- 常见追问：多租户 RAG 怎么防越权
- 高级回答：索引层权限过滤、metadata ACL、tenant isolation、audit log、引用可追踪
- 容易掉坑：把权限交给 prompt

## 5. Agent 与工具调用考点

### Tool Schema

- 要会讲：工具 schema 是模型和真实系统之间的契约
- 常见追问：schema 怎么设计更稳
- 高级回答：强类型、参数约束、幂等键、错误码、dry-run、权限声明、可观测 trace
- 容易掉坑：只写 function name 和 description

### Planning

- 要会讲：planning 适合长任务拆解，但会引入偏航和复杂度
- 常见追问：什么时候不用 planner
- 高级回答：路径固定、高风险、可工作流化的任务优先显式 workflow，不盲目让模型规划
- 容易掉坑：把 planner 当成高级的代名词

### Multi-Agent

- 要会讲：multi-agent 适合并行、角色专业化和互审，但增加协调成本
- 常见追问：如何避免多 agent 互相扯皮
- 高级回答：明确角色、共享状态、终止条件、仲裁者、预算、trace、任务级 eval
- 容易掉坑：简单任务也上多 agent

### Sandbox

- 要会讲：sandbox 限制 agent 的执行环境，保护文件、网络、凭证和系统状态
- 常见追问：shell agent 最大风险是什么
- 高级回答：prompt injection、危险命令、数据泄露、供应链安装、越权修改；需要 allowlist、approval、network policy、artifact review
- 容易掉坑：只说“加权限控制”

### Computer Use

- 要会讲：computer use 适合没有 API 或跨 UI 的任务，但脆弱且风险高
- 常见追问：为什么能用 API 就别优先 computer use
- 高级回答：UI 漂移、不可复现、动作风险、审计困难；API/tool integration 更可控
- 容易掉坑：被 demo 酷炫感带跑

## 6. Eval 与上线治理考点

### Golden Set

- 要会讲：golden set 是代表关键场景和风险边界的评测集
- 常见追问：golden set 怎么维护
- 高级回答：线上 bad case 回灌、版本化、去污染、覆盖高频/高风险/长尾、定期抽样复核
- 容易掉坑：一次性手工凑几十题

### Task-Level Eval

- 要会讲：AI 系统最终看任务是否完成，而不是单轮回答漂不漂亮
- 常见追问：coding agent 怎么评测
- 高级回答：看 patch 是否通过测试、是否最小修改、是否符合约束、是否引入回归、是否解释清楚
- 容易掉坑：只用 LLM-as-judge 评分

### Release Gate

- 要会讲：release gate 是上线前必须过的质量、安全、成本、回滚门槛
- 常见追问：哪些指标不过坚决不上线
- 高级回答：高风险事实错误、越权、安全回归、成本失控、人工接管率异常、核心任务完成率下降
- 容易掉坑：只靠人工主观验收

### A/B Test

- 要会讲：A/B 要看护栏指标，不能只看点击率或满意度
- 常见追问：短期指标提升、长期变差怎么办
- 高级回答：增加观察窗口、分人群分析、看投诉/人工接管/复访/成本，必要时停止放量
- 容易掉坑：只看平均值

### Incident Review

- 要会讲：事故复盘要从单点修复升级到机制修复
- 常见追问：如何把事故变成长期能力
- 高级回答：补 regression、runbook、alert、release gate、owner、培训和设计评审 checklist
- 容易掉坑：只说“以后注意”

## 7. 安全、隐私与合规考点

### Prompt Injection

- 要会讲：攻击者通过输入诱导模型忽略规则、泄露信息或滥用工具
- 常见追问：怎么防
- 高级回答：输入隔离、指令优先级、工具权限、内容检测、引用边界、approval、日志审计、红队评测
- 容易掉坑：只靠 system prompt

### Tool Abuse

- 要会讲：模型调用真实工具时可能造成外部副作用
- 常见追问：高风险工具如何上线
- 高级回答：risk tier、dry-run、human approval、rate limit、idempotency、rollback、audit
- 容易掉坑：把所有工具都同等对待

### PII

- 要会讲：PII 需要识别、最小化、脱敏、权限、审计和保留策略
- 常见追问：客服 Copilot 如何处理敏感信息
- 高级回答：输入输出双向检测、按角色授权、敏感字段 mask、高风险回答人工复核、日志脱敏
- 容易掉坑：只说“不把数据传出去”

### Tenant Isolation

- 要会讲：多租户隔离要覆盖数据、索引、日志、缓存、模型上下文和工具权限
- 常见追问：RAG 越权怎么查
- 高级回答：trace query、retrieval result、ACL metadata、引用、用户角色、索引版本和审计日志
- 容易掉坑：只隔离数据库，不隔离向量索引和缓存

### Audit

- 要会讲：审计不是事后日志堆积，而是能复现决策链
- 常见追问：AI 动作如何审计
- 高级回答：记录输入、上下文、检索结果、模型版本、prompt 版本、工具调用、审批、输出和用户确认
- 容易掉坑：只保留最终回答

## 8. 产品落地与组织考点

### Workflow Fit

- 要会讲：AI 能力必须嵌入真实工作流，而不是停在聊天框
- 常见追问：如何判断场景适合 AI
- 高级回答：高频、耗时、可验证、有容错或可兜底、有明确 owner 的场景优先
- 容易掉坑：看到任务就想自动化

### Assistant vs Copilot vs Automation

- 要会讲：assistant 偏问答，copilot 偏辅助决策，automation 偏流程执行
- 常见追问：什么时候从 copilot 升级到 automation
- 高级回答：当任务边界清晰、错误可控、指标稳定、审批和回滚完备时再升级
- 容易掉坑：一开始就全自动

### Adoption

- 要会讲：adoption 不只是 DAU，还要看 retained usage 和 workflow dependency
- 常见追问：用户试了但不用怎么办
- 高级回答：看任务真实痛点、答案可信度、入口摩擦、延迟、培训、激励和 manager loop
- 容易掉坑：只做功能不做 change management

### ROI

- 要会讲：ROI = 收益 - 全成本，不只是节省 token 或调用次数
- 常见追问：AI 项目 ROI 怎么算
- 高级回答：节省人时、提升转化、降低错误、缩短周期、降低培训成本，同时扣除模型、工程、运维、审核、治理成本
- 容易掉坑：只报“节省多少小时”

### Team Mechanism

- 要会讲：高级候选人要把一次项目沉淀成团队机制
- 常见追问：如何避免团队各写各的 prompt
- 高级回答：prompt registry、eval suite、release review、shared components、incident library、培训和设计模板
- 容易掉坑：只靠口头分享

## 9. 面试官最爱追的“边界题”

- `什么时候不用大模型？`
- `什么时候不用 RAG？`
- `什么时候不用 Agent？`
- `什么时候不用多 Agent？`
- `什么时候不用 fine-tuning？`
- `什么时候不上线？`
- `什么时候宁愿牺牲体验也要加审批？`
- `什么时候强模型不如小模型？`
- `什么时候 voice 不如 text？`
- `什么时候 computer use 不如 API integration？`

回答这些题的结构：

1. 先说适用边界
2. 再说不适用条件
3. 再给替代方案
4. 最后给验证指标

## 10. 面试前最后检查

- 我能否用 2 分钟讲清 `Transformer -> Pretraining -> SFT/RLHF -> Serving -> RAG/Agent -> Eval -> Governance -> ROI`
- 我能否解释 3 个失败根因：事实错、任务失败、风险越界
- 我能否给出 5 个生产指标：任务完成率、事实错误率、人工接管率、延迟、单位成本
- 我能否讲一个事故，并说明机制化改进
- 我能否讲清一个“不上线”的判断
- 我能否把一个 demo 改造成 production-ready design
- 我能否从研究、工程、产品、治理四种角度回答同一道题

## 关联

- [[./AI 面试上帝视角：从底层原理到业务落地|AI 面试上帝视角]]
- [[./06-Answer-Playbooks/大模型与 AI 全景回答母版|大模型与 AI 全景回答母版]]
- [[./05-Question-Banks/15-细节追问与深挖题库|细节追问与深挖题库]]
- [[./完整面试题蓝图：如果是我会怎么准备|完整面试题蓝图]]
