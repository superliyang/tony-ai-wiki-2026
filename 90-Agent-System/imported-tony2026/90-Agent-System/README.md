# Agent Knowledge Automation

## 目标

本目录用于管理知识库自动化系统。

第一版自动生成：

- Daily Digest
- Weekly Digest
- Candidate Notes
- Study Queue
- Vault Health Report

默认巡检不会自动修改 `01-Areas/`。只有用户明确确认 Curator 合入执行后，系统才会把候选写入对应专题的 `00-Inbox/Curated/` 作为待整合 intake。

## 本地 dry-run

```bash
python scripts/knowledge_daily.py --dry-run
python scripts/knowledge_weekly.py --dry-run
python scripts/agent_ops.py --rounds 2 --mode dry-run
python scripts/automation_doctor.py --network --dry-run
```

`dry-run` 会把中间文件写入系统临时目录中的镜像路径，用于完整验证流水线；不会向仓库写入预览文件，也不会真实发送通知。

`agent_ops.py` 是完整链路巡检入口，会连续运行 Daily / Weekly / Review Queue / Merge Plan / Merge Execution Preview / Vault Health，并写入：

```text
90-Agent-System/reports/automation-ops-*.md
```

`automation_doctor.py` 是标准化体检入口，会检查依赖、密钥、目录、信息源配置、launchd 状态，并可选检查信息源网络可达性：

```bash
python scripts/automation_doctor.py
python scripts/automation_doctor.py --network
```

输出位置：

```text
90-Agent-System/reports/automation-doctor-*.md
```

Daily / Weekly 还会生成两个反馈报告：

```text
90-Agent-System/reports/source-quality-*.md
90-Agent-System/reports/topic-opportunities-*.md
```

它们用于判断哪些来源最有价值、哪些主题正在形成学习机会。

## 本地真实运行但不通知

```bash
python scripts/knowledge_daily.py --no-notify
python scripts/knowledge_weekly.py --no-notify
python scripts/agent_ops.py --rounds 1 --mode real
```

如果要验证主动推送，可以显式打开通知：

```bash
python scripts/agent_ops.py --rounds 1 --mode real --notify --notify-report
```

## 配置飞书通知

```bash
export FEISHU_WEBHOOK_URL="..."
export FEISHU_WEBHOOK_SECRET="..."
python scripts/knowledge_daily.py
```

同时需要在 `90-Agent-System/notification.yaml` 中将 `feishu.enabled` 设置为 `true`。

也可以把本地密钥放到 `90-Agent-System/.env.local`。该文件被 `.gitignore` 忽略，不会提交到仓库。

## 配置企业微信通知

```bash
export WECOM_WEBHOOK_URL="..."
python scripts/notify_wecom.py --file 00-Agent-Inbox/Daily-Digests/YYYY-MM-DD.md
```

同时需要在 `90-Agent-System/notification.yaml` 中将 `wecom.enabled` 设置为 `true`。

## GitHub Actions Secrets

GitHub Actions 当前保留为手动备用执行入口，不启用定时 `schedule`；自动定时任务以本机 `launchd` 主节点为准，避免两套调度同时写入仓库和重复推送。

- `FEISHU_WEBHOOK_URL`
- `FEISHU_WEBHOOK_SECRET`
- `WECOM_WEBHOOK_URL`
- `BARK_ENDPOINT`
- `DEEPSEEK_API_KEY`
- `GITHUB_TOKEN`：可选，但推荐配置，用于提高 GitHub Releases 信息源的 API rate limit。

## AI 语义分析

规则分类会先运行；如果 `90-Agent-System/ai-analysis.yaml` 启用，并且本地或 GitHub Secrets 配置了 `DEEPSEEK_API_KEY`，系统会调用 DeepSeek 为高价值条目补充语义判断。

输出位置：

```text
90-Agent-System/logs/semantic-analysis-YYYY-MM-DD.json
90-Agent-System/logs/semantic-analysis-YYYY-WW.json
00-Agent-Inbox/Review-Queue/AI-Triage/YYYY-WW.md
```

语义分析会补充：

- `learning_value`
- `vault_relationship`
- `suggested_action`
- `reason`
- `confidence`

如果 DeepSeek API 失败，系统会记录 warning，并继续使用规则分类结果。

Review Queue 不再按生成时间简单排列，而是根据 `90-Agent-System/review-policy.yaml` 综合排序：

- 候选重要性评分
- 所属学习主线
- 来源信号强度
- DeepSeek 建议动作

`/review` 返回的每项都会包含优先级分数和排序原因，便于直接在飞书中快速决策。后续观察一周数据时，可以只调整该策略文件和语义 prompt，而不改调度流程。

再次分析到仍处于 `pending-review` 的已有候选时，系统会刷新其 AI 学习价值、关系判断和建议动作；已经人工决策的候选不会被覆盖。

为避免一次模型波动直接改变决策优先级，候选卡片同时记录本轮 `latest_action` 和用于排序的 `stable_ai_action`：

