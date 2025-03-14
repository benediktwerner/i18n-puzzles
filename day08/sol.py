#!/usr/bin/env python3

from unidecode import unidecode


VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

result = 0

with open("input.txt") as f:
    for line in f.read().splitlines():
        line = unidecode(line)
        if len(line) < 4 or len(line) > 12:
            continue
        if not any(c.isdigit() for c in line):
            continue
        if not any(c.lower() in VOWELS for c in line):
            continue
        if not any(c.lower() in CONSONANTS for c in line):
            continue
        if len(set(line.lower())) != len(line):
            continue
        result += 1

print(result)
