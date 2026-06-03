from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import os
import time
from pathlib import Path
from typing import Any

from utils import clamp, http_post, load_local_env, load_yaml, relative_to_repo, repo_root, safe_print


def summarize_markdown(path: Path, max_items: int = 5) -> str:
    text = path.read_text(encoding="utf-8")
    title = next((line.lstrip("# ").strip() for line in text.splitlines() if line.startswith("# ")), path.name)
    bullets = [line for line in text.splitlines() if line.startswith("- ")][:max_items]
    body = "\n".join(bullets)
    return clamp(f"{title}\n\n{body}\n\n文件：{relative_to_repo(path)}", 1800)


def sign(secret: str, timestamp: str) -> str:
    string_to_sign = f"{timestamp}\n{secret}".encode("utf-8")
    digest = hmac.new(string_to_sign, b"", digestmod=hashlib.sha256).digest()
    return base64.b64encode(digest).decode("utf-8")


def notify(file_path: Path, dry_run: bool = False) -> bool:
    load_local_env()
    root = repo_root()
    config = load_yaml(root / "90-Agent-System/notification.yaml").get("feishu", {})
    content = summarize_markdown(file_path, int(config.get("max_items", 5)))
    webhook_env = config.get("webhook_url_env", "FEISHU_WEBHOOK_URL")
    secret_env = config.get("secret_env", "FEISHU_WEBHOOK_SECRET")
    webhook = os.getenv(webhook_env, "")
    secret = os.getenv(secret_env, "")
    if dry_run:
        safe_print("[notify:feishu] dry-run message:")
        safe_print(content)
        return True
    if not config.get("enabled", False):
        safe_print("[notify:feishu] disabled in notification.yaml")
        return False
    if not webhook:
        safe_print(f"WARNING: {webhook_env} is not configured; skip Feishu notification")
        return False
    payload: dict[str, Any] = {"msg_type": "text", "content": {"text": content}}
    if secret:
        timestamp = str(int(time.time()))
        payload["timestamp"] = timestamp
        payload["sign"] = sign(secret, timestamp)
    try:
        http_post(webhook, payload, timeout=20)
    except Exception as exc:
        safe_print(f"WARNING: Feishu notification failed: {exc}")
        return False
    safe_print("[notify:feishu] sent")
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
