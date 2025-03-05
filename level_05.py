#!/bin/env python
# coding=utf-8
# http://www.pythonchallenge.com/pc/def/peak.html
# Peak hell pronounced like 'pickle'.
import pickle
import re
from io import BytesIO

import requests

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'peak.html'


def catch(text, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, text, re.DOTALL)[cnt]


def solve(url):
    print("Unpacking the message:")
    something = requests.get(url).content
    banner = pickle.load(BytesIO(something))
    result_lines = []
    for line in banner:
        result_lines.append("".join(ch * count for ch, count in line))
    return "\n".join(result_lines)


if __name__ == "__main__":
    r = requests.get(url)
    src = catch(r.text, r'<peakhell src="(.*?)"/>')
    answer = solve(PREFIX + src)
    print(answer)
    # channel

    # http://www.pythonchallenge.com/pc/def/channel.html
