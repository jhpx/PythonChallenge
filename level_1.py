#!/bin/env python
# coding=utf-8
# Decrypt a string.
import urllib
import contextlib
import re

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'map.html'


def catch(url, pattern=r'<!--(.*?)-->', cnt=0):
    with contextlib.closing(urllib.urlopen(url)) as page:
        return re.findall(pattern, page.read(), re.DOTALL)[cnt]


def move2(c):
    if re.match(r'[a-z]', c):
        return chr(ord('a') + (ord(c) - ord('a') + 2) % 26)
    else:
        return c


def decrypter(str):
    """just move 2"""
    return "".join(map(move2, str))


if __name__ == "__main__":
    pattern = r'<font color="#f000f0">(.*?)<'
    ciphertext = catch(url, pattern)
    print decrypter(ciphertext)
    answer = decrypter('map')
    # ocr
    print PREFIX + answer + '.html'
    # http://www.pythonchallenge.com/pc/def/ocr.html
