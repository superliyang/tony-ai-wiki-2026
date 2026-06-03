---
title: AI 架构师面试题地图
type: interview-map
status: active
domain: AI-Architect
created: 2026-05-05
updated: 2026-05-05
---

# AI 架构师面试题地图

## 1. 总体认知题

- AI 时代的架构师和传统互联网架构师有什么区别？
- 为什么说 AI 系统是概率系统？架构上如何应对？
- POC 成功到生产可用之间差什么？
- 什么时候不应该用大模型？
- Copilot、Workflow、Agent 的边界是什么？

## 2. 场景识别题

- 给一个客服场景，如何判断是否适合 AI？
- 给一个内部知识库场景，如何从 0 到 1 落地？
- 给一个审批流场景，如何判断用 workflow 还是 agent？
- 给一个代码助手场景，如何设计权限和回滚？
- 给一个数据分析助手场景，如何防止错误 SQL 和数据泄露？

## 3. RAG 架构题

- RAG 为什么不是向量库加大模型？
- 如何设计企业知识库 RAG？
- chunking、embedding、rerank、metadata 如何取舍？
- RAG 权限过滤应该发生在哪一层？
- 如何评测 retrieval quality 和 answer faithfulness？
- 如何处理知识过期、引用错误和幻觉？

关联：[[../05-Topics/RAG 架构师视角|RAG 架构师视角]]

## 4. Agent 架构题

- Agent 和 workflow 的区别是什么？
- Tool calling 如何做权限控制？
- 高风险工具调用如何审批？
- Agent 状态、记忆和产物怎么管理？
- Agent 失败如何重试、降级、人工接管和回滚？
- 如何设计 agent 的 eval？

关联：[[../05-Topics/Agent 架构师视角|Agent 架构师视角]]

## 5. LLMOps / AgentOps 题

- Prompt、model、dataset、eval 如何版本化？
- AI 系统如何做灰度、shadow、rollback？
- 线上 trace 应该记录哪些信息？
- 如何设计 AI observability dashboard？
- 模型切换如何做回归？
- incident 如何回写到 eval？

关联：[[../05-Topics/LLMOps 与 AgentOps 架构师视角|LLMOps 与 AgentOps 架构师视角]]

## 6. 成本、延迟与容量题

- AI 应用的成本由哪些部分组成？
- 如何降低 RAG / Agent 的 p95 延迟？
- 什么时候用缓存，什么时候用小模型？
- 如何估算 token 成本和成功任务成本？
- 如何做模型路由和 fallback？

关联：[[../05-Topics/AI 成本、延迟与容量架构师视角|AI 成本、延迟与容量架构师视角]]

## 7. 安全治理题

- Prompt injection 怎么防？
- RAG 如何防数据泄露？
- Agent tool abuse 怎么控制？
- AI 系统日志如何脱敏和审计？
- AI red team 应该覆盖哪些攻击包？
- 高风险 AI 系统上线门槛是什么？

关联：[[../05-Topics/AI 安全治理架构师视角|AI 安全治理架构师视角]]

## 8. 数据治理题

- 哪些数据可以进入 prompt、RAG、fine-tuning、eval、日志？
- eval 数据如何治理？
- 用户反馈是否可以用于训练？
- 企业知识库如何设计 owner、版本和权限？
- 如何处理数据保留和删除？

关联：[[../05-Topics/AI 数据治理架构师视角|AI 数据治理架构师视角]]

## 9. 系统设计题

- 设计一个企业知识库问答系统。
- 设计一个面向销售团队的 AI Copilot。
- 设计一个能调用内部系统的报销 Agent。
- 设计一个 AI 代码审查系统。
- 设计一个企业级模型网关。
- 设计一个 AI 应用上线评测平台。

回答结构：

`目标 -> 边界 -> 架构 -> 数据 -> 模型 -> 工具 -> eval -> 安全 -> 成本 -> 运营`

## 10. 管理与组织题

- 如何选择第一批 AI use case？
- 如何建立企业 AI 平台团队？
- 如何避免 AI 项目停留在 POC？
- 如何设计 AI 架构评审机制？
- 如何向管理层解释 AI ROI 和风险？

## 关联

- [[./AI 架构师面试专题总览|AI 架构师面试专题总览]]
- [[./AI 架构师表达总纲|AI 架构师表达总纲]]
- [[../08-Playbooks/AI 架构评审 Playbook|AI 架构评审 Playbook]]

