from datetime import datetime

from pydantic import BaseModel


class EventItem(BaseModel):
    event_name: str
    player_id: str
    match_id: str | None = None
    emitted_at: datetime
    payload: dict = {}


class EventIngestRequest(BaseModel):
    events: list[EventItem]


class EventIngestResponse(BaseModel):
    accepted_count: int
    rejected_count: int
