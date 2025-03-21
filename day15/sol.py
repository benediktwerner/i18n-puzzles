#!/usr/bin/env python3

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo


HOLIDAY_FORMAT = "%-d %B %Y"


@dataclass
class Supporter:
    timezone: str
    holidays: list[str]

    def works_at(self, now: datetime) -> bool:
        now = now.astimezone(ZoneInfo(self.timezone))
        return (
            now.weekday() < 5
            and now.strftime(HOLIDAY_FORMAT) not in self.holidays
            and ((now.hour == 8 and now.minute >= 30) or now.hour in range(9, 17))
        )


with open("input.txt") as f:
    offices, customers = map(str.splitlines, f.read().split("\n\n"))


supporters = []

for office in offices:
    _, tz, holidays = office.split("\t")
    supporters.append(Supporter(tz, holidays.split(";")))


lowest = float("inf")
highest = 0

for i, customer in enumerate(customers):
    print(i + 1, "/", len(customers))

    _, tz, holidays = customer.split("\t")
    tz = ZoneInfo(tz)
    holidays = holidays.split(";")
    overtime = 0

    now = datetime(2022, 1, 1, 0, 0, 0, tzinfo=timezone.utc).astimezone(tz)
    end = datetime(2023, 1, 1, 0, 0, 0, tzinfo=timezone.utc).astimezone(tz)
    while now < end:
        if (
            now.weekday() < 5
            and now.strftime(HOLIDAY_FORMAT) not in holidays
            and not any(supporter.works_at(now) for supporter in supporters)
        ):
            overtime += 15

        now = now.astimezone(timezone.utc)
        now += timedelta(minutes=15)
        now = now.astimezone(tz)

    lowest = min(lowest, overtime)
    highest = max(highest, overtime)

print(highest - lowest)
