from enum import Enum

TRAVEL_STEP = 11

class GameAction(str, Enum):
    REST = "rest"
    WORK_ON_PRODUCT = "work_on_product"
    MARKETING_PUSH = "marketing_push"
    TRAVEL = "travel"


GAME_ACTION_EFFECTS = {
    GameAction.REST: {
        "team_energy": 15,
        "cash": 0,
        "bug_count": 0,
        "caffeine": 0,
        "market_traction": 0,
        "travel_progress": 0,
        "current_day": 1,
    },
    GameAction.WORK_ON_PRODUCT: {
        "team_energy": -10,
        "cash": 0,
        "bug_count": -1,
        "caffeine": -1,
        "market_traction": 0,
        "travel_progress": 0,
        "current_day": 1,
    },
    GameAction.MARKETING_PUSH: {
        "team_energy": -5,
        "cash": -15,
        "bug_count": 0,
        "caffeine": 0,
        "market_traction": 10,
        "travel_progress": 0,
        "current_day": 1,
    },
    GameAction.TRAVEL: {
        "team_energy": -10,
        "cash": -5,
        "bug_count": 0,
        "caffeine": -1,
        "market_traction": 0,
        "travel_progress": TRAVEL_STEP,
        "current_day": 1,
    },
}