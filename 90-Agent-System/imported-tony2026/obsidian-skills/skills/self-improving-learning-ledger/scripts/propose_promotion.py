#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

ENTRY_RE = re.compile(r"^## (?P<ts>[^|]+)\| (?P<title>.+)$")
FIELD_RE = re.compile(r"^- (?P<key>[a-z_]+): (?P<value>.*)$")
EVIDENCE_RE = re.compile(r"^  - (?P<value>.+)$")


@dataclass
class Entry:
    title: str
    timestamp: str
    summary: str = ""
    scope: str = "project"
    confidence: float = 0.0
    recurring: bool = False
    verified: bool = False
    source: str = "runtime"
    risk: str = "medium"
    proposed_action: str = "observe"
    rollback: str = ""
    tags: str = ""
    evidence: List[str] = field(default_factory=list)


def parse_bool(value: str) -> bool:
    return value.strip().lower() in {"yes", "true", "1"}


def parse_entries(text: str) -> List[Entry]:
    entries: List[Entry] = []
    current: Entry | None = None
    in_evidence = False

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        entry_match = ENTRY_RE.match(line)
        if entry_match:
            if current:
                entries.append(current)
            current = Entry(title=entry_match.group("title").strip(), timestamp=entry_match.group("ts").strip())
            in_evidence = False
            continue
        if current is None:
            continue
        if line == "- evidence:":
            in_evidence = True
            continue
        if in_evidence:
            evidence_match = EVIDENCE_RE.match(line)
            if evidence_match:
                current.evidence.append(evidence_match.group("value").strip())
                continue
            in_evidence = False
        field_match = FIELD_RE.match(line)
        if not field_match:
            continue
        key = field_match.group("key")
        value = field_match.group("value").strip()
        if key == "summary":
            current.summary = value
        elif key == "scope":
            current.scope = value
        elif key == "confidence":
            current.confidence = float(value or 0)
        elif key == "recurring":
            current.recurring = parse_bool(value)
        elif key == "verified":
            current.verified = parse_bool(value)
        elif key == "source":
            current.source = value
        elif key == "risk":
            current.risk = value
        elif key == "proposed_action":
            current.proposed_action = value
        elif key == "rollback":
            current.rollback = value
        elif key == "tags":
            current.tags = value
    if current:
        entries.append(current)
    return entries


def score(entry: Entry) -> int:
    total = round(entry.confidence * 40)
    if entry.recurring:
        total += 20
    if entry.verified:
        total += 20
    total += min(len(entry.evidence), 3) * 5
    if entry.scope in {"team", "global"}:
        total += 10
    elif entry.scope == "project":
        total += 5
    if entry.risk == "low":
        total += 5
    elif entry.risk == "high":
        total -= 20
    return total


def classify(entry: Entry, total: int) -> str:
    if total >= 75 and entry.verified and entry.recurring and entry.risk != "high":
        return "skill_candidate" if entry.scope in {"team", "global"} else "durable_rule"
    if total >= 55:
        return "shadow"
    return "observe"


def render(entries: List[Entry]) -> str:
    lines = ["# Promotion Review Report", ""]
    if not entries:
        lines.append("No learning entries matched the requested slice.")
        return "\n".join(lines)
    for entry in entries:
        total = score(entry)
        classification = classify(entry, total)
        lines.extend([
            f"## {entry.title}",
            f"- timestamp: {entry.timestamp}",
            f"- score: {total}",
            f"- recommendation: {classification}",
            f"- scope: {entry.scope}",
            f"- confidence: {entry.confidence:.2f}",
            f"- recurring: {'yes' if entry.recurring else 'no'}",
            f"- verified: {'yes' if entry.verified else 'no'}",
            f"- risk: {entry.risk}",
            f"- evidence_count: {len(entry.evidence)}",
            f"- rollback: {entry.rollback or 'missing'}",
            "",
        ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Review structured learning entries and propose promotion decisions.")
    parser.add_argument("--target", default=".learnings/LEARNINGS.md")
    parser.add_argument("--last", type=int, default=10, help="Only review the last N entries.")
    parser.add_argument("--title-contains", default="", help="Optional substring filter for titles.")
    parser.add_argument("--output", default="", help="Optional markdown output path.")
    args = parser.parse_args()

    text = Path(args.target).read_text(encoding="utf-8") if Path(args.target).exists() else ""
    entries = parse_entries(text)
    if args.title_contains:
        entries = [entry for entry in entries if args.title_contains.lower() in entry.title.lower()]
    entries = entries[-args.last:]
    report = render(entries)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report + "\n", encoding="utf-8")
        print(f"Wrote promotion report to {output_path}")
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
