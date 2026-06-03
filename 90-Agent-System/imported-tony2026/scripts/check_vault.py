from __future__ import annotations

import argparse
import re
import subprocess
from collections import Counter
from pathlib import Path

from utils import now_iso, repo_root, safe_print, today_str, write_text


WIKILINK_RE = re.compile(r"\[\[([^\]#|]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
REQUIRED_AREA_FILES = ["专题总览.md", "学习进度.md", "恢复笔记.md"]
IGNORED_PARTS = {".git", ".obsidian", ".p_obsidian", "obsidian-skills", "axton-obsidian-visual-skills", "copilot"}


def strip_code(text: str) -> str:
    without_fences = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    return re.sub(r"`[^`\n]+`", "", without_fences)


def markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        if any(part in IGNORED_PARTS for part in path.parts):
            continue
        if path.match("90-Agent-System/reports/vault-health-*.md"):
            continue
        files.append(path)
    return files


def vault_targets(root: Path) -> set[Path]:
    targets: set[Path] = set()
    for suffix in ("*.md", "*.canvas", "*.base"):
        for path in root.rglob(suffix):
            if any(part in IGNORED_PARTS for part in path.parts):
                continue
            targets.add(path.resolve())
    return targets


def build_note_index(files: list[Path], root: Path) -> set[str]:
    index: set[str] = set()
    for path in vault_targets(root):
        rel = path.relative_to(root)
        no_suffix = rel.with_suffix("")
        index.add(str(rel))
        index.add(str(no_suffix))
        index.add(path.name)
        index.add(path.stem)
    return index


def link_exists(source: Path, target: str, root: Path, index: set[str], target_paths: set[Path]) -> bool:
    cleaned = target.strip()
    candidates = {cleaned, f"{cleaned}.md", Path(cleaned).name, Path(cleaned).stem}
    if candidates & index:
        return True
    path_target = Path(cleaned)
    possible_paths = [root / path_target, source.parent / path_target]
    if not path_target.suffix:
        possible_paths.extend([root / f"{cleaned}.md", source.parent / f"{cleaned}.md"])
    for candidate in possible_paths:
        try:
            resolved = candidate.resolve()
        except OSError:
            continue
        if resolved in target_paths:
            return True
    return False


def find_broken_links(files: list[Path], root: Path) -> list[tuple[Path, str]]:
    index = build_note_index(files, root)
    targets = vault_targets(root)
    broken: list[tuple[Path, str]] = []
    for path in files:
        text = strip_code(path.read_text(encoding="utf-8", errors="ignore"))
        for target in WIKILINK_RE.findall(text):
            cleaned = target.strip()
            if not cleaned or cleaned.startswith(("http://", "https://")):
                continue
            if not link_exists(path, cleaned, root, index, targets):
                broken.append((path, cleaned))
    return broken


def git_touched_state(root: Path) -> list[str]:
    try:
        result = subprocess.run(["git", "status", "--short", ".obsidian", ".p_obsidian"], cwd=root, text=True, capture_output=True, check=False)
    except OSError:
        return ["git status unavailable"]
    return [line for line in result.stdout.splitlines() if line.strip()]


def check_vault(dry_run: bool = False, date_str: str | None = None) -> Path:
    root = repo_root()
    target_date = date_str or today_str()
    files = markdown_files(root)
    broken = find_broken_links(files, root)
    incoming = Counter()
    outgoing = Counter()
    for path in files:
        text = strip_code(path.read_text(encoding="utf-8", errors="ignore"))
        outgoing[path] += len(WIKILINK_RE.findall(text))
        for target in WIKILINK_RE.findall(text):
            incoming[target.split("|", 1)[0].split("#", 1)[0]] += 1
    orphan_count = sum(1 for path in files if outgoing[path] == 0 and incoming[path.stem] == 0)

    area_findings: list[str] = []
    areas_root = root / "01-Areas"
    if areas_root.exists():
        for area in sorted(path for path in areas_root.iterdir() if path.is_dir()):
            for required in REQUIRED_AREA_FILES:
                if not (area / required).exists():
                    area_findings.append(f"- {area.relative_to(root)} 缺少 `{required}`")

    config_findings: list[str] = []
    for rel in ["90-Agent-System/sources.yaml", "90-Agent-System/topic-router.yaml", "90-Agent-System/notification.yaml"]:
        if not (root / rel).exists():
            config_findings.append(f"- 缺少 `{rel}`")

    digest_findings: list[str] = []
    if not list((root / "00-Agent-Inbox/Daily-Digests").glob("*.md")):
        digest_findings.append("- 还没有 Daily Digest。")
    if not list((root / "00-Agent-Inbox/Weekly-Digests").glob("*.md")):
        digest_findings.append("- 还没有 Weekly Digest。")

    state_changes = git_touched_state(root)
    lines = [
        "---",
        f"title: Vault Health Report - {target_date}",
        "type: vault-health-report",
        "status: generated",
        f"date: {target_date}",
        "---",
        "",
        f"# Vault Health Report - {target_date}",
        "",
        "## 摘要",
        "",
        f"- generated_at: {now_iso()}",
        f"- markdown_files: {len(files)}",
        f"- broken_wikilinks_conservative: {len(broken)}",
        f"- orphan_notes_rough_count: {orphan_count}",
        f"- state_file_changes: {len(state_changes)}",
        "",
        "## Broken Wikilinks",
        "",
    ]
    if broken:
        for path, target in broken[:80]:
            lines.append(f"- {path.relative_to(root)} -> [[{target}]]")
        if len(broken) > 80:
            lines.append(f"- 另有 {len(broken) - 80} 条未展开。")
    else:
        lines.append("- 未发现保守规则下的 broken wikilink。")

    lines.extend(["", "## 专题健康度", ""])
    lines.extend(area_findings or ["- `01-Areas/*` 关键入口文件检查通过。"])
    lines.extend(["", "## Inbox 与配置", ""])
    lines.extend(config_findings or ["- `90-Agent-System` 核心配置存在。"])
    lines.extend(digest_findings or ["- Inbox 已存在 Daily / Weekly Digest。"])
    lines.extend(["", "## Runtime State 风险", ""])
    if state_changes:
        lines.extend([f"- {line}" for line in state_changes])
    else:
        lines.append("- 未发现 `.obsidian` / `.p_obsidian` 当前变更。")
    lines.extend(["", "## 说明", "", "- wikilink 检查为第一版保守实现，优先减少误报。"])
    output = root / f"90-Agent-System/reports/vault-health-{target_date}.md"
    actual_output = write_text(output, "\n".join(lines), dry_run=dry_run)
    safe_print(f"[health] output={output.relative_to(root)} broken={len(broken)}")
    return actual_output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    check_vault(dry_run=args.dry_run, date_str=args.date)


if __name__ == "__main__":
    main()
