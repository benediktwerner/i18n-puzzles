#!/usr/bin/env python3

from collections import defaultdict
from datetime import datetime
from itertools import permutations


def full_year(year: int) -> int:
    return 2000 + year if year < 20 else 1900 + year


def parse_with_order(date: str, order: tuple) -> datetime | None:
    parts = map(int, date.split("-"))
    kwargs = {k: (full_year(v) if k == "year" else v) for k, v in zip(order, parts)}
    try:
        return datetime(**kwargs)
    except ValueError as e:
        return None


with open("input.txt") as f:
    dates_of_author = defaultdict(list)
    for line in f.read().splitlines():
        date, authors = line.split(": ")
        for author in authors.split(", "):
            dates_of_author[author].append(date)

    relevant_authors = []

    for author, dates in dates_of_author.items():
        orders = [
            order
            for order in permutations(("day", "month", "year"))
            if all(parse_with_order(date, order) is not None for date in dates)
        ]
        assert len(orders) == 1
        order = orders[0]
        if any(
            parse_with_order(date, order) == datetime(2001, 9, 11) for date in dates
        ):
            relevant_authors.append(author)

    print(" ".join(sorted(relevant_authors)))
