#!/bin/env python
# coding=utf-8
# No url
# Decompress, decompress and reverse.
# @see http://tools.ietf.org/html/rfc1950#section-2.2
# @see http://en.wikipedia.org/wiki/Bzip2#File_format
import urllib2
from cStringIO import StringIO
import zipfile

PREFIX = "http://www.pythonchallenge.com/pc/hex/"
url = PREFIX + 'unreal.jpg'


def prepare():
    request = urllib2.Request(url)
    base64string = 'butter:fly'.encode('base64').rstrip()
    request.add_header("Authorization", "Basic " + base64string)
    arch_pos = 1152983631
    passwd = 'redavni'
    request.headers['Range'] = 'bytes={}-'.format(arch_pos)
    resp = urllib2.urlopen(request)
    with zipfile.ZipFile(StringIO(resp.read()), 'r') as zip:
        return zip.read('package.pack', passwd)


def solve(pack):
    zlib_header = '\x78\x9c'
    bz2_header = 'BZh'
    result = ''
    while(True):
        if pack.startswith(zlib_header):
            pack = pack.decode('zlib')
            result += ' '
        elif pack.startswith(bz2_header):
            pack = pack.decode('bz2')
            result += '#'
        elif pack.endswith(zlib_header[::-1]):
            pack = pack[::-1]
            result += '\n'
        else:
            print result
            break


if __name__ == "__main__":
    pack = prepare()
    answer = solve(pack)
    # copper

    # http://butter:fly@www.pythonchallenge.com/pc/hex/copper.html
