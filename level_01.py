#!/bin/env python
# coding=utf-8
# http://www.pythonchallenge.com/pc/def/274877906944.html
# Decrypt a string.
import re

import requests

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'map.html'


def catch(text, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, text, re.DOTALL)[cnt]


def decrypter(str):
    """Trim the string and move each alphabetic character by 2."""

    def move2(c):
        if re.match(r'[a-z]', c):
            return chr(ord('a') + (ord(c) - ord('a') + 2) % 26)
        else:
            return c

    return "".join(map(move2, str.strip()))


def solve(something):
    print('Decrypt the hint:')
    print(decrypter(something))
    print('Decrypt the url:')
    result = decrypter('map')
    print('map -> ' + result)
    print()
    return result


if __name__ == "__main__":
    r = requests.get(url)
    something = catch(r.text, r'<font color="#f000f0">(.*?)<')
    answer = solve(something)
    # ocr
    print(PREFIX + answer + '.html')
    # http://www.pythonchallenge.com/pc/def/ocr.html
