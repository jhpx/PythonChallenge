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
    for i in range(25):
        r = requests.get(PREFIX + 'lake' + str(i + 1) + '.wav')
        f = wave.open(BytesIO(r.content))
        nframes = f.getnframes()  # 10800
        piecesize = int((nframes // 3) ** (.5))  # 60
        pieces.append(Image.frombytes('RGB', (piecesize, piecesize), f.readframes(nframes)))
    #
    canvas = Image.new('RGB', (piecesize * 5, piecesize * 5))
    for i in range(25):
        canvas.paste(pieces[i], ((i % 5) * piecesize, (i // 5) * piecesize))
    canvas.show()
    return


if __name__ == "__main__":
    answer = solve()
    # decent

    # http://butter:fly@www.pythonchallenge.com/pc/hex/decent.html
