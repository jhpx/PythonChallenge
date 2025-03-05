#!/bin/env python
# coding=utf-8
# http://butter:fly@www.pythonchallenge.com/pc/hex/lake.html
# Splice the wav(image) files.
import wave
from io import BytesIO

import requests
from PIL import Image

PREFIX = "http://butter:fly@www.pythonchallenge.com/pc/hex/"
url = PREFIX + 'lake.html'


def solve():
    pieces = []
    piece_size = 0
    for i in range(25):
        r = requests.get(PREFIX + 'lake' + str(i + 1) + '.wav')
        f = wave.open(BytesIO(r.content))
        frames = f.getnframes()  # 10800
        piece_size = int((frames // 3) ** .5)  # 60
        pieces.append(Image.frombytes('RGB', (piece_size, piece_size), f.readframes(frames)))
    #
    canvas = Image.new('RGB', (piece_size * 5, piece_size * 5))
    for i in range(25):
        canvas.paste(pieces[i], ((i % 5) * piece_size, (i // 5) * piece_size))

    return canvas


def plot(im):
    im.show()


if __name__ == "__main__":
    answer = solve()
    # decent
    plot(answer)

    # http://butter:fly@www.pythonchallenge.com/pc/hex/decent.html
