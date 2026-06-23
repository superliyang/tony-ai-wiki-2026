#!/usr/bin/env python3
from __future__ import annotations

import argparse
import filecmp
import json
import re
import shutil
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path


VAULT = Path(__file__).resolve().parents[1]
LEGACY_ROOT = VAULT / "10-Knowledge" / "_Imported" / "tony2026"
REPORT_DIR = VAULT / "90-Agent-System" / "migration" / "legacy-vault-extraction"


AREA_TARGETS = {
    "AI-Learning": "10-Knowledge/AI",
    "AI-Foundations": "10-Knowledge/AI-Foundations",
    "AI-Applications": "10-Knowledge/AI-Applications",
    "AI-Architect": "10-Knowledge/AI-Architecture",
    "AI-Engineering": "10-Knowledge/AI-Engineering",
    "AI-Open-Source": "10-Knowledge/AI-Open-Source",
    "Big-Data": "10-Knowledge/Big-Data",
    "Cloud-Native": "10-Knowledge/Cloud-Native",
    "Engineering-Management": "10-Knowledge/Engineering-Management",
    "English-Learning": "10-Knowledge/English-Learning",
    "International-Payments": "10-Knowledge/International-Payments",
    "Macro-Insight": "10-Knowledge/Macro-Insight",
    "Security": "10-Knowledge/Security",
    "Skills-Gaming": "10-Knowledge/Skills-Gaming",
    "_Meta": "90-Agent-System/legacy-tony2026/meta",
}


ROOT_NOTE_TARGET = "10-Knowledge/AI/00-Navigation"
SHARED_TEMPLATE_TARGET = "10-Knowledge/Shared-Templates/tony2026"
ARCHIVE_TARGET = "90-Agent-System/legacy-tony2026/archive"
ROOT_NOTES_TARGET = "00-Home/legacy-tony2026"
TAGS_TARGET = "90-Agent-System/legacy-tony2026/tags"


@dataclass
class MoveRecord:
    source: str
    target: str
    action: str


def rel(path: Path) -> str:
    return path.relative_to(VAULT).as_posix()


def note_stem(path: Path) -> str:
    return path.with_suffix("").as_posix()


def conflict_path(target: Path) -> Path:
    index = 2
    first = True
    while True:
        if first:
            if target.suffix:
                candidate = target.with_name(f"{target.stem} - 旧库{target.suffix}")
            else:
                candidate = target.with_name(f"{target.name} - 旧库")
            first = False
        else:
            if target.suffix:
                candidate = target.with_name(f"{target.stem} - 旧库 {index}{target.suffix}")
            else:
                candidate = target.with_name(f"{target.name} - 旧库 {index}")
            index += 1

        if not candidate.exists():
            return candidate


def existing_conflict_copy(source: Path, target: Path) -> Path | None:
    index = 2
    first = True
    while True:
        if first:
            if target.suffix:
                candidate = target.with_name(f"{target.stem} - 旧库{target.suffix}")
            else:
                candidate = target.with_name(f"{target.name} - 旧库")
            first = False
        else:
            if target.suffix:
                candidate = target.with_name(f"{target.stem} - 旧库 {index}{target.suffix}")
            else:
                candidate = target.with_name(f"{target.name} - 旧库 {index}")
            index += 1

        if not candidate.exists():
            return None
        if filecmp.cmp(source, candidate, shallow=False):
            return candidate
        index += 1


def target_for(source: Path) -> Path | None:
    rel_source = source.relative_to(LEGACY_ROOT)
    parts = rel_source.parts

    if parts[0] == "01-Areas":
        if len(parts) == 1:
            return None
        if len(parts) >= 2 and source.is_file():
            if len(parts) == 2:
                return VAULT / ROOT_NOTE_TARGET / parts[1]
            area = parts[1]
            target_base = AREA_TARGETS.get(area)
            if not target_base:
                return None
            return VAULT / target_base / Path(*parts[2:])

    if parts[0] == "08-Shared-Templates":
        return VAULT / SHARED_TEMPLATE_TARGET / Path(*parts[1:])

    if parts[0] == "99-Archive":
        return VAULT / ARCHIVE_TARGET / Path(*parts[1:])

    if parts[0] == "root-notes":
        return VAULT / ROOT_NOTES_TARGET / Path(*parts[1:])

    if parts[0] == "Tags":
        return VAULT / TAGS_TARGET / Path(*parts[1:])

    if len(parts) == 1 and source.name == "README.md":
        return VAULT / "90-Agent-System" / "legacy-tony2026" / "README.md"

    return None


