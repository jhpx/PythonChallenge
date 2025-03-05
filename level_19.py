#!/bin/env python
# coding=utf-8
# http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html
# Indian? Endian!
# @see http://www.lightlink.com/tjweber/StripWav/Canon.html
import email
import re
from array import array

import requests

PREFIX = "http://butter:fly@www.pythonchallenge.com/pc/hex/"
url = PREFIX + 'bin.html'


def catch(text, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, text, re.DOTALL)[cnt]


def solve(something):
    msg = email.message_from_string(something.strip())
    attachment = msg.get_payload()[0]
    fname = attachment.get_filename()
    audio = attachment.get_payload(decode=True)
    header = audio[:44]  # copy wav-header
    a = array('H', audio[44:])
    a.byteswap()
    with open(fname, 'wb') as file:
        file.write(header)
        a.tofile(file)
    # Generate "indian.wav" in current folder

if __name__ == "__main__":
    r = requests.get(url)
    something = catch(r.text)
    solve(something)
    # You are an idiot ha ha ha ha ah ha ha haha ha haha.

    # http://butter:fly@www.pythonchallenge.com/pc/hex/idiot.html
