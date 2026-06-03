from __future__ import annotations

import argparse
import subprocess
from datetime import datetime, time, timedelta
from pathlib import Path

from utils import repo_root, safe_print, week_str


DAILY_TIME = time(hour=8, minute=30)
WEEKLY_TIME = time(hour=9, minute=0)


def missed_jobs(now: datetime | None = None) -> list[str]:
    current = now or datetime.now()
    root = repo_root()
    jobs: list[str] = []
    daily_output = root / f"00-Agent-Inbox/Daily-Digests/{current.date().isoformat()}.md"
    if current.time() >= DAILY_TIME and not daily_output.exists():
        jobs.append("daily")
    monday = current.date() - timedelta(days=current.weekday())
    weekly_due = datetime.combine(monday, WEEKLY_TIME)
    weekly_output = root / f"00-Agent-Inbox/Weekly-Digests/{week_str(current.date())}.md"
    if current >= weekly_due and not weekly_output.exists():
        jobs.append("weekly")
    return jobs


def run_recovery(execute: bool = False) -> list[str]:
    jobs = missed_jobs()
    if not jobs:
        safe_print("[recovery] no missed current-period jobs.")
        return jobs
    safe_print(f"[recovery] missed jobs: {', '.join(jobs)}")
    if not execute:
        safe_print("[recovery] preview only; pass --execute to run them.")
        return jobs
    root = repo_root()
    for job in jobs:
        script = root / f"scripts/run_knowledge_{job}.sh"
        safe_print(f"[recovery] executing {job}.")
        subprocess.run(["/bin/bash", str(script)], cwd=root, check=True)
    return jobs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()
    run_recovery(execute=args.execute)


if __name__ == "__main__":
    main()