def copy_file(source: Path, target: Path, apply: bool) -> tuple[Path, str]:
    if target.exists():
        if filecmp.cmp(source, target, shallow=False):
            return target, "same"
        existing = existing_conflict_copy(source, target)
        if existing is not None:
            return existing, "same"
        target = conflict_path(target)
        action = "conflict-copy"
    else:
        action = "copy"

    if apply:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    return target, action


def build_replacements(records: list[MoveRecord]) -> list[tuple[str, str]]:
    replacements: list[tuple[str, str]] = []
    for record in records:
        old = note_stem(Path(record.source))
        new = note_stem(Path(record.target))
        replacements.append((old, new))
    replacements.sort(key=lambda item: len(item[0]), reverse=True)
    return replacements


def rewrite_text(text: str, replacements: list[tuple[str, str]]) -> tuple[str, int]:
    if "_Imported/tony2026" not in text and "10-Knowledge/_Imported" not in text:
        return text, 0

    changes = 0
    for old, new in replacements:
        escaped = re.escape(old)
        patterns = [
            (re.compile(rf"\[\[{escaped}([#|\]])"), rf"[[{new}\1"),
            (re.compile(rf"`{escaped}`"), f"`{new}`"),
            (re.compile(escaped), new),
        ]
        for pattern, replacement in patterns:
            text, count = pattern.subn(replacement, text)
            changes += count
    return text, changes


def markdown_files_for_rewrite() -> list[Path]:
    ignored_parts = {
        ".git",
        ".obsidian",
        ".stfolder",
        "node_modules",
    }
    files: list[Path] = []
    for path in VAULT.rglob("*.md"):
        if any(part in ignored_parts for part in path.parts):
            continue
        if LEGACY_ROOT in path.parents:
            continue
        files.append(path)
    return files


def run(apply: bool) -> int:
    records: list[MoveRecord] = []
    skipped: list[str] = []

    for source in sorted(LEGACY_ROOT.rglob("*")):
        if not source.is_file():
            continue
        target = target_for(source)
        if target is None:
            skipped.append(rel(source))
            continue
        actual_target, action = copy_file(source, target, apply)
        records.append(MoveRecord(rel(source), rel(actual_target), action))

    replacements = build_replacements(records)
    rewrite_records: list[dict[str, str | int]] = []

    if apply:
        for md_file in markdown_files_for_rewrite():
            original = md_file.read_text(encoding="utf-8")
            updated, changes = rewrite_text(original, replacements)
            if changes:
                md_file.write_text(updated, encoding="utf-8")
                rewrite_records.append({"file": rel(md_file), "changes": changes})

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    report = {
        "mode": "apply" if apply else "dry-run",
        "generated_at": timestamp,
        "legacy_root": rel(LEGACY_ROOT),
        "copied_or_mapped": [asdict(record) for record in records],
        "skipped": skipped,
        "rewritten_files": rewrite_records,
        "summary": {
            "records": len(records),
            "copy": sum(1 for record in records if record.action == "copy"),
            "same": sum(1 for record in records if record.action == "same"),
            "conflict_copy": sum(1 for record in records if record.action == "conflict-copy"),
            "skipped": len(skipped),
            "rewritten_files": len(rewrite_records),
        },
    }

    if apply:
        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        report_path = REPORT_DIR / f"{timestamp}-extraction-report.json"
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        print(report_path.relative_to(VAULT))
    else:
        print(json.dumps(report["summary"], ensure_ascii=False, indent=2))

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract legacy tony2026 knowledge out of 10-Knowledge/_Imported.")
    parser.add_argument("--apply", action="store_true", help="Copy files and rewrite links. Without this, only prints a dry-run summary.")
    args = parser.parse_args()
    return run(apply=args.apply)


if __name__ == "__main__":
    raise SystemExit(main())
