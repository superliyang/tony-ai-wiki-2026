from __future__ import annotations

import argparse
import os
import tempfile

from check_vault import check_vault
from classify_items import classify_items
from collect_sources import collect_sources
from generate_candidates import generate_candidates
from generate_ai_triage_report import generate_report as generate_ai_triage_report
from generate_digest import generate_digest
from generate_ops_insights import generate_ops_insights
from generate_decision_board import generate_decision_board
from generate_study_queue import generate_study_queue
from notify_feishu import notify as notify_feishu
from semantic_analyze import semantic_analyze
from utils import repo_root, safe_print, today_str, week_str


def run_weekly(week: str | None = None, dry_run: bool = False, no_notify: bool = False) -> dict[str, object]:
    target_week = week or week_str()
    target_date = today_str()
    previous_preview = os.getenv("KNOWLEDGE_DRY_RUN_DIR")
    temp_dir: tempfile.TemporaryDirectory[str] | None = None
    if dry_run and not previous_preview:
        temp_dir = tempfile.TemporaryDirectory(prefix="knowledge-weekly-")
        os.environ["KNOWLEDGE_DRY_RUN_DIR"] = temp_dir.name
        safe_print(f"[weekly] dry-run preview dir: {temp_dir.name}")
    try:
        safe_print(f"[weekly] week={target_week} dry_run={dry_run}")
        source_path = collect_sources(days=7, dry_run=dry_run, date_str=target_week)
        classified_path = classify_items(source_path, dry_run=dry_run, date_str=target_week)
        analyzed_path = semantic_analyze(classified_path, dry_run=dry_run, date_str=target_week)
        triage_path = generate_ai_triage_report(analyzed_path, output_key=target_week, dry_run=dry_run)
        digest_path = generate_digest("weekly", analyzed_path, dry_run=dry_run, week=target_week)
        candidates = generate_candidates(analyzed_path, dry_run=dry_run, date_str=target_date)
        study_queue_path = generate_study_queue(analyzed_path, dry_run=dry_run, date_str=target_date)
        insights = generate_ops_insights(analyzed_path, source_path=source_path, key=target_week, dry_run=dry_run)
        decision_board_path = generate_decision_board(week=target_week, dry_run=dry_run)
        health_path = check_vault(dry_run=dry_run, date_str=target_date)
        notified = False
        decision_board_notified = False
        if no_notify:
            safe_print("[weekly] notification skipped by --no-notify")
        else:
            notified = notify_feishu(digest_path, dry_run=dry_run)
            decision_board_notified = notify_feishu(decision_board_path, dry_run=dry_run)
        summary = {
            "source_items": str(source_path),
            "classified_items": str(classified_path),
            "semantic_analysis": str(analyzed_path),
            "ai_triage_report": str(triage_path),
            "weekly_digest": str(digest_path),
            "candidates": len(candidates),
            "study_queue": str(study_queue_path),
            "source_quality": str(insights["source_quality"]),
            "topic_opportunities": str(insights["topic_opportunities"]),
            "decision_board": str(decision_board_path),
            "health_report": str(health_path),
            "notified": notified,
            "decision_board_notified": decision_board_notified,
        }
        safe_print(f"[weekly] summary={summary}")
        return summary
    finally:
        if dry_run and not previous_preview:
            os.environ.pop("KNOWLEDGE_DRY_RUN_DIR", None)
        if temp_dir:
            temp_dir.cleanup()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--week", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-notify", action="store_true")
    args = parser.parse_args()
    run_weekly(week=args.week, dry_run=args.dry_run, no_notify=args.no_notify)


if __name__ == "__main__":
    main()
