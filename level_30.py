#!/bin/env python
# coding=utf-8
# http://repeat:switch@www.pythonchallenge.com/pc/ring/yankeedoodle.html
# Floats, image, formula.

import requests
from PIL import Image

PREFIX = "http://repeat:switch@www.pythonchallenge.com/pc/ring/"
url = PREFIX + 'yankeedoodle.csv'


def factor(n):
    "Adapted from http://www.math.utah.edu/~carlson/notes/python.pdf"
    d = 2
    factors = []
    while not n % d:
        factors.append(d)
        n //= d
    d = 3
    while n > 1 and d * d <= n:
        if not n % d:
            factors.append(d)
            n //= d
        else:
            d += 2
    if n > 1:
        factors.append(n)
    return factors


def perthree(data):
    data = iter(data)
    while True:
        yield next(data), next(data), next(data)


def solve(something):
    text = something.replace('\n', ' ').split(', ')
    values = [float(p) for p in text]
    size = factor(len(values))
    im = Image.new("F", size)
    im.putdata(values, 256)
    im = im.transpose(Image.FLIP_LEFT_RIGHT)
    im = im.transpose(Image.ROTATE_90)
    im.show()
    # n=str(x[i])[5]
    # +str(x[i+1])[5]
    # +str(x[i+2])[6]

    result = []
    for i in range(0, len(text), 3):
        group = text[i:i + 3]
        if len(group) != 3:
            break
        a, b, c = group
        result.append(int(a[5] + b[5] + c[6]))
    message = bytes(result).decode()
    return message


if __name__ == "__main__":
    r = requests.get(url)
    something = r.text
    answer = solve(something)

    print(answer)
    # So, you found the hidden message.
    # There is lots of room here for a long message, but we only need very little space to say "look at grandpa", so the rest is just garbage.

    # http://repeat:switch@www.pythonchallenge.com/pc/ring/grandpa.html
