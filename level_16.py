#!/bin/env python
# coding=utf-8
# http://huge:file@www.pythonchallenge.com/pc/return/mozart.html
# let me get this straight
import urllib
from itertools import groupby
# never use PIL 1.1.7 but Pillow 2.5+
from PIL import Image


PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + 'mozart.gif'


def download(url, cnt=0):
    return urllib.urlretrieve(url)[cnt]


def solve(fname):
    im = Image.open(fname)
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
    fname = download(url)
    answer = solve(fname)
    # romance

    # http://huge:file@www.pythonchallenge.com/pc/return/romance.html
