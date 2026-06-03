from datetime import datetime

from pydantic import BaseModel, Field

from app.schemas.result import ScoreBreakdownItem


class ScoreSubmitRequest(BaseModel):
    match_id: str
    player_id: str
    correct_count: int = Field(ge=0)
    error_count: int = Field(ge=0)
    streak_bonus: int = Field(default=0, ge=0)
    error_penalty: int = Field(default=2, ge=0)
    duration_ms: int = Field(ge=0)
    client_version: str


class ScoreSubmitResponse(BaseModel):
    accepted: bool
    match_id: str
    result_id: str
    total_score: int
    explanation: str
    breakdown: list[ScoreBreakdownItem]
    submitted_at: datetime
