from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

from app.models.game import GameStatus


class GameCreate(BaseModel):
    guest_username: Optional[str] = Field(default= None, min_length=3, max_length=50)
    

class GameResponse(BaseModel):
    id: int 
    user_id: Optional[int]  
    status: GameStatus
    current_location: str
    
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
