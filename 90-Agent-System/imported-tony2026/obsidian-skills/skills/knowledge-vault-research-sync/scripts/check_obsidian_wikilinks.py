#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

PATTERN = re.compile(r"\[\[([^\]]+)\]\]")


def resolve_candidates(root: Path, file_path: Path, target: str, by_name: dict[str, list[Path]]) -> list[Path]:
    target = target.split("|", 1)[0].split("#", 1)[0].strip()
    if not target:
        return []

    candidates: list[Path] = []
    if "/" in target or target.startswith("."):
        base = file_path.parent / target
        if base.suffix:
            candidates.append(base.resolve())
        else:
            candidates.append(base.with_suffix(".md").resolve())
            candidates.append(base.with_suffix(".canvas").resolve())
            candidates.append(base.with_suffix(".base").resolve())
    else:
        base = file_path.parent / target
        if base.suffix:
            candidates.append(base.resolve())
        else:
            candidates.append(base.with_suffix(".md").resolve())
            candidates.append(base.with_suffix(".canvas").resolve())
            candidates.append(base.with_suffix(".base").resolve())
        candidates.extend(p.resolve() for p in by_name.get(Path(target).stem, []))
        for other in root.rglob(Path(target).stem + ".md"):
            candidates.append(other.resolve())
        for other in root.rglob(Path(target).stem + ".canvas"):
            candidates.append(other.resolve())
        for other in root.rglob(Path(target).stem + ".base"):
            candidates.append(other.resolve())
    return list(dict.fromkeys(candidates))


def check_root(root: Path) -> int:
    md_files = list(root.rglob("*.md"))
    extras = list(root.rglob("*.canvas")) + list(root.rglob("*.base"))
    by_name: dict[str, list[Path]] = {}
    for p in md_files + extras:
        by_name.setdefault(p.stem, []).append(p)

    missing: list[tuple[Path, str]] = []
    for md in md_files:
        text = md.read_text(encoding="utf-8")
        for raw in PATTERN.findall(text):
            candidates = resolve_candidates(root, md, raw, by_name)
            if candidates and any(c.exists() for c in candidates):
                continue
            target = raw.split("|", 1)[0].split("#", 1)[0].strip()
            if target:
                missing.append((md, target))

    print(f"{root}: missing={len(missing)}")
    for md, target in missing[:50]:
        print(f"  {md.relative_to(root)} -> {target}")
    return 1 if missing else 0


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: check_obsidian_wikilinks.py <root> [<root> ...]", file=sys.stderr)
        return 2
    code = 0
    for raw in argv[1:]:
        root = Path(raw).expanduser().resolve()
        if not root.exists():
            print(f"Missing root: {root}", file=sys.stderr)
            code = 2
            continue
        code = max(code, check_root(root))
    return code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
