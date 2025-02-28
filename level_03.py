#!/bin/env python
# coding=utf-8
# http://www.pythonchallenge.com/pc/def/equality.html
# Regular expression.
import re

import requests

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'equality.html'



def catch(text, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, text, re.DOTALL)[cnt]


def solve(something):
    answer = "".join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', something))
    print("One small letter, surrounded by EXACTLY three big bodyguards", end=' ')
    print(" on each of its sides:\n{}\n".format(answer))
    return answer


if __name__ == "__main__":
    r = requests.get(url)
    something = catch(r.text)
    answer = solve(something)
    # linkedlist
    print(PREFIX + answer + '.php')
    # http://www.pythonchallenge.com/pc/def/linkedlist.php
