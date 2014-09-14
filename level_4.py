#!/bin/env python
# coding=utf-8
# http://www.pythonchallenge.com/pc/def/linkedlist.php
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
    print "Following the nothing chain!"
    for i in range(400):
        weburl = "{}?nothing={}".format(url, nothing)
        with contextlib.closing(urllib.urlopen(weburl)) as page:
            text = page.read()
        m = reo.search(text)
        print '{}: {}'.format(i, text)
        if m:
            nothing = m.group(1)
        elif text.find(r'Divide by two') > -1:
            nothing = int(nothing) / 2
        else:
            break
    print "Done\n"
    return text


if __name__ == "__main__":
    pattern = r'and the next nothing is ([0-9]+)'
    answer = solve(url, pattern)
    # peak.html
    print PREFIX + answer
    # http://www.pythonchallenge.com/pc/def/peak.html
