---
title: Automation Doctor - 2026-05-23
type: automation-doctor-report
status: passed
network_checks: true
generated_at: 2026-05-24T01:57:14+00:00
---

# Automation Doctor - 2026-05-23

## 总览

- failed: 0
- warnings: 2
- checks: 49

## 检查项

| status | check | detail |
| --- | --- | --- |
| ok | python package: yaml | installed |
| ok | python package: feedparser | installed |
| ok | python package: requests | installed |
| ok | python package: lark_oapi | installed |
| ok | env: FEISHU_WEBHOOK_URL | configured for Feishu active push |
| ok | env: FEISHU_APP_ID | configured for Feishu WebSocket bot |
| ok | env: FEISHU_APP_SECRET | configured for Feishu WebSocket bot |
| ok | env: DEEPSEEK_API_KEY | configured for DeepSeek semantic analysis |
| warning | env: GITHUB_TOKEN | missing; GitHub release sources may hit anonymous API rate limits |
| ok | directory: 00-Agent-Inbox/Daily-Digests | exists |
| ok | directory: 00-Agent-Inbox/Weekly-Digests | exists |
| ok | directory: 00-Agent-Inbox/Candidates | exists |
| ok | directory: 00-Agent-Inbox/Review-Queue | exists |
| ok | directory: 00-Agent-Inbox/Review-Queue/Merge-Executions | exists |
| ok | directory: 00-Agent-Inbox/Study-Queue | exists |
| ok | directory: 90-Agent-System/logs | exists |
| ok | directory: 90-Agent-System/reports | exists |
| ok | source: openai-blog | type=rss enabled=True |
| ok | source: anthropic-news | type=url enabled=True |
| ok | source: deepseek-news | type=url enabled=True |
| ok | source: github-trending-ai | type=github_trending enabled=True |
| ok | source: manual-url-inbox | type=manual_urls enabled=True |
| ok | source: aws-security-blog | type=rss enabled=True |
| ok | source: cloudflare-blog | type=rss enabled=True |
| ok | source: apache-flink | type=url enabled=True |
| ok | source: arxiv-ai-agents | type=rss enabled=True |
| ok | source: github-langgraph-releases | type=github_releases enabled=True |
| ok | source: github-litellm-releases | type=github_releases enabled=True |
| ok | source: github-opencode-releases | type=github_releases enabled=True |
| ok | source: cisa-alerts | type=rss enabled=True |
| ok | source: cisa-kev | type=cisa_kev enabled=True |
| ok | launchd: com.tony2026.knowledge-feishu-bot | 14242	-15	com.tony2026.knowledge-feishu-bot |
| ok | launchd: com.tony2026.knowledge-daily | -	0	com.tony2026.knowledge-daily |
| ok | launchd: com.tony2026.knowledge-weekly | -	0	com.tony2026.knowledge-weekly |
| ok | launchd: com.tony2026.knowledge-recovery | -	0	com.tony2026.knowledge-recovery |
| ok | source network: openai-blog | entries=967 |
| ok | source network: anthropic-news | http=200 bytes=374044 |
| ok | source network: deepseek-news | http=200 bytes=39800 |
| ok | source network: github-trending-ai | http=200 bytes=629801 |
| ok | source network: manual-url-inbox | inbox=00-Agent-Inbox/Manual-URLs/inbox.md |
| ok | source network: aws-security-blog | entries=20 |
| ok | source network: cloudflare-blog | entries=20 |
| ok | source network: apache-flink | http=200 bytes=73391 |
| warning | source network: arxiv-ai-agents | 429 Client Error: Unknown Error for url: https://export.arxiv.org/api/query?search_query=all:%22LLM%20agent%22%20OR%20all:%22AI%20agent%22&start=0&max_results=10&sortBy=submittedDate&sortOrder=descending; non-critical source degraded |
| ok | source network: github-langgraph-releases | releases=30 |
| ok | source network: github-litellm-releases | releases=30 |
| ok | source network: github-opencode-releases | releases=30 |
| ok | source network: cisa-alerts | entries=10 |
| ok | source network: cisa-kev | vulnerabilities=1602 |

## 建议

- `failed=0` 才适合认为自动化环境可稳定运行。
- warning 不一定阻塞运行，但应该进入后续优化清单。
- 如果 source network 失败，优先判断是信息源失效、网络抖动，还是本地 TLS / DNS 问题。
