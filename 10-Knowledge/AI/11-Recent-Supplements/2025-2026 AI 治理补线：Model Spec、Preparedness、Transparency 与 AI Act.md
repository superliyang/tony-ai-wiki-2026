---
title: 2025-2026 AI 治理补线：Model Spec、Preparedness、Transparency 与 AI Act
type: guide
status: active
updated: 2026-04-13
---

# 2025-2026 AI 治理补线：Model Spec、Preparedness、Transparency 与 AI Act

> 这页补的是过去很容易被当成“合规附录”，但到 `2025-2026` 已经开始决定产品上线、企业采购和模型部署边界的那条线：`模型行为治理`。

## 先说边界

- 这里讨论的不是一般意义上的 app guardrails，而是 `模型如何被约束、解释、披露和放行`。
- 这条线跨 `AI Safety`、`AI Security`、`产品治理` 和 `监管义务`。
- 这里的关键不是把法律条文全背下来，而是理解为什么 frontier AI 已经开始把行为规范、准备度框架和透明度资产做成正式公开界面。

## 一页总表

| 锚点 | 时间 | 它真正补上的东西 | 你该如何理解 |
| --- | --- | --- | --- |
| [OpenAI Preparedness Framework update](https://openai.com/index/updating-our-preparedness-framework/) | 2025-04-15 | 把 `Capabilities Reports + Safeguards Reports + deployment decisions` 讲成正式治理流程 | frontier deployment 已经不再只靠内部直觉 |
| [OpenAI Model Spec](https://model-spec.openai.com/) | 持续更新 | 把模型行为准则做成公开、版本化说明 | 行为边界开始从隐式 prompt 变成显式资产 |
| [Claude’s Constitution — January 2026](https://www-cdn.anthropic.com/9214f02e82c4489fb6cf45441d448a1ecd1a3aca/claudes-constitution.pdf) | 2026-01-21 | 把 operator、user、other AI agent、honesty、context confidentiality 讲成细化规则 | model behavior governance 越来越接近真实部署语境 |
| [Anthropic Transparency](https://www.anthropic.com/transparency) | 2025-2026 | 把系统级透明度做成长期入口 | transparency 不再只是发一篇 system card 就结束 |
| [EU AI Act GPAI guidelines](https://digital-strategy.ec.europa.eu/en/library/guidelines-scope-obligations-providers-general-purpose-ai-models-under-ai-act) | 2025-07-18 | 明确 general-purpose AI model obligations，并指出 `2025-08-02` 起开始适用 | 外部监管开始真正进入 GPAI 主路径 |

## 路线一：模型行为不再只藏在 system prompt 里

以前很多人谈模型行为治理，实际停留在：

- safety policy
- usage policy
- 系统 prompt
- content moderation

但 `2025-2026` 的变化是，frontier 公司开始把“模型应该如何表现”做成显式文档层。

这代表几件事：

- 行为边界开始可以被公开讨论
- 行为准则开始具备版本化和外部审视性
- `operator / user / system / other agent` 的角色关系开始被写清楚

尤其是 `2026-01-21` 发布的 [Claude’s Constitution — January 2026](https://www-cdn.anthropic.com/9214f02e82c4489fb6cf45441d448a1ecd1a3aca/claudes-constitution.pdf)，已经不是一句抽象“helpful, honest, harmless”，而是把：

- operator 指令
- user 请求
- 其他 AI agent 的互动
- system prompt 的保密与诚实边界

放进更细的行为判断语境里。

## 路线二：Preparedness 变成上线前的正式门槛语言

[OpenAI Preparedness Framework update](https://openai.com/index/updating-our-preparedness-framework/) 很值得单独记住，因为它把一个重要变化说得很清楚：

- 不只发布 capabilities findings
- 还要发布 safeguards design 与 verification
- 最终由更正式的流程决定是否部署

这件事会影响你对 frontier 模型发布的判断方式：

- 不能只看 benchmark
- 不能只看 system card
- 还要看它如何描述风险阈值、缓解措施和 residual risk

更直白地说，frontier AI 的部署语言开始从：

- “这个模型很强”

转向：

- “这个模型强到了什么程度”
- “风险在哪里”
- “用什么 safeguards 才敢放”

## 路线三：Transparency 变成持续界面，而不是一次性公关材料

这一轮另一个很关键的变化，是 transparency 开始被当成长期资产，而不是单篇博客。

如果你把这条线只理解成“发 system card”，就会低估它。

更准确地说，现在的 transparency 资产正在分成几层：

- `system card / trust report`
- `preparedness / safeguards reporting`
- `behavior spec / constitution`
- `policy / external commitments`
- `regulator-facing obligations`

这意味着成熟组织不再只是说“我们很重视安全”，而是逐步把：

- 风险语言
- 行为语言
- 审核语言
- 放行语言

收成更稳定的治理资产。

## 路线四：外部监管已经开始真正约束 GPAI 主路径

[EU AI Act GPAI guidelines](https://digital-strategy.ec.europa.eu/en/library/guidelines-scope-obligations-providers-general-purpose-ai-models-under-ai-act) 有一个特别值得记住的具体日期：

- `2025-07-18` 发布指南
- 针对 GPAI model providers 的相关义务在 `2025-08-02` 起开始适用

这说明一件很关键的事：

- `general-purpose AI model` 不再只是技术分类
- 它已经是监管分类和义务分类

所以如果你研究的是企业 AI、平台 AI 或 frontier provider，这条线必须进知识骨架，而不能永远放在“以后再补的法律问题”里。

## 这一轮补线后，你应该怎么调整自己的判断框架

现在如果你只会问：

- 模型强不强
- 价格贵不贵
- context 大不大

那已经不够。

更成熟的判断至少要多问四类问题：

1. `行为边界`：模型默认怎么做决定，谁能约束它
2. `准备度`：上线前做了哪些 capabilities / safeguards 评估
3. `透明度`：哪些资产是公开可审视的，哪些只是口头承诺
4. `监管义务`：外部规则会如何反过来影响部署和采购

## 最短回顾顺序

1. [[../06-Topics/AI Safety 与 AI Security|AI Safety 与 AI Security]]
2. [[../06-Topics/模型行为治理：Model Spec、Preparedness、Transparency 与 AI Act|模型行为治理：Model Spec、Preparedness、Transparency 与 AI Act]]
3. [[../06-Topics/安全治理线：AI Safety、AI Security、Prompt Injection、Approval、Audit 与 Release Gate|安全治理线]]
4. [[../06-Topics/产品落地线：Model、Workflow、Case Study、Rollout、ROI 与 Governance|产品落地线]]
5. [[2025-2026 AI 新路线补线：Deep Research、Memory 与 Agent Runtime|2025-2026 AI 新路线补线：Deep Research、Memory 与 Agent Runtime]]

## 读完这页后你应该能自己回答

- 为什么 model behavior governance 不能只等于 app-level guardrails
- 为什么 Preparedness / Safeguards reporting 会影响 deployment judgment
- 为什么 transparency 资产已经是产品和平台竞争力的一部分
- 为什么 `2025-08-02` 这样的具体日期会开始改变企业部署和采购问题

## 关联

- [[2025-2026 AI 新路线补线：Deep Research、Memory 与 Agent Runtime|2025-2026 AI 新路线补线：Deep Research、Memory 与 Agent Runtime]]
- [[../06-Topics/模型行为治理：Model Spec、Preparedness、Transparency 与 AI Act|模型行为治理：Model Spec、Preparedness、Transparency 与 AI Act]]
- [[../06-Topics/AI Safety 与 AI Security|AI Safety 与 AI Security]]
- [[../06-Topics/AI Safety|AI Safety]]
- [[../06-Topics/AI Security|AI Security]]
- [[../06-Topics/安全治理线：AI Safety、AI Security、Prompt Injection、Approval、Audit 与 Release Gate|安全治理线]]
- [[../06-Topics/产品落地线：Model、Workflow、Case Study、Rollout、ROI 与 Governance|产品落地线]]
