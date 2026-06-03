from __future__ import annotations

import argparse
import html
import os
import re
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any

import feedparser

from utils import clamp, http_get, load_yaml, now_iso, read_json, relative_to_repo, repo_root, safe_print, today_str, write_json


def parse_entry_datetime(entry: Any) -> str:
    for key in ("published", "updated", "created"):
        value = getattr(entry, key, None) or entry.get(key) if isinstance(entry, dict) else None
        if value:
            try:
                parsed = parsedate_to_datetime(value)
                if parsed.tzinfo is None:
                    parsed = parsed.replace(tzinfo=timezone.utc)
                return parsed.astimezone(timezone.utc).replace(microsecond=0).isoformat()
            except Exception:
                return str(value)
    return ""


def clean_html(text: str) -> str:
    without_tags = re.sub(r"<[^>]+>", " ", text or "")
    return html.unescape(re.sub(r"\s+", " ", without_tags)).strip()


def in_window(published_at: str, days: int) -> bool:
    if not published_at:
        return True
    try:
        parsed = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
    except ValueError:
        return True
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed >= datetime.now(timezone.utc) - timedelta(days=days)


def collect_rss(source: dict[str, Any], days: int) -> tuple[list[dict[str, Any]], list[str]]:
    warnings: list[str] = []
    items: list[dict[str, Any]] = []
    try:
        response = http_get(source["url"], timeout=20)
    except Exception as exc:
        return [], [f"{source['id']}: RSS fetch failed: {exc}"]
    parsed = feedparser.parse(response.content)
    if getattr(parsed, "bozo", False):
        warnings.append(f"{source['id']}: RSS parse warning: {getattr(parsed, 'bozo_exception', 'unknown')}")
    for entry in parsed.entries:
        published_at = parse_entry_datetime(entry)
        if not in_window(published_at, days):
            continue
        title = clean_html(entry.get("title", "Untitled"))
        summary = clean_html(entry.get("summary", entry.get("description", "")))
        url = entry.get("link", source["url"])
        items.append(
            {
                "source_id": source["id"],
                "source_name": source["name"],
                "source_type": source["type"],
                "source_priority": source.get("priority", "medium"),
                "title": title,
                "url": url,
                "published_at": published_at,
                "summary": clamp(summary, 800),
                "raw_text": clamp(summary, 1600),
                "fetched_at": now_iso(),
            }
        )
    return items, warnings


def collect_url(source: dict[str, Any]) -> tuple[list[dict[str, Any]], list[str]]:
    warnings: list[str] = []
    try:
        response = http_get(source["url"], timeout=20)
    except Exception as exc:
        return [], [f"{source['id']}: URL fetch failed: {exc}"]
    text = response.text
    title_match = re.search(r"<title[^>]*>(.*?)</title>", text, flags=re.IGNORECASE | re.DOTALL)
    title = clean_html(title_match.group(1)) if title_match else source["name"]
    raw_text = clean_html(text)
    if not raw_text:
        warnings.append(f"{source['id']}: URL fetched but no readable text extracted")
    return [
        {
            "source_id": source["id"],
            "source_name": source["name"],
            "source_type": source["type"],
            "source_priority": source.get("priority", "medium"),
            "title": title,
            "url": source["url"],
            "published_at": "",
            "summary": clamp(raw_text, 800),
            "raw_text": clamp(raw_text, 2000),
            "fetched_at": now_iso(),
        }
    ], warnings


def item_from_url(source: dict[str, Any], url: str, extra_summary: str = "") -> tuple[dict[str, Any] | None, list[str]]:
    try:
        response = http_get(url, timeout=20)
    except Exception as exc:
        return None, [f"{source['id']}: URL fetch failed for {url}: {exc}"]
    text = response.text
    title_match = re.search(r"<title[^>]*>(.*?)</title>", text, flags=re.IGNORECASE | re.DOTALL)
    title = clean_html(title_match.group(1)) if title_match else url
    raw_text = clean_html(text)
    summary = extra_summary or raw_text
    return {
        "source_id": source["id"],
        "source_name": source["name"],
        "source_type": source["type"],
        "source_priority": source.get("priority", "medium"),
        "title": title,
        "url": url,
        "published_at": "",
        "summary": clamp(summary, 800),
        "raw_text": clamp(raw_text or summary, 2000),
        "fetched_at": now_iso(),
    }, []


