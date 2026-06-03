from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from review_queue import review_items
from utils import load_items, now_iso, relative_to_repo, repo_root, safe_print, today_str, write_text


ACTIVE_WEIGHTS = {
    "AI-Engineering": 3,
    "Security": 3,
    "Big-Data": 2,
    "AI-Open-Source": 2,
    "Cloud-Native": 1,
}


def generate_study_queue(input_path: Path, dry_run: bool = False, date_str: str | None = None) -> Path:
    root = repo_root()
    target_date = date_str or today_str()
    items = load_items(input_path)
    by_topic: dict[str, list[dict[str, Any]]] = defaultdict(list)
    scores: Counter[str] = Counter()
    for item in items:
        topic = item.get("topic", "Others")
        score = int(item.get("importance_score", 1)) + ACTIVE_WEIGHTS.get(topic, 0)
        scores[topic] += score
        by_topic[topic].append(item)

    selected_topics = [topic for topic, _ in scores.most_common(3)]
    output = root / f"00-Agent-Inbox/Study-Queue/{target_date}.md"
    lines = [
        "---",
        f"title: Study Queue - {target_date}",
        "type: study-queue",
        "status: generated",
        f"date: {target_date}",
        "---",
        "",
        f"# Study Queue - {target_date}",
        "",
        "## 本周推荐主线",
        "",
    ]
    if not selected_topics:
        lines.append("- 暂无足够数据生成学习主线。")
    for index, topic in enumerate(selected_topics, 1):
        top = sorted(by_topic[topic], key=lambda item: item.get("importance_score", 0), reverse=True)[0]
        lines.append(f"{index}. {topic}：围绕 `{top.get('title', 'Untitled')}` 做一次快速判断。")

    lines.extend(["", "## 推荐学习顺序", ""])
    for index, topic in enumerate(selected_topics, 1):
        lines.append(f"{index}. 先看 `{topic}` 的最高重要性候选，再决定是否进入正式专题 review。")

    lines.extend(["", "## 为什么推荐这些", ""])
    for topic in selected_topics:
        lines.append(f"- {topic}：近期出现频率和重要性较高，并且贴近当前 vault 的活跃学习主线。")

    confirmed_study = [
        item for item in review_items(limit=50) if item.suggested_action == "study" and item.stability == "confirmed"
    ]
    lines.extend(["", "## Agent 已确认建议学习", ""])
    if confirmed_study:
        for item in confirmed_study[:5]:
            lines.append(f"- [{item.topic}] [[{item.path.relative_to(root).with_suffix('')}]]；priority: {item.priority_score}；依据：{item.priority_reason}")
    else:
        lines.append("- 暂无经过多轮一致判断的学习建议，继续观察候选信号。")

    lines.extend(
        [
            "",
            "## 可选动作",
            "",
            "- [ ] 学习",
            "- [ ] 暂存",
            "- [ ] 放弃",
            "- [ ] 转为专题",
            "- [ ] 转为 Playbook",
            "",
            "## 关联候选卡片",
            "",
        ]
    )
    candidate_paths = sorted((root / "00-Agent-Inbox/Candidates").glob(f"*/{target_date}-*.md"))
    if candidate_paths:
        for path in candidate_paths[:12]:
            lines.append(f"- [[{path.relative_to(root).with_suffix('')}]]")
    else:
        lines.append("- 暂无。")
    lines.extend(["", "## 生成信息", "", f"- generated_at: {now_iso()}", f"- classified_items: {relative_to_repo(input_path)}"])
    actual_output = write_text(output, "\n".join(lines), dry_run=dry_run)
    safe_print(f"[study-queue] output={output.relative_to(root)}")
    return actual_output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None)
    parser.add_argument("--input", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    root = repo_root()
    date_str = args.date or today_str()
    input_path = Path(args.input) if args.input else root / f"90-Agent-System/logs/classified-items-{date_str}.json"
    if not input_path.is_absolute():
        input_path = root / input_path
    generate_study_queue(input_path, dry_run=args.dry_run, date_str=date_str)


if __name__ == "__main__":
    main()
