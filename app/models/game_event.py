from datetime import datetime, timezone
from enum import Enum
from typing import Optional
from sqlalchemy import Column, DateTime
from sqlmodel import SQLModel, Field


class EventType(str,Enum):
    HACKATHON = "hackathon"
    BUGS = "bugs"
    NETWORKING = "networking"
    FEATURE_REQUEST = "feature_request"
    COFFEE_SHORTAGE = "coffee_shortage"

class EventChoice(str, Enum):
    ACCEPT = "accept"
    REJECT = "reject"
    ATTEND = "attend"
    IGNORE = "ignore"
    BUILD  = "build"
    BUY = "buy"
    SKIP = "skip"


class GameEvent(SQLModel, table=True):
    __tablename__= "game_events"

    id: Optional[int] = Field(default=None,primary_key=True)
    game_id: int = Field(foreign_key="games.id")
    event_type: EventType
    outcome: Optional[str] = None
    player_choice: EventChoice
    day: int
    description: str
    created_at: datetime = Field( sa_column=Column(DateTime(timezone=True)), default_factory=lambda: datetime.now(timezone.utc))
