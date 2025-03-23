#!/usr/bin/env python3

with open("input.txt", encoding="cp437") as f:
    data = f.read()

with open("input-utf8.txt", "w") as f:
    f.write(data)
