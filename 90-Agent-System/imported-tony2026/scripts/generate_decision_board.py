from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from review_queue import ReviewItem, parse_candidate, review_items
from utils import extract_frontmatter, parse_datetime, relative_to_repo, repo_root, safe_print, week_str, write_text


@dataclass
class TopicSignal:
    topic: str
    count: int = 0
    high_value: int = 0
    confirmed_study: int = 0
    ready_to_merge: int = 0
    observing: int = 0
    total_importance: int = 0

    @property
    def avg_importance(self) -> float:
        return self.total_importance / self.count if self.count else 0.0

    @property
    def decision_score(self) -> int:
        return self.high_value * 10 + self.confirmed_study * 12 + self.ready_to_merge * 15 + self.observing * 3 + int(self.avg_importance * 2)


def candidate_week(item: ReviewItem) -> str:
    meta, _ = extract_frontmatter(item.path.read_text(encoding="utf-8"))
    meta_date = parse_datetime(meta.get("captured_at") or meta.get("published_at"))
    if meta_date:
        return week_str(meta_date.date())
    prefix = item.path.name[:10]
    try:
        return week_str(date.fromisoformat(prefix))
    except ValueError:
        return week_str(date.fromtimestamp(item.path.stat().st_mtime))


def all_review_items_for_week(target_week: str) -> list[ReviewItem]:
    root = repo_root()
    items: list[ReviewItem] = []
    for index, path in enumerate(sorted((root / "00-Agent-Inbox/Candidates").glob("*/*.md")), 1):
        item = parse_candidate(path, index)
        if candidate_week(item) == target_week:
            items.append(item)
    items.sort(key=lambda item: (item.priority_score, item.path.stat().st_mtime), reverse=True)
    return items


def safe_importance(value: str) -> int:
    try:
        return int(value or 1)
    except ValueError:
        return 1


def topic_signals(items: list[ReviewItem]) -> list[TopicSignal]:
    by_topic: dict[str, TopicSignal] = defaultdict(lambda: TopicSignal(topic=""))
    for item in items:
        signal = by_topic[item.topic]
        signal.topic = item.topic
        signal.count += 1
        importance = safe_importance(item.importance_score)
        signal.total_importance += importance
        if importance >= 4:
            signal.high_value += 1
        if item.status == "ready-to-merge":
            signal.ready_to_merge += 1
        if item.suggested_action == "study" and item.stability == "confirmed":
            signal.confirmed_study += 1
        elif item.status == "pending-review":
            signal.observing += 1
    return sorted(by_topic.values(), key=lambda signal: signal.decision_score, reverse=True)


def format_item(item: ReviewItem, include_command: bool = True) -> str:
    root = repo_root()
    suggested_command = item.suggested_action if item.suggested_action in {"study", "merge"} else "keep"
    command = f"；飞书：`/decide {item.index} {suggested_command}`" if include_command and item.status == "pending-review" else ""
    return (
        f"- [{item.topic}] [[{item.path.relative_to(root).with_suffix('')}]]"
        f"；priority={item.priority_score}；stable={item.suggested_action}/{item.stability}"
        f"；status={item.status}{command}"
    )


def render_board(target_week: str, weekly_items: list[ReviewItem], ranked_pending: list[ReviewItem]) -> str:
    signals = topic_signals(weekly_items)
    confirmed_study = [item for item in ranked_pending if item.suggested_action == "study" and item.stability == "confirmed"]
    ready_to_merge = [item for item in weekly_items if item.status == "ready-to-merge"]
    observing = [
        item
        for item in ranked_pending
        if item.suggested_action in {"study", "merge-plan"} and item.stability != "confirmed"
    ]
    high_review = [
        item
        for item in ranked_pending
        if item.suggested_action == "review" and safe_importance(item.importance_score) >= 4
    ]

    lines = [
        "---",
        f"title: Learning Decision Board - {target_week}",
        "type: learning-decision-board",
        "status: generated",
        f"week: {target_week}",
        "---",
        "",
        f"# Learning Decision Board - {target_week}",
        "",
        "## 一句话结论",
        "",
    ]
    if signals:
        top = signals[0]
        lines.append(f"- 本周最值得投入的主线是 `{top.topic}`：decision_score={top.decision_score}，high_value={top.high_value}，confirmed_study={top.confirmed_study}。")
    else:
        lines.append("- 本周暂无足够候选信号。")

    lines.extend(["", "## 主题投资组合", "", "| topic | candidates | high_value | confirmed_study | ready_to_merge | observing | avg_importance | decision_score |", "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"])
    for signal in signals:
        lines.append(
            f"| {signal.topic} | {signal.count} | {signal.high_value} | {signal.confirmed_study} | {signal.ready_to_merge} | {signal.observing} | {signal.avg_importance:.2f} | {signal.decision_score} |"
        )

    lines.extend(["", "## 建议立刻学习", ""])
    if confirmed_study:
        lines.extend(format_item(item) for item in confirmed_study[:8])
    else:
        lines.append("- 暂无经过多轮确认的学习项。")

    lines.extend(["", "## 准备合入的候选", ""])
    if ready_to_merge:
        lines.extend(format_item(item, include_command=False) for item in ready_to_merge[:8])
        lines.append("- 下一步：发送 `合入预览`，确认无误后再执行 `确认执行合入 <编号>`。")
    else:
        lines.append("- 暂无 ready-to-merge 候选；保持人工确认边界。")

    lines.extend(["", "## 继续观察", ""])
    if observing:
        lines.extend(format_item(item) for item in observing[:8])
    else:
        lines.append("- 暂无需要观察的 study / merge-plan 波动项。")

    lines.extend(["", "## 高重要性待判断", ""])
    if high_review:
        lines.extend(format_item(item) for item in high_review[:8])
    else:
        lines.append("- 暂无高重要性 review 项。")

    lines.extend(
        [
            "",
            "## 飞书快捷入口",
            "",
            "- `决策面板` / `/board`：查看这张面板。",
            "- `候选` / `/review`：查看待决策候选。",
            "- `/decide <编号> study|ignore|keep|merge`：做出决策。",
            "- `合入预览`：查看 ready-to-merge 的执行预览。",
            "",
            "## 输入",
            "",
            f"- weekly_candidates: {len(weekly_items)}",
            f"- ranked_pending_candidates: {len(ranked_pending)}",
        ]
    )
    return "\n".join(lines)


def generate_decision_board(week: str | None = None, dry_run: bool = False) -> Path:
    root = repo_root()
    target_week = week or week_str()
    weekly_items = all_review_items_for_week(target_week)
    ranked_pending = review_items(status="pending-review", limit=50)
    output = root / f"00-Agent-Inbox/Decision-Board/{target_week}.md"
    actual_output = write_text(output, render_board(target_week, weekly_items, ranked_pending), dry_run=dry_run)
    safe_print(f"[decision-board] output={relative_to_repo(output)}")
    return actual_output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--week", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    generate_decision_board(week=args.week, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
