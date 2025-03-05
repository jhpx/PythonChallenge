#!/bin/env python
# coding=utf-8
# http://butter:fly@www.pythonchallenge.com/pc/hex/decent.html
# Email leopold and fix the broken zip.
import hashlib
import zipfile
from io import BytesIO

from PIL import Image

PREFIX = "http://butter:fly@www.pythonchallenge.com/pc/hex/"
url = PREFIX + 'decent.html'


def prepare():
    # Apologize for reading Leopold's email in level 19
    # Send a 'sorry' email to <leopold.moz@pythonchallenge.com>
    # And then get a response like this:
    #   Never mind that.
    #   Have you found my broken zip?
    #   md5: bbb8b499a0eef99b52c7f13f4e78c24b
    #   Can you believe what one mistake can lead to?
    broken = bytearray(open('mybroken.zip', "rb").read())
    MD5 = 'bbb8b499a0eef99b52c7f13f4e78c24b'
    return broken, MD5


def repair(broken, MD5):
    all_chars = list(range(256))
    for i, bak in enumerate(broken):
        for ch in all_chars:
            broken[i] = ch
            if hashlib.md5(broken).hexdigest() == MD5:
                print('Find it:{}-{}'.format(i, ch))
                return broken
        broken[i] = bak
    return


def solve(data):
    result = None
    with zipfile.ZipFile(BytesIO(data), 'r') as zip:
        for name in zip.namelist():
            if name.endswith('.gif'):
                zip.extract(name)
                result = BytesIO(zip.read(name))
    return result

def plot(byte_io):
    Image.open(byte_io).show()

if __name__ == "__main__":
    broken, MD5 = prepare()
    data = repair(broken, MD5)
    answer = solve(data)
    plot(answer)
    # speed

    # Hurry up, I'm missing the boat
    # http://butter:fly@www.pythonchallenge.com/pc/hex/speedboat.html
