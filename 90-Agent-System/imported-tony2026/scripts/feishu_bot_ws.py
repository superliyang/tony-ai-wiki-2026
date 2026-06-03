from __future__ import annotations

import argparse
import re
from pathlib import Path

from agent_ops import run_ops
from curator_merge_execute import execute_ready_candidate, generate_execution_preview
from curator_merge_plan import generate_merge_plan
from generate_decision_board import generate_decision_board
from knowledge_daily import run_daily
from knowledge_weekly import run_weekly
from notify_feishu import summarize_markdown
from review_queue import decide, format_review, review_items, write_review_queue
from utils import load_local_env, load_yaml, now_iso, repo_root, safe_print


def latest_markdown(folder: Path) -> Path | None:
    files = sorted(folder.glob("*.md"), key=lambda path: path.stat().st_mtime, reverse=True)
    return files[0] if files else None


ACTION_ALIASES = {
    "study": "study",
    "queue": "study",
    "learn": "study",
    "学习": "study",
    "加入学习": "study",
    "加入学习队列": "study",
    "ignore": "ignore",
    "discard": "ignore",
    "drop": "ignore",
    "忽略": "ignore",
    "丢弃": "ignore",
    "放弃": "ignore",
    "keep": "keep",
    "保留": "keep",
    "暂存": "keep",
    "merge": "merge",
    "curate": "merge",
    "合入": "merge",
    "准备合入": "merge",
}


def parse_decision_intent(text: str) -> tuple[int, str] | None:
    cleaned = text.strip().lower()
    if not cleaned:
        return None
    compact = re.sub(r"\s+", "", cleaned)

    for action_text, action in ACTION_ALIASES.items():
        action_compact = re.sub(r"\s+", "", action_text.lower())
        patterns = [
            rf"^(?:第)?(\d+)(?:个|条)?{re.escape(action_compact)}$",
            rf"^{re.escape(action_compact)}(?:第)?(\d+)(?:个|条)?$",
        ]
        for pattern in patterns:
            match = re.match(pattern, compact)
            if match:
                return int(match.group(1)), action

    spaced = cleaned.split()
    if len(spaced) == 2:
        if spaced[0].isdigit() and spaced[1] in ACTION_ALIASES:
            return int(spaced[0]), ACTION_ALIASES[spaced[1]]
        if spaced[1].isdigit() and spaced[0] in ACTION_ALIASES:
            return int(spaced[1]), ACTION_ALIASES[spaced[0]]
    return None


def is_review_request(text: str) -> bool:
    cleaned = text.strip().lower()
    return cleaned in {"/review", "review", "候选", "看候选", "查看候选", "review queue", "待决策", "决策列表"}


def is_decision_board_request(text: str) -> bool:
    cleaned = text.strip().lower()
    return cleaned in {"/board", "board", "决策面板", "学习面板", "本周决策", "学习决策", "机会面板"}


def is_merge_plan_request(text: str) -> bool:
    cleaned = text.strip().lower()
    return cleaned in {"/merge-plan", "merge plan", "合入计划", "生成合入计划", "准备合入"}


def is_merge_execution_preview_request(text: str) -> bool:
    cleaned = text.strip().lower()
    return cleaned in {"/merge-preview", "merge preview", "合入预览", "执行合入预览"}


def parse_merge_execution_confirmation(text: str) -> int | None:
    cleaned = text.strip().lower()
    chinese = re.match(r"^确认执行合入\s*(\d+)$", cleaned)
    if chinese:
        return int(chinese.group(1))
    cli_style = re.match(r"^/merge-apply\s+(\d+)\s+confirm$", cleaned)
    return int(cli_style.group(1)) if cli_style else None


def parse_save_url(text: str) -> str | None:
    match = re.match(r"^(?:/save|save|收藏|收录|保存链接)\s+(https?://\S+)$", text.strip(), flags=re.IGNORECASE)
    return match.group(1).rstrip(".,;") if match else None


def save_manual_url(url: str) -> Path:
    root = repo_root()
    output = root / "00-Agent-Inbox/Manual-URLs/inbox.md"
    text = output.read_text(encoding="utf-8")
    if url in text:
        return output
    addition = f"\n- [ ] {now_iso()} {url}\n"
    output.write_text(text.rstrip() + addition, encoding="utf-8")
    return output


