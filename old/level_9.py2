#!/bin/env python
# coding=utf-8
# http://huge:file@www.pythonchallenge.com/pc/return/good.html
# Connect the dots.
import urllib
import contextlib
import re
# never use PIL 1.1.7 but Pillow 2.5+
from PIL import Image
from PIL import ImageDraw

PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + 'good.html'


def catch(url, pattern=r'<!--(.*?)-->', cnt=0):
    with contextlib.closing(urllib.urlopen(url)) as page:
        return re.findall(pattern, page.read(), re.DOTALL)[cnt]


def solve(text):
    first, second = re.findall(
        r'first:(.*?)second:(.*)', text.replace('\n', ''))[0]
    L1 = map(int, first.split(','))
    L2 = map(int, second.split(','))

    im = Image.new("RGB", (640, 480))
    draw = ImageDraw.Draw(im)
    draw.polygon(L1)
    draw.polygon(L2)

    im.show()


if __name__ == "__main__":
    text = catch(url, cnt=1)
    answer = solve(text)
    # bull graph

    # http://huge:file@www.pythonchallenge.com/pc/return/bull.html
