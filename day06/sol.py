#!/usr/bin/env python3

with open("input.txt") as f:
    words, grid = f.read().split("\n\n")

words = words.splitlines()

for i, word in enumerate(words, 1):
    if i % 3 == 0:
        word = word.encode("latin-1").decode()
    if i % 5 == 0:
        word = word.encode("latin-1").decode()
    words[i - 1] = word

result = 0

for line in grid.splitlines():
    line = line.strip()
    length = len(line)
    char = line.strip(".")
    index = line.index(char)

    for i, word in enumerate(words, 1):
        if len(word) == length and word[index] == char:
            result += i

print(result)
