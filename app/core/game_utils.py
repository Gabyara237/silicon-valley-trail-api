import random
from app.core.game_settings import ROUTE_MILESTONES
from app.models.game import Location, GameStatus
from app.schemas.game import DataTraffic, LocationCoordinates



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
    
    for milestone in ROUTE_MILESTONES:
        if milestone["location"] == location:
            return LocationCoordinates(
                latitude=milestone["latitude"],
                longitude=milestone["longitude"]
            )

    raise ValueError(f"Location {location} not found in route milestones")


def get_milestone_by_location(location: Location) -> dict:
    for milestone in ROUTE_MILESTONES:
        if milestone["location"] == location:
            return milestone
    raise ValueError(f"Location {location} not found in route milestones")


def get_fallback_duration_seconds(distance_meters: int) -> int:
    if distance_meters <= 5000:
        return random.choice([300, 360, 420, 480, 540])  
    elif distance_meters <= 9000:
        return random.choice([600, 720, 840, 960])       
    else:
        return random.choice([1200, 1500, 1800, 2100])   


def get_fallback_traffic(distance_meters: int) -> DataTraffic:
    duration_seconds = get_fallback_duration_seconds(distance_meters)

    return DataTraffic(
        distance=distance_meters,
        duration=f"{duration_seconds}s",
        source="fallback"
    )
