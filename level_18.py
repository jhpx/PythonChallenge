#!/bin/env python
# coding=utf-8
# http://huge:file@www.pythonchallenge.com/pc/return/balloons.html
# Images inside hex deltas.
import urllib
from cStringIO import StringIO
# never use PIL 1.1.7 but Pillow 2.5+
from PIL import Image
import gzip
import difflib

PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + 'deltas.gz'


def download(url, cnt=0):
    return urllib.urlretrieve(url)[cnt]


def solve(fname):
    with gzip.GzipFile(fname) as file:
        data1 = []
        data2 = []
        for line in file.read().splitlines():
            if line[:54].strip():
                data1.append(line[:54].replace(' ', '').decode('hex'))
            if line[55:].strip():
                data2.append(line[55:].replace(' ', '').decode('hex'))

    s = difflib.SequenceMatcher(None, data1, data2)
    # Time consuming: ndiff() > SequenceMatcher.get_opcodes()
    common = delta1 = delta2 = ""
    for tag, i1, i2, j1, j2 in s.get_opcodes():
        if tag == 'equal':
            common += "".join(data1[i1:i2])
        elif tag == 'insert':
            delta1 += "".join(data2[j1:j2])
        elif tag == 'delete':
            delta2 += "".join(data1[i1:i2])
        elif tag == 'replace':
            delta1 += "".join(data2[j1:j2])
            delta2 += "".join(data1[i1:i2])

    im1 = Image.open(StringIO("".join(common)))
    im2 = Image.open(StringIO("".join(delta1)))
    im3 = Image.open(StringIO("".join(delta2)))
    width = max(im1.size[0], im2.size[0], im3.size[0])
    height = im1.size[1] + im2.size[1] + im3.size[1]
    background = Image.new(im1.mode, (width, height))
    background.paste(im1, (0, 0))
    background.paste(im2, (0, im1.size[1]))
    background.paste(im3, (0, im1.size[1] + im2.size[1]))
    background.show()


if __name__ == "__main__":
    fname = download(url)
    answer = solve(fname)
    # ../hex/bin.html, butter, fly

    # http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html
