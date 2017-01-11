#!/bin/env python
# coding=utf-8
# http://www.pythonchallenge.com/pc/def/oxygen.html
# ASCII inside an image.
import re
from io import BytesIO

import requests
from PIL import Image

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'oxygen.png'


def solve(something):
    im = Image.open(BytesIO(something))
    width, height = im.size

    upper = -1
    for j in range(height):
        for i in range(0, width, 7):
            px = im.getpixel((i, j))
            if px[0] == px[1] == px[2]:
                continue
            elif i > 0:
                if upper == -1:
                    upper = j
                    left = 0
                lower = j + 1
                right = i
            break
    box = (left, upper, right, lower)
    print("Selecting the message area: " + str(box))
    samplesize = ((right - left + 1) // 7, 1)
    text = im.crop(box).convert('L').resize(samplesize).tobytes().decode()
    hidden = "".join([chr(int(x)) for x in re.findall(r'\d+', text)])
    print("The hidden message is: {}\n".format(hidden))
    return hidden


if __name__ == "__main__":
    r = requests.get(url)
    something = r.content
    answer = solve(something)
    # integrity
    print(PREFIX + answer + '.html')
    # http://www.pythonchallenge.com/pc/def/integrity.html
