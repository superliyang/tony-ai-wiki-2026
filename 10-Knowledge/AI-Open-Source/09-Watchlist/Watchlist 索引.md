---
title: "AI Open Source Watchlist 索引"
created: 2026-06-16
updated: 2026-06-21
status: active
type: index
domain: ai-open-source
as_of: 2026-06-21
---

# Watchlist 索引

Watchlist 只放值得周期性跟踪的项目，不放所有热门项目。

## Candidate Watchlist

| Project | Reason | Cadence |
|---|---|---|
| Unsloth | 单 GPU 微调、GRPO、训练效率和 license 边界会影响工具链判断 | weekly |
| vLLM | 生产 serving、硬件适配、RL rollout 和 omni workload 会影响 deployment 判断 | biweekly |
| LangGraph | stateful agent runtime 的核心样本，影响 workflow / agent 边界判断 | biweekly |
| Langfuse | agent observability、eval、MCP evaluator 会影响 evaluation / release gate | biweekly |
| Qwen Code / Qwen3-Coder | open-source coding agent 与 code model 协同路线，影响 China AI 和 coding agent 生态 | weekly |
| Cube Studio | 一站式 AI infra / MLOps 平台样本，适合快速理解企业 AI 平台全链路 | biweekly |

## 2026-06 Watchlist Update

| Project | Track | 关注什么 | 当前动作 |
|---|---|---|---|
| [[10-Knowledge/AI-Open-Source/03-Projects/Unsloth]] | Local Training / Fine-tuning | 模型支持、Studio 化、训练效率、license 和部署边界 | 新增项目卡 |
| [[10-Knowledge/AI-Open-Source/03-Projects/Qwen Code]] | Coding Agent / China AI | coding agent CLI、Qwen3-Coder、repo 级任务、生态配套 | 新增项目卡 |
| [[10-Knowledge/AI-Open-Source/03-Projects/Cube Studio]] | AI Infrastructure / MLOps Platform | 多租户、算力、Notebook、Pipeline、训练、模型服务、AIHUB | 新增项目卡 |
| [[10-Knowledge/AI-Open-Source/03-Projects/vLLM]] | Serving / Inference | release、硬件覆盖、RL rollout、multi-modal serving | 保持跟踪 |
| [[10-Knowledge/AI-Open-Source/03-Projects/LangGraph]] | Agent Runtime | stateful agent、workflow/agent 边界、production runtime | 保持跟踪 |
| [[10-Knowledge/AI-Open-Source/03-Projects/Langfuse]] | Eval / Observability | evaluator、MCP、trace、release gate | 保持跟踪 |

## Current Refresh

- [[10-Knowledge/AI-Open-Source/09-Watchlist/2026-06 Watchlist 刷新]]

## Rules

项目进入 Watchlist 至少满足一条：

- 对当前学习主线有战略重要性；
- 更新快到值得周期性跟踪；
- 代表可复用模式；
- 更新会改变推荐技术栈。

## Legacy Source

- [[10-Knowledge/AI-Open-Source/09-Watchlist/Watchlist 索引 - 旧库]]
- [[10-Knowledge/AI-Open-Source/09-Watchlist/重点 Watchlist]]

## Source Links

- Unsloth GitHub: https://github.com/unslothai/unsloth
- Unsloth releases: https://github.com/unslothai/unsloth/releases
- Qwen Code GitHub: https://github.com/QwenLM/qwen-code
- Qwen3-Coder GitHub: https://github.com/QwenLM/Qwen3-Coder
- Cube Studio GitHub: https://github.com/data-infra/cube-studio
- Cube Studio Wiki: https://github.com/data-infra/cube-studio/wiki
- vLLM releases: https://github.com/vllm-project/vllm/releases
- LangGraph releases: https://github.com/langchain-ai/langgraph/releases
- Langfuse changelog: https://langfuse.com/changelog
