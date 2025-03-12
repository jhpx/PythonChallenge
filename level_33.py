#!/bin/env python
# coding=utf-8
# http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/beer.html
#
# If you are blinded by the light,
# remove its power, with its might.
# Then from the ashes, fair and square,
# another truth at you will glare.
import re
from io import BytesIO

import numpy as np
import requests
from PIL import Image

PREFIX = "http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/"
url = PREFIX + 'beer2.jpg'


def catch(text, pattern=r'<a href="(.*?)">', cnt=0):
    return re.findall(pattern, text, re.DOTALL)[cnt]


def solve(something):
    im = Image.open(BytesIO(something))
    im.show()
    # no, png

    url2 = PREFIX + 'beer2.png'
    im = Image.open(BytesIO(requests.get(url2).content))

    # use numpy to accelerate
    data = np.array(im.getdata())
    # use histogram to skip non-existing pixels
    histogram = im.histogram()

    hidden_images = []
    for value in range(254, -1, -1):
        if histogram[value] == 0:
            continue
        # Remove the brightest pixels
        data = data[data < value]
        # Reshape the array to a square image
        sq = np.sqrt(len(data))
        if sq.is_integer() and sq > 0:
            max_val = np.max(data)
            ashes = np.array([255 if v == max_val else 0 for v in data], dtype=np.uint8)
            image = Image.fromarray(ashes.reshape(int(sq), int(sq)))
            hidden_images.append(image)

    # combine the images
    total_width = hidden_images[0].width*len(hidden_images)
    max_height = hidden_images[0].height
    composite_image = Image.new('L', (total_width, max_height))
    x_offset = 0
    for img in hidden_images:
        composite_image.paste(img, (x_offset, 0))
        x_offset += img.width

    return composite_image


def plot(im):
    im.show()


if __name__ == "__main__":
    r = requests.get(url)
    something = r.content
    answer = solve(something)
    plot(answer)
    # gremlins

    # http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/gremlins.html
