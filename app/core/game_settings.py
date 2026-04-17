from app.models.game import GameStatus, Location


DEFAULT_GAME_STATE ={
    "cash": 100,
    "current_day": 1,
    "team_energy": 80,
    "bug_count": 0,
    "caffeine": 3,
    "market_traction": 10,
    "travel_progress": 0,
    "status": GameStatus.in_progress,
    "current_location":Location.SAN_JOSE ,
}