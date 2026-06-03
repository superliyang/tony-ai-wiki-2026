from pydantic import BaseModel


class ScoreBreakdownItem(BaseModel):
    label: str
    value: int


class MatchResultResponse(BaseModel):
    match_id: str
    total_score: int
    outcome: str
    delta_to_opponent: int
    opponent_score: int
    explanation: str
    breakdown: list[ScoreBreakdownItem]
