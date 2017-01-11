#!/bin/env python
# coding=utf-8
# http://butter:fly@www.pythonchallenge.com/pc/hex/copper.html
# Draw points according to the image sequence.
from io import BytesIO

import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageSequence

PREFIX = "http://butter:fly@www.pythonchallenge.com/pc/hex/"
url = PREFIX + 'white.gif'

def solve(something):
    im = Image.open(BytesIO(something))
    unknown = Image.new('RGB', im.size)
    draw = ImageDraw.Draw(unknown)
    cx, cy = 0, 100
    for frame in ImageSequence.Iterator(im):
        left, upper, _, _ = frame.getbbox()
        dx = (left - 100) // 2
        dy = (upper - 100) // 2
        if cx:
            draw.point((cx, cy))
        cx += dx
        cy += dy
        if dx == dy == 0:
            cx += 25
            cy = 100
    unknown.show()


if __name__ == "__main__":
    r = requests.get(url)
    something = r.content
    answer = solve(something)
    # bonus

    # http://butter:fly@www.pythonchallenge.com/pc/hex/bonus.html
