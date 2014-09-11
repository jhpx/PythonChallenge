# coding=utf-8
#!/bin/env python
# Bee is busy.
import urllib
import contextlib
import re
import bz2

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'integrity.html'


def catch(url, pattern=r'<!--(.*?)-->', cnt=0):
    with contextlib.closing(urllib.urlopen(url)) as page:
        return re.findall(pattern, page.read(), re.DOTALL)[cnt]


def solve(text):
    un = re.findall(r'un: \'(.*?)\'', text)[0].decode('string-escape')
    pw = re.findall(r'pw: \'(.*?)\'', text)[0].decode('string-escape')
    return bz2.decompress(un), bz2.decompress(pw)


if __name__ == "__main__":
    text = catch(url)
    un, pw = solve(text)
    # huge, file
    print "http://{}:{}@".format(un, pw) + PREFIX[7:-4] + 'return/good.html'
    # url: http://huge:file@www.pythonchallenge.com/pc/return/good.html
