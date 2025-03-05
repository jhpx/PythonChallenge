#!/bin/env python
# coding=utf-8
# http://repeat:switch@www.pythonchallenge.com/pc/ring/grandpa.html
# Google the grandpa rock and find the differences between two Mandelbrot images.
# @see https://en.wikipedia.org/wiki/Mandelbrot_set
import re
from io import BytesIO

import requests
from PIL import Image
from sympy import primefactors

# First google the picture.
# Koh Samui
# Thailand
# http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/grandpa.html

PREFIX = "http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/"
url1 = PREFIX + 'grandpa.html'
url2 = PREFIX + 'mandelbrot.gif'


def catch(text, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, text, re.DOTALL)[cnt]


def mandelbrot(left, top, width, height, max, size):
    xstep = width / size[0]
    ystep = height / size[1]
    for y in range(size[1] - 1, -1, -1):
        for x in range(size[0]):
            c = complex(left + x * xstep, top + y * ystep)
            z = 0 + 0j
            for i in range(max):
                z = z * z + c
                if abs(z) > 2:
                    break
            yield i


def solve(page, picture):
    ufos = Image.open(BytesIO(picture))

    pattern = r'<window left="(\d+\.\d+)" top="(\d+\.\d+)" width="(\d+\.\d+)" height="(\d+\.\d+)"/>'
    (left, top, width, height) = tuple(map(float, catch(page, pattern)))
    pattern = r'<option iterations="(\d+)"/>'
    iterations = int(catch(page, pattern))

    mandel = ufos.copy()
    mandel.putdata(list(mandelbrot(left, top, width, height, iterations, ufos.size)))

    differences = [a - b for a, b in zip(ufos.getdata(), mandel.getdata()) if a != b]

    plot = Image.new('L', primefactors(len(differences)))
    plot.putdata([(i < 16) and 255 or 0 for i in differences])

    return plot


def plot(im):
    im.show()


if __name__ == "__main__":
    r1 = requests.get(url1)
    r2 = requests.get(url2)
    page = r1.text
    picture = r2.content
    answer = solve(page, picture)
    plot(answer)
    # Google this plot and the answer is Arecibo message
    # https://en.wikipedia.org/wiki/Arecibo_message

    # http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/arecibo.html
