---
title: AI 生产运行 Runbook
type: runbook
status: active
domain: AI-Architect
created: 2026-05-09
updated: 2026-05-09
---

# AI 生产运行 Runbook

> 目标：AI 系统上线后，不靠“大家盯着看”，而是用 SLO、告警、分级响应、回滚和 bad case 运营维持稳定。

## 运行总原则

AI 生产运行要同时盯五类指标：

1. **Availability**：服务是否可用。
2. **Quality**：回答、建议或动作是否正确。
3. **Safety**：是否出现越权、泄露、危险输出或 tool abuse。
4. **Cost**：token、模型、工具和 eval 成本是否异常。
5. **Latency**：p95 / p99 是否影响体验。

## 1. 运行对象

| 对象 | 需要监控什么 |
|---|---|
| 应用服务 | availability、error rate、p95 latency |
| 模型调用 | timeout、rate limit、fallback、token、cost |
| RAG 检索 | recall、空召回、权限过滤、引用准确率 |
| Agent 工具 | tool success、tool error、side-effect、approval |
| Eval | pass rate、regression fail、bad case 回归 |
| 安全策略 | injection hit、PII hit、permission block、tool block |
| 用户反馈 | thumbs down、纠错、人工接管、投诉 |

## 2. SLO 模板

| 指标 | 示例目标 | 备注 |
|---|---|---|
| Availability | 99.5% / 99.9% | 按业务重要性定义 |
| p95 latency | RAG 3-5 秒，Agent 可异步 | 复杂任务可拆同步/异步 |
| Model error rate | < 1% | 包括超时、限流、供应商错误 |
| Safety P0 | 0 | 越权、泄露、高风险误操作 |
| Eval regression | 关键用例 100% 通过 | 上线 gate |
| Cost per task | 在预算阈值内 | 按业务价值反推 |
| Trace coverage | > 95% | 生产问题必须能复盘 |

## 3. 告警分级

| 级别 | 触发条件 | 响应 |
|---|---|---|
| SEV0 | 数据泄露、越权写操作、资金/合同重大风险 | 立即 kill switch，安全和业务负责人介入 |
| SEV1 | 大面积错误回答、高风险建议误放行、模型调用整体不可用 | 降级或回滚，启动 incident |
| SEV2 | 局部业务线质量下降、成本异常、延迟明显上升 | 限流、切模型、修复后回归 |
| SEV3 | 单点 bad case、体验问题、低风险误答 | 进入 bad case 队列 |

## 4. 常见故障与处置

### 模型不可用或超时

- 检查供应商状态、限额、网络、gateway。
- 切换 fallback model。
- 对非关键任务返回异步处理。
- 对关键任务降级为传统搜索或人工入口。

### RAG 答案错误

- 查看 trace 中 retrieval docs。
- 判断是 query rewrite、召回、rerank、chunk、知识过期还是生成问题。
- 修复知识或检索策略。
- 将 case 加入 regression eval。

### 越权或敏感数据泄露

- 立即关闭相关知识源或能力。
- 查 trace、权限过滤、输出日志。
- 评估影响范围。
- 通知安全和业务 Owner。
- 修复后必须通过 permission / PII eval。

### Agent 工具误调用

- 立即关闭高风险 tool 或切到人工确认。
- 检查 tool schema、参数校验、workflow 状态。
- 确认是否需要业务回滚或补偿。
- 增加 tool abuse eval 和审批 gate。

### 成本异常

- 检查流量、token、重试、循环调用、超长上下文。
- 启用限流、budget、cache、context compression。
- 低价值任务切低成本模型。
- 复盘是否被滥用或攻击。

## 5. 回滚策略

AI 系统的回滚对象不只有代码：

| 对象 | 回滚方式 |
|---|---|
| 模型 | 切回上一模型或 fallback 模型 |
| Prompt | 回滚到上一 prompt version |
| 知识索引 | 回滚到上一 index snapshot |
| 工具 | 关闭 tool、切只读、强制人工确认 |
| 策略 | 恢复旧 policy 或提高拦截等级 |
| 流量 | 灰度降级、按用户组关闭 |
| 应用 | 退回传统流程或人工入口 |

## 6. Incident 复盘模板

| 字段 | 内容 |
|---|---|
| incident_id |  |
| 时间 |  |
| 影响范围 | 用户、业务线、请求量 |
| 严重级别 | SEV0 / SEV1 / SEV2 / SEV3 |
| 触发方式 | 告警 / 用户反馈 / 人工巡检 |
| 根因 | 模型 / prompt / retrieval / tool / policy / data / infra |
| 处置动作 |  |
| 回滚动作 |  |
| 恢复时间 |  |
| 后续改进 |  |
| 是否进入 eval | yes / no |

## 7. Bad Case 运营节奏

| 周期 | 动作 |
|---|---|
| 每日 | 看 P0/P1 bad case、安全命中、成本异常 |
| 每周 | 聚类 bad case，更新 eval set，修复知识和 prompt |
| 每双周 | 复盘指标趋势，调整模型路由和成本策略 |
| 每月 | 评审 risk register、权限策略、供应商风险和平台规范 |

## 8. 值班检查清单

- 昨日请求量是否异常？
- p95 / p99 是否异常？
- 模型 error / fallback 是否上升？
- 成本是否超预算？
- 安全策略命中是否异常？
- RAG 空召回和低置信度是否上升？
- Agent tool failure 是否上升？
- Top bad cases 是否已分配 Owner？
- 是否有需要进入 eval 的新 case？

## 9. 面试表达

一句话：

> AI 生产运行不只是服务可用，还要同时运行质量、安全、成本、延迟和反馈闭环；回滚对象也不只是代码，还包括模型、prompt、索引、工具和策略。

三分钟：

> 我会把 AI 线上运行分成 availability、quality、safety、cost、latency 五类指标。每次请求保留 trace，能看到模型、prompt、retrieval、tool、token、成本和安全命中。故障分 SEV0 到 SEV3：数据泄露或高风险误操作立即 kill switch；质量下降则回滚模型、prompt、索引或策略；普通 bad case 进入运营队列并回灌 eval。这样 AI 系统不是上线后靠感觉维护，而是像生产系统一样有 SLO、告警、回滚和复盘。

## 关联

- [[./AI 生产化 Readiness Playbook|AI 生产化 Readiness Playbook]]
- [[../07-Templates/AI Eval 与 Trace 工作簿|AI Eval 与 Trace 工作簿]]
- [[../07-Templates/AI 安全威胁建模模板|AI 安全威胁建模模板]]
- [[../05-Topics/LLMOps 与 AgentOps 架构师视角|LLMOps 与 AgentOps 架构师视角]]
- [[../05-Topics/AI 成本、延迟与容量架构师视角|AI 成本、延迟与容量架构师视角]]
