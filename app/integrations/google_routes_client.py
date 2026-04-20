import httpx
from app.config import google_api
from app.core.game_utils import get_fallback_traffic, get_milestone_by_location
from app.models.game import Location
from app.schemas.game import DataTraffic, LocationCoordinates


GOOGLE_API_KEY= google_api.GOOGLE_API_KEY

async def get_traffic(origin:LocationCoordinates, destination:LocationCoordinates, current_location:Location)-> DataTraffic:

    url= "https://routes.googleapis.com/directions/v2:computeRoutes"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": GOOGLE_API_KEY,
        "X-Goog-FieldMask": "routes.duration,routes.distanceMeters"
    }

    body = {
        "origin": {
            "location": {
                "latLng": {
                    "latitude": origin.latitude,
                    "longitude": origin.longitude
                }
            }
        },
        "destination": {
            "location": {
                "latLng": {
                    "latitude": destination.latitude,
                    "longitude": destination.longitude
                }
            }
        },
        "travelMode": "DRIVE",
        "routingPreference": "TRAFFIC_AWARE"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=body)
            # print(f"Traffic API status: {response.status_code}")
            # print(f"Traffic API body: {response.text}")
            response.raise_for_status()
            data = response.json()
            
            routes = data.get("routes")
            if not routes:
                raise ValueError("No routes found")

            route = routes[0]

            distance_data = route.get("distanceMeters")
            duration_data = route.get("duration")

            if not distance_data or not duration_data:
                raise ValueError("Missing traffic data")
            
            return DataTraffic(
                distance=distance_data,
                duration=duration_data,
                source="api"
            )
        
        except (httpx.HTTPError, ValueError):
            # print("Using traffic fallback data")
            milestone = get_milestone_by_location(current_location)
            fallback_distance = milestone["distance_to_next_meters"]

            return get_fallback_traffic(fallback_distance)