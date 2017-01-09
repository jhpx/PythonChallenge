#!/bin/env python
# coding=utf-8
# http://www.pythonchallenge.com/pc/def/peak.html
# Peak hell pronounced like 'pickle'.
import requests
import re
import pickle
from io import BytesIO

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'peak.html'


def catch(text, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, text, re.DOTALL)[cnt]


def solve(url):
    print("Unpacking the message:")
    something = requests.get(url).content
    banner = pickle.load(BytesIO(something))
    for line in banner:
        print("".join(ch * count for ch, count in line))


if __name__ == "__main__":
    r = requests.get(url)
    src = catch(r.text, r'<peakhell src="(.*?)"/>')
    answer = solve(PREFIX + src)
    # channel

    # http://www.pythonchallenge.com/pc/def/channel.html
