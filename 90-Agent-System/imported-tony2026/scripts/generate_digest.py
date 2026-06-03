from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
from typing import Any

from utils import clamp, load_items, now_iso, relative_to_repo, repo_root, safe_print, today_str, week_str, write_text


TOPIC_ORDER = [
    "AI-Engineering",
    "AI-Open-Source",
    "Security",
    "Big-Data",
    "Cloud-Native",
    "Skills-Gaming",
    "English-Learning",
    "Others",
]


def action_for(item: dict[str, Any]) -> str:
    score = int(item.get("importance_score", 1))
    if score >= 4:
        return "加入学习队列 / 加入候选池"
    if score >= 3:
        return "加入候选池"
    return "人工判断 / 暂时忽略"


def item_line(item: dict[str, Any]) -> str:
    return (
        f"- [{item.get('title', 'Untitled')}]({item.get('url', '')}) "
        f"- 来源：{item.get('source_name', '')}；重要性：{item.get('importance_score', 1)}；建议：{action_for(item)}"
    )


def generate_daily(items: list[dict[str, Any]], date_str: str, input_path: Path) -> str:
    by_topic: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in sorted(items, key=lambda i: i.get("importance_score", 0), reverse=True):
        by_topic[item.get("topic", "Others")].append(item)
    top_items = sorted(items, key=lambda i: i.get("importance_score", 0), reverse=True)[:5]

    lines = [
        "---",
        f"title: Daily Knowledge Digest - {date_str}",
        "type: daily-digest",
        "status: generated",
        f"date: {date_str}",
        "---",
        "",
        f"# Daily Knowledge Digest - {date_str}",
        "",
        "## 今日最值得关注",
        "",
    ]
    if not top_items:
        lines.append("- 今天没有采集到可用条目。")
    for index, item in enumerate(top_items, 1):
        lines.extend(
            [
                f"### {index}. {item.get('title', 'Untitled')}",
                "",
                f"- 来源：{item.get('source_name', '')}",
                f"- 领域：{item.get('topic', 'Others')}",
                f"- 重要性：{item.get('importance_score', 1)}",
                f"- 链接：{item.get('url', '')}",
                f"- 为什么值得关注：{clamp(item.get('classification_reason', ''), 180)}",
                f"- 建议动作：{action_for(item)}",
                "",
            ]
        )

    lines.extend(["## 按专题分类", ""])
    for topic in TOPIC_ORDER:
        lines.extend([f"### {topic}", ""])
        selected = by_topic.get(topic, [])[:3]
        lines.extend([item_line(item) for item in selected] or ["- 暂无。"])
        lines.append("")

    best = top_items[0] if top_items else None
    lines.extend(
        [
            "## 今日建议",
            "",
            f"- 最推荐学习：{best.get('title') if best else '暂无'}",
            f"- 最推荐沉淀：{best.get('topic') if best else '暂无'}",
            "- 最推荐忽略：低重要性且未命中当前专题关键词的条目。",
            "",
            "## 生成信息",
            "",
            f"- generated_at: {now_iso()}",
            f"- source_items: {len(items)}",
            f"- classified_items: {input_path}",
        ]
    )
    return "\n".join(lines)


def generate_weekly(items: list[dict[str, Any]], week: str, input_path: Path) -> str:
    by_topic: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in sorted(items, key=lambda i: i.get("importance_score", 0), reverse=True):
        by_topic[item.get("topic", "Others")].append(item)
    top_items = sorted(items, key=lambda i: i.get("importance_score", 0), reverse=True)[:5]
    top_topics = sorted(by_topic.items(), key=lambda pair: (len(pair[1]), max(i.get("importance_score", 0) for i in pair[1])), reverse=True)[:3]

    lines = [
        "---",
        f"title: Weekly Knowledge Digest - {week}",
        "type: weekly-digest",
        "status: generated",
        f"week: {week}",
        "---",
        "",
        f"# Weekly Knowledge Digest - {week}",
        "",
        "## 本周最值得关注的 5 件事",
        "",
    ]
    lines.extend([item_line(item) for item in top_items] or ["- 本周没有采集到可用条目。"])
    lines.extend(["", "## 本周按专题摘要", ""])
    for topic in TOPIC_ORDER:
        selected = by_topic.get(topic, [])[:3]
        if selected:
            lines.extend([f"### {topic}", ""])
            lines.extend([item_line(item) for item in selected])
            lines.append("")

    lines.extend(["## 本周建议学习路径", ""])
    if top_topics:
        for index, (topic, topic_items) in enumerate(top_topics, 1):
            lines.append(f"{index}. {topic}：先看 {topic_items[0].get('title', 'Untitled')}，再决定是否转成候选卡片或专题补线。")
    else:
        lines.append("- 暂无。")
    lines.extend(["", "## 建议进入候选池的内容", ""])
    lines.extend([item_line(item) for item in top_items if item.get("importance_score", 1) >= 3] or ["- 暂无。"])
    lines.extend(
        [
            "",
            "## 需要人工判断的问题",
            "",
            "- 哪些候选内容值得合入正式专题，仍需要人工 review。",
            "- 规则分类无法判断和现有笔记的深层关系。",
            "",
            "## 下周建议关注",
            "",
            "- Agent First 工程链路、Security / WAF / API 风控、Big-Data 实时链路。",
            "",
            "## 生成信息",
            "",
            f"- generated_at: {now_iso()}",
            f"- source_items: {len(items)}",
            f"- classified_items: {input_path}",
        ]
    )
    return "\n".join(lines)


def generate_digest(mode: str, input_path: Path, dry_run: bool = False, date_str: str | None = None, week: str | None = None) -> Path:
    root = repo_root()
    items = load_items(input_path)
    if mode == "daily":
        target_date = date_str or today_str()
        output = root / f"00-Agent-Inbox/Daily-Digests/{target_date}.md"
        text = generate_daily(items, target_date, Path(relative_to_repo(input_path)))
    elif mode == "weekly":
        target_week = week or week_str()
        output = root / f"00-Agent-Inbox/Weekly-Digests/{target_week}.md"
        text = generate_weekly(items, target_week, Path(relative_to_repo(input_path)))
    else:
        raise ValueError(f"Unsupported digest mode: {mode}")
    actual_output = write_text(output, text, dry_run=dry_run)
    safe_print(f"[digest] mode={mode} output={output.relative_to(root)}")
    return actual_output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["daily", "weekly"], required=True)
    parser.add_argument("--date", default=None)
    parser.add_argument("--week", default=None)
    parser.add_argument("--input", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    root = repo_root()
    default_key = args.week if args.mode == "weekly" and args.week else args.date or today_str()
    input_path = Path(args.input) if args.input else root / f"90-Agent-System/logs/classified-items-{default_key}.json"
    if not input_path.is_absolute():
        input_path = root / input_path
    generate_digest(args.mode, input_path, dry_run=args.dry_run, date_str=args.date, week=args.week)


if __name__ == "__main__":
    main()
