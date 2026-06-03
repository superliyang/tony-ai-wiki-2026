from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

from utils import load_items, load_yaml, now_iso, relative_to_repo, repo_root, safe_print, today_str, write_json


IMPORTANCE_KEYWORDS = [
    "release",
    "new model",
    "vulnerability",
    "security",
    "agent",
    "coding",
    "benchmark",
    "eval",
    "WAF",
    "API",
    "database",
    "streaming",
]


def count_keyword(text: str, keyword: str) -> int:
    return len(re.findall(re.escape(keyword), text, flags=re.IGNORECASE))


def classify_item(item: dict[str, Any], router: dict[str, Any]) -> dict[str, Any]:
    text = " ".join([item.get("title", ""), item.get("summary", ""), item.get("raw_text", "")])
    scores: dict[str, int] = {}
    reasons: list[str] = []
    topics = router.get("topics", {})
    for topic, rule in topics.items():
        score = 0
        matched: list[str] = []
        for keyword in rule.get("keywords", []):
            hits = count_keyword(text, keyword)
            if hits:
                score += hits
                matched.append(keyword)
        if score:
            scores[topic] = score
            reasons.append(f"{topic}: 命中 {', '.join(matched[:6])}")

    default_topic = router.get("default_topic", "Others")
    topic = max(scores.items(), key=lambda pair: pair[1])[0] if scores else default_topic
    importance = min(5, 1 + sum(1 for keyword in IMPORTANCE_KEYWORDS if count_keyword(text, keyword)))
    priority = item.get("source_priority", "medium")
    if priority == "high":
        importance = min(5, importance + 1)
    elif priority == "low":
        importance = max(1, importance - 1)
    if scores:
        importance = min(5, importance + 1)

    result = dict(item)
    result.update(
        {
            "topic": topic,
            "topic_scores": scores or {default_topic: 0},
            "importance_score": importance,
            "classification_reason": "；".join(reasons) if reasons else "未命中专题关键词，进入 Others。",
            "classified_at": now_iso(),
        }
    )
    return result


def classify_items(input_path: Path, dry_run: bool = False, date_str: str | None = None) -> Path:
    root = repo_root()
    router = load_yaml(root / "90-Agent-System/topic-router.yaml")
    items = load_items(input_path)
    classified = [classify_item(item, router) for item in items]
    output_date = date_str or input_path.stem.replace("source-items-", "") or today_str()
    output = root / f"90-Agent-System/logs/classified-items-{output_date}.json"
    payload = {"generated_at": now_iso(), "input": relative_to_repo(input_path), "items": classified}
    actual_output = write_json(output, payload, dry_run=dry_run)
    safe_print(f"[classify] items={len(classified)} output={output.relative_to(root)}")
    return actual_output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None)
    parser.add_argument("--input", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    root = repo_root()
    date_str = args.date or today_str()
    input_path = Path(args.input) if args.input else root / f"90-Agent-System/logs/source-items-{date_str}.json"
    if not input_path.is_absolute():
        input_path = root / input_path
    classify_items(input_path, dry_run=args.dry_run, date_str=date_str)


if __name__ == "__main__":
    main()
