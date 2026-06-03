from fastapi import APIRouter

from app.schemas.events import EventIngestRequest, EventIngestResponse
from app.schemas.result import MatchResultResponse
from app.schemas.score import ScoreSubmitRequest, ScoreSubmitResponse
from app.schemas.tournament import EligibilityResponse, TournamentResponse
from app.core.services import (
    build_current_tournament,
    build_eligibility,
    build_result,
    ingest_event_batch,
    submit_score,
)

router = APIRouter()


@router.get("/tournament/current", response_model=TournamentResponse)
def get_current_tournament() -> TournamentResponse:
    return build_current_tournament()


@router.post("/match/submit-score", response_model=ScoreSubmitResponse)
def post_score(payload: ScoreSubmitRequest) -> ScoreSubmitResponse:
    return submit_score(payload)


@router.post("/events", response_model=EventIngestResponse)
def post_events(payload: EventIngestRequest) -> EventIngestResponse:
    return ingest_event_batch(payload)


@router.get("/result/{match_id}", response_model=MatchResultResponse)
def get_result(match_id: str) -> MatchResultResponse:
    return build_result(match_id)


@router.get("/eligibility", response_model=EligibilityResponse)
def get_eligibility() -> EligibilityResponse:
    return build_eligibility()
