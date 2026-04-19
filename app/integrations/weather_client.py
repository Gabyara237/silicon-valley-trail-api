import httpx
import random

from app.schemas.game import LocationCoordinates, Weather

BASE_URL= "https://api.open-meteo.com/v1/forecast"

FALLBACK_TEMPERATURES = [12,15,18,20,22,25,28,30]

async def get_weather(location_coordinates: LocationCoordinates)->Weather:

    async with httpx.AsyncClient() as client:

        try:
            params = {
                "latitude": location_coordinates.latitude,
                "longitude": location_coordinates.longitude,
                "current": "temperature_2m"
            }

            response = await client.get(BASE_URL, params=params)
            print("status:", response.status_code)
            print("body:", response.text)
            response.raise_for_status()

            data = response.json()
            current = data.get("current")
            
            if not current or "temperature_2m" not in current:
                raise ValueError ("Missing temperature_2m in response")
            
            weather = current["temperature_2m"]

            return Weather(
                temperature= weather,
                unit= "celsius",
                source="api"
                
            )

        except (httpx.HTTPError, ValueError):

            fallback_temperature = random.choice(FALLBACK_TEMPERATURES)

            return Weather(
                temperature=fallback_temperature,
                unit="celsius",
                source="fallback"
            )

