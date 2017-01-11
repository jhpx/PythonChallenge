#!/bin/env python
# coding=utf-8
# http://huge:file@www.pythonchallenge.com/pc/return/mozart.html
# Let me get #FF00FF straight.
from io import BytesIO
from itertools import groupby

import requests
from PIL import Image

PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + 'mozart.gif'


def solve(something):
    im = Image.open(BytesIO(something))
    width, height = im.size
    p = list(im.getdata())

    sample = p[:width]
    maxlen = 0
    for (k, v) in groupby(sample):
        curlen = len(list(v))
        if curlen > maxlen:
            maxlen = curlen
            separator = k
    # separator = 195

    unknown = im.copy()
    data = []
    for j in range(height):
        line = p[j * width:j * width + width]
        index = line.index(separator)
        data += line[index:] + line[:index]
    unknown.putdata(data)
    unknown.show()


if __name__ == "__main__":
    r = requests.get(url)
    something = r.content
    answer = solve(something)
    # romance

    # http://huge:file@www.pythonchallenge.com/pc/return/romance.html
