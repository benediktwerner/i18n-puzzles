#!/usr/bin/env python3

with open("input.txt") as f:
    result = 0
    for line in f.read().splitlines():
        if len(line) < 4 or len(line) > 12:
            continue
        if not any(c.isdigit() for c in line):
            continue
        if not any(c.islower() for c in line):
            continue
        if not any(c.isupper() for c in line):
            continue
        if not any(ord(c) > 127 for c in line):
            continue
        result += 1
    print(result)
