#!/bin/env python
# coding=utf-8
# http://www.pythonchallenge.com/pc/def/ocr.html
# Find readable characters.
import re

import requests

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'ocr.html'


def catch(text, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, text, re.DOTALL)[cnt]


def solve(text):
    answer = "".join(re.findall(r'[a-z]+', text))
    print("Recognize the characters: {}\n".format(answer))
    return answer


if __name__ == "__main__":
    r = requests.get(url)
    something = catch(r.text, cnt=1)
    answer = solve(something)
    # equality
    print(PREFIX + answer + '.html')
    # http://www.pythonchallenge.com/pc/def/equality.html
