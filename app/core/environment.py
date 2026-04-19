from app.schemas.game import DataTraffic


def parse_duration_to_seconds(duration: str) -> int:
    return int(duration.replace("s", ""))


def get_traffic_effect(data_traffic: DataTraffic) -> str:
    duration_seconds = parse_duration_to_seconds(data_traffic.duration)

    if duration_seconds == 0:
        return "unknown"

    speed_kmh = (data_traffic.distance / duration_seconds) * 3.6

    if speed_kmh < 25:
        return {"energy": -2, "coffee": -2 , "description": "Heavy traffic slowed your team down. They lost energy and drank more caffeine"}
    elif speed_kmh < 50:
        return {"energy": -1, "coffee": -1, "description": "Moderate traffic caused some delays. Your team lost a bit of energy and used some caffeine to stay focused."}
    return {"energy": 0, "coffee": 0, "description": "Traffic was light, so your team stayed on schedule without extra stress."}