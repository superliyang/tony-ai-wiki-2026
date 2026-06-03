from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path

from check_vault import check_vault
from classify_items import classify_items
from collect_sources import collect_sources
from generate_candidates import generate_candidates
from generate_digest import generate_digest
from generate_ops_insights import generate_ops_insights
from generate_study_queue import generate_study_queue
from notify_feishu import notify as notify_feishu
from semantic_analyze import semantic_analyze
from utils import parse_date, repo_root, safe_print, today_str


def run_daily(date_str: str | None = None, days: int = 1, dry_run: bool = False, no_notify: bool = False) -> dict[str, object]:
    root = repo_root()
    target_date = date_str or today_str()
    previous_preview = os.getenv("KNOWLEDGE_DRY_RUN_DIR")
    temp_dir: tempfile.TemporaryDirectory[str] | None = None
    if dry_run and not previous_preview:
        temp_dir = tempfile.TemporaryDirectory(prefix="knowledge-daily-")
        os.environ["KNOWLEDGE_DRY_RUN_DIR"] = temp_dir.name
        safe_print(f"[daily] dry-run preview dir: {temp_dir.name}")
    try:
        safe_print(f"[daily] date={target_date} days={days} dry_run={dry_run}")
        source_path = collect_sources(days=days, dry_run=dry_run, date_str=target_date)
        classified_path = classify_items(source_path, dry_run=dry_run, date_str=target_date)
        analyzed_path = semantic_analyze(classified_path, dry_run=dry_run, date_str=target_date)
        digest_path = generate_digest("daily", analyzed_path, dry_run=dry_run, date_str=target_date)
        candidates = generate_candidates(analyzed_path, dry_run=dry_run, date_str=target_date)
        study_queue_path = generate_study_queue(analyzed_path, dry_run=dry_run, date_str=target_date)
        insights = generate_ops_insights(analyzed_path, source_path=source_path, key=target_date, dry_run=dry_run)
        health_path = check_vault(dry_run=dry_run, date_str=target_date)
        notified = False
        if no_notify:
            safe_print("[daily] notification skipped by --no-notify")
        else:
            notified = notify_feishu(digest_path, dry_run=dry_run)
        summary = {
            "source_items": str(source_path),
            "classified_items": str(classified_path),
            "semantic_analysis": str(analyzed_path),
            "digest": str(digest_path),
            "candidates": len(candidates),
            "study_queue": str(study_queue_path),
            "source_quality": str(insights["source_quality"]),
            "topic_opportunities": str(insights["topic_opportunities"]),
            "health_report": str(health_path),
            "notified": notified,
        }
        safe_print(f"[daily] summary={summary}")
        return summary
    finally:
        if dry_run and not previous_preview:
            os.environ.pop("KNOWLEDGE_DRY_RUN_DIR", None)
        if temp_dir:
            temp_dir.cleanup()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None)
    parser.add_argument("--days", type=int, default=1, choices=[1, 7, 30])
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-notify", action="store_true")
    args = parser.parse_args()
    if args.date:
        parse_date(args.date)
    run_daily(date_str=args.date, days=args.days, dry_run=args.dry_run, no_notify=args.no_notify)


if __name__ == "__main__":
    main()
