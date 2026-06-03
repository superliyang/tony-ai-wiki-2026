from pydantic import BaseModel


class TournamentResponse(BaseModel):
    tournament_id: str
    mode: str
    duration_seconds: int
    error_penalty: int
    streak_bonus: int
    status: str


class EligibilityResponse(BaseModel):
    eligible: bool
    reason: str
    region: str
    notes: str
