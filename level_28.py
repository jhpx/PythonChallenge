#!/bin/env python
# coding=utf-8
# http://repeat:switch@www.pythonchallenge.com/pc/ring/bell.html
# Difference between next(green) and next(green).
from io import BytesIO

import requests
from PIL import Image

PREFIX = "http://repeat:switch@www.pythonchallenge.com/pc/ring/"
url = PREFIX + 'bell.png'


def solve(something):
    im = Image.open(BytesIO(something))
    red, green, blue = im.split()
    data1 = list(green.getdata())[::2]
    data2 = list(green.getdata())[1::2]
    differences = [abs(a - b) for a, b in zip(data1, data2) if a != b]
    result = filter(lambda x: x != 42, differences)
    answer = bytes(result).decode()
    return answer


if __name__ == "__main__":
    r = requests.get(url)
    something = r.content
    answer = solve(something)

    print(answer)
    # whodunnit().split()[0] ?

    # Python was developed by Guido van Rossum

    # http://repeat:switch@www.pythonchallenge.com/pc/ring/guido.html
