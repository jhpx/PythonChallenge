#!/bin/env python
# coding=utf-8
# http://huge:file@www.pythonchallenge.com/pc/return/italy.html
# 100*100 = (100+99+99+98) + (...) + (2,1,1,0)
from io import BytesIO

import requests
from PIL import Image

PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + 'wire.png'


def solve(something):
    unknown = Image.new('RGB', (100, 100))
    im = Image.open(BytesIO(something))
    piv = unknown.load()
    i, j = 0, 0
    L = 99  # length of sprial edge, decrease by 2 for every circle
    N = 0  # count accessed pixels, increase by 4*L for every circle
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
    return unknown


def plot(im):
    im.show()


if __name__ == "__main__":
    r = requests.get(url)
    something = r.content
    answer = solve(something)
    plot(answer)
    # cat

    # http://huge:file@www.pythonchallenge.com/pc/return/cat.html
    # see the cat's name is uzi
    # http://huge:file@www.pythonchallenge.com/pc/return/uzi.html
