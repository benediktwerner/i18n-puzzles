#!/usr/bin/env python3

import math
import re

import unidecode


def get_middle_number(key_fn) -> int:
    s = sorted(names, key=key_fn)
    return int(s[len(s) // 2].split(": ")[1])


def english_key(name):
    name = unidecode.unidecode(name.lower().replace("Æ", "AE"))
    return re.sub(r"[^a-z,]+", "", name)


def swedish_key(name):
    name = unidecode.unidecode(
        name.upper()
        .replace("Å", "a")  # lower case letters will be sorted after upper case letters
        .replace("Æ", "b")
        .replace("Ä", "b")
        .replace("Ø", "c")
        .replace("Ö", "c")
    )
    return re.sub(r"[^A-Za-z,]+", "", name)


def dutch_key(name):
    name = re.sub(r"^[a-z ]+", "", name)
    name = unidecode.unidecode(name.lower().replace("æ", "ae"))
    return re.sub(r"[^a-z,]+", "", name)


with open("input.txt") as f:
    names = f.read().splitlines()

print(math.prod(get_middle_number(fn) for fn in [english_key, swedish_key, dutch_key]))
