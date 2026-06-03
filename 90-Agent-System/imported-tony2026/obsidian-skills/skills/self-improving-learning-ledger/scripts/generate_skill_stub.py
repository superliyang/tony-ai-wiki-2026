#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def build_skill(name: str, title: str, description: str) -> str:
    return f"""---
name: {name}
description: {description}
---

# {title}

## Overview

[TODO: Explain the repeated pattern this candidate skill captures.]

## When To Use This Skill

- [TODO: Add concrete trigger requests.]

## Workflow

1. [TODO: Capture the repeated situation.]
2. [TODO: Apply the bounded action pattern.]
3. [TODO: State the eval gate or rollback path.]

## Boundaries

- Do not enable this candidate globally until it passes evaluation.
- Keep the first rollout scoped and reversible.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a review-only skill stub from a promoted learning.")
    parser.add_argument("--name", default="")
    parser.add_argument("--title", required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--path", required=True, help="Directory where the candidate skill folder should be created.")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    name = args.name or slugify(args.title)
    target_dir = Path(args.path) / name
    skill_file = target_dir / "SKILL.md"

    if skill_file.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing candidate: {skill_file}")

    target_dir.mkdir(parents=True, exist_ok=True)
    skill_file.write_text(build_skill(name, args.title, args.description), encoding="utf-8")
    print(f"Created candidate skill stub at {skill_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
