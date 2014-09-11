# coding=utf-8
#!/bin/env python
# Find readable characters.
import urllib
import re

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'ocr.html'


def catch(url, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, urllib.urlopen(url).read(), re.DOTALL)[cnt]


def solve(text):
    return "".join(re.findall(r'[a-z]+', text))


if __name__ == "__main__":
    text = catch(url, cnt=1)
    answer = solve(text)
    # equality
    print PREFIX + answer + '.html'
    # url: http://www.pythonchallenge.com/pc/def/equality.html
