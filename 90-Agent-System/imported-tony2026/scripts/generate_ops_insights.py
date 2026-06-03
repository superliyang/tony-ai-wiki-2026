from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from utils import load_items, read_json, relative_to_repo, repo_root, safe_print, today_str, week_str, write_text


def average(values: list[int]) -> float:
    return sum(values) / len(values) if values else 0.0


def source_quality_rows(items: list[dict[str, Any]], warnings: list[str]) -> list[dict[str, Any]]:
    by_source: dict[str, list[dict[str, Any]]] = defaultdict(list)
    warning_counts: Counter[str] = Counter()
    for warning in warnings:
        source_id = warning.split(":", 1)[0].strip()
        if source_id:
            warning_counts[source_id] += 1
    for item in items:
        by_source[item.get("source_id", "unknown")].append(item)

    rows: list[dict[str, Any]] = []
    for source_id, source_items in by_source.items():
        scores = [int(item.get("importance_score", 1)) for item in source_items]
        high_value = sum(1 for score in scores if score >= 4)
        topics = Counter(str(item.get("topic", "Others")) for item in source_items)
        rows.append(
            {
                "source_id": source_id,
                "source_name": source_items[0].get("source_name", source_id),
                "count": len(source_items),
                "high_value": high_value,
                "avg_importance": average(scores),
                "warnings": warning_counts[source_id],
                "top_topic": topics.most_common(1)[0][0] if topics else "Others",
            }
        )
    rows.sort(key=lambda row: (row["high_value"], row["avg_importance"], row["count"]), reverse=True)
    return rows


def topic_opportunity_rows(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_topic: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in items:
        by_topic[str(item.get("topic", "Others"))].append(item)

    rows: list[dict[str, Any]] = []
    for topic, topic_items in by_topic.items():
        scores = [int(item.get("importance_score", 1)) for item in topic_items]
        sources = Counter(str(item.get("source_name", "Unknown")) for item in topic_items)
        top_items = sorted(topic_items, key=lambda item: int(item.get("importance_score", 1)), reverse=True)[:3]
        rows.append(
            {
                "topic": topic,
                "count": len(topic_items),
                "high_value": sum(1 for score in scores if score >= 4),
                "avg_importance": average(scores),
                "top_sources": ", ".join(name for name, _ in sources.most_common(3)),
                "top_items": top_items,
            }
        )
    rows.sort(key=lambda row: (row["high_value"], row["avg_importance"], row["count"]), reverse=True)
    return rows


def render_source_quality(rows: list[dict[str, Any]], warnings: list[str], key: str, input_path: Path) -> str:
    lines = [
        "---",
        f"title: Source Quality Report - {key}",
        "type: source-quality-report",
        "status: generated",
        f"key: {key}",
        "---",
        "",
        f"# Source Quality Report - {key}",
        "",
        "## 来源质量排名",
        "",
        "| source | items | high_value | avg_importance | warnings | top_topic |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['source_name']} | {row['count']} | {row['high_value']} | {row['avg_importance']:.2f} | {row['warnings']} | {row['top_topic']} |"
        )
    lines.extend(["", "## 建议", ""])
    if rows:
        best = rows[0]
        lines.append(f"- 优先保留和调优 `{best['source_name']}`：本轮 high_value={best['high_value']}，avg={best['avg_importance']:.2f}。")
    noisy = [row for row in rows if row["warnings"] or (row["count"] > 0 and row["high_value"] == 0)]
    if noisy:
        for row in noisy[:5]:
            lines.append(f"- 观察 `{row['source_name']}`：warnings={row['warnings']}，high_value={row['high_value']}。")
    else:
        lines.append("- 本轮来源没有明显噪音，继续观察多轮趋势。")
    lines.extend(["", "## Warnings", ""])
    if warnings:
        lines.extend([f"- {warning}" for warning in warnings])
    else:
        lines.append("- 无。")
    lines.extend(["", "## 输入", "", f"- classified_items: {relative_to_repo(input_path)}"])
    return "\n".join(lines)


def render_topic_opportunities(rows: list[dict[str, Any]], key: str, input_path: Path) -> str:
    lines = [
        "---",
        f"title: Topic Opportunity Report - {key}",
        "type: topic-opportunity-report",
        "status: generated",
        f"key: {key}",
        "---",
        "",
        f"# Topic Opportunity Report - {key}",
        "",
        "## 主题机会排名",
        "",
        "| topic | items | high_value | avg_importance | top_sources |",
        "| --- | ---: | ---: | ---: | --- |",
    ]
    for row in rows:
        lines.append(f"| {row['topic']} | {row['count']} | {row['high_value']} | {row['avg_importance']:.2f} | {row['top_sources']} |")
    lines.extend(["", "## 推荐动作", ""])
    if rows:
        for row in rows[:3]:
            action = "进入学习队列" if row["high_value"] else "继续观察"
            lines.append(f"- `{row['topic']}`：{action}；本轮 high_value={row['high_value']}，avg={row['avg_importance']:.2f}。")
    else:
        lines.append("- 暂无足够数据。")
    lines.extend(["", "## Top Items", ""])
    for row in rows[:5]:
        lines.append(f"### {row['topic']}")
        for item in row["top_items"]:
            lines.append(f"- {item.get('title', 'Untitled')} ({item.get('source_name', '')}, importance={item.get('importance_score', 1)})")
        lines.append("")
    lines.extend(["## 输入", "", f"- classified_items: {relative_to_repo(input_path)}"])
    return "\n".join(lines)


def generate_ops_insights(classified_path: Path, source_path: Path | None = None, key: str | None = None, dry_run: bool = False) -> dict[str, Path]:
    root = repo_root()
    target_key = key or classified_path.stem.replace("classified-items-", "") or today_str()
    items = load_items(classified_path)
    warnings: list[str] = []
    if source_path and source_path.exists():
        source_data = read_json(source_path, {})
        if isinstance(source_data, dict):
            warnings = [str(warning) for warning in source_data.get("warnings", [])]

    source_output = root / f"90-Agent-System/reports/source-quality-{target_key}.md"
    topic_output = root / f"90-Agent-System/reports/topic-opportunities-{target_key}.md"
    actual_source = write_text(source_output, render_source_quality(source_quality_rows(items, warnings), warnings, target_key, classified_path), dry_run=dry_run)
    actual_topic = write_text(topic_output, render_topic_opportunities(topic_opportunity_rows(items), target_key, classified_path), dry_run=dry_run)
    safe_print(f"[ops-insights] source_quality={relative_to_repo(source_output)} topic_opportunities={relative_to_repo(topic_output)}")
    return {"source_quality": actual_source, "topic_opportunities": actual_topic}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", default=None)
    parser.add_argument("--classified", default=None)
    parser.add_argument("--source", default=None)
    parser.add_argument("--weekly", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    root = repo_root()
    key = args.key or (week_str() if args.weekly else today_str())
    classified_path = Path(args.classified) if args.classified else root / f"90-Agent-System/logs/classified-items-{key}.json"
    source_path = Path(args.source) if args.source else root / f"90-Agent-System/logs/source-items-{key}.json"
    if not classified_path.is_absolute():
        classified_path = root / classified_path
    if not source_path.is_absolute():
        source_path = root / source_path
    generate_ops_insights(classified_path, source_path=source_path, key=key, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
