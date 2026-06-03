from __future__ import annotations

import argparse
import os
from pathlib import Path

import requests

from notify_feishu import summarize_markdown
from utils import load_local_env, load_yaml, repo_root, safe_print


def notify(file_path: Path, dry_run: bool = False) -> bool:
    load_local_env()
    root = repo_root()
    config = load_yaml(root / "90-Agent-System/notification.yaml").get("wecom", {})
    content = summarize_markdown(file_path, int(config.get("max_items", 5)))
    webhook_env = config.get("webhook_url_env", "WECOM_WEBHOOK_URL")
    webhook = os.getenv(webhook_env, "")
    if dry_run:
        safe_print("[notify:wecom] dry-run message:")
        safe_print(content)
        return True
    if not config.get("enabled", False):
        safe_print("[notify:wecom] disabled in notification.yaml")
        return False
    if not webhook:
        safe_print(f"WARNING: {webhook_env} is not configured; skip WeCom notification")
        return False
    response = requests.post(webhook, json={"msgtype": "markdown", "markdown": {"content": content}}, timeout=20)
    if response.status_code >= 400:
        safe_print(f"WARNING: WeCom notification failed with HTTP {response.status_code}")
        return False
    safe_print("[notify:wecom] sent")
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
