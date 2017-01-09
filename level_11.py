#!/bin/env python
# coding=utf-8
# http://huge:file@www.pythonchallenge.com/pc/return/5808.html
# Odd even of an image.
import requests
from io import BytesIO
# never use PIL 1.1.7 but Pillow 2.5+
from PIL import Image

PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + 'cave.jpg'


def solve(something):
    im = Image.open(BytesIO(something))
    data = list(im.getdata())
    im.putdata(data[::2] + data[1::2])
    im.show()


if __name__ == "__main__":
    r = requests.get(url)
    something = r.content
    answer = solve(something)
    # evil

    # http://huge:file@www.pythonchallenge.com/pc/return/evil.html
