---
title: AI 项目从 0 到 1 落地 Playbook
type: playbook
status: active
domain: AI-Architect
created: 2026-05-05
updated: 2026-05-05
---

# AI 项目从 0 到 1 落地 Playbook

> 用于把一个 AI 想法从业务机会变成可上线、可运营、可治理的系统。

## 总原则

AI 项目最容易死在两个地方：

- POC 很惊艳，但没有 eval、安全、权限、成本和运维，无法上线。
- 技术很完整，但业务流程没有改变，ROI 不成立。

所以从 0 到 1 的核心不是“先做 demo”，而是：

`场景选择 -> 任务边界 -> 数据准备 -> 最小原型 -> 评测闭环 -> 安全治理 -> 灰度上线 -> 运营改进`

## Step 1：选择场景

优先选择：

- 高频任务。
- 知识密集任务。
- 结果可评估任务。
- 有明确 owner 的任务。
- 错误可控、可人工兜底的任务。

暂缓选择：

- 高风险、不可逆、强监管但无治理基础的任务。
- 数据权限不清的任务。
- 成功标准说不清的任务。
- 只为“用 AI”而用 AI 的任务。

## Step 2：定义任务边界

写清楚：

- AI 要完成什么？
- 不完成什么？
- 输入是什么？
- 输出是什么？
- 谁审核？
- 谁承担结果？
- 失败时怎么办？

输出：

- AI task brief
- success criteria
- human handoff rules

## Step 3：判断架构模式

| 任务类型 | 推荐模式 |
|---|---|
| 文档问答 | RAG |
| 信息抽取 | LLM + schema |
| 报告生成 | RAG + structured generation |
| 多步骤业务办理 | workflow + tool calling |
| 需要自主执行 | bounded agent + approval |
| 高风险决策 | decision support + human review |

## Step 4：准备数据和知识

必须准备：

- 数据源清单。
- 权限规则。
- 敏感数据处理。
- 文档清洗和结构化。
- metadata 和版本。
- 初始 eval set。

如果这一步做不清，项目不要急着做 agent。

## Step 5：做最小原型

最小原型应该验证：

- 模型能否完成核心任务。
- 知识能否被正确检索。
- 输出是否可解释、可引用。
- 工具调用是否可控。
- 用户是否真的愿意用。

不要一开始就做：

- 完整平台。
- 多 Agent 系统。
- 复杂微调。
- 全自动闭环。

## Step 6：建立评测闭环

至少建立：

- 20-50 条 golden cases。
- 正常样例、边界样例、失败样例、恶意样例。
- 人工评审标准。
- 回归测试流程。

指标：

- task success rate
- faithfulness
- retrieval precision / recall
- policy violation rate
- human handoff rate
- cost per successful task

## Step 7：补安全和治理

上线前必须有：

- 数据权限过滤。
- prompt injection 测试。
- 高风险工具审批。
- 日志脱敏。
- 审计链路。
- kill switch。
- 事故响应 owner。

## Step 8：灰度上线

建议路径：

1. 内部测试。
2. shadow mode。
3. 小流量灰度。
4. 人工审核模式。
5. 半自动模式。
6. 局部自动化。

每一步都要有退出条件。

## Step 9：运营改进

上线后持续看：

- 用户真实任务分布。
- 失败样例。
- 高成本请求。
- 高风险输入。
- 工具失败。
- 人工接管。
- 投诉和事故。

把这些回写到：

- prompt
- retrieval
- eval set
- policy
- workflow
- training / fine-tuning 候选

## 常见失败模式

- 只做 demo，不做 eval。
- 只做问答，不做权限。
- 只接工具，不做审批。
- 只看准确率，不看成本和延迟。
- 只做 POC，不改业务流程。
- 只靠模型，不做产品和运营。
- 没有 owner，出了错没人管。

## 0 到 1 交付物清单

- AI 场景选择表
- AI 架构设计文档
- 数据与权限说明
- eval set 和评测报告
- 安全评审报告
- 灰度上线计划
- 运营指标看板
- 复盘与迭代计划

## 关联

- [[./AI 架构评审 Playbook|AI 架构评审 Playbook]]
- [[../07-Templates/AI 架构设计模板|AI 架构设计模板]]
- [[../08-Playbooks/AI 架构师 90 天迁移 Playbook|AI 架构师 90 天迁移 Playbook]]
- [[../../AI-Applications/05-Topics/Agent Portfolio and Use Case Prioritization|Agent Portfolio and Use Case Prioritization]]
- [[../../AI-Engineering/08-Maps/MLOps 与 LLMOps 工程图|MLOps 与 LLMOps 工程图]]

