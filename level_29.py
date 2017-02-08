#!/bin/env python
# coding=utf-8
# http://repeat:switch@www.pythonchallenge.com/pc/ring/guido.html
# Count spaces.
import bz2
import re

import requests

PREFIX = "http://repeat:switch@www.pythonchallenge.com/pc/ring/"
url = PREFIX + 'guido.html'


def catch(text, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, text, re.DOTALL)[cnt]


def solve(something):
    spaces = catch(something,r'</html>\n(.*)').split('\n')
    counts = bytes(map(len, spaces))
    answer = bz2.decompress(bytes(counts)).decode()
    return answer


if __name__ == "__main__":
    r = requests.get(url)
    something = r.text
    answer = solve(something)

    print(answer)
    # Isn't it clear? I am yankeedoodle!

    # http://repeat:switch@www.pythonchallenge.com/pc/ring/yankeedoodle.html
