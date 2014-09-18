#!/bin/env python
# coding=utf-8
# http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html
# Indian? Endian!
import urllib
import contextlib
import re
from cStringIO import StringIO
import email
from array import array

PREFIX = "http://butter:fly@www.pythonchallenge.com/pc/hex/"
url = PREFIX + 'bin.html'


def catch(url, pattern=r'<!--(.*?)-->', cnt=0):
    with contextlib.closing(urllib.urlopen(url)) as page:
        return re.findall(pattern, page.read(), re.DOTALL)[cnt]


def solve(text):
    msg = email.message_from_string(text.strip())
    attachment = msg.get_payload()[0]
    fname = attachment.get_filename()
    audio = attachment.get_payload(decode=True)
    header = audio[:44]  # copy wav-header
    a = array('H', audio[44:])
    a.byteswap()
    with open(fname, 'wb') as file:
        file.write(header)
        a.tofile(file)


if __name__ == "__main__":
    text = catch(url)
    answer = solve(text)
    # You are an idiot ha ha ha ha ah ha ha haha ha haha.

    # http://butter:fly@www.pythonchallenge.com/pc/hex/idiot.html
