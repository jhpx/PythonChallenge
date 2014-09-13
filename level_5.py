#!/bin/env python
# coding=utf-8
# Peak hell pronounced like 'pickle'.
import urllib
import contextlib
import re
import pickle

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'peak.html'


def catch(url, pattern=r'<!--(.*?)-->', cnt=0):
    with contextlib.closing(urllib.urlopen(url)) as page:
        return re.findall(pattern, page.read(), re.DOTALL)[cnt]


def solve(text):
    banner = pickle.load(urllib.urlopen(PREFIX + text))
    for line in banner:
        print "".join(ch * count for ch, count in line)


if __name__ == "__main__":
    pattern = r'<peakhell src="(.*?)"/>'
    text = catch(url, pattern)
    answer = solve(text)
    # channel

    # http://www.pythonchallenge.com/pc/def/channel.html
