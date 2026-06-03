#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
from typing import Iterable


def yes_no(value: bool) -> str:
    return "yes" if value else "no"


def normalize_tags(tags: Iterable[str]) -> str:
    cleaned = [tag.strip() for tag in tags if tag.strip()]
    return ", ".join(cleaned) if cleaned else "none"


def ensure_header(path: Path) -> None:
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("# Learnings Ledger\n\n", encoding="utf-8")


def build_entry(args: argparse.Namespace) -> str:
    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
    evidence_lines = args.evidence or ["No evidence supplied yet."]
    lines = [
        f"## {timestamp} | {args.title}",
        f"- summary: {args.summary}",
        f"- scope: {args.scope}",
        f"- confidence: {args.confidence:.2f}",
        f"- recurring: {yes_no(args.recurring)}",
        f"- verified: {yes_no(args.verified)}",
        f"- source: {args.source}",
        f"- risk: {args.risk}",
        f"- proposed_action: {args.proposed_action}",
        f"- rollback: {args.rollback}",
        f"- tags: {normalize_tags(args.tag)}",
        "- evidence:",
    ]
    lines.extend(f"  - {item}" for item in evidence_lines)
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Append a structured learning entry to a markdown ledger.")
    parser.add_argument("--target", default=".learnings/LEARNINGS.md", help="Markdown ledger to append to.")
    parser.add_argument("--title", required=True, help="Short title for the learning.")
    parser.add_argument("--summary", required=True, help="One-sentence explanation of the learning.")
    parser.add_argument("--scope", choices=["session", "project", "team", "global"], default="project")
    parser.add_argument("--confidence", type=float, default=0.50)
    parser.add_argument("--source", default="runtime")
    parser.add_argument("--recurring", action="store_true")
    parser.add_argument("--verified", action="store_true")
    parser.add_argument("--risk", choices=["low", "medium", "high"], default="medium")
    parser.add_argument("--proposed-action", default="observe")
    parser.add_argument("--rollback", default="Define rollback before promotion.")
    parser.add_argument("--evidence", action="append", default=[])
    parser.add_argument("--tag", action="append", default=[])
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    target = Path(args.target)
    ensure_header(target)
    entry = build_entry(args)

    if args.dry_run:
        print(entry)
        return 0

    with target.open("a", encoding="utf-8") as handle:
        handle.write(entry)
    print(f"Appended learning entry to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