- `study` / `merge-plan` 需要至少两轮一致观测后，才成为稳定建议。
- `review` / `ignore` 会及时降温，避免把不确定内容继续推在首屏。
- 每张卡片保存 `Agent 判断历史`，便于一周后复盘 DeepSeek 的一致性和误判趋势。
- AI Triage Report 展示本轮意见；飞书 `/review` 与 Review Queue 才使用稳定意见做决策排序。
- Study Queue 会展示已经获得多轮一致支持的学习建议，但仍需要你在 Review Queue 中确认，不自动改变候选状态。

## 信息源类型

`90-Agent-System/sources.yaml` 当前支持：

- `rss`：RSS / Atom 信息源
- `url`：弱网页抓取
- `manual_urls`：读取 `00-Agent-Inbox/Manual-URLs/inbox.md` 中未勾选 URL
- `github_trending`：抓取 GitHub Trending 页面
- `github_releases`：GitHub Releases API，配置 `repo: owner/name`
- `cisa_kev`：CISA Known Exploited Vulnerabilities JSON

默认已接入：

- AI 官方博客
- AWS / Cloudflare / CISA 安全源
- arXiv AI agent 查询
- GitHub Trending Python
- LangGraph / LiteLLM / OpenCode release 源
- CISA KEV 已知被利用漏洞源

手动收藏入口：

```text
00-Agent-Inbox/Manual-URLs/inbox.md
```

把链接粘到 `## 待采集` 下，保持未勾选状态即可进入下一轮自动采集。

也可以直接在飞书中发送：

```text
收藏 https://example.org/article
```

机器人会将链接写入 Manual URL Inbox，下一次 Daily / Weekly 自动分析。

## 飞书 WebSocket Bot

Webhook 只适合主动推送日报/周报。若要接收飞书消息，需要创建飞书自建应用并启用机器人能力，然后使用长连接 WebSocket 事件订阅。

本地配置：

```bash
cp 90-Agent-System/.env.example 90-Agent-System/.env.local
```

在 `.env.local` 中填写：

```bash
FEISHU_APP_ID="..."
FEISHU_APP_SECRET="..."
```

然后把 `90-Agent-System/feishu-bot.yaml` 里的 `websocket_bot.enabled` 改成 `true`，运行：

```bash
scripts/bootstrap_agent_env.sh
scripts/run_feishu_bot.sh --dry-run
scripts/run_feishu_bot.sh
```

如果你想指定 Conda 或其他 Python：

```bash
PYTHON_BIN="$(which python3)" scripts/bootstrap_agent_env.sh
PYTHON_BIN="$(which python3)" scripts/run_feishu_bot.sh
```

也可以直接运行：

```bash
python scripts/feishu_bot_ws.py --dry-run
python scripts/feishu_bot_ws.py
```

## 一键本地服务

macOS 推荐使用 `launchd` 托管服务：

```bash
scripts/setup_agent.sh
scripts/launchd_agent.sh status
scripts/launchd_agent.sh logs
```

首次运行 `scripts/setup_agent.sh` 时，如果尚未配置密钥，会生成未提交的 `90-Agent-System/.env.local` 模板并暂停；填写飞书与 DeepSeek 配置后再次运行，它会安装依赖、做环境体检、验证 Git 远端可达性并安装服务。

这会安装四项服务：

- `com.tony2026.knowledge-feishu-bot`：飞书 WebSocket bot 常驻运行
- `com.tony2026.knowledge-daily`：每天 08:30 生成日报
- `com.tony2026.knowledge-weekly`：每周一 09:00 生成周报
- `com.tony2026.knowledge-recovery`：用户登录后检查是否错过当前日报或本周周报，仅补跑缺失产物

常用管理命令：

```bash
scripts/launchd_agent.sh restart
scripts/launchd_agent.sh stop
scripts/launchd_agent.sh start
scripts/launchd_agent.sh uninstall
```

日志写入：

```text
90-Agent-System/logs/launchd/
```

由 `launchd` 触发的 Daily / Weekly 以及恢复补跑完成后，会安全地提交并推送自动产物目录：

```text
00-Agent-Inbox/
90-Agent-System/logs/
90-Agent-System/reports/
```

自动 checkpoint 不会提交 `.obsidian/`、`.p_obsidian/`、代码改动或 `01-Areas/` 手写正文；如果检测到非自动产物的本地改动，或者远端领先/分叉，它会停止自动推送并在日志中提示人工处理。

需要临时运行但不自动推送时：

```bash
KNOWLEDGE_SKIP_GIT_SYNC=1 scripts/run_knowledge_daily.sh
```

如果 vault 放在 `~/Documents`、`~/Desktop` 或 `~/Downloads` 下，macOS 可能阻止 `launchd` 访问目录，日志里会出现 `Operation not permitted`。处理方式：

```bash
scripts/launchd_agent.sh privacy
```

然后在 Full Disk Access 中添加并启用：

- `/bin/bash`
- `/usr/bin/python3`

授权后重新运行：

```bash
scripts/launchd_agent.sh install
```

如果不想处理 macOS 隐私授权，也可以把 vault 移到 `~/Developer/tony2026` 这类非保护目录后重新安装服务。