def collect_manual_urls(source: dict[str, Any]) -> tuple[list[dict[str, Any]], list[str]]:
    root = repo_root()
    path = root / source.get("path", "00-Agent-Inbox/Manual-URLs/inbox.md")
    if not path.exists():
        return [], [f"{source['id']}: manual URL inbox not found: {relative_to_repo(path)}"]
    text = path.read_text(encoding="utf-8")
    urls = []
    for match in re.finditer(r"https?://[^\s)>\]]+", text):
        url = match.group(0).rstrip(".,;")
        line_start = text.rfind("\n", 0, match.start()) + 1
        line_end = text.find("\n", match.end())
        line = text[line_start : line_end if line_end != -1 else len(text)].strip()
        if "[x]" in line.lower() or "status: done" in line.lower():
            continue
        urls.append((url, line))
    items: list[dict[str, Any]] = []
    warnings: list[str] = []
    seen: set[str] = set()
    for url, line in urls[: int(source.get("limit", 20))]:
        if url in seen:
            continue
        seen.add(url)
        item, item_warnings = item_from_url(source, url, extra_summary=clean_html(line))
        warnings.extend(item_warnings)
        if item:
            items.append(item)
    return items, warnings


def collect_github_trending(source: dict[str, Any]) -> tuple[list[dict[str, Any]], list[str]]:
    language = str(source.get("language", "")).strip("/")
    since = source.get("since", "daily")
    url = f"https://github.com/trending/{language}?since={since}" if language else f"https://github.com/trending?since={since}"
    try:
        response = http_get(url, timeout=20)
    except Exception as exc:
        cached = cached_source_items(source["id"], days=7)
        if cached:
            return cached, [f"{source['id']}: GitHub Trending fetch failed, using cached items from previous logs: {exc}"]
        return [], [f"{source['id']}: GitHub Trending fetch failed: {exc}"]
    articles = re.findall(r"<article\b.*?</article>", response.text, flags=re.IGNORECASE | re.DOTALL)
    items: list[dict[str, Any]] = []
    for article in articles[: int(source.get("limit", 10))]:
        repo_match = re.search(r'<h2[^>]*>.*?<a[^>]+href="(/[^"/]+/[^"/]+)"', article, flags=re.IGNORECASE | re.DOTALL)
        if not repo_match:
            continue
        repo_path = clean_html(repo_match.group(1)).strip("/")
        description_match = re.search(r'<p[^>]*class="[^"]*col-9[^"]*"[^>]*>(.*?)</p>', article, flags=re.IGNORECASE | re.DOTALL)
        description = clean_html(description_match.group(1)) if description_match else ""
        stars_today_match = re.search(r"([\d,]+)\s+stars?\s+today", clean_html(article), flags=re.IGNORECASE)
        stars_today = stars_today_match.group(1) if stars_today_match else ""
        summary = description
        if stars_today:
            summary = f"{description} Trending signal: {stars_today} stars today."
        items.append(
            {
                "source_id": source["id"],
                "source_name": source["name"],
                "source_type": source["type"],
                "source_priority": source.get("priority", "medium"),
                "title": repo_path,
                "url": f"https://github.com/{repo_path}",
                "published_at": now_iso(),
                "summary": clamp(summary, 800),
                "raw_text": clamp(clean_html(article), 2000),
                "fetched_at": now_iso(),
            }
        )
    if not items:
        return [], [f"{source['id']}: GitHub Trending fetched but no repositories parsed"]
    return items, []


def collect_github_releases(source: dict[str, Any], days: int) -> tuple[list[dict[str, Any]], list[str]]:
    repo = source.get("repo", "")
    if not repo or "/" not in repo:
        return [], [f"{source['id']}: github_releases requires repo owner/name"]
    url = f"https://api.github.com/repos/{repo}/releases"
    headers = {"Accept": "application/vnd.github+json"}
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        response = http_get(url, timeout=20, headers=headers)
    except Exception as exc:
        cached = cached_source_items(source["id"], days)
        if cached:
            return cached, [f"{source['id']}: GitHub releases fetch failed, using cached items from previous logs: {exc}"]
        return [], [f"{source['id']}: GitHub releases fetch failed: {exc}"]
    items: list[dict[str, Any]] = []
    for release in response.json()[: int(source.get("limit", 10))]:
        published_at = release.get("published_at") or release.get("created_at") or ""
        if not in_window(published_at, days):
            continue
        title = release.get("name") or release.get("tag_name") or "Untitled release"
        body = clean_html(release.get("body") or "")
        items.append(
            {
                "source_id": source["id"],
                "source_name": source["name"],
                "source_type": source["type"],
                "source_priority": source.get("priority", "medium"),
                "title": title,
                "url": release.get("html_url") or f"https://github.com/{repo}/releases",
                "published_at": published_at,
                "summary": clamp(body, 800),
                "raw_text": clamp(body, 2000),
                "fetched_at": now_iso(),
            }
        )
    return items, []


