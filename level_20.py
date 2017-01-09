#!/bin/env python
# coding=utf-8
# http://butter:fly@www.pythonchallenge.com/pc/hex/idiot2.html
# HTTP/1.1 206 Partial content
# @see http://tools.ietf.org/html/rfc2616#section-14.16
import requests
import re
from io import BytesIO
import zipfile

PREFIX = "http://butter:fly@www.pythonchallenge.com/pc/hex/"
url = PREFIX + 'unreal.jpg'


def catch(text, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, text, re.DOTALL)[cnt]


def explore(reo, next, forward=True):
    while (True):
        headers = {'Range': 'bytes={}-'.format(next)}
        r = requests.get(url, headers=headers)
        if r.ok:
            msg = r.text
            print("{}:{}".format(next, msg.strip()))
            start, end, size = reo.findall(r.headers['content-range'])[0]
            if (forward):
                next = int(end) + 1
            else:
                next = int(start) - 1
        else:
            print("HTTP Error {}: {}\n".format(r.status_code, r.reason))
            break
    return msg


def solve():
    reo = re.compile(r'bytes (\d+)-(\d+)/(\d+)')
    r = requests.get(url, headers={'Range': ''})
    start, end, size = reo.findall(r.headers['content-range'])[0]

    print("Following the content-range in forward direction!")
    msg = explore(reo, int(end) + 1)
    name = catch(msg, r'\s([a-z]+).')  # name = 'invader'
    #
    print("Following the content-range in backward direction!")
    msg = explore(reo, size, False)
    arch_pos = catch(msg, r'\s(\d+).')  # arch_pos = 1152983631
    passwd = name[::-1].encode()  # passwd = b'redavni'
    #
    print("Access the hidden zipfile in {}:".format(arch_pos))
    headers = {'Range': 'bytes={}-'.format(arch_pos)}
    r = requests.get(url, headers=headers)
    with zipfile.ZipFile(BytesIO(r.content), 'r') as zip:
        for name in zip.namelist():
            if name.endswith('.txt'):
                print(name)
                print("----------------------")
                print(zip.read(name, passwd).decode())
            else:
                # Generate 'package.pack' in current folder
                outfile = open(name, 'wb')
                outfile.write(zip.read(name, passwd))
                outfile.close()


if __name__ == "__main__":
    answer = solve()
    # A package.pack in a zip

    # No url
