from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

from review_stability import Observation, parse_observations, render_history, stable_action, with_observation
from utils import clamp, extract_frontmatter, load_yaml, now_iso, read_json, repo_root, safe_print, slugify, today_str, write_text


def existing_candidates(topic_dir: Path) -> dict[str, Path]:
    candidates: dict[str, Path] = {}
    for path in topic_dir.glob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        match = re.search(r"^source_url:\s*(.+)$", text, flags=re.MULTILINE)
        if match:
            candidates[match.group(1).strip().strip('"')] = path
    return candidates


def set_frontmatter_value(text: str, key: str, value: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end == -1:
        return text
    head = text[:end]
    body = text[end:]
    pattern = re.compile(rf"^{re.escape(key)}:\s*.*$", re.MULTILINE)
    if pattern.search(head):
        head = pattern.sub(f"{key}: {value}", head)
    else:
        head = f"{head}\n{key}: {value}"
    return head + body


def update_section(text: str, heading: str, content: str) -> str:
    pattern = re.compile(rf"({re.escape(heading)}\n\n).*?(\n\n# )", flags=re.DOTALL)
    return pattern.sub(lambda match: f"{match.group(1)}{content}{match.group(2)}", text, count=1)


def set_agent_actions(text: str, latest_action: str, stable: str, stability: str) -> str:
    block = f"Agent 当前建议：`{latest_action}`\n\nAgent 稳定建议：`{stable}`（{stability}）"
    pattern = re.compile(r"Agent (?:建议动作|当前建议)：`[^`]+`(?:\n\nAgent 稳定建议：`[^`]+`（[^）]+）)?")
    if pattern.search(text):
        return pattern.sub(block, text, count=1)
    return text.replace("\n# 原始来源", f"\n{block}\n\n# 原始来源", 1)


def set_analysis_line(text: str, key: str, value: str) -> str:
    pattern = re.compile(rf"^- {re.escape(key)}:.*$", flags=re.MULTILINE)
    replacement = f"- {key}: {value}"
    if pattern.search(text):
        return pattern.sub(replacement, text, count=1)
    return text.replace("- captured_date:", f"{replacement}\n- captured_date:", 1)


def set_history(text: str, observations: list[Observation]) -> str:
    history = render_history(observations)
    pattern = re.compile(r"# Agent 判断历史\n\n.*?(?=\n\n# |\Z)", flags=re.DOTALL)
    if pattern.search(text):
        return pattern.sub(history, text, count=1)
    return text.rstrip() + "\n\n" + history + "\n"


def observation_for_item(item: dict[str, Any]) -> Observation | None:
    semantic = item.get("semantic_analysis") if isinstance(item.get("semantic_analysis"), dict) else {}
    if not semantic:
        return None
    return Observation(
        run_at=str(item.get("_analysis_run_at") or now_iso()),
        action=str(item.get("ai_suggested_action") or semantic.get("suggested_action") or "review"),
        confidence=str(semantic.get("confidence", "0.5")),
    )


def refresh_pending_candidate(path: Path, item: dict[str, Any], dry_run: bool = False) -> bool:
    semantic = item.get("semantic_analysis") if isinstance(item.get("semantic_analysis"), dict) else {}
    if not semantic:
        return False
    text = path.read_text(encoding="utf-8")
    meta, _ = extract_frontmatter(text)
    if meta.get("status", "pending-review") != "pending-review":
        return False
    latest = observation_for_item(item)
    if latest is None:
        return False
    observations = parse_observations(text)
    if not observations and meta.get("ai_suggested_action"):
        observations = [
            Observation(
                run_at=meta.get("captured_at", "legacy"),
                action=meta.get("ai_suggested_action", "review"),
                confidence=meta.get("ai_confidence", "0.5"),
            )
        ]
    observations = with_observation(observations, latest.run_at, latest.action, latest.confidence)
    stable, stability = stable_action(observations, meta.get("stable_ai_action", "review"))
    updated = set_frontmatter_value(text, "ai_suggested_action", latest.action)
    updated = set_frontmatter_value(updated, "ai_confidence", latest.confidence)
    updated = set_frontmatter_value(updated, "stable_ai_action", stable)
    updated = set_frontmatter_value(updated, "ai_action_stability", stability)
    updated = set_frontmatter_value(updated, "ai_observation_count", str(len(observations)))
    updated = update_section(updated, "# 为什么值得关注", str(semantic.get("learning_value", "")).strip())
    updated = update_section(updated, "# 和现有知识库的关系", f"- {semantic.get('vault_relationship', '')}".strip())
    updated = set_agent_actions(updated, latest.action, stable, stability)
    updated = set_analysis_line(updated, "semantic_topic", str(semantic.get("semantic_topic", "")))
    updated = set_analysis_line(updated, "ai_reason", str(semantic.get("reason", "")))
    updated = set_history(updated, observations)
    if updated == text:
        return False
    write_text(path, updated, dry_run=dry_run)
    return True


def candidate_text(item: dict[str, Any], date_str: str) -> str:
    title = item.get("title", "Untitled")
    semantic = item.get("semantic_analysis") if isinstance(item.get("semantic_analysis"), dict) else {}
    learning_value = item.get("ai_learning_value") or semantic.get("learning_value") or item.get("classification_reason", "")
    vault_relationship = item.get("ai_vault_relationship") or semantic.get("vault_relationship") or f"建议先放入 `{item.get('topic', 'Others')}` 候选池，后续由人工判断是否合入正式专题。"
    suggested_action = item.get("ai_suggested_action") or semantic.get("suggested_action") or "review"
    ai_reason = item.get("ai_reason") or semantic.get("reason") or item.get("classification_reason", "")
    observation = observation_for_item(item)
    observations = [observation] if observation else []
    stable, stability = stable_action(observations)
    return "\n".join(
        [
            "---",
            f"title: {title}",
            "type: candidate-note",
            "status: pending-review",
            f"topic: {item.get('topic', 'Others')}",
            f"source: {item.get('source_name', '')}",
            f"source_url: {item.get('url', '')}",
            f"published_at: {item.get('published_at', '')}",
            f"captured_at: {now_iso()}",
            f"importance_score: {item.get('importance_score', 1)}",
            f"ai_suggested_action: {suggested_action}",
            f"ai_confidence: {semantic.get('confidence', '')}",
            f"stable_ai_action: {stable}",
            f"ai_action_stability: {stability}",
            f"ai_observation_count: {len(observations)}",
            "---",
            "",
            "# 这是什么",
            "",
            clamp(item.get("summary") or item.get("raw_text") or "外部来源条目，等待人工 review。", 500),
            "",
            "# 为什么值得关注",
            "",
            learning_value or "规则分类认为该条目和当前专题有关。",
            "",
            "# 和现有知识库的关系",
            "",
            f"- {vault_relationship}",
            "",
            "# 建议进入哪个专题",
            "",
            f"- {item.get('topic', 'Others')}",
            "",
            "# 建议动作",
            "",
            "- [ ] 忽略",
            "- [ ] 加入学习队列",
            "- [ ] 合入正式专题",
            "- [ ] 生成 Playbook",
            "- [ ] 生成对比表",
            "",
            f"Agent 当前建议：`{suggested_action}`",
            "",
            f"Agent 稳定建议：`{stable}`（{stability}）",
            "",
            "# 原始来源",
            "",
            f"- 来源：{item.get('source_name', '')}",
            f"- 链接：{item.get('url', '')}",
            f"- 发布时间：{item.get('published_at', '') or '未知'}",
            "",
            "# Agent 判断依据",
            "",
            f"- importance_score: {item.get('importance_score', 1)}",
            f"- topic_scores: {item.get('topic_scores', {})}",
            f"- semantic_topic: {semantic.get('semantic_topic', '')}",
            f"- ai_reason: {ai_reason}",
            f"- captured_date: {date_str}",
            "",
            render_history(observations) if observations else "# Agent 判断历史\n\n- 暂无语义分析观测。",
        ]
    )


def generate_candidates(input_path: Path, dry_run: bool = False, date_str: str | None = None) -> list[Path]:
    root = repo_root()
    router = load_yaml(root / "90-Agent-System/topic-router.yaml")
    topics = router.get("topics", {})
    default_topic = router.get("default_topic", "Others")
    payload = read_json(input_path)
    raw_items = payload.get("items", []) if isinstance(payload, dict) else payload
    run_at = payload.get("generated_at", now_iso()) if isinstance(payload, dict) else now_iso()
    items = [dict(item, _analysis_run_at=run_at) for item in raw_items if isinstance(item, dict) and int(item.get("importance_score", 1)) >= 3]
    output_date = date_str or today_str()
    written: list[Path] = []
    refreshed = 0
    for item in items:
        topic = item.get("topic", default_topic)
        output_dir = root / topics.get(topic, {}).get("output_dir", f"00-Agent-Inbox/Candidates/{topic}")
        existing = existing_candidates(output_dir) if output_dir.exists() else {}
        existing_path = existing.get(item.get("url", ""))
        if existing_path:
            if refresh_pending_candidate(existing_path, item, dry_run=dry_run):
                refreshed += 1
                safe_print(f"[candidates] refreshed AI triage: {existing_path.relative_to(root)}")
            else:
                safe_print(f"[candidates] skip existing URL: {item.get('url')}")
            continue
        output = output_dir / f"{output_date}-{slugify(item.get('title', 'untitled'))}.md"
        if output.exists():
            safe_print(f"[candidates] skip existing file: {output.relative_to(root)}")
            continue
        write_text(output, candidate_text(item, output_date), dry_run=dry_run)
        written.append(output)
    safe_print(f"[candidates] created={len(written)} refreshed={refreshed}")
    return written


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None)
    parser.add_argument("--input", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    root = repo_root()
    date_str = args.date or today_str()
    input_path = Path(args.input) if args.input else root / f"90-Agent-System/logs/classified-items-{date_str}.json"
    if not input_path.is_absolute():
        input_path = root / input_path
    generate_candidates(input_path, dry_run=args.dry_run, date_str=date_str)


if __name__ == "__main__":
    main()