def collect_cisa_kev(source: dict[str, Any], days: int) -> tuple[list[dict[str, Any]], list[str]]:
    url = source.get("url", "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json")
    try:
        response = http_get(url, timeout=20)
    except Exception as exc:
        cached = cached_source_items(source["id"], days)
        if cached:
            return cached, [f"{source['id']}: CISA KEV fetch failed, using cached items from previous logs: {exc}"]
        return [], [f"{source['id']}: CISA KEV fetch failed: {exc}"]
    data = response.json()
    vulnerabilities = data.get("vulnerabilities", []) if isinstance(data, dict) else []
    items: list[dict[str, Any]] = []
    for vuln in vulnerabilities[: int(source.get("limit", 50))]:
        if not isinstance(vuln, dict):
            continue
        date_added = vuln.get("dateAdded", "")
        if not in_window(date_added, days):
            continue
        cve = vuln.get("cveID", "CVE")
        vendor = vuln.get("vendorProject", "")
        product = vuln.get("product", "")
        name = vuln.get("vulnerabilityName", "")
        title = f"{cve} - {vendor} {product}".strip()
        summary = " ".join(
            part
            for part in [
                name,
                vuln.get("shortDescription", ""),
                f"Required action: {vuln.get('requiredAction', '')}" if vuln.get("requiredAction") else "",
                f"Known ransomware use: {vuln.get('knownRansomwareCampaignUse', '')}" if vuln.get("knownRansomwareCampaignUse") else "",
            ]
            if part
        )
        items.append(
            {
                "source_id": source["id"],
                "source_name": source["name"],
                "source_type": source["type"],
                "source_priority": source.get("priority", "high"),
                "title": title,
                "url": vuln.get("notes") or "https://www.cisa.gov/known-exploited-vulnerabilities-catalog",
                "published_at": date_added,
                "summary": clamp(summary, 800),
                "raw_text": clamp(summary, 2000),
                "fetched_at": now_iso(),
            }
        )
    return items, []


def cached_source_items(source_id: str, days: int, limit: int = 20) -> list[dict[str, Any]]:
    root = repo_root()
    cached: list[dict[str, Any]] = []
    for path in sorted((root / "90-Agent-System/logs").glob("source-items-*.json"), key=lambda item: item.stat().st_mtime, reverse=True):
        try:
            data = read_json(path, {})
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        for item in data.get("items", []):
            if not isinstance(item, dict) or item.get("source_id") != source_id:
                continue
            if not in_window(str(item.get("published_at", "")), days):
                continue
            enriched = dict(item)
            enriched["cache_fallback"] = True
            enriched["cache_source_log"] = relative_to_repo(path)
            cached.append(enriched)
            if len(cached) >= limit:
                return cached
        if cached:
            return cached
    return cached


def collect_sources(days: int, dry_run: bool = False, date_str: str | None = None) -> Path:
    root = repo_root()
    config = load_yaml(root / "90-Agent-System/sources.yaml")
    output_date = date_str or today_str()
    output = root / f"90-Agent-System/logs/source-items-{output_date}.json"
    all_items: list[dict[str, Any]] = []
    warnings: list[str] = []
    seen: set[tuple[str, str]] = set()

    for source in config.get("sources", []):
        if not source.get("enabled", False):
            continue
        safe_print(f"[collect] {source['id']} ({source['type']})")
        try:
            if source["type"] == "rss":
                items, source_warnings = collect_rss(source, days)
            elif source["type"] == "url":
                items, source_warnings = collect_url(source)
            elif source["type"] == "manual_urls":
                items, source_warnings = collect_manual_urls(source)
            elif source["type"] == "github_trending":
                items, source_warnings = collect_github_trending(source)
            elif source["type"] == "github_releases":
                items, source_warnings = collect_github_releases(source, days)
            elif source["type"] == "cisa_kev":
                items, source_warnings = collect_cisa_kev(source, days)
            else:
                items, source_warnings = [], [f"{source['id']}: unsupported type {source.get('type')}"]
        except Exception as exc:
            items, source_warnings = [], [f"{source['id']}: unexpected failure: {exc}"]
        warnings.extend(source_warnings)
        for item in items:
            key = (item.get("title", ""), item.get("url", ""))
            if key in seen:
                continue
            seen.add(key)
            all_items.append(item)

    payload = {"generated_at": now_iso(), "days": days, "warnings": warnings, "items": all_items}
    actual_output = write_json(output, payload, dry_run=dry_run)
    safe_print(f"[collect] items={len(all_items)} warnings={len(warnings)} output={output.relative_to(root)}")
    for warning in warnings:
        safe_print(f"WARNING: {warning}")
    return actual_output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=1, choices=[1, 7, 30])
    parser.add_argument("--date", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    collect_sources(args.days, dry_run=args.dry_run, date_str=args.date)


if __name__ == "__main__":
    main()
