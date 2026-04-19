from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

from app.core.game_actions import GameAction
from app.models.game import GameStatus
from app.models.game import Location
from app.models.game_event import EventChoice, EventType



class GuestGameCreate(BaseModel):
    guest_username: Optional[str] = Field(default= None, min_length=3, max_length=50)
    

class GameResponse(BaseModel):
    id: int 
    user_id: Optional[int]  
    status: GameStatus
    current_location: Location
    
    cash: int 
    current_day: int
    team_energy: int
    bug_count: int 
    caffeine: int
    market_traction: int
    travel_progress: int

    created_at: datetime 
    updated_at: datetime 

    model_config = ConfigDict(from_attributes=True)


class GuestGameResponse(BaseModel):
    guest_username: str
    status: GameStatus
    current_location: Location
    cash: int 
    current_day: int
    team_energy: int
    bug_count: int 
    caffeine: int
    market_traction: int
    travel_progress: int


class GameActionRequest(BaseModel):
    action: GameAction

class GuestActionRequest(BaseModel):
    action: GameAction
    game: dict


class TriggeredEventResponse(BaseModel):
    event_type: EventType
    title: str
    description: str
    choices: list[str]

class GameActionResult(BaseModel):
    game: GameResponse
    event: TriggeredEventResponse | None = None
    weather_description: str | None = None


class GuestGameActionResult(BaseModel):
    game:GuestGameResponse
    event: TriggeredEventResponse | None = None
    weather_description: str | None = None


class GameEventRequest(BaseModel):
    event: EventType
    player_choice: EventChoice


class GuestGameEventRequest(BaseModel):
    game: dict
    event: EventType
    player_choice: EventChoice


class LocationCoordinates(BaseModel):
    latitude: float
    longitude: float


class Weather(BaseModel):
    temperature: float
    unit: str
    source:str