第一版支持命令：

- `/ping`
- `/daily`
- `/weekly`
- `/health`
- `/review`
- `/decide <编号> study|ignore|keep|merge`
- `/run daily`
- `/run weekly`

也支持更短的自然语言命令：

- `日报`
- `周报`
- `健康`
- `决策面板`
- `候选`
- `收藏 <URL>`
- `/save <URL>`
- `1 学习`
- `2 忽略`
- `3 保留`
- `4 合入`
- `合入计划`
- `巡检`
- `真实巡检`
- `跑日报`
- `跑周报`

Review Queue 是这套 Agent First 工作流的人工决策入口：

- `/board` / `决策面板`：生成 `00-Agent-Inbox/Decision-Board/<week>.md`，把本周候选压缩成主题投资组合、建议立刻学习、准备合入、继续观察和高重要性待判断几类
- `/review`：按稳定建议的可解释优先级列出当前最需要你决策的候选卡片，并生成 `00-Agent-Inbox/Review-Queue/YYYY-MM-DD.md`
- `/decide <编号> study`：把候选标记为 `queued-for-study`
- `/decide <编号> ignore`：把候选标记为 `discarded`
- `/decide <编号> keep`：继续保留 `pending-review`
- `/decide <编号> merge`：标记为 `ready-to-merge`，等待 Curator Agent 半自动合入

短命令等价写法：

- `1 学习` 等价于 `/decide 1 study`
- `2 忽略` 等价于 `/decide 2 ignore`
- `3 保留` 等价于 `/decide 3 keep`
- `4 合入` 等价于 `/decide 4 merge`

当候选被标记为 `ready-to-merge` 后，可以发送：

- `合入计划`
- `/merge-plan`

系统会生成 `00-Agent-Inbox/Review-Queue/Merge-Plans/YYYY-MM-DD.md`，列出目标专题、建议检查文件和人工确认点。第一版只生成计划，不自动修改 `01-Areas/`。

### Curator Merge Execution

候选标记为 `ready-to-merge` 后，可以先发送：

- `合入预览`
- `/merge-preview`

系统会生成 `00-Agent-Inbox/Review-Queue/Merge-Executions/YYYY-MM-DD.md`，展示将写入哪个专题 intake。确认后再发送：

- `确认执行合入 <编号>`
- `/merge-apply <编号> confirm`

明确确认后，系统才会：

- 写入 `01-Areas/<专题>/00-Inbox/Curated/` 的待整合卡片
- 将原候选标记为 `merged-to-area-inbox`
- 运行 `check_vault.py`

这里的 “execution” 仍然是安全 landing，不会未经复核直接重写 `专题总览.md`、`学习进度.md` 或正文结构。

## 输出目录

- `00-Agent-Inbox/Daily-Digests`
- `00-Agent-Inbox/Weekly-Digests`
- `00-Agent-Inbox/Candidates`
- `00-Agent-Inbox/Study-Queue`
- `00-Agent-Inbox/Review-Queue/Merge-Executions`
- `90-Agent-System/reports`
- `90-Agent-System/logs`

## 安全边界

- 定时巡检不会自动修改 `01-Areas/`
- 所有外部信息只进入 Inbox
- 正式区 intake 合入需要明确发送确认命令
- 不修改 `.obsidian/*`
- 不修改 `.p_obsidian/*`
- Webhook URL 只从环境变量读取，不写入仓库

## 可移植性

这套自动化是仓库内自包含的轻量系统。迁移到其他 Obsidian vault 时，通常需要带走：

- `00-Agent-Inbox/`
- `90-Agent-System/`
- `scripts/`
- `.github/workflows/`
- `requirements.txt`

然后按新 vault 的专题名调整 `90-Agent-System/topic-router.yaml` 和 `90-Agent-System/sources.yaml`。

## 多机器运行

这套工具可以在多台机器上使用：代码、配置模板和知识产物均随 Git 同步；每台 macOS 主机只需各自配置未提交的 `90-Agent-System/.env.local` 后运行 `scripts/setup_agent.sh`。Linux 当前可运行 Python 流程，但还没有同等级的一键 `systemd` 安装器。

建议采用单写入者模式：

- 只让一台主机器启用 Daily / Weekly / `agent_ops.py` 定时任务并主动 push，避免重复日报、冲突候选和重复通知。
- 只让一台机器保持飞书 WebSocket Bot 长连接，避免同一消息由多个进程竞争处理。
- 其他机器用于阅读、手动触发或备用接管；接管前先停掉主机器服务并执行 `git pull --ff-only`。
- 如后续确实要多节点同时执行，需要增加远端任务锁或统一调度中心；这也是引入 Windmill 的合适时机。

重启行为边界：

- Mac 关机后，登录当前用户时飞书 Bot 会自动重连，不需要手动执行 Python 命令。
- 登录后恢复服务会补跑“当天已错过但尚未生成”的日报，以及“本周已错过但尚未生成”的周报。
- 它不会追补关机期间的每一个历史日，避免开机后一次性生成大量重复通知；长期回填可由手动任务或未来 Windmill 工作流管理。
