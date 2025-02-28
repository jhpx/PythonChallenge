#!/bin/env python
# coding=utf-8
# http://www.pythonchallenge.com/pc/def/channel.html
# Nothing in zipfile.
import re
import zipfile
from io import BytesIO

import requests

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'channel.zip'


def catch(text, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, text, re.DOTALL)[cnt]


def analysis(something):
    with zipfile.ZipFile(BytesIO(something), 'r') as channel:
        readme = channel.read('readme.txt').decode()
        NOTHING = catch(readme, r'start from ([0-9]+)')
        MAXRANGE = len(channel.infolist())
    return NOTHING, MAXRANGE


def solve(something, NOTHING, MAXRANGE):
    reo = re.compile(r'nothing is ([0-9]+)')
    nothing = NOTHING
    print("Following the nothing chain and picking up the crumbs!")
    with zipfile.ZipFile(BytesIO(something), 'r') as channel:
        comments = ""
        for i in range(int(MAXRANGE)):
            name = '{}.txt'.format(nothing)
            text = channel.read(name).decode()
            comments += channel.getinfo(name).comment.decode()
            m = reo.search(text)
            print('{}:{}'.format(i, text))
            if m:
                nothing = m.group(1)
            else:
                break
    print("Done\n")
    print(comments)


if __name__ == "__main__":
    r = requests.get(url)
    something = r.content
    NOTHING, MAXRANGE = analysis(something)
    # NOTHING=90052, MAXRANGE = 910
    answer = solve(something, NOTHING, MAXRANGE)
    # oxygen

    # http://www.pythonchallenge.com/pc/def/oxygen.html
