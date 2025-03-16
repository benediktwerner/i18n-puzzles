#!/usr/bin/env python3

from functools import cache
import unicodedata
import bcrypt
import concurrent.futures


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


def check_pwd(user, pwd):
    return any(bcrypt_check(v, users[user]) for v in variations(pwd))


with open("input.txt") as f:
    pwds, attempts = f.read().split("\n\n")


users = {user: hash for user, hash in map(str.split, pwds.splitlines())}

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [
        executor.submit(check_pwd, user, pwd)
        for user, pwd in map(str.split, attempts.splitlines())
    ]
    print(sum(future.result() for future in futures))
