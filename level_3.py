#!/bin/env python
# coding=utf-8
# Regular expression.
import urllib
import contextlib
import re


PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'equality.html'


def catch(url, pattern=r'<!--(.*?)-->', cnt=0):
    with contextlib.closing(urllib.urlopen(url)) as page:
        return re.findall(pattern, page.read(), re.DOTALL)[cnt]


def solve(text):
    return "".join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', text))


if __name__ == "__main__":
    text = catch(url)
    answer = solve(text)
    # linkedlist
    print PREFIX + answer + '.php'
    # http://www.pythonchallenge.com/pc/def/linkedlist.php
