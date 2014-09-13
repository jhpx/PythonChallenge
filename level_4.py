#!/bin/env python
# coding=utf-8
# And the next nothing is ?
import urllib
import contextlib
import re

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'linkedlist.php'
NOTHING = 12345


def solve(url, pattern):
    reo = re.compile(pattern)
    nothing = NOTHING
    for i in range(400):
        print 'nothing: {}'.format(nothing)
        weburl = "{}?nothing={}".format(url, nothing)
        with contextlib.closing(urllib.urlopen(weburl)) as page:
            text = page.read()
        m = reo.search(text)
        if m:
            nothing = m.group(1)
        elif text.find(r'Yes. Divide by two and keep going.') > -1:
            nothing = int(nothing) / 2
        else:
            # print text
            return text


if __name__ == "__main__":
    pattern = r'and the next nothing is ([0-9]+)'
    answer = solve(url, pattern)
    # peak.html
    print PREFIX + answer
    # http://www.pythonchallenge.com/pc/def/peak.html
