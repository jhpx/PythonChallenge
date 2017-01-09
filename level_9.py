#!/bin/env python
# coding=utf-8
# http://huge:file@www.pythonchallenge.com/pc/return/good.html
# Connect the dots.
import requests
import re
# never use PIL 1.1.7 but Pillow 2.5+
from PIL import Image
from PIL import ImageDraw

PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + 'good.html'


def catch(text, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, text, re.DOTALL)[cnt]


def solve(something):
    first, second = re.findall(
        r'first:(.*?)second:(.*)', something.replace('\n', ''))[0]
    L1 = list(map(int, first.split(',')))
    L2 = list(map(int, second.split(',')))

    im = Image.new("RGB", (640, 480))
    draw = ImageDraw.Draw(im)
    draw.polygon(L1)
    draw.polygon(L2)

    im.show()


if __name__ == "__main__":
    r = requests.get(url)
    something = catch(r.text, cnt=1)
    answer = solve(something)
    # bull graph

    # http://huge:file@www.pythonchallenge.com/pc/return/bull.html
