#!/bin/env python
# coding=utf-8
# http://huge:file@www.pythonchallenge.com/pc/return/balloons.html
# Images in difflib.
import difflib
import gzip
from io import BytesIO

import requests
from PIL import Image

PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + 'deltas.gz'


def solve(something):
    with gzip.GzipFile(fileobj=BytesIO(something)) as file:
        data1 = []
        data2 = []
        for line in file.read().splitlines():
            if line[:54].strip():
                data1.append(bytes.fromhex(line[:54].decode()))
            if line[55:].strip():
                data2.append(bytes.fromhex(line[55:].decode()))

    s = difflib.SequenceMatcher(None, data1, data2)
    # Time consuming: ndiff() > SequenceMatcher.get_opcodes()
    common = delta1 = delta2 = b''
    for tag, i1, i2, j1, j2 in s.get_opcodes():
        if tag == 'equal':
            common += b''.join(data1[i1:i2])
        elif tag == 'insert':
            delta1 += b''.join(data2[j1:j2])
        elif tag == 'delete':
            delta2 += b''.join(data1[i1:i2])
        elif tag == 'replace':
            delta1 += b''.join(data2[j1:j2])
            delta2 += b''.join(data1[i1:i2])

    im1 = Image.open(BytesIO(common))
    im2 = Image.open(BytesIO(delta1))
    im3 = Image.open(BytesIO(delta2))
    width = max(im1.size[0], im2.size[0], im3.size[0])
    height = im1.size[1] + im2.size[1] + im3.size[1]
    background = Image.new(im1.mode, (width, height))
    background.paste(im1, (0, 0))
    background.paste(im2, (0, im1.size[1]))
    background.paste(im3, (0, im1.size[1] + im2.size[1]))
    background.show()


if __name__ == "__main__":
    r = requests.get(url)
    something = r.content
    answer = solve(something)
    # ../hex/bin.html, butter, fly

    # http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html
