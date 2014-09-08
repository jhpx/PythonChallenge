# coding=utf-8
#!/bin/env python
import urllib
import re
import bz2

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'integrity.html'


def catch(url, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, urllib.urlopen(url).read(), re.DOTALL)[cnt]


def solve(text):
    un = re.findall(r'un: \'(.*?)\'', text)[0].decode('string-escape')
    pw = re.findall(r'pw: \'(.*?)\'', text)[0].decode('string-escape')
    return bz2.decompress(un), bz2.decompress(pw)

if __name__ == "__main__":
    text = catch(url)
    answer = solve(text)
    print answer
    # huge, file
