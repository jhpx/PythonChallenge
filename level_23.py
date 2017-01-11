#!/bin/env python
# coding=utf-8
# http://butter:fly@www.pythonchallenge.com/pc/hex/bonus.html
# The 'this' module.
import codecs
import re
import sys
from io import StringIO

import requests

PREFIX = "http://butter:fly@www.pythonchallenge.com/pc/hex/"
url = PREFIX + 'bonus.html'


def catch(text, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, text, re.DOTALL)[cnt]


def solve(something):
    capture = StringIO()
    save_stdout, sys.stdout = sys.stdout, capture
    sys.stdout = save_stdout
    guts = capture.getvalue().lower()
    message = codecs.encode(something,"rot13").strip('\n\'')
    # in the face of what?
    searchfor = " ".join(message.split()[:-1])
    # in the face
    m = re.search(searchfor + r" (\w+)", guts)
    return m.group(1)


if __name__ == "__main__":
    r = requests.get(url)
    something = catch(r.text, cnt=2)
    answer = solve(something)
    # ambiguity
    print(PREFIX + answer + '.html')
    # http://butter:fly@www.pythonchallenge.com/pc/hex/ambiguity.html
