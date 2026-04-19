from app.schemas.game import DataTraffic


def parse_duration_to_seconds(duration: str) -> int:
    return int(duration.replace("s", ""))


def get_traffic_level(data_traffic: DataTraffic) -> str:
    duration_seconds = parse_duration_to_seconds(data_traffic.duration)

    if duration_seconds == 0:
        return "unknown"

    speed_kmh = (data_traffic.distance / duration_seconds) * 3.6

    if speed_kmh < 25:
        return "heavy"
    elif speed_kmh < 50:
        return "moderate"
    return "light"