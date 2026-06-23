---
title: "2026-06 AI Engineering 近期变化雷达"
created: 2026-06-18
updated: 2026-06-18
status: learning
type: map
domain: ai-engineering
as_of: 2026-06-18
tags:
  - knowledge
  - ai-engineering
  - content-refresh
---

# 2026-06 AI Engineering 近期变化雷达

这页记录第一批内容刷新中，AI Engineering 里会改变工程判断的近期变化。

## 当前判断

| 变化 | 影响 | 主库动作 |
|---|---|---|
| Agent runtime 正在向 long-running、stateful、tool-rich 任务靠拢 | workflow vs agent 的判断要加入运行时、状态、审批、回放和成本维度 | 更新 [[10-Knowledge/AI-Engineering/07-Topics/主题索引]] |
| Agent evaluation 正从“最终回答打分”扩展为 trajectory / tool-use / single-step / deterministic evaluator | eval 索引需要明确 black-box / glass-box / white-box 三层 | 更新 [[10-Knowledge/AI-Engineering/04-Evaluation/评测索引]] |
| Langfuse 等平台开始把 evaluator 暴露给 agents / MCP | observability 和 eval 之间的边界变薄，agent 可以参与创建和维护 eval | 更新 Evaluation & Reliability Track |
| vLLM 继续朝生产 serving、硬件覆盖、RL rollout 和 omni workload 扩展 | deployment 不是单纯 serving，还要关注 RL、multi-modal、硬件适配和 CI 稳定性 | 更新 [[10-Knowledge/AI-Engineering/05-Deployment/部署索引]] |
| 本地训练 / fine-tuning 工具开始产品化成 UI / Studio | Mac AI Lab 和 training stack 应关注“本地实验到可复用工作台” | 更新 [[10-Knowledge/AI-Engineering/06-Projects/项目索引]] |

## Evaluation 新分层

| Layer | 关注点 | 示例 |
|---|---|---|
| Final Response / Black-Box | 最终答案是否正确、有用、安全 | summary quality、answer accuracy |
| Trajectory / Glass-Box | tool sequence、retrieval path、state transition 是否合理 | tool selection、trace diff、step grading |
| Single-Step / White-Box | 单个决策或工具参数是否合规 | JSON schema、required args、policy rule |
| Release Gate | 是否允许上线或扩大权限 | regression suite、approval、rollback |

## 对学习路径的影响

[[10-Knowledge/AI-Engineering/学习路径]] 的 Track B 应从“工具怎么选”升级为：

1. 先定义任务和 failure mode。
2. 再决定 black-box / trajectory / single-step 哪些需要测。
3. 再选择 Langfuse / Phoenix / Promptfoo / custom harness。
4. 最后把 eval 接到 release gate 和 review queue。

## Source Links

- LangGraph releases: https://github.com/langchain-ai/langgraph/releases
- LangGraph repository: https://github.com/langchain-ai/langgraph
- Langfuse changelog, evaluators via MCP: https://langfuse.com/changelog/2026-06-10-evaluators-via-mcp
- Langfuse code evaluators: https://langfuse.com/changelog/2026-05-28-code-evaluators
- Langfuse agent evaluation guide: https://langfuse.com/guides/cookbook/example_pydantic_ai_mcp_agent_evaluation
- vLLM releases: https://github.com/vllm-project/vllm/releases
- vLLM Q2 roadmap: https://github.com/vllm-project/vllm/issues/39749
- vLLM RL roadmap: https://github.com/vllm-project/vllm/issues/41733

## Next Promotion Candidates

| Candidate | Target |
|---|---|
| Agent Evaluation 三层法 | [[10-Knowledge/AI-Engineering/04-Evaluation/评测索引]] |
| Agent Runtime Map | [[10-Knowledge/AI-Engineering/08-Maps/地图索引]] |
| Serving / RL / Omni deployment 视角 | [[10-Knowledge/AI-Engineering/05-Deployment/部署索引]] |
