#!/bin/env python
# coding=utf-8
# http://www.pythonchallenge.com/pc/def/linkedlist.php
# And the next nothing is ?
import re

import requests

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'linkedlist.php'


def catch(text, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, text, re.DOTALL)[cnt]

def analysis(text):
    NOTHING = catch(text, r'nothing=([0-9]+)">')
    MAX_RANGE = catch(text, r'([0-9]+) times is more than enough')
    return NOTHING, MAX_RANGE

def solve(url, nothing, maxrange):
    reo = re.compile(r'and the next nothing is ([0-9]+)')
    next = nothing
    text = ''
    print("Following the nothing chain!")
    for i in range(int(maxrange)):
        response = requests.get(url, params={'nothing': next})
        text = response.text
        m = reo.search(text)
        print('{}: {}'.format(i, text))
        if m:
            next = m.group(1)
        elif text.find(r'Divide by two') > -1:
            next = int(next) / 2
        else:
            break
    print("Done\n")
    return text


if __name__ == "__main__":
    r = requests.get(url)
    NOTHING, MAX_RANGE = analysis(r.text)
    # NOTHING=12345, MAX_RANGE=400
    answer = solve(url, NOTHING, MAX_RANGE)
    # peak.html
    print(PREFIX + answer)
    # http://www.pythonchallenge.com/pc/def/peak.html
