#!/bin/env python
# coding=utf-8
# http://huge:file@www.pythonchallenge.com/pc/return/italy.html
# 100*100 = (100+99+99+98) + (...
import urllib
# never use PIL 1.1.7 but Pillow 2.5+
from PIL import Image


PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + 'wire.png'


def download(url, cnt=0):
    return urllib.urlretrieve(url)[cnt]


def solve(fname):
    unknown = Image.new('RGB', (100, 100))
    im = Image.open(fname)
    piv = unknown.load()
    i, j = 0, 0
    L = 99  # length of sprial edge, decrease by 2 circle by circle
    N = 0  # count accessed pixels, increase by 4*L circle by circle
    for k, px in enumerate(im.getdata()):
        piv[i, j] = px
        if (k - N) // L == 0:  # right
            i += 1
        elif (k - N) // L == 1:  # down
            j += 1
        elif (k - N) // L == 2:  # left
            i -= 1
        elif (k - N + 1) // L == 3:  # up
            j -= 1
        elif (k - N + 1) // L == 4:  # nex circle
            i += 1
            N += 4 * L
            L -= 2
    unknown.show()


if __name__ == "__main__":
    fname = download(url)
    answer = solve(fname)
    # cat

    # http://huge:file@www.pythonchallenge.com/pc/return/cat.html
