#!/usr/bin/env python3

from functools import cache
import unicodedata
import bcrypt
import concurrent.futures


def variations(s: str) -> list[str]:
    result = [""]
    for c in s:
        decomposed = unicodedata.normalize("NFD", c)
        if decomposed == c:
            result = [r + c for r in result]
        else:
            result = [r + c for r in result] + [r + decomposed for r in result]
    return result


@cache
def bcrypt_check(pwd: str, hash: str) -> bool:
    return bcrypt.checkpw(pwd.encode(), hash.encode())


def check_pwd(user, pwd):
    pwd = unicodedata.normalize("NFC", pwd)
    hash, opt = users[user]
    if opt:
        return pwd == hash
    elif any(bcrypt_check(v, hash) for v in variations(pwd)):
        users[user] = (pwd, True)
        return True
    return False


with open("input.txt") as f:
    pwds, attempts = f.read().split("\n\n")


users = {user: (hash, False) for user, hash in map(str.split, pwds.splitlines())}

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [
        executor.submit(check_pwd, user, pwd)
        for user, pwd in map(str.split, attempts.splitlines())
    ]
    print(sum(future.result() for future in futures))
