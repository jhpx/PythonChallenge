#!/bin/env python
# coding=utf-8
# No url
# Decompress, decompress and reverse.
# @see http://tools.ietf.org/html/rfc1950#section-2.2
# @see http://en.wikipedia.org/wiki/Bzip2#File_format
import codecs
import zipfile
from io import BytesIO

import requests

PREFIX = "http://butter:fly@www.pythonchallenge.com/pc/hex/"
url = PREFIX + 'unreal.jpg'
ARCH_POS = 1152983631
PASSWD = b'redavni'


def prepare():
    headers = {'Range': 'bytes={}-'.format(ARCH_POS)}
    r = requests.get(url, headers=headers)
    with zipfile.ZipFile(BytesIO(r.content), 'r') as zip:
        return zip.read('package.pack', PASSWD)


def solve(pack):
    zlib_header = b'\x78\x9c'
    bz2_header = b'BZh'
    result = []
    while (True):
        if pack.startswith(zlib_header):
            pack = codecs.decode(pack, 'zlib')
            result.append(' ')
        elif pack.startswith(bz2_header):
            pack = codecs.decode(pack, 'bz2')
            result.append('#')
        elif pack.endswith(zlib_header[::-1]):
            pack = pack[::-1]
            result.append('\n')
        else:
            break
    return "".join(result)


if __name__ == "__main__":
    pack = prepare()
    answer = solve(pack)
    print(answer)
    # copper

    # http://butter:fly@www.pythonchallenge.com/pc/hex/copper.html
