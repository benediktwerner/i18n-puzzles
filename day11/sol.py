#!/usr/bin/env python3

UPPER = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
LOWER = "αβγδεζηθικλμνξοπρστυφχψω"

NAMES = [
    "Οδυσσευσ",
    "Οδυσσεωσ",
    "Οδυσσει",
    "Οδυσσεα",
    "Οδυσσευ",
]


def rotate(line: str) -> str:
    result = ""
    for c in line:
        if c in UPPER:
            result += UPPER[(UPPER.index(c) + 1) % len(UPPER)]
        elif c in LOWER:
            result += LOWER[(LOWER.index(c) + 1) % len(LOWER)]
        else:
            result += c
    return result


with open("input.txt") as f:
    result = 0
    for line in f.read().replace("ς", "σ").splitlines():
        for i in range(24):
            if any(name in line for name in NAMES):
                result += i
                break

            line = rotate(line)
    print(result)
