#!/bin/env python
# coding=utf-8
# http://butter:fly@www.pythonchallenge.com/pc/hex/idiot2.html
# HTTP/1.1 206 Partial content
# @see http://tools.ietf.org/html/rfc2616#section-14.16
import urllib2
import re
from cStringIO import StringIO
import zipfile

PREFIX = "http://www.pythonchallenge.com/pc/hex/"
url = PREFIX + 'unreal.jpg'


def explore(request, reo,  next, reverse=False):
    while(True):
        request.headers['Range'] = 'bytes={}-'.format(next)
        try:
            resp = urllib2.urlopen(request)
        except urllib2.HTTPError, err:
            print "HTTP Error {}:{}\n".format(err.code, err.msg)
            break
        msg = resp.read()
        print "{}:{}".format(next, msg.strip())
        start, end, size = reo.findall(resp.info()['content-range'])[0]
        if (reverse):
            next = int(start) - 1
        else:
            next = int(end) + 1

    return msg


def solve():
    request = urllib2.Request(url)
    base64string = 'butter:fly'.encode('base64').rstrip()
    request.add_header("Authorization", "Basic " + base64string)
    request.add_header("Range", '')

    reo = re.compile('bytes (\d+)-(\d+)/(\d+)')
    resp = urllib2.urlopen(request)
    start, end, size = reo.findall(resp.info()['content-range'])[0]

    print "Following the content-range in forward direction!"
    msg = explore(request, reo, int(end) + 1)
    name = re.findall(r'\s([a-z]+).', msg)[0]

    print "Following the content-range in backward direction!"
    msg = explore(request, reo, size, True)
    arch_pos = re.findall(r'\s(\d+).', msg)[0]
    passwd = name[::-1]

    request.headers['Range'] = 'bytes={}-'.format(arch_pos)
    resp = urllib2.urlopen(request)
    print "Found the hidden pack in {}:".format(arch_pos)
    with zipfile.ZipFile(StringIO(resp.read()), 'r') as zip:
        for name in zip.namelist():
            if name.endswith('txt'):
                print zip.read(name, passwd)
            else:
                return zip.read(name, passwd)


if __name__ == "__main__":
    answer = solve()
    # A package.pack in a zip

    # No url
