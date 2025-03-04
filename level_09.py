#!/bin/env python
# coding=utf-8
# http://huge:file@www.pythonchallenge.com/pc/return/good.html
# Connect the dots.
import re

import requests
from PIL import Image
from PIL import ImageDraw

PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + 'good.html'


def catch(text, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, text, re.DOTALL)[cnt]


def solve(something):
    first, second = re.findall(
        r'first:(.*?)second:(.*)', something.replace('\n', ''))[0]
    l1 = list(map(int, first.split(',')))
    l2 = list(map(int, second.split(',')))

    return l1, l2


def plot(l1, l2):
    im = Image.new("RGB", (640, 480))
    draw = ImageDraw.Draw(im)
    draw.polygon(l1)
    draw.polygon(l2)

    im.show()


if __name__ == "__main__":
    r = requests.get(url)
    something = catch(r.text, cnt=1)
    answer = solve(something)
    plot(*answer)
    # bull graph

    # http://huge:file@www.pythonchallenge.com/pc/return/bull.html
