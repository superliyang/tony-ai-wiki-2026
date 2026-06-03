---
title: Source Quality Report - 2026-05-29
type: source-quality-report
status: generated
key: 2026-05-29
---

# Source Quality Report - 2026-05-29

## 来源质量排名

| source | items | high_value | avg_importance | warnings | top_topic |
| --- | ---: | ---: | ---: | ---: | --- |
| GitHub Trending AI | 10 | 2 | 2.20 | 0 | Others |
| Anthropic News | 1 | 1 | 5.00 | 0 | AI-Engineering |
| DeepSeek News | 1 | 1 | 5.00 | 0 | AI-Engineering |
| Apache Flink Blog | 1 | 1 | 5.00 | 0 | Big-Data |
| CISA Known Exploited Vulnerabilities | 1 | 1 | 5.00 | 0 | Security |
| LiteLLM Releases | 1 | 0 | 3.00 | 0 | AI-Open-Source |

## 建议

- 优先保留和调优 `GitHub Trending AI`：本轮 high_value=2，avg=2.20。
- 观察 `LiteLLM Releases`：warnings=0，high_value=0。

## Warnings

- openai-blog: RSS fetch failed: HTTPSConnectionPool(host='openai.com', port=443): Read timed out. (read timeout=20)
- aws-security-blog: RSS fetch failed: HTTPSConnectionPool(host='aws.amazon.com', port=443): Max retries exceeded with url: /blogs/security/feed/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)')))
- github-opencode-releases: GitHub releases fetch failed: HTTPSConnectionPool(host='api.github.com', port=443): Max retries exceeded with url: /repos/sst/opencode/releases (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)')))
- cisa-alerts: RSS fetch failed: HTTPSConnectionPool(host='www.cisa.gov', port=443): Max retries exceeded with url: /news.xml (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)')))

## 输入

- classified_items: 90-Agent-System/logs/semantic-analysis-2026-05-29.json
