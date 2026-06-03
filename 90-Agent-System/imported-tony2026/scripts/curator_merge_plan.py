from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

from utils import clamp, extract_frontmatter, repo_root, safe_print, today_str, write_text


@dataclass
class MergeCandidate:
    path: Path
    title: str
    topic: str
    status: str
    source_url: str
    importance_score: str
    body: str


def candidate_files() -> list[Path]:
    return sorted((repo_root() / "00-Agent-Inbox/Candidates").glob("*/*.md"), key=lambda path: path.stat().st_mtime, reverse=True)


def parse_candidate(path: Path) -> MergeCandidate:
    text = path.read_text(encoding="utf-8")
    meta, body = extract_frontmatter(text)
    return MergeCandidate(
        path=path,
        title=meta.get("title", path.stem),
        topic=meta.get("topic", "Others"),
        status=meta.get("status", "pending-review"),
        source_url=meta.get("source_url", ""),
        importance_score=meta.get("importance_score", "1"),
        body=body.strip(),
    )


def ready_candidates(limit: int = 10) -> list[MergeCandidate]:
    items: list[MergeCandidate] = []
    for path in candidate_files():
        item = parse_candidate(path)
        if item.status == "ready-to-merge":
            items.append(item)
        if len(items) >= limit:
            break
    return items


def target_area(topic: str) -> Path:
    root = repo_root()
    direct = root / "01-Areas" / topic
    if direct.exists():
        return direct
    return root / "01-Areas"


def existing_target_files(area: Path) -> list[Path]:
    candidates = [
        area / "专题总览.md",
        area / "学习进度.md",
        area / "恢复笔记.md",
        area / "05-Topics/主题索引.md",
        area / "06-Maps/地图索引.md",
        area / "07-Topics/主题索引.md",
        area / "08-Maps/地图索引.md",
    ]
    return [path for path in candidates if path.exists()]


def candidate_summary(item: MergeCandidate) -> str:
    lines: list[str] = []
    capture = False
    for line in item.body.splitlines():
        if line.startswith("# 这是什么"):
            capture = True
            continue
        if capture and line.startswith("# "):
            break
        if capture and line.strip():
            lines.append(line.strip())
    return clamp(" ".join(lines) or item.body, 300)


def render_plan(items: list[MergeCandidate], date_str: str) -> str:
    lines = [
        "---",
        f"title: Curator Merge Plan - {date_str}",
        "type: curator-merge-plan",
        "status: pending-human-confirmation",
        f"date: {date_str}",
        "---",
        "",
        f"# Curator Merge Plan - {date_str}",
        "",
        "## 目标",
        "",
        "把 `ready-to-merge` 候选转成正式知识区合入计划。第一版只生成计划，不自动修改 `01-Areas/`。",
        "",
    ]
    if not items:
        lines.extend(
            [
                "## 当前状态",
                "",
                "- 暂无 `ready-to-merge` 候选。",
                "- 可以先在飞书里发送 `候选`，再用 `1 合入` 标记一个候选。",
            ]
        )
        return "\n".join(lines)

    for index, item in enumerate(items, 1):
        area = target_area(item.topic)
        target_files = existing_target_files(area)
        lines.extend(
            [
                f"## {index}. {item.title}",
                "",
                f"- candidate: [[{item.path.relative_to(repo_root()).with_suffix('')}]]",
                f"- topic: {item.topic}",
                f"- target_area: `{area.relative_to(repo_root())}`",
                f"- importance_score: {item.importance_score}",
                f"- source_url: {item.source_url}",
                "",
                "### 内容摘要",
                "",
                f"- {candidate_summary(item)}",
                "",
                "### 建议合入方式",
                "",
                "- 先判断它是 `topic note`、`system/project note`、`playbook` 还是 `case`。",
                "- 如果只是新闻信号，优先合入现有专题进度或 recent supplement，不要新建孤立正文。",
                "- 如果代表可复用模式，再考虑新增 topic / playbook，并更新索引。",
                "",
                "### 建议检查/更新文件",
                "",
            ]
        )
        if target_files:
            lines.extend([f"- [[{path.relative_to(repo_root()).with_suffix('')}]]" for path in target_files])
        else:
            lines.append("- 未找到标准专题入口，需人工选择目标专题。")
        lines.extend(
            [
                "",
                "### 人工确认点",
                "",
                "- 这个候选是否真的值得进入正式知识区？",
                "- 是否只是日报/周报里保留即可？",
                "- 如果合入，最小改动是什么？",
                "- 是否需要同步更新 `学习进度.md` 和 `恢复笔记.md`？",
                "",
            ]
        )
    lines.extend(
        [
            "## 下一步",
            "",
            "- 人工确认后，再由 Curator Agent 执行具体合入。",
            "- 合入后必须运行 `python3 scripts/check_vault.py`。",
            "- 若出现断链或结构风险，先生成修复建议，不自动提交正式知识区。",
        ]
    )
    return "\n".join(lines)


def generate_merge_plan(limit: int = 10, date_str: str | None = None, dry_run: bool = False) -> Path:
    root = repo_root()
    target_date = date_str or today_str()
    output = root / f"00-Agent-Inbox/Review-Queue/Merge-Plans/{target_date}.md"
    items = ready_candidates(limit=limit)
    write_text(output, render_plan(items, target_date), dry_run=dry_run)
    safe_print(f"[merge-plan] ready={len(items)} output={output.relative_to(root)}")
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--date", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    generate_merge_plan(limit=args.limit, date_str=args.date, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
