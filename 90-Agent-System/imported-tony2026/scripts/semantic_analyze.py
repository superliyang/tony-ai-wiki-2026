from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

from utils import clamp, http_post, load_items, load_local_env, load_yaml, now_iso, relative_to_repo, repo_root, safe_print, today_str, write_json


def should_analyze(item: dict[str, Any], min_score: int) -> bool:
    try:
        score = int(item.get("importance_score", 1))
    except (TypeError, ValueError):
        score = 1
    return score >= min_score


def compact_item(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "title": item.get("title", ""),
        "url": item.get("url", ""),
        "source": item.get("source_name", ""),
        "rule_topic": item.get("topic", ""),
        "importance_score": item.get("importance_score", 1),
        "classification_reason": item.get("classification_reason", ""),
        "summary": clamp(item.get("summary") or item.get("raw_text") or "", 1000),
    }


def normalize_analysis(data: Any) -> dict[str, Any]:
    if not isinstance(data, dict):
        data = {}
    return {
        "semantic_topic": str(data.get("semantic_topic") or ""),
        "learning_value": str(data.get("learning_value") or ""),
        "vault_relationship": str(data.get("vault_relationship") or ""),
        "suggested_action": str(data.get("suggested_action") or "review"),
        "reason": str(data.get("reason") or ""),
        "confidence": data.get("confidence", 0.5),
    }


def call_deepseek(item: dict[str, Any], config: dict[str, Any], prompt: str) -> dict[str, Any]:
    api_key_env = config.get("api_key_env", "DEEPSEEK_API_KEY")
    api_key = os.getenv(api_key_env)
    if not api_key:
        raise RuntimeError(f"{api_key_env} is not configured")
    base_url = str(config.get("base_url", "https://api.deepseek.com")).rstrip("/")
    payload = {
        "model": config.get("model", "deepseek-chat"),
        "temperature": float(config.get("temperature", 0.2)),
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": "请分析这条候选信息，并只输出 JSON。\n\n" + json.dumps(compact_item(item), ensure_ascii=False, indent=2)},
        ],
    }
    response = http_post(
        f"{base_url}/chat/completions",
        payload,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        timeout=int(config.get("timeout_seconds", 45)),
    )
    content = response.json()["choices"][0]["message"]["content"]
    return normalize_analysis(json.loads(content))


def semantic_analyze(input_path: Path, dry_run: bool = False, date_str: str | None = None) -> Path:
    load_local_env()
    root = repo_root()
    config = load_yaml(root / "90-Agent-System/ai-analysis.yaml").get("semantic_analysis", {})
    key = date_str or input_path.stem.replace("classified-items-", "") or today_str()
    output = root / f"{config.get('output_dir', '90-Agent-System/logs')}/semantic-analysis-{key}.json"
    items = load_items(input_path)
    if not config.get("enabled", False):
        safe_print("[semantic] disabled")
        write_json(output, {"generated_at": now_iso(), "input": relative_to_repo(input_path), "items": items, "warnings": ["semantic analysis disabled"]}, dry_run=dry_run)
        return output

    prompt = (root / "90-Agent-System/prompts/semantic-classifier.md").read_text(encoding="utf-8")
    min_score = int(config.get("min_importance_score", 3))
    max_items = int(config.get("max_items", 8))
    analyzed = 0
    warnings: list[str] = []
    enriched: list[dict[str, Any]] = []

    for item in items:
        result = dict(item)
        if should_analyze(item, min_score) and analyzed < max_items:
            try:
                analysis = call_deepseek(item, config, prompt)
                result["semantic_analysis"] = analysis
                result["ai_learning_value"] = analysis["learning_value"]
                result["ai_vault_relationship"] = analysis["vault_relationship"]
                result["ai_suggested_action"] = analysis["suggested_action"]
                result["ai_reason"] = analysis["reason"]
                analyzed += 1
                safe_print(f"[semantic] analyzed: {item.get('title', 'Untitled')}")
            except Exception as exc:
                warning = f"{item.get('title', 'Untitled')}: {exc}"
                warnings.append(warning)
                result["semantic_analysis_error"] = str(exc)
                safe_print(f"WARNING: semantic analysis failed: {warning}")
        enriched.append(result)

    payload = {
        "generated_at": now_iso(),
        "provider": config.get("provider", "deepseek"),
        "model": config.get("model", "deepseek-chat"),
        "input": relative_to_repo(input_path),
        "analyzed_items": analyzed,
        "warnings": warnings,
        "items": enriched,
    }
    actual_output = write_json(output, payload, dry_run=dry_run)
    safe_print(f"[semantic] analyzed={analyzed} warnings={len(warnings)} output={relative_to_repo(output)}")
    return actual_output


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
    semantic_analyze(input_path, dry_run=args.dry_run, date_str=date_str)


if __name__ == "__main__":
    main()
