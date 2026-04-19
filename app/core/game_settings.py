from app.models.game import GameStatus, Location

ROUTE_MILESTONES = [
    {"location": Location.SAN_JOSE, "progress": 0, "latitude":37.33856738132785, "longitude":-121.88471668492491, "next_location": Location.SANTA_CLARA, "distance_to_next_meters": 7813},
    {"location": Location.SANTA_CLARA, "progress": 11, "latitude":37.35326628981983, "longitude":-121.95482923732612, "next_location": Location.SUNNYVALE,"distance_to_next_meters": 12238},
    {"location": Location.SUNNYVALE, "progress": 22, "latitude":37.36887703188547, "longitude":-122.03666434116397,"next_location": Location.MOUNTAIN_VIEW,"distance_to_next_meters": 6340},
    {"location": Location.MOUNTAIN_VIEW, "progress": 33, "latitude":37.38918496845874, "longitude":-122.08084297555753,"next_location": Location.PALO_ALTO, "distance_to_next_meters": 7570},
    {"location": Location.PALO_ALTO, "progress": 44, "latitude":37.44208560135573, "longitude": -122.14332771520503,"next_location": Location.MENLO_PARK, "distance_to_next_meters": 5460},
    {"location": Location.MENLO_PARK, "progress": 56, "latitude":37.45298830186796, "longitude":-122.18109321914831,"next_location": Location.REDWOOD_CITY, "distance_to_next_meters": 6570},
    {"location": Location.REDWOOD_CITY, "progress": 67, "latitude":37.482962533761494, "longitude":-122.22641182153001,"next_location": Location.SAN_MATEO, "distance_to_next_meters": 9380},
    {"location": Location.SAN_MATEO, "progress": 78, "latitude":37.56356076609011, "longitude":-122.32254219270969,"next_location": Location.BURLINGAME, "distance_to_next_meters": 4230},
    {"location": Location.BURLINGAME, "progress": 89, "latitude":37.57883547388158, "longitude":-122.34728451695459,"next_location": Location.SAN_FRANCISCO, "distance_to_next_meters": 13020},
    {"location": Location.SAN_FRANCISCO, "progress": 100, "latitude":37.77557033101038, "longitude":-122.41947589127662,"next_location": None, "distance_to_next_meters": 0},
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