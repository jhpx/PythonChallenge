#!/bin/env python
# coding=utf-8
# Deal cards? Deal evils?
import urllib
from cStringIO import StringIO
# never use PIL 1.1.7 but Pillow 2.5+
from PIL import Image
from PIL import ImageFile


PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + 'evil2.gfx'


def download(url, cnt=0):
    return urllib.urlretrieve(url)[cnt]


def solve(fname):
    s = open(fname, "rb").read()
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    background = Image.new('RGB', (640, 96))
    cur_width = 0
    for i in range(5):
        piece = s[i::5]
        im = Image.open(StringIO(piece)).resize((640 / 5, 96))
        background.paste(im, (cur_width, 0))
        cur_width += im.size[0]
    background.show()


if __name__ == "__main__":
    fname = download(url)
    answer = solve(fname)
    # disproportional

    # http://huge:file@www.pythonchallenge.com/pc/return/disproportional.html
