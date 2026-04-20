from app.core.game_actions import GAME_ACTION_EFFECTS, GameAction
from app.core.game_settings import ROUTE_MILESTONES
from app.core.game_utils import get_coordinates_from_location, get_game_status
from app.models.game import GameStatus, Location



class DummyGame:
    def __init__(self):
        self.market_traction = 0
        self.caffeine = 0
        self.team_energy = 50

def test_game_lost_when_energy_zero():
    status = get_game_status(travel_progress=50, team_energy=0, cash=100)
    assert status == GameStatus.lost


def test_game_lost_when_cash_zero():
    status = get_game_status(travel_progress=50, team_energy=10, cash=0)
    assert status == GameStatus.lost


def test_game_won_when_progress_100():
    status = get_game_status(travel_progress=100, team_energy=10, cash=10)
    assert status == GameStatus.won


def test_game_in_progress():
    status = get_game_status(travel_progress=50, team_energy=10, cash=10)
    assert status == GameStatus.in_progress


def test_get_coordinates_from_location():
    coordinates = get_coordinates_from_location(Location.SAN_JOSE)
    milestone = next(
        milestone for milestone in ROUTE_MILESTONES
        if milestone["location"] == Location.SAN_JOSE
    )
    assert coordinates.latitude == milestone["latitude"]
    assert coordinates.longitude == milestone["longitude"]

def test_buy_coffee_effect():
    effect = GAME_ACTION_EFFECTS[GameAction.BUY_COFFEE]

    assert effect["cash"] < 0
    assert effect["caffeine"] > 0


