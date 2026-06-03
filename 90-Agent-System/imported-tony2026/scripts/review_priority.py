from __future__ import annotations

from functools import lru_cache
from typing import Any

from utils import load_yaml, repo_root


@lru_cache(maxsize=1)
def review_ranking_policy() -> dict[str, Any]:
    config = load_yaml(repo_root() / "90-Agent-System/review-policy.yaml")
    policy = config.get("review_ranking", {})
    if not isinstance(policy, dict):
        raise ValueError("review-policy.yaml review_ranking must be a mapping")
    return policy


def priority_score(importance: str | int, topic: str, source: str, action: str) -> int:
    policy = review_ranking_policy()
    multiplier = int(policy.get("importance_multiplier", 10))
    importance_value = int(importance or 1)
    action_weights = policy.get("action_weights", {})
    topic_weights = policy.get("topic_weights", {})
    source_weights = policy.get("source_weights", {})
    return (
        importance_value * multiplier
        + int(action_weights.get(action, 0))
        + int(topic_weights.get(topic, 0))
        + int(source_weights.get(source, 0))
    )


def priority_reason(importance: str | int, topic: str, source: str, action: str, action_label: str = "稳定建议") -> str:
    policy = review_ranking_policy()
    reasons = [f"重要性 {importance}"]
    if int(policy.get("topic_weights", {}).get(topic, 0)) > 0:
        reasons.append(f"{topic} 主线")
    if int(policy.get("source_weights", {}).get(source, 0)) > 0:
        reasons.append(source)
    if action and action != "review":
        reasons.append(f"{action_label} {action}")
    return "；".join(reasons)
