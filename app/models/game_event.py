from datetime import datetime, timezone
from enum import Enum
from typing import Optional
from sqlmodel import SQLModel, Field


class EventType(str,Enum):
    hackathon ="hackathon"
    bugs= "bugs"
    networking = "networking"
    new_feature = "new_feature"
    coffee_shortage = "coffee_shortage"


class GameEvent(SQLModel, table=True):
    __tablename__= "game_events"

    id: Optional[int] = Field(default=None,primary_key=True)
    game_id: int = Field(foreign_key="games.id")
    event_type: EventType
    player_choice: str
    day: int
    description: str
    created_at: datetime = Field(default_factory= lambda:datetime.now(timezone.utc))

