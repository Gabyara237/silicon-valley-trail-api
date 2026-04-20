import random
from app.core.game_actions import GameAction
from app.models.game_event import EventType

EVENT_POOL = [
    EventType.HACKATHON,
    EventType.BUGS,
    EventType.NETWORKING,
    EventType.FEATURE_REQUEST,
    EventType.COFFEE_SHORTAGE,
    None,
    None,
    None
]

HACKATHON_OUTCOMES = ["win", "lose"]

GAME_EVENTS = {
    EventType.HACKATHON: {
        "title": "Hackathon Invitation",
        "description": "A local startup incubator invited your team to join a hackathon. It could boost your visibility, but it will also demand time and energy.",
        "choices": ["accept", "reject"],
        "effects": {
            "accept": {
                "random_outcomes": {
                    "win": {
                        "cash": 30,
                        "market_traction": 20,
                        "team_energy": 0,
                        "bug_count": 0,
                        "caffeine": 0,
                    },
                    "lose": {
                        "cash": 0,
                        "market_traction": 0,
                        "team_energy": -10,
                        "bug_count": 0,
                        "caffeine": 0,
                    },
                }
            },
            "reject": {
                "cash": 0,
                "market_traction": -5,
                "team_energy": 0,
                "bug_count": 0,
                "caffeine": 0,
            },
        },
    },
    EventType.BUGS: {
        "title": "Critical Bugs Found",
        "description": "Your team discovered a set of critical bugs right before a product demo. Fixing them now will cost energy and caffeine, but ignoring them may hurt your traction.",
        "choices": ["accept", "reject"],
        "effects": {
            "accept": {
                "cash": 0,
                "market_traction": 5,
                "team_energy": -5,
                "bug_count": -2,
                "caffeine": -1,
            },
            "reject": {
                "cash": 0,
                "market_traction": -10,
                "team_energy": 0,
                "bug_count": 2,
                "caffeine": 0,
            },
        },
    },
    EventType.NETWORKING: {
        "title": "Networking Meetup",
        "description": "A startup networking event is happening nearby. Attending may increase your market traction, but tickets and transportation cost money.",
        "choices": ["attend", "ignore"],
        "effects": {
            "attend": {
                "cash": -10,
                "market_traction": 15,
                "team_energy": 0,
                "bug_count": 0,
                "caffeine": 0,
            },
            "ignore": {
                "cash": 0,
                "market_traction": -5,
                "team_energy": 0,
                "bug_count": 0,
                "caffeine": 0,
            },
        },
    },
    EventType.FEATURE_REQUEST: {
        "title": "New Feature Request",
        "description": "Early users are asking for a new feature. Building it may improve traction, but your team will need extra effort and caffeine.",
        "choices": ["build", "ignore"],
        "effects": {
            "build": {
                "cash": 0,
                "market_traction": 12,
                "team_energy": -8,
                "bug_count": 0,
                "caffeine": -1,
            },
            "ignore": {
                "cash": 0,
                "market_traction": -8,
                "team_energy": 0,
                "bug_count": 0,
                "caffeine": 0,
            },
        },
    },
    EventType.COFFEE_SHORTAGE: {
        "title": "Coffee Shortage",
        "description": "Your office is running out of coffee. Buying more will cost cash, but without it your team's energy may drop.",
        "choices": ["buy", "skip"],
        "effects": {
            "buy": {
                "cash": -8,
                "market_traction": 0,
                "team_energy": 0,
                "bug_count": 0,
                "caffeine": 2,
            },
            "skip": {
                "cash": 0,
                "market_traction": 0,
                "team_energy": -8,
                "bug_count": 0,
                "caffeine": 0,
            },
        },
    },
}


def get_random_event():
    return random.choice(EVENT_POOL)


def get_hackathon_outcome():
    return random.choice(HACKATHON_OUTCOMES)


def maybe_get_event(action: GameAction):
    if action != GameAction.TRAVEL:
        return None
    return get_random_event()


def get_weather_effect(temperature: float):
    if temperature < 10:
        return {"energy":-1, "coffee":-2, "description": f"The current temperature is {temperature} °C, as it gets colder, your team started to drink more coffee and its energy has dropped a bit."}
    elif temperature >28:
        return{"energy": -2, "coffee":0, "description": f"The current temperature is {temperature} °C, as it is hot your team feels uncomfortable and its energy has dropped a bit."}
    else:
        return{"energy":+2, "coffee":0, "description": f"The current temperature is {temperature} °C, so your team is in high spirits and has increased its energy."}