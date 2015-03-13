#!/bin/env python
# coding=utf-8
# http://butter:fly@www.pythonchallenge.com/pc/hex/bonus.html
# The 'this' module.
import urllib
import contextlib
import re
import sys
from cStringIO import StringIO

PREFIX = "http://butter:fly@www.pythonchallenge.com/pc/hex/"
url = PREFIX + 'bonus.html'


def catch(url, pattern=r'<!--(.*?)-->', cnt=0):
    with contextlib.closing(urllib.urlopen(url)) as page:
        return re.findall(pattern, page.read(), re.DOTALL)[cnt]


def solve(text):
    capture = StringIO()
    save_stdout, sys.stdout = sys.stdout, capture
    import this
    sys.stdout = save_stdout
    guts = capture.getvalue().lower()
    message = text.decode('rot13').strip('\n\'')
    # in the face of what?
    searchfor = " ".join(message.split()[:-1])
    # in the face
    m = re.search(searchfor + r" (\w+)", guts)
    return m.group(1)


if __name__ == "__main__":
    text = catch(url, cnt=2)
    answer = solve(text)
    # ambiguity
    print PREFIX + answer + '.html'
    # http://butter:fly@www.pythonchallenge.com/pc/hex/ambiguity.html
