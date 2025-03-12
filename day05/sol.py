#!/usr/bin/env python3

with open("input.txt") as f:
    result = 0
    x = 0
    for line in f.read().splitlines():
        if line[x] == "💩":
            result += 1
        x = (x + 2) % len(line)
    print(result)
