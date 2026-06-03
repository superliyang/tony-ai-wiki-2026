---
title: Agent First Knowledge Automation Roadmap
type: system-roadmap
status: active
updated: 2026-05-23
---

# Agent First Knowledge Automation Roadmap

## 目标状态

这套系统的目标不是“用户想到主题后让 AI 整理”，而是：

1. Agent 每天 / 每周自动巡检外部世界
2. 自动发现值得学习的主题
3. 自动放入候选池和 Review Queue
4. 汇总推送到飞书
5. 用户在飞书里选择候选内容去向
6. Curator Agent 在人工确认后半自动合入正式专题

正式知识区 `01-Areas/` 仍然保持人工确认边界。自动化默认只写入 `00-Agent-Inbox/` 和 `90-Agent-System/`。

## 当前已实现

- RSS / URL 采集：`scripts/collect_sources.py`
- 规则分类与重要性评分：`scripts/classify_items.py`
- DeepSeek 语义分析：`scripts/semantic_analyze.py`
- Daily Digest：`scripts/generate_digest.py --mode daily`
- Weekly Digest：`scripts/generate_digest.py --mode weekly`
- Candidate Notes：`scripts/generate_candidates.py`
- Study Queue：`scripts/generate_study_queue.py`
- Review Queue：`scripts/review_queue.py`
- 可解释 Review 排序策略：`90-Agent-System/review-policy.yaml`
- Curator Merge Plan：`scripts/curator_merge_plan.py`
- Curator Merge Execution Preview / confirmed intake landing：`scripts/curator_merge_execute.py`
- Vault Health Report：`scripts/check_vault.py`
- Automation Ops Run：`scripts/agent_ops.py`
- Automation Doctor：`scripts/automation_doctor.py`
- 飞书 Webhook 主动推送：`scripts/notify_feishu.py`
- 飞书 WebSocket Bot 交互入口：`scripts/feishu_bot_ws.py`
- GitHub Actions 手动备用执行脚手架：`.github/workflows/`

## 能力分层

### 1. 调度层

当前主力：

- 本地手动命令
- GitHub Actions 手动备用触发
- macOS `launchd` 本地服务：`scripts/launchd_agent.sh`
- 开机登录后的缺失日报/周报恢复：`scripts/startup_recover.py`
- 自动产物安全 Git checkpoint：`scripts/git_checkpoint.sh`
- macOS 一键初始化入口：`scripts/setup_agent.sh`
- 多轮自动化巡检：`scripts/agent_ops.py`
- 标准化环境体检：`scripts/automation_doctor.py`

后续可视化调度层：

- `n8n`：适合可视化流程、失败记录、跨服务集成
- `Windmill`：适合把 Python / TypeScript 脚本产品化为 workflow、webhook、内部工具
- `Activepieces`：适合 AI-first / no-code 工作流

第一阶段仍以 Python 脚本为主，避免过早把核心逻辑散进平台节点里。

### 2. 信息源层

当前主力：

- OpenAI / Anthropic / AWS / Cloudflare / Flink RSS
- 弱 URL 抓取
- 手动 URL Inbox
- GitHub Trending
- GitHub Releases：LangGraph / LiteLLM / OpenCode
- arXiv AI agent 查询
- CISA 安全情报 RSS
- CISA KEV 已知被利用漏洞 JSON

后续增强：

- OWASP / Security advisories
- PDF / OCR / Screenshot 来源

### 3. AI 分析层

当前主力：

- 规则分类
- 规则重要性评分
- DeepSeek 语义分析增强
- DeepSeek 建议动作与来源质量结合的 Review Queue 优先级排序
- 多轮 AI 判断历史与稳定建议门控，避免单轮波动直接影响决策队列

后续增强：

- OpenAI 语义分类备选 provider
- 候选内容和现有 vault 的关系判断
- 向量检索已有笔记
- 自动识别“该进哪个专题 / 哪张地图 / 哪个 playbook”

### 4. 结构化产物层

当前主力：

- Daily Digest
- Weekly Digest
- Candidate Notes
- Study Queue
- Review Queue
- Learning Decision Board
- AI Triage Report
- Curator Merge Plan
- Vault Health Report
- Source Quality Report
- Topic Opportunity Report

后续增强：

- Learning Debt Report
- Curator 自动整合正式专题正文、索引与恢复记忆

### 5. 人工决策层

当前主力：

- 飞书命令 `/review`
- 飞书命令 `/decide <编号> study|ignore|keep|merge`
- 飞书命令 `合入计划`
- 飞书命令 `巡检` / `真实巡检`

状态含义：

- `pending-review`：候选池等待人工判断
- `queued-for-study`：进入学习队列
- `discarded`：忽略
- `ready-to-merge`：准备交给 Curator Agent 半自动合入

### 6. 正式合入层

当前边界：

- 日常巡检不自动修改 `01-Areas/`
- 只有用户明确确认后，Curator 才会写入专题 `00-Inbox/Curated/` 作为待整合入口

后续 Curator Agent 合入时必须：

- 读取相关专题 `专题总览.md`
- 判断是否更新 `学习进度.md`
- 判断是否更新 `恢复笔记.md`
- 判断是否更新地图索引 / 主题索引
- 运行 `check_vault.py`
- 生成 Git commit / PR

## 推荐下一步

1. 观察 `agent_ops.py` 多轮巡检报告，沉淀失败趋势和质量指标。
2. 观察 DeepSeek 语义分析与 `review-policy.yaml` 排序一周，按误报、漏报和人工决策结果调优权重与 prompt。
3. 增加 GitHub Trending / Security Advisory / 手动收藏 URL Inbox。
4. 观察 Curator Merge Execution 的 intake 质量，再扩展到正式专题正文与索引整合。
5. 稳定两周后，再评估是否把调度层迁移到 n8n 或 Windmill。
