#!/usr/bin/env python3

from datetime import datetime, timedelta
import zoneinfo

HALIFAX = zoneinfo.ZoneInfo("America/Halifax")
SANTIAGO = zoneinfo.ZoneInfo("America/Santiago")


result = 0

with open("input.txt") as f:
    for i, line in enumerate(f.read().splitlines(), 1):
        time, correct, wrong = line.split()
        time = datetime.fromisoformat(time)

        if HALIFAX.utcoffset(time) == time.utcoffset():
            zone = HALIFAX
        else:
            zone = SANTIAGO

        delta = timedelta(minutes=int(correct) - int(wrong))
        correct_time = (time + delta).astimezone(zone)
        result += correct_time.hour * i

print(result)
