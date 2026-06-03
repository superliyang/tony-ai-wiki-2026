from __future__ import annotations

import json
import os
import re
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import requests
import yaml


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def ensure_dir(path: Path | str) -> Path:
    target = Path(path)
    target.mkdir(parents=True, exist_ok=True)
    return target


def load_yaml(path: Path | str) -> dict[str, Any]:
    target = Path(path)
    if not target.exists():
        raise FileNotFoundError(f"YAML config not found: {target}")
    with target.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    if not isinstance(data, dict):
        raise ValueError(f"YAML config must be a mapping: {target}")
    return data


def load_local_env() -> None:
    """Load local, ignored env files without overriding shell-provided values."""
    for path in [repo_root() / ".env", repo_root() / ".env.local", repo_root() / "90-Agent-System/.env.local"]:
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8") as fh:
            for line in fh:
                stripped = line.strip()
                if not stripped or stripped.startswith("#") or "=" not in stripped:
                    continue
                key, value = stripped.split("=", 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if key and key not in os.environ:
                    os.environ[key] = value


def write_json(path: Path | str, data: Any, dry_run: bool = False) -> Path:
    target = Path(path)
    original = target
    if dry_run:
        preview_root = os.getenv("KNOWLEDGE_DRY_RUN_DIR")
        if preview_root:
            target = Path(preview_root) / relative_to_repo(original)
        safe_print(f"[dry-run] would write JSON: {relative_to_repo(original)}")
    ensure_dir(target.parent)
    if dry_run and not os.getenv("KNOWLEDGE_DRY_RUN_DIR"):
        return target
    with target.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    return target


def read_json(path: Path | str, default: Any = None) -> Any:
    target = Path(path)
    if not target.exists():
        if default is not None:
            return default
        raise FileNotFoundError(f"JSON file not found: {target}")
    with target.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def write_text(path: Path | str, text: str, dry_run: bool = False) -> Path:
    target = Path(path)
    original = target
    if dry_run:
        preview_root = os.getenv("KNOWLEDGE_DRY_RUN_DIR")
        if preview_root:
            target = Path(preview_root) / relative_to_repo(original)
        safe_print(f"[dry-run] would write Markdown: {relative_to_repo(original)}")
    ensure_dir(target.parent)
    if dry_run and not os.getenv("KNOWLEDGE_DRY_RUN_DIR"):
        return target
    with target.open("w", encoding="utf-8") as fh:
        fh.write(text)
        if not text.endswith("\n"):
            fh.write("\n")
    return target


def slugify(text: str, max_length: int = 80) -> str:
    value = text.strip().lower()
    value = re.sub(r"https?://", "", value)
    value = re.sub(r"[^\w\u4e00-\u9fff]+", "-", value, flags=re.UNICODE)
    value = re.sub(r"-+", "-", value).strip("-")
    return (value[:max_length].strip("-") or "untitled")


def today_str() -> str:
    return date.today().isoformat()


def week_str(day: date | None = None) -> str:
    target = day or date.today()
    year, week, _ = target.isocalendar()
    return f"{year}-W{week:02d}"


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def safe_print(message: str) -> None:
    print(message, flush=True)


def extract_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 5 :]
    meta: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip().strip('"')
    return meta, body


def relative_to_repo(path: Path | str) -> str:
    target = Path(path)
    try:
        return str(target.resolve().relative_to(repo_root()))
    except ValueError:
        return str(target)


def parse_date(value: str | None) -> date:
    if not value:
        return date.today()
    return date.fromisoformat(value)


def parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    cleaned = value.strip()
    if not cleaned:
        return None
    try:
        if cleaned.endswith("Z"):
            cleaned = cleaned[:-1] + "+00:00"
        return datetime.fromisoformat(cleaned)
    except ValueError:
        return None


def clamp(text: str, limit: int) -> str:
    compact = re.sub(r"\s+", " ", text or "").strip()
    if len(compact) <= limit:
        return compact
    return compact[: limit - 3].rstrip() + "..."


def load_items(path: Path | str) -> list[dict[str, Any]]:
    data = read_json(path)
    if isinstance(data, dict) and "items" in data:
        items = data["items"]
    else:
        items = data
    if not isinstance(items, list):
        raise ValueError(f"Expected a JSON list or object with items: {path}")
    return [item for item in items if isinstance(item, dict)]


def env_flag(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def exit_with_error(message: str, code: int = 1) -> None:
    safe_print(f"ERROR: {message}")
    sys.exit(code)


DEFAULT_USER_AGENT = "Mozilla/5.0 (compatible; tony-vault-knowledge-agent/1.0; +https://github.com/tony-vault)"


def http_get(url: str, timeout: int = 20, retries: int = 3, backoff_seconds: float = 1.0, headers: dict[str, str] | None = None) -> requests.Response:
    merged_headers = {"User-Agent": DEFAULT_USER_AGENT}
    if headers:
        merged_headers.update(headers)
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=timeout, headers=merged_headers)
            response.raise_for_status()
            return response
        except requests.RequestException as exc:
            last_error = exc
            if attempt >= retries:
                break
            time.sleep(backoff_seconds * attempt)
    raise last_error or RuntimeError(f"GET failed: {url}")


def http_post(
    url: str,
    json_payload: Any,
    timeout: int = 20,
    retries: int = 3,
    backoff_seconds: float = 1.0,
    headers: dict[str, str] | None = None,
) -> requests.Response:
    merged_headers = {"User-Agent": DEFAULT_USER_AGENT}
    if headers:
        merged_headers.update(headers)
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            response = requests.post(url, json=json_payload, timeout=timeout, headers=merged_headers)
            response.raise_for_status()
            return response
        except requests.RequestException as exc:
            last_error = exc
            if attempt >= retries:
                break
            time.sleep(backoff_seconds * attempt)
    raise last_error or RuntimeError(f"POST failed: {url}")
