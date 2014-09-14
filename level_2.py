#!/bin/env python
# coding=utf-8
# http://www.pythonchallenge.com/pc/def/ocr.html
# Find readable characters.
import urllib
import re

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'ocr.html'


def catch(url, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, urllib.urlopen(url).read(), re.DOTALL)[cnt]


def solve(text):
    answer = "".join(re.findall(r'[a-z]+', text))
    print "Recognize the characters: {}\n".format(answer)
    return answer


if __name__ == "__main__":
    text = catch(url, cnt=1)
    answer = solve(text)
    # equality
    print PREFIX + answer + '.html'
    # http://www.pythonchallenge.com/pc/def/equality.html