def command_response(text: str) -> str:
    root = repo_root()
    cleaned = text.strip().lower()
    if cleaned in {"/help", "help", ""}:
        return "可用命令：日报、周报、健康、决策面板、候选、收藏 <URL>、1 学习、2 忽略、3 保留、4 合入、合入计划、合入预览、确认执行合入 <编号>、巡检、真实巡检、跑日报、跑周报"
    if cleaned in {"/ping", "ping"}:
        return "pong: knowledge automation bot is alive."
    if cleaned.startswith("/daily") or cleaned in {"daily", "日报", "看日报", "今日摘要"}:
        path = latest_markdown(root / "00-Agent-Inbox/Daily-Digests")
        return summarize_markdown(path, 5) if path else "还没有 Daily Digest。"
    if cleaned.startswith("/weekly") or cleaned in {"weekly", "周报", "看周报", "本周摘要"}:
        path = latest_markdown(root / "00-Agent-Inbox/Weekly-Digests")
        return summarize_markdown(path, 5) if path else "还没有 Weekly Digest。"
    if cleaned.startswith("/health") or cleaned in {"health", "健康", "健康检查"}:
        path = latest_markdown(root / "90-Agent-System/reports")
        return summarize_markdown(path, 5) if path else "还没有 Vault Health Report。"
    if is_review_request(cleaned):
        items = review_items(limit=8)
        write_review_queue(items)
        return format_review(items, title="Review Queue: pending candidates")
    if is_decision_board_request(cleaned):
        path = generate_decision_board()
        return summarize_markdown(path, 8)
    if is_merge_plan_request(cleaned):
        path = generate_merge_plan(limit=8)
        return summarize_markdown(path, 5)
    if is_merge_execution_preview_request(cleaned):
        path = generate_execution_preview(limit=8)
        return summarize_markdown(path, 8)
    confirmed_index = parse_merge_execution_confirmation(text)
    if confirmed_index:
        try:
            result = execute_ready_candidate(confirmed_index, confirmed=True)
        except Exception as exc:
            return f"执行合入失败：{exc}"
        return (
            f"已执行合入：{result.candidate.title}\n"
            f"- target: {result.target.relative_to(root)}\n"
            f"- health_report: {result.health_report.relative_to(root)}\n"
            "- status: merged-to-area-inbox，后续仍需整合到专题正文。"
        )
    saved_url = parse_save_url(text)
    if saved_url:
        path = save_manual_url(saved_url)
        return f"已放入手动巡检池：{saved_url}\n- file: {path.relative_to(root)}\n- 下一次日报/周报会自动分析。"
    intent = parse_decision_intent(cleaned)
    if intent:
        index, action = intent
        try:
            item = decide(index, action)
        except Exception as exc:
            return f"决策失败：{exc}"
        response = f"已处理：{item.title}\n- action: {action}\n- status: {item.status}\n- file: {item.path.relative_to(root)}"
        if action == "merge":
            path = generate_merge_plan(limit=8)
            response += f"\n- merge_plan: {path.relative_to(root)}"
        return response
    if cleaned.startswith("/decide"):
        parts = cleaned.split()
        if len(parts) != 3:
            return "用法：/decide <编号> study|ignore|keep|merge"
        try:
            item = decide(int(parts[1]), parts[2])
        except Exception as exc:
            return f"决策失败：{exc}"
        response = f"已处理：{item.title}\n- action: {parts[2]}\n- status: {item.status}\n- file: {item.path.relative_to(root)}"
        if parts[2] in {"merge", "curate", "合入", "准备合入"}:
            path = generate_merge_plan(limit=8)
            response += f"\n- merge_plan: {path.relative_to(root)}"
        return response
    if cleaned.startswith("/run daily") or cleaned in {"跑日报", "生成日报", "run daily"}:
        summary = run_daily(dry_run=False, no_notify=True)
        return "Daily automation finished.\n" + "\n".join(f"- {key}: {value}" for key, value in summary.items())
    if cleaned.startswith("/run weekly") or cleaned in {"跑周报", "生成周报", "run weekly"}:
        summary = run_weekly(dry_run=False, no_notify=True)
        return "Weekly automation finished.\n" + "\n".join(f"- {key}: {value}" for key, value in summary.items())
    if cleaned in {"/ops", "ops", "巡检", "自动化巡检", "压测", "完整巡检"}:
        path = run_ops(rounds=1, mode="dry-run", notify=False, notify_report=False)
        return "Automation ops dry-run finished.\n" + summarize_markdown(path, 5)
    if cleaned in {"/ops real", "真实巡检", "真实跑一轮", "完整跑一轮"}:
        path = run_ops(rounds=1, mode="real", notify=False, notify_report=False)
        return "Automation ops real run finished.\n" + summarize_markdown(path, 5)
    return "我还不认识这个说法。可以发：候选、日报、周报、健康、收藏 <URL>、巡检、1 学习、2 忽略、3 保留、4 合入、合入计划、合入预览。"


def run_bot(dry_run: bool = False) -> None:
    load_local_env()
    root = repo_root()
    config = load_yaml(root / "90-Agent-System/feishu-bot.yaml").get("websocket_bot", {})
    app_id_env = config.get("app_id_env", "FEISHU_APP_ID")
    app_secret_env = config.get("app_secret_env", "FEISHU_APP_SECRET")

    import os

    app_id = os.getenv(app_id_env)
    app_secret = os.getenv(app_secret_env)
    if dry_run:
        safe_print(f"[feishu-bot] enabled={config.get('enabled', False)} app_id_configured={bool(app_id)} app_secret_configured={bool(app_secret)}")
        safe_print(f"[feishu-bot] commands={', '.join(config.get('commands', []))}")
        return
    if not config.get("enabled", False):
        safe_print("[feishu-bot] disabled in feishu-bot.yaml")
        return
    if not app_id or not app_secret:
        raise SystemExit(f"Missing {app_id_env} or {app_secret_env}. Put them in 90-Agent-System/.env.local or shell env.")

    try:
        from lark_oapi.channel import FeishuChannel
    except ImportError as exc:
        raise SystemExit("Missing dependency: pip install lark-oapi") from exc

    channel = FeishuChannel(app_id=app_id, app_secret=app_secret)

    async def on_message(msg) -> None:
        text = getattr(msg, "content_text", "") or ""
        chat_id = getattr(msg, "chat_id", "")
        if not chat_id:
            safe_print("[feishu-bot] received message without chat_id; skip reply")
            return
        response = command_response(text)
        await channel.send(chat_id, {"text": response})
        safe_print(f"[feishu-bot] handled command: {text.strip() or '<empty>'}")

    channel.on("message", on_message)
    safe_print("[feishu-bot] connecting via WebSocket. Press Ctrl+C to stop.")
    channel.start()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    run_bot(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
