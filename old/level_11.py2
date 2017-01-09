#!/bin/env python
# coding=utf-8
# http://huge:file@www.pythonchallenge.com/pc/return/5808.html
# Odd even of an image.
import urllib
# never use PIL 1.1.7 but Pillow 2.5+
from PIL import Image

PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + 'cave.jpg'


def download(url, cnt=0):
    return urllib.urlretrieve(url)[cnt]


def solve(fname):
    im = Image.open(fname)
    data = list(im.getdata())
    im.putdata(data[::2] + data[1::2])
    im.show()


if __name__ == "__main__":
    fname = download(url)
    answer = solve(fname)
    # evil

    # http://huge:file@www.pythonchallenge.com/pc/return/evil.html
