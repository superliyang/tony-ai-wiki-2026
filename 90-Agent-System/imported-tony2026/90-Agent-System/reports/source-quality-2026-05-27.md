---
title: Source Quality Report - 2026-05-27
type: source-quality-report
status: generated
key: 2026-05-27
---

# Source Quality Report - 2026-05-27

## 来源质量排名

| source | items | high_value | avg_importance | warnings | top_topic |
| --- | ---: | ---: | ---: | ---: | --- |
| arXiv AI Agents | 3 | 3 | 4.00 | 0 | AI-Engineering |
| AWS Security Blog | 2 | 2 | 4.00 | 0 | Cloud-Native |
| Anthropic News | 1 | 1 | 5.00 | 0 | AI-Engineering |
| DeepSeek News | 1 | 1 | 5.00 | 0 | AI-Engineering |
| Apache Flink Blog | 1 | 1 | 5.00 | 0 | Big-Data |
| OpenAI Blog | 1 | 1 | 4.00 | 0 | AI-Engineering |
| LangGraph Releases | 1 | 1 | 4.00 | 0 | AI-Open-Source |
| GitHub Trending AI | 10 | 1 | 1.80 | 0 | Others |
| LiteLLM Releases | 2 | 0 | 3.00 | 0 | AI-Open-Source |

## 建议

- 优先保留和调优 `arXiv AI Agents`：本轮 high_value=3，avg=4.00。
- 观察 `LiteLLM Releases`：warnings=0，high_value=0。

## Warnings

- github-opencode-releases: GitHub releases fetch failed: 403 Client Error: rate limit exceeded for url: https://api.github.com/repos/sst/opencode/releases
- cisa-kev: CISA KEV fetch failed: HTTPSConnectionPool(host='www.cisa.gov', port=443): Max retries exceeded with url: /sites/default/files/feeds/known_exploited_vulnerabilities.json (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)')))

## 输入

- classified_items: 90-Agent-System/logs/semantic-analysis-2026-05-27.json
