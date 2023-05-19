import requests
from time import sleep


def sync(timezone):
    timeResponse = requests.get(
        "http://timeapi.io/api/Time/current/zone?timeZone=" + timezone
    )
    curr = timeResponse.json()

    hour = curr["hour"]
    minute = curr["minute"]
    sec = curr["seconds"]

    return hour, minute, sec


while True:
    hour, minute, sec = sync("Asia/Kolkata")
    ap = "AM"
    if hour > 12:
        hour = hour - 12
        ap = "PM"
    elif hour == 12:
        ap = "PM"
    elif hour == 0:
        hour = 12
    print(
        str(hour).rjust(2, "0")
        + ":"
        + str(minute).rjust(2, "0")
        + ":"
        + str(sec).rjust(2, "0")
        + " "
        + ap
    )
    sleep(0.1)
