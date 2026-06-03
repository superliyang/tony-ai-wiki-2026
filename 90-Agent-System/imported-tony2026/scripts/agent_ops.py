from __future__ import annotations

import argparse
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from automation_doctor import run_doctor
from check_vault import check_vault
from curator_merge_execute import generate_execution_preview
from curator_merge_plan import generate_merge_plan
from generate_decision_board import generate_decision_board
from knowledge_daily import run_daily
from knowledge_weekly import run_weekly
from notify_feishu import notify as notify_feishu
from review_queue import format_review, review_items, write_review_queue
from utils import now_iso, relative_to_repo, repo_root, safe_print, today_str, write_text


@dataclass
class StepResult:
    name: str
    status: str
    seconds: float
    summary: dict[str, Any]
    error: str = ""


def run_step(name: str, fn: Callable[[], dict[str, Any]]) -> StepResult:
    started = time.monotonic()
    try:
        summary = fn()
        return StepResult(name=name, status="ok", seconds=time.monotonic() - started, summary=summary)
    except Exception as exc:
        return StepResult(name=name, status="failed", seconds=time.monotonic() - started, summary={}, error=str(exc))


def compact_summary(summary: dict[str, Any]) -> str:
    interesting_keys = [
        "source_items",
        "classified_items",
        "semantic_analysis",
        "digest",
        "weekly_digest",
        "ai_triage_report",
        "candidates",
        "study_queue",
        "source_quality",
        "topic_opportunities",
        "decision_board",
        "health_report",
        "notified",
        "decision_board_notified",
        "doctor_report",
        "review_queue",
        "merge_plan",
        "merge_execution_preview",
    ]
    lines: list[str] = []
    for key in interesting_keys:
        if key not in summary:
            continue
        value = summary[key]
        if isinstance(value, str):
            value = relative_to_repo(value)
        lines.append(f"- {key}: {value}")
    return "\n".join(lines) if lines else "- no summary"


def render_report(mode: str, rounds: int, results: list[StepResult], generated_at: str) -> str:
    ok_count = sum(1 for result in results if result.status == "ok")
    failed_count = len(results) - ok_count
    lines = [
        "---",
        f"title: Automation Ops Run - {generated_at}",
        "type: automation-ops-report",
        f"status: {'passed' if failed_count == 0 else 'failed'}",
        f"mode: {mode}",
        f"rounds: {rounds}",
        f"generated_at: {generated_at}",
        "---",
        "",
        f"# Automation Ops Run - {generated_at}",
        "",
        "## 总览",
        "",
        f"- mode: `{mode}`",
        f"- rounds: {rounds}",
        f"- steps: {len(results)}",
        f"- ok: {ok_count}",
        f"- failed: {failed_count}",
        "",
        "## 步骤结果",
        "",
    ]
    for index, result in enumerate(results, 1):
        lines.extend(
            [
                f"### {index}. {result.name}",
                "",
                f"- status: {result.status}",
                f"- seconds: {result.seconds:.2f}",
            ]
        )
        if result.error:
            lines.append(f"- error: {result.error}")
        lines.extend(["", compact_summary(result.summary), ""])
    lines.extend(
        [
            "## 结论",
            "",
            "- 如果 `failed=0`，说明当前自动化主链路可用。",
            "- 如果某一步失败，优先看对应 step 的 error，再看 `90-Agent-System/logs/`。",
            "- `dry-run` 主要验证链路，`real` 会写入知识库并可选择主动推送飞书。",
        ]
    )
    return "\n".join(lines)


def run_ops(rounds: int = 2, mode: str = "dry-run", notify: bool = False, notify_report: bool = False) -> Path:
    if rounds < 1:
        raise ValueError("rounds must be >= 1")
    if mode not in {"dry-run", "real"}:
        raise ValueError("mode must be dry-run or real")
    dry_run = mode == "dry-run"
    results: list[StepResult] = []

    results.append(run_step("automation doctor", lambda: {"doctor_report": str(run_doctor(network=False, dry_run=dry_run))}))

    for round_index in range(1, rounds + 1):
        results.append(
            run_step(
                f"round-{round_index}: daily",
                lambda: run_daily(dry_run=dry_run, no_notify=(dry_run or not notify)),
            )
        )
        results.append(
            run_step(
                f"round-{round_index}: weekly",
                lambda: run_weekly(dry_run=dry_run, no_notify=(dry_run or not notify)),
            )
        )

    results.append(
        run_step(
            "review queue",
            lambda: {
                "pending": len(review_items(limit=50)),
                "review_queue": str(write_review_queue(review_items(limit=12), dry_run=dry_run)),
                "preview": format_review(review_items(limit=5)),
            },
        )
    )
    results.append(run_step("decision board", lambda: {"decision_board": str(generate_decision_board(dry_run=dry_run))}))
    results.append(run_step("merge plan", lambda: {"merge_plan": str(generate_merge_plan(limit=12, dry_run=dry_run))}))
    results.append(
        run_step(
            "merge execution preview",
            lambda: {"merge_execution_preview": str(generate_execution_preview(limit=12, dry_run=dry_run))},
        )
    )
    results.append(run_step("vault health", lambda: {"health_report": str(check_vault(dry_run=dry_run))}))

    generated_at = now_iso().replace(":", "-")
    output = repo_root() / f"90-Agent-System/reports/automation-ops-{today_str()}-{int(time.time())}.md"
    report = render_report(mode, rounds, results, generated_at)
    actual_output = write_text(output, report, dry_run=False)
    safe_print(f"[ops] report={relative_to_repo(actual_output)}")

    if notify_report:
        notify_feishu(actual_output, dry_run=False)

    failed = [result for result in results if result.status != "ok"]
    if failed:
        raise RuntimeError(f"automation ops failed: {', '.join(result.name for result in failed)}")
    return actual_output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rounds", type=int, default=2)
    parser.add_argument("--mode", choices=["dry-run", "real"], default="dry-run")
    parser.add_argument("--notify", action="store_true", help="Allow daily/weekly notifications in real mode.")
    parser.add_argument("--notify-report", action="store_true", help="Push the final ops report to Feishu.")
    args = parser.parse_args()
    run_ops(rounds=args.rounds, mode=args.mode, notify=args.notify, notify_report=args.notify_report)


if __name__ == "__main__":
    main()
