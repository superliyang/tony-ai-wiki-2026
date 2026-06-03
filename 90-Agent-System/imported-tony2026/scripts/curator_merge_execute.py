from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from check_vault import check_vault
from curator_merge_plan import MergeCandidate, candidate_summary, existing_target_files, ready_candidates, target_area
from utils import now_iso, relative_to_repo, repo_root, safe_print, slugify, today_str, write_text


@dataclass
class ExecutionResult:
    candidate: MergeCandidate
    target: Path
    health_report: Path


def curated_target(item: MergeCandidate, date_str: str) -> Path:
    return target_area(item.topic) / "00-Inbox" / "Curated" / f"{date_str}-{slugify(item.title)}.md"


def note_link(path: Path) -> str:
    return f"[[{Path(relative_to_repo(path)).with_suffix('')}]]"


def render_curated_note(item: MergeCandidate, date_str: str) -> str:
    root = repo_root()
    area = target_area(item.topic)
    related = existing_target_files(area)
    lines = [
        "---",
        f"title: {item.title}",
        "type: curated-intake",
        "status: needs-domain-integration",
        f"topic: {item.topic}",
        f"source_url: {item.source_url}",
        f"curated_at: {now_iso()}",
        f"candidate: \"{note_link(item.path)}\"",
        "---",
        "",
        f"# {item.title}",
        "",
        "## 合入定位",
        "",
        "- 当前状态：已由人工确认进入正式专题的 intake 区，尚待整合到专题正文或 playbook。",
        f"- 来源候选：{note_link(item.path)}",
        f"- 目标专题：`{area.relative_to(root)}`",
        "",
        "## 内容摘要",
        "",
        f"- {candidate_summary(item)}",
        "",
        "## 为什么值得纳入",
        "",
        "- 该候选已经通过 Review Queue 的人工确认，值得在本专题中继续消化。",
        "- 下一步应判断它属于主题知识、案例、系统观察还是可复用工程模式。",
        "",
        "## 整合清单",
        "",
        "- [ ] 判断是否抽象为可复用结论，而不是只保留新闻事实。",
        "- [ ] 判断是否需要更新专题总览、学习进度或恢复笔记。",
        "- [ ] 判断是否需要补充主题索引、地图或 playbook。",
        "",
        "## 相关专题入口",
        "",
    ]
    if related:
        lines.extend([f"- {note_link(path)}" for path in related])
    else:
        lines.append("- 暂无标准入口文件，需要人工确认专题结构。")
    lines.extend(["", "## 原始来源", "", f"- {item.source_url}"])
    return "\n".join(lines)


def render_execution_preview(items: list[MergeCandidate], date_str: str) -> str:
    root = repo_root()
    lines = [
        "---",
        f"title: Curator Merge Execution Preview - {date_str}",
        "type: curator-merge-execution-preview",
        "status: awaiting-explicit-confirmation",
        f"date: {date_str}",
        "---",
        "",
        f"# Curator Merge Execution Preview - {date_str}",
        "",
        "## 安全边界",
        "",
        "- 本预览不会修改 `01-Areas/`。",
        "- 只有发送明确确认命令后，系统才会写入目标专题的 `00-Inbox/Curated/`。",
        "- 写入后仍保持 `needs-domain-integration`，不会冒充已经完成的知识整合。",
        "",
    ]
    if not items:
        lines.extend(["## 当前状态", "", "- 暂无 `ready-to-merge` 候选。"])
        return "\n".join(lines)
    for index, item in enumerate(items, 1):
        target = curated_target(item, date_str)
        lines.extend(
            [
                f"## {index}. {item.title}",
                "",
                f"- candidate: {note_link(item.path)}",
                f"- target: `{relative_to_repo(target)}`",
                f"- topic: {item.topic}",
                f"- source_url: {item.source_url}",
                f"- summary: {candidate_summary(item)}",
                f"- confirm_command: `确认执行合入 {index}`",
                "",
            ]
        )
    return "\n".join(lines)


def generate_execution_preview(limit: int = 8, date_str: str | None = None, dry_run: bool = False) -> Path:
    root = repo_root()
    target_date = date_str or today_str()
    output = root / f"00-Agent-Inbox/Review-Queue/Merge-Executions/{target_date}.md"
    items = ready_candidates(limit=limit)
    write_text(output, render_execution_preview(items, target_date), dry_run=dry_run)
    safe_print(f"[merge-execution-preview] ready={len(items)} output={output.relative_to(root)}")
    return output


def update_candidate_as_executed(item: MergeCandidate, target: Path, dry_run: bool = False) -> None:
    text = item.path.read_text(encoding="utf-8")
    text = re.sub(r"^status:\s*ready-to-merge$", "status: merged-to-area-inbox", text, count=1, flags=re.MULTILINE)
    audit = "\n".join(
        [
            "",
            "",
            "# Curator Merge Execution",
            "",
            f"- executed_at: {now_iso()}",
            "- status: merged-to-area-inbox",
            f"- target: {note_link(target)}",
        ]
    )
    write_text(item.path, text.rstrip() + audit, dry_run=dry_run)


def execute_ready_candidate(index: int, confirmed: bool = False, date_str: str | None = None, dry_run: bool = False) -> ExecutionResult:
    if not confirmed:
        raise ValueError("Explicit confirmation required. Use --confirm or send `确认执行合入 <编号>`.")
    items = ready_candidates(limit=50)
    if index < 1 or index > len(items):
        raise IndexError(f"Ready-to-merge item index out of range: {index}")
    item = items[index - 1]
    target_date = date_str or today_str()
    target = curated_target(item, target_date)
    if target.exists() and not dry_run:
        raise FileExistsError(f"Curated target already exists: {relative_to_repo(target)}")
    write_text(target, render_curated_note(item, target_date), dry_run=dry_run)
    update_candidate_as_executed(item, target, dry_run=dry_run)
    health_report = check_vault(dry_run=dry_run)
    safe_print(f"[merge-execution] candidate={item.title} target={relative_to_repo(target)}")
    return ExecutionResult(candidate=item, target=target, health_report=health_report)


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    preview = sub.add_parser("preview")
    preview.add_argument("--limit", type=int, default=8)
    preview.add_argument("--date", default=None)
    preview.add_argument("--dry-run", action="store_true")
    apply = sub.add_parser("apply")
    apply.add_argument("index", type=int)
    apply.add_argument("--confirm", action="store_true")
    apply.add_argument("--date", default=None)
    apply.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.cmd == "preview":
        generate_execution_preview(limit=args.limit, date_str=args.date, dry_run=args.dry_run)
    else:
        execute_ready_candidate(index=args.index, confirmed=args.confirm, date_str=args.date, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
