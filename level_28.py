#!/bin/env python
# coding=utf-8
# http://repeat:switch@www.pythonchallenge.com/pc/ring/bell.html
# Difference between next(green) and next(green).
from io import BytesIO

import requests
from PIL import Image

PREFIX = "http://repeat:switch@www.pythonchallenge.com/pc/ring/"
url = PREFIX + 'bell.png'


def paired(data):
    data = iter(data)
    while True:
        yield next(data), next(data)


def solve(something):
    im = Image.open(BytesIO(something))
    red, green, blue = im.split()
    result = []
    for a, b in paired(green.getdata()):
        diff = abs(a - b)
        if diff != 42:
            result.append(diff)
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
