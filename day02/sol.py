#!/usr/bin/env python3

from collections import Counter
from datetime import datetime, timezone

with open("input.txt") as f:
    counts = Counter()

    for line in f.read().splitlines():
        counts[datetime.fromisoformat(line).astimezone(timezone.utc).isoformat()] += 1

    time, count = counts.most_common(1)[0]
    assert count >= 4
    print(time)
