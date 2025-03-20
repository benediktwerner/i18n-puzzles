#!/usr/bin/env python3

# 10,000 Mo (毛) = 1 Shaku (尺) = 10/33 m
# 1 Mo (毛) = 10/330000 m
# 1 Mo^2 (毛) = 1/1089000000 m^2
MO_SQUARED_TO_METERS_SQUARED = 1089000000

# 10,000 Mo (毛) = 1 Shaku (尺)
# 1000 Rin (厘) = 1 Shaku (尺)
# 100 Bu (分) = 1 Shaku (尺)
# 10 Sun (寸) = 1 Shaku (尺)
# 1 Ken (間) = 6 Shaku (尺)
# 1 Jo (丈) = 10 Shaku (尺)
# 1 Cho (町) = 360 Shaku (尺)
# 1 Ri (里) = 12960 Shaku (尺)
UNITS_TO_MO = {
    "毛": 1,
    "厘": 10,
    "分": 100,
    "寸": 1000,
    "尺": 10_000,
    "間": 6 * 10_000,
    "丈": 10 * 10_000,
    "町": 360 * 10_000,
    "里": 12960 * 10_000,
}


# 1 一 (ichi)
# 2 二 (ni)
# 3 三 (san)
# 4 四 (yon)
# 5 五 (go)
# 6 六 (roku)
# 7 七 (nana)
# 8 八 (hachi)
# 9 九 (kyu)
# 10 十 (ju)
# 100 百 (hyaku)
# 1000 千 (sen)
# 10,000 万 (man)
# 100,000,000 億 (ichioku)
NUMBERS = {
    "一": 1,
    "二": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
    "十": 10,
    "百": 100,
    "千": 1000,
    "万": 10_000,
    "億": 100_000_000,
}


def decode_as_mo(s: str) -> int:
    *digits, unit = s
    result = 0
    myriad_chunk = 0
    chunk = 0
    for d in digits:
        if d in "億万":
            result += (myriad_chunk + chunk) * NUMBERS[d]
            myriad_chunk = 0
            chunk = 0
        elif d in "十百千":
            myriad_chunk += (chunk or 1) * NUMBERS[d]
            chunk = 0
        else:
            chunk = NUMBERS[d]
    return (result + myriad_chunk + chunk) * UNITS_TO_MO[unit]


result = 0

with open("input.txt") as f:
    for line in f.read().splitlines():
        width, height = map(decode_as_mo, line.split(" × "))
        result += width * height // MO_SQUARED_TO_METERS_SQUARED

print(result)
