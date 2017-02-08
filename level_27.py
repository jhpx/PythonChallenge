#!/bin/env python
# coding=utf-8
# http://butter:fly@www.pythonchallenge.com/pc/hex/speedboat.html
# Difference between data and palette[data].
# @see https://www.w3.org/Graphics/GIF/spec-gif87.txt
import requests
from io import BytesIO
from PIL import Image
import bz2

PREFIX = "http://butter:fly@www.pythonchallenge.com/pc/hex/"
url = PREFIX + 'zigzag.gif'


def solve(something):
    im = Image.open(BytesIO(something))
    palette = im.getpalette()
    palette_gray = palette[::3]
    data1 = list(im.getdata())

    im2 = Image.new("L", im.size, 255)
    data2 = [255] * len(data1)

    exceptions = []
    expected = None
    for i, p in enumerate(data1):
        if expected is not None and p != expected:
            exceptions.append(p)
            data2[i] = 0
        expected = palette_gray[p]
    im2.putdata(data2)
    im2.show()
    # not key word
    # busy 2

    allwords = bz2.decompress(bytes(exceptions)).decode().split(' ')
    import keyword
    answer = []
    for word in allwords:
        if not keyword.iskeyword(word) and word != 'print' and word != 'exec' and word not in answer:
            answer.append(word)
    return answer


if __name__ == "__main__":
    r = requests.get(url)
    something = r.content
    answer = solve(something)
    # ../ring/bell.html, repeat, switch
    print(",".join(answer))
    # http://repeat:switch@www.pythonchallenge.com/pc/ring/bell.html
