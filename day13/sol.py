#!/usr/bin/env python3

import re


def decode(s: str) -> list[str]:
    b = bytes.fromhex(s)

    if s.startswith("fffe") or s.startswith("feff"):
        return [b.decode("utf-16")]
    elif s.startswith("efbbbf"):
        return [b.decode("utf-8-sig")]

    result = []
    for encoding in ("utf-8", "utf-16-le", "utf-16-be", "latin-1"):
        try:
            decoded = b.decode(encoding)
        except:
            continue

        if not any(bad in decoded for bad in ("©", "\ufeff", "¶", "Ã¤", "Ã\x9f", "\0")):
            result.append(decoded)

    assert result, f"failed to decode {s}"
    return result


with open("input.txt") as f:
    words_encoded, riddle = map(str.splitlines, f.read().split("\n\n"))

words = []

for i, word in enumerate(words_encoded):
    words.extend([(i, w) for w in decode(word)])

result = 0

for line in riddle:
    pattern = line.strip()
    # print(pattern)
    results = []
    for i, word in words:
        if re.fullmatch(pattern, word):
            # print(word)
            results.append(i)
    assert len(results) == 1, results
    result += results[0] + 1

print(result)
