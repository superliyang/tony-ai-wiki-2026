from __future__ import annotations

import argparse
import os
from pathlib import Path
from urllib.parse import quote

import requests

from notify_feishu import summarize_markdown
from utils import load_local_env, load_yaml, repo_root, safe_print


def notify(file_path: Path, dry_run: bool = False) -> bool:
    load_local_env()
    root = repo_root()
    config = load_yaml(root / "90-Agent-System/notification.yaml").get("bark", {})
    content = summarize_markdown(file_path, 3)
    endpoint_env = config.get("endpoint_env", "BARK_ENDPOINT")
    endpoint = os.getenv(endpoint_env, "")
    if dry_run:
        safe_print("[notify:bark] dry-run message:")
        safe_print(content)
        return True
    if not config.get("enabled", False):
        safe_print("[notify:bark] disabled in notification.yaml")
        return False
    if not endpoint:
        safe_print(f"WARNING: {endpoint_env} is not configured; skip Bark notification")
        return False
    url = f"{endpoint.rstrip('/')}/{quote('Knowledge Digest')}/{quote(content[:900])}"
    response = requests.get(url, timeout=20)
    if response.status_code >= 400:
        safe_print(f"WARNING: Bark notification failed with HTTP {response.status_code}")
        return False
    safe_print("[notify:bark] sent")
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    path = Path(args.file)
    if not path.is_absolute():
        path = repo_root() / path
    notify(path, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
