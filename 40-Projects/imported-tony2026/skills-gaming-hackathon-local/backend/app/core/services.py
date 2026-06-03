from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from uuid import uuid4

from app.core.config import DURATION_SECONDS, ERROR_PENALTY, MODE, STREAK_BONUS_STEP, TOURNAMENT_ID
from app.schemas.events import EventIngestRequest, EventIngestResponse
from app.schemas.result import MatchResultResponse, ScoreBreakdownItem
from app.schemas.score import ScoreSubmitRequest, ScoreSubmitResponse
from app.schemas.tournament import EligibilityResponse, TournamentResponse

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
EVENT_LOG = DATA_DIR / "events.jsonl"
RESULT_LOG = DATA_DIR / "results.json"


class ResultStore:
    def __init__(self) -> None:
        self._results: dict[str, dict] = {}
        self._load()

    def _load(self) -> None:
        if RESULT_LOG.exists():
            self._results = json.loads(RESULT_LOG.read_text(encoding="utf-8"))

    def _save(self) -> None:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        RESULT_LOG.write_text(json.dumps(self._results, ensure_ascii=False, indent=2), encoding="utf-8")

    def set(self, match_id: str, payload: dict) -> None:
        self._results[match_id] = payload
        self._save()

    def get(self, match_id: str) -> dict | None:
        return self._results.get(match_id)


RESULTS = ResultStore()


def build_current_tournament() -> TournamentResponse:
    return TournamentResponse(
        tournament_id=TOURNAMENT_ID,
        mode=MODE,
        duration_seconds=DURATION_SECONDS,
        error_penalty=ERROR_PENALTY,
        streak_bonus=STREAK_BONUS_STEP,
        status="active",
    )


def _mock_opponent_score(total: int, duration_ms: int, error_count: int) -> int:
    pacing_adjust = 5 if duration_ms < 42000 else 0
    consistency_penalty = error_count * 2
    return max(18, total - 7 + pacing_adjust + consistency_penalty)


def submit_score(payload: ScoreSubmitRequest) -> ScoreSubmitResponse:
    total = payload.correct_count * 10 + payload.streak_bonus - payload.error_count * payload.error_penalty
    opponent_score = _mock_opponent_score(total, payload.duration_ms, payload.error_count)
    outcome = "win" if total >= opponent_score else "loss"
    delta = total - opponent_score
    breakdown = [
        ScoreBreakdownItem(label="words_found", value=payload.correct_count * 10),
        ScoreBreakdownItem(label="scan_chain_bonus", value=payload.streak_bonus),
        ScoreBreakdownItem(label="miss_penalty", value=-(payload.error_count * payload.error_penalty)),
    ]
    RESULTS.set(
        payload.match_id,
        {
            "total_score": total,
            "outcome": outcome,
            "delta_to_opponent": delta,
            "opponent_score": opponent_score,
            "explanation": "Found words score points, scan chains add bonus, and misses reduce your final score.",
            "breakdown": [item.model_dump() for item in breakdown],
        },
    )
    return ScoreSubmitResponse(
        accepted=True,
        match_id=payload.match_id,
        result_id=str(uuid4()),
        total_score=total,
        explanation="words found x10 + scan chain bonus - miss penalty",
        breakdown=breakdown,
        submitted_at=datetime.now(UTC),
    )


def ingest_event_batch(payload: EventIngestRequest) -> EventIngestResponse:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with EVENT_LOG.open("a", encoding="utf-8") as fh:
        for event in payload.events:
            fh.write(json.dumps(event.model_dump(mode="json"), ensure_ascii=False) + "\n")
    return EventIngestResponse(accepted_count=len(payload.events), rejected_count=0)


def build_result(match_id: str) -> MatchResultResponse:
    data = RESULTS.get(match_id)
    if not data:
        data = {
            "total_score": 84,
            "outcome": "win",
            "delta_to_opponent": 7,
            "opponent_score": 77,
            "explanation": "You found more words cleanly and kept a better chain than your opponent.",
            "breakdown": [
                {"label": "words_found", "value": 80},
                {"label": "scan_chain_bonus", "value": 8},
                {"label": "miss_penalty", "value": -4},
            ],
        }
    return MatchResultResponse(
        match_id=match_id,
        total_score=data["total_score"],
        outcome=data["outcome"],
        delta_to_opponent=data["delta_to_opponent"],
        opponent_score=data["opponent_score"],
        explanation=data["explanation"],
        breakdown=[ScoreBreakdownItem(**item) for item in data["breakdown"]],
    )


def build_eligibility() -> EligibilityResponse:
    return EligibilityResponse(
        eligible=True,
        reason="demo_mode",
        region="US-CA",
        notes="Demo placeholder only; not real-money eligible logic.",
    )
