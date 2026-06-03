from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from review_priority import priority_reason, priority_score
from utils import load_items, repo_root, safe_print, today_str, write_text


def render_item(index: int, item: dict[str, Any]) -> list[str]:
    analysis = item.get("semantic_analysis") if isinstance(item.get("semantic_analysis"), dict) else {}
    title = item.get("title", "Untitled")
    action = analysis.get("suggested_action") or item.get("ai_suggested_action") or "review"
    topic = item.get("topic", "Others")
    semantic_topic = analysis.get("semantic_topic") or topic
    value = analysis.get("learning_value") or item.get("ai_learning_value") or item.get("classification_reason", "")
    relationship = analysis.get("vault_relationship") or item.get("ai_vault_relationship") or ""
    confidence = analysis.get("confidence", "")
    source = item.get("source_name", "")
    score = priority_score(item.get("importance_score", 1), topic, source, action)
    return [
        f"### {index}. {title}",
        "",
        f"- topic: {topic}",
        f"- semantic_topic: {semantic_topic}",
        f"- suggested_action: {action}",
        f"- priority_score: {score}",
        f"- why_ranked: {priority_reason(item.get('importance_score', 1), topic, source, action, action_label='本轮建议')}",
        f"- confidence: {confidence}",
        f"- source: {item.get('url', '')}",
        f"- learning_value: {value}",
        f"- vault_relationship: {relationship}",
        "",
    ]


def generate_report(input_path: Path, output_key: str | None = None, dry_run: bool = False) -> Path:
    root = repo_root()
    data_items = load_items(input_path)
    analyzed = [item for item in data_items if isinstance(item.get("semantic_analysis"), dict)]
    analyzed.sort(key=analysis_priority, reverse=True)
    key = output_key or input_path.stem.replace("semantic-analysis-", "") or today_str()
    output = root / f"00-Agent-Inbox/Review-Queue/AI-Triage/{key}.md"
    lines = [
        "---",
        f"title: AI Triage Report - {key}",
        "type: ai-triage-report",
        "status: generated",
        f"key: {key}",
        "---",
        "",
        f"# AI Triage Report - {key}",
        "",
        "## 摘要",
        "",
        f"- analyzed_items: {len(analyzed)}",
        "- 这份报告来自 DeepSeek 语义分析，用于辅助 Review Queue 决策。",
        "- 它不会自动修改 `01-Areas/`。",
        "",
        "## 建议优先 review",
        "",
    ]
    if analyzed:
        for index, item in enumerate(analyzed[:8], 1):
            lines.extend(render_item(index, item))
    else:
        lines.append("- 暂无 AI 语义分析结果。")
    lines.extend(
        [
            "## 下一步",
            "",
            "- 在飞书发送 `候选` 查看 Review Queue。",
            "- 用 `1 学习`、`2 忽略`、`3 保留`、`4 合入` 做决策。",
            "- 对 `ready-to-merge` 候选发送 `合入计划`。",
        ]
    )
    actual_output = write_text(output, "\n".join(lines), dry_run=dry_run)
    safe_print(f"[ai-triage] analyzed={len(analyzed)} output={output.relative_to(root)}")
    return actual_output


def analysis_priority(item: dict[str, Any]) -> int:
    analysis = item.get("semantic_analysis") if isinstance(item.get("semantic_analysis"), dict) else {}
    return priority_score(
        item.get("importance_score", 1),
        item.get("topic", "Others"),
        item.get("source_name", ""),
        analysis.get("suggested_action") or item.get("ai_suggested_action") or "review",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--key", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    input_path = Path(args.input)
    if not input_path.is_absolute():
        input_path = repo_root() / input_path
    generate_report(input_path, output_key=args.key, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
