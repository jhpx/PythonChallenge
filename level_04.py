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


def solve(url, NOTHING, MAXRANGE):
    reo = re.compile(r'and the next nothing is ([0-9]+)')
    nothing = NOTHING
    print("Following the nothing chain!")
    for i in range(int(MAXRANGE)):
        response = requests.get(url, params={'nothing': nothing})
        text = response.text
        m = reo.search(text)
        print('{}: {}'.format(i, text))
        if m:
            nothing = m.group(1)
        elif text.find(r'Divide by two') > -1:
            nothing = int(nothing) / 2
        else:
            break
    print("Done\n")
    return text


if __name__ == "__main__":
    r = requests.get(url)
    NOTHING = catch(r.text, r'nothing=([0-9]+)">')
    MAXRANGE = catch(r.text, r'([0-9]+) times is more than enough')

    # NOTHING=12345, MAXRANGE=400
    answer = solve(url, NOTHING, MAXRANGE)
    # peak.html
    print(PREFIX + answer)
    # http://www.pythonchallenge.com/pc/def/peak.html
