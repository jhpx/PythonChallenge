# coding=utf-8
#!/bin/env python
# Regular expression.
import urllib
import re

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'equality.html'


def catch(url, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, urllib.urlopen(url).read(), re.DOTALL)[cnt]


def solve(text):
    return "".join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', text))

if __name__ == "__main__":
    text = catch(url)
    answer = solve(text)
    # linkedlist
    print PREFIX + answer + '.php'
    # url: http://www.pythonchallenge.com/pc/def/linkedlist.php
