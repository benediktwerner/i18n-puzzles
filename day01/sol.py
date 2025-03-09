#!/usr/bin/env python3

with open("input.txt") as f:
    result = 0

    for line in f.read().splitlines():
        tweet = len(line) <= 140
        sms = len(line.encode()) <= 160
        if tweet and sms:
            result += 13
        elif tweet:
            result += 7
        elif sms:
            result += 11

    print(result)
