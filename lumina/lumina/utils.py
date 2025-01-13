import time
import geocoder


def current_timestamp() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S")

def current_location() -> str:
    g = geocoder.ip('me')
    return f"{g.latlng}" if g.ok else "Unknown"


def metadata() -> dict:
    current_time = current_timestamp()
    location = current_location()
    return {"timestamp": current_time, "location": location}
