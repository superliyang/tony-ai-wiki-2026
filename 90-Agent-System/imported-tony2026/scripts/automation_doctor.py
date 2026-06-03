from __future__ import annotations

import argparse
import importlib.util
import os
import platform
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import feedparser

from utils import http_get, load_local_env, load_yaml, now_iso, relative_to_repo, repo_root, safe_print, today_str, write_text


@dataclass
class Check:
    name: str
    status: str
    detail: str


def ok(name: str, detail: str) -> Check:
    return Check(name, "ok", detail)


def warn(name: str, detail: str) -> Check:
    return Check(name, "warning", detail)


def fail(name: str, detail: str) -> Check:
    return Check(name, "failed", detail)


def check_python_packages() -> list[Check]:
    packages = ["yaml", "feedparser", "requests", "lark_oapi"]
    checks: list[Check] = []
    for package in packages:
        checks.append(ok(f"python package: {package}", "installed") if importlib.util.find_spec(package) else fail(f"python package: {package}", "missing"))
    return checks


def check_env() -> list[Check]:
    load_local_env()

    required_for_active = [
        ("FEISHU_WEBHOOK_URL", "Feishu active push"),
        ("FEISHU_APP_ID", "Feishu WebSocket bot"),
        ("FEISHU_APP_SECRET", "Feishu WebSocket bot"),
        ("DEEPSEEK_API_KEY", "DeepSeek semantic analysis"),
    ]
    checks = [ok(f"env: {name}", f"configured for {purpose}") if os.getenv(name) else warn(f"env: {name}", f"missing; {purpose} may be disabled") for name, purpose in required_for_active]
    checks.append(ok("env: GITHUB_TOKEN", "configured for GitHub API rate limit") if os.getenv("GITHUB_TOKEN") else warn("env: GITHUB_TOKEN", "missing; GitHub release sources may hit anonymous API rate limits"))
    return checks


def check_directories() -> list[Check]:
    root = repo_root()
    required = [
        "00-Agent-Inbox/Daily-Digests",
        "00-Agent-Inbox/Weekly-Digests",
        "00-Agent-Inbox/Candidates",
        "00-Agent-Inbox/Decision-Board",
        "00-Agent-Inbox/Review-Queue",
        "00-Agent-Inbox/Review-Queue/Merge-Executions",
        "00-Agent-Inbox/Study-Queue",
        "90-Agent-System/logs",
        "90-Agent-System/reports",
    ]
    return [ok(f"directory: {path}", "exists") if (root / path).exists() else fail(f"directory: {path}", "missing") for path in required]


def validate_sources_schema() -> list[Check]:
    root = repo_root()
    config = load_yaml(root / "90-Agent-System/sources.yaml")
    checks: list[Check] = []
    source_ids: set[str] = set()
    supported = {"rss", "url", "manual_urls", "github_trending", "github_releases", "cisa_kev"}
    for source in config.get("sources", []):
        source_id = str(source.get("id", ""))
        if not source_id:
            checks.append(fail("source schema", "source without id"))
            continue
        if source_id in source_ids:
            checks.append(fail(f"source: {source_id}", "duplicate id"))
        source_ids.add(source_id)
        source_type = source.get("type")
        if source_type not in supported:
            checks.append(fail(f"source: {source_id}", f"unsupported type: {source_type}"))
        elif source_type in {"rss", "url", "cisa_kev"} and not source.get("url"):
            checks.append(fail(f"source: {source_id}", "missing url"))
        elif source_type == "manual_urls" and not source.get("path"):
            checks.append(fail(f"source: {source_id}", "missing path"))
        elif source_type == "github_releases" and "/" not in str(source.get("repo", "")):
            checks.append(fail(f"source: {source_id}", "missing repo owner/name"))
        else:
            checks.append(ok(f"source: {source_id}", f"type={source_type} enabled={bool(source.get('enabled', False))}"))
    return checks


def check_source_network() -> list[Check]:
    root = repo_root()
    config = load_yaml(root / "90-Agent-System/sources.yaml")
    checks: list[Check] = []
    for source in config.get("sources", []):
        if not source.get("enabled", False):
            continue
        source_id = source["id"]
        source_type = source["type"]
        try:
            if source_type == "rss":
                response = http_get(source["url"], timeout=15, retries=2)
                parsed = feedparser.parse(response.content)
                detail = f"entries={len(parsed.entries)}"
                checks.append(ok(f"source network: {source_id}", detail) if parsed.entries else warn(f"source network: {source_id}", "reachable but no entries"))
            elif source_type == "url":
                response = http_get(source["url"], timeout=15, retries=2)
                checks.append(ok(f"source network: {source_id}", f"http={response.status_code} bytes={len(response.text)}"))
            elif source_type == "manual_urls":
                path = root / source.get("path", "")
                checks.append(ok(f"source network: {source_id}", f"inbox={path.relative_to(root)}") if path.exists() else warn(f"source network: {source_id}", f"inbox missing: {path.relative_to(root)}"))
            elif source_type == "github_trending":
                language = str(source.get("language", "")).strip("/")
                since = source.get("since", "daily")
                url = f"https://github.com/trending/{language}?since={since}" if language else f"https://github.com/trending?since={since}"
                response = http_get(url, timeout=15, retries=2)
                checks.append(ok(f"source network: {source_id}", f"http={response.status_code} bytes={len(response.text)}"))
            elif source_type == "github_releases":
                repo = source["repo"]
                headers = {"Accept": "application/vnd.github+json"}
                token = os.getenv("GITHUB_TOKEN")
                if token:
                    headers["Authorization"] = f"Bearer {token}"
                response = http_get(f"https://api.github.com/repos/{repo}/releases", timeout=15, retries=2, headers=headers)
                data = response.json()
                checks.append(ok(f"source network: {source_id}", f"releases={len(data) if isinstance(data, list) else 0}"))
            elif source_type == "cisa_kev":
                response = http_get(source["url"], timeout=15, retries=2)
                data = response.json()
                vulnerabilities = data.get("vulnerabilities", []) if isinstance(data, dict) else []
                checks.append(ok(f"source network: {source_id}", f"vulnerabilities={len(vulnerabilities)}"))
        except Exception as exc:
            detail = str(exc)
            if source_type == "github_releases" and ("rate limit" in detail.lower() or "403" in detail):
                checks.append(warn(f"source network: {source_id}", f"{detail}; configure GITHUB_TOKEN for stable release polling"))
            elif source.get("priority") != "high":
                checks.append(warn(f"source network: {source_id}", f"{detail}; non-critical source degraded"))
            else:
                checks.append(fail(f"source network: {source_id}", detail))
    return checks


def check_launchd() -> list[Check]:
    if platform.system() != "Darwin":
        return [warn("launchd", "not macOS; skipped")]
    try:
        result = subprocess.run(["launchctl", "list"], check=False, capture_output=True, text=True, timeout=10)
    except Exception as exc:
        return [warn("launchd", f"unable to inspect: {exc}")]
    checks: list[Check] = []
    for label in [
        "com.tony2026.knowledge-feishu-bot",
        "com.tony2026.knowledge-daily",
        "com.tony2026.knowledge-weekly",
        "com.tony2026.knowledge-recovery",
    ]:
        line = next((line for line in result.stdout.splitlines() if label in line), "")
        if not line:
            checks.append(warn(f"launchd: {label}", "not loaded"))
        else:
            checks.append(ok(f"launchd: {label}", line.strip()))
    return checks


def render_report(checks: list[Check], network: bool) -> str:
    failed = sum(1 for check in checks if check.status == "failed")
    warnings = sum(1 for check in checks if check.status == "warning")
    lines = [
        "---",
        f"title: Automation Doctor - {today_str()}",
        "type: automation-doctor-report",
        f"status: {'failed' if failed else 'passed'}",
        f"network_checks: {str(network).lower()}",
        f"generated_at: {now_iso()}",
        "---",
        "",
        f"# Automation Doctor - {today_str()}",
        "",
        "## 总览",
        "",
        f"- failed: {failed}",
        f"- warnings: {warnings}",
        f"- checks: {len(checks)}",
        "",
        "## 检查项",
        "",
        "| status | check | detail |",
        "| --- | --- | --- |",
    ]
    for check in checks:
        lines.append(f"| {check.status} | {check.name} | {check.detail.replace('|', '/')} |")
    lines.extend(
        [
            "",
            "## 建议",
            "",
            "- `failed=0` 才适合认为自动化环境可稳定运行。",
            "- warning 不一定阻塞运行，但应该进入后续优化清单。",
            "- 如果 source network 失败，优先判断是信息源失效、网络抖动，还是本地 TLS / DNS 问题。",
        ]
    )
    return "\n".join(lines)


def run_doctor(network: bool = False, dry_run: bool = False) -> Path:
    checks: list[Check] = []
    checks.extend(check_python_packages())
    checks.extend(check_env())
    checks.extend(check_directories())
    checks.extend(validate_sources_schema())
    checks.extend(check_launchd())
    if network:
        checks.extend(check_source_network())
    output = repo_root() / f"90-Agent-System/reports/automation-doctor-{today_str()}.md"
    actual_output = write_text(output, render_report(checks, network), dry_run=dry_run)
    failed = sum(1 for check in checks if check.status == "failed")
    warnings = sum(1 for check in checks if check.status == "warning")
    safe_print(f"[doctor] failed={failed} warnings={warnings} output={relative_to_repo(output)}")
    return actual_output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--network", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    run_doctor(network=args.network, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
