#!/bin/env python
# coding=utf-8
# http://www.pythonchallenge.com/pc/def/channel.html
# Nothing in zipfile.
import urllib
import re
import zipfile

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'channel.zip'
NOTHING = 90052


def download(url, cnt=0):
    return urllib.urlretrieve(url)[cnt]


def solve(fname, pattern):
    reo = re.compile(pattern)
    nothing = NOTHING
    print "Following the nothing chain and picking up the crumbs!"
    with zipfile.ZipFile(fname, 'r') as channel:
        comments = ""
        for i in range(1000):
            name = '{}.txt'.format(nothing)
            text = channel.read(name)
            comments += channel.getinfo(name).comment
            m = reo.search(text)
            print '{}:{}'.format(i, text)
            if m:
                nothing = m.group(1)
            else:
                break
    print "Done\n"
    print comments


if __name__ == "__main__":
    pattern = r'nothing is ([0-9]+)'
    fname = download(url)
    answer = solve(fname, pattern)
    # oxygen

    # http://www.pythonchallenge.com/pc/def/oxygen.html
