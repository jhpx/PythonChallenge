#!/bin/env python
# coding=utf-8
# http://www.pythonchallenge.com/pc/def/integrity.html
# Bee is busy.
import bz2
import re

import requests

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'integrity.html'


def catch(text, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, text, re.DOTALL)[cnt]


def solve(something):
    un_bz2 = re.findall(r'un: \'(.*?)\'', something)[0].encode().decode('unicode_escape').encode('latin1')
    pw_bz2 = re.findall(r'pw: \'(.*?)\'', something)[0].encode().decode('unicode_escape').encode('latin1')
    un = bz2.decompress(un_bz2).decode()
    pw = bz2.decompress(pw_bz2).decode()
    print("username: " + un)
    print("password: " + pw)
    print()
    return un, pw


if __name__ == "__main__":
    r = requests.get(url)
    something = catch(r.text)
    un, pw = solve(something)
    # huge, file
    print("http://{}:{}@".format(un, pw) + PREFIX[7:-4] + 'return/good.html')
    # http://huge:file@www.pythonchallenge.com/pc/return/good.html
