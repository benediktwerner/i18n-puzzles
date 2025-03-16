#!/usr/bin/env python3

from functools import cache
import unicodedata
import bcrypt


@cache
def bcrypt_check(pwd, hash):
    return bcrypt.checkpw(pwd.encode(), hash.encode())


def variations(s):
    result = [""]
    for c in unicodedata.normalize("NFC", s):
        decomposed = unicodedata.normalize("NFD", c)
        if decomposed == c:
            result = [r + c for r in result]
        else:
            result = [r + c for r in result] + [r + decomposed for r in result]
    return result


with open("input.txt") as f:
    pwds, attempts = f.read().split("\n\n")


result = 0
users = {user: hash for user, hash in map(str.split, pwds.splitlines())}

for user, pwd in map(str.split, attempts.splitlines()):
    if any(bcrypt_check(v, users[user]) for v in variations(pwd)):
        result += 1

print(result)
