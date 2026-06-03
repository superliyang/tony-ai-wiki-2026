from __future__ import annotations

import re
from dataclasses import dataclass

from review_priority import review_ranking_policy


HISTORY_PATTERN = re.compile(
    r"^- (?P<run_at>\S+) \| action=`(?P<action>[^`]+)` \| confidence=(?P<confidence>[0-9.]+)$",
    flags=re.MULTILINE,
)


@dataclass(frozen=True)
class Observation:
    run_at: str
    action: str
    confidence: str


def parse_observations(text: str) -> list[Observation]:
    return [
        Observation(
            run_at=match.group("run_at"),
            action=match.group("action"),
            confidence=match.group("confidence"),
        )
        for match in HISTORY_PATTERN.finditer(text)
    ]


def with_observation(observations: list[Observation], run_at: str, action: str, confidence: str) -> list[Observation]:
    current = Observation(run_at=run_at, action=action, confidence=confidence or "0.5")
    retained = [observation for observation in observations if observation.run_at != run_at]
    return retained + [current]


def stable_action(observations: list[Observation], previous_stable: str = "review") -> tuple[str, str]:
    if not observations:
        return previous_stable or "review", "unobserved"
    stability = review_ranking_policy().get("decision_stability", {})
    confirmation_runs = int(stability.get("confirmation_runs", 2))
    window = int(stability.get("observation_window", 3))
    protected_actions = set(stability.get("protected_actions", ["study", "merge-plan"]))
    latest = observations[-1].action
    if latest not in protected_actions:
        return latest, "latest"
    support = sum(1 for observation in observations[-window:] if observation.action == latest)
    if support >= confirmation_runs:
        return latest, "confirmed"
    if previous_stable in protected_actions:
        return previous_stable, "holding"
    return "review", "observing"


def render_history(observations: list[Observation], limit: int = 8) -> str:
    lines = ["# Agent 判断历史", ""]
    for observation in observations[-limit:]:
        lines.append(f"- {observation.run_at} | action=`{observation.action}` | confidence={observation.confidence}")
    return "\n".join(lines)
