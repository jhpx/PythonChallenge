#!/bin/env python
# coding=utf-8
# http://huge:file@www.pythonchallenge.com/pc/return/evil.html
# Deal cards? Deal evils? 1,2,3,4,5.
import requests
from io import BytesIO
# never use PIL 1.1.7 but Pillow 2.5+
from PIL import Image
from PIL import ImageFile

PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + 'evil2.gfx'


def solve(something):
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    background = Image.new('RGB', (640, 96))
    cur_width = 0
    for i in range(5):
        piece = something[i::5]
        im = Image.open(BytesIO(piece)).resize((640 // 5, 96))
        background.paste(im, (cur_width, 0))
        cur_width += im.size[0]
    background.show()


if __name__ == "__main__":
    r = requests.get(url)
    something = r.content
    answer = solve(something)
    # disproportional

    # http://huge:file@www.pythonchallenge.com/pc/return/disproportional.html
