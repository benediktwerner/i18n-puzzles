#!/usr/bin/env python3

from datetime import datetime
import zoneinfo


def parse(s: str) -> datetime:
    _, zone, *date = s.split()
    dt = datetime.strptime(" ".join(date), "%b %d, %Y, %H:%M")
    return dt.replace(tzinfo=zoneinfo.ZoneInfo(zone))


with open("input.txt") as f:
    result = 0
    for trip in f.read().split("\n\n"):
        departure, arrival = map(parse, trip.splitlines())
        result += (arrival - departure).seconds // 60
    print(result)
