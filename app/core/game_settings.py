from app.models.game import GameStatus, Location

ROUTE_MILESTONES = [
    {"location": Location.SAN_JOSE, "progress": 0},
    {"location": Location.SANTA_CLARA, "progress": 11},
    {"location": Location.SUNNYVALE, "progress": 22},
    {"location": Location.MOUNTAIN_VIEW, "progress": 33},
    {"location": Location.PALO_ALTO, "progress": 44},
    {"location": Location.MENLO_PARK, "progress": 56},
    {"location": Location.REDWOOD_CITY, "progress": 67},
    {"location": Location.SAN_MATEO, "progress": 78},
    {"location": Location.BURLINGAME, "progress": 89},
    {"location": Location.SAN_FRANCISCO, "progress": 100},
]


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