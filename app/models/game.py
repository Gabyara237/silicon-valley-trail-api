from datetime import datetime, timezone
from sqlalchemy import Column, DateTime
from enum import Enum
from typing import Optional
from sqlmodel import SQLModel, Field

class GameStatus(str,Enum):
    in_progress =  "in_progress"
    won= "won"
    lost ="lost"
    abandoned = "abandoned"


class Location(str, Enum):
    SAN_JOSE = "San Jose"
    SANTA_CLARA = "Santa Clara"
    SUNNYVALE = "Sunnyvale"
    MOUNTAIN_VIEW = "Mountain View"
    PALO_ALTO = "Palo Alto"
    MENLO_PARK = "Menlo Park"
    REDWOOD_CITY = "Redwood City"
    SAN_MATEO = "San Mateo"
    BURLINGAME = "Burlingame"
    SAN_FRANCISCO = "San Francisco"


class Game(SQLModel, table=True):

    __tablename__= "games"

    id: Optional[int] = Field(default=None,primary_key=True)
    user_id: Optional[int]  = Field(default=None, foreign_key="users.id")
    cash: int 
    current_day: int
    team_energy: int
    bug_count: int 
    caffeine: int
    market_traction: int
    travel_progress: int
    status: GameStatus = Field(default= GameStatus.in_progress)
    current_location: Location = Field(default=Location.SAN_JOSE)
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True)), default_factory=lambda: datetime.now(timezone.utc))    
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True)), default_factory=lambda: datetime.now(timezone.utc))