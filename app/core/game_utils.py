from app.core.game_settings import ROUTE_MILESTONES
from app.models.game import Location, GameStatus
from app.schemas.game import LocationCoordinates



def get_location_from_progress(travel_progress:int)-> Location:

    current_location = Location.SAN_JOSE

    for milestone in ROUTE_MILESTONES:
        if travel_progress >= milestone["progress"]:
            current_location = milestone["location"]
        else:
            break

    return current_location

def get_game_status(travel_progress: int, team_energy: int) -> GameStatus:
    if travel_progress >= 100:
        return GameStatus.won
    if team_energy <= 0:
        return GameStatus.lost
    return GameStatus.in_progress

def get_coordinates_from_location(location: Location)-> LocationCoordinates:
    latitude = ROUTE_MILESTONES[location]["latitude"]
    longitude = ROUTE_MILESTONES[location]["longitude"]

    return {
        "latitude": latitude,
        "longitude": longitude
    }