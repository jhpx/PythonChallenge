# coding=utf-8
#!/bin/env python
# Message inside image.
import urllib
import re
import Image  # need PIL 1.1.7+

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'oxygen.png'


def catch(url, cnt=0):
    return urllib.urlretrieve(url)[cnt]


def solve(fname):
    im = Image.open(fname)
    width, height = im.size
    piv = im.load()

    upper = -1
    for j in range(height):
        for i in range(0, width, 7):
            px = piv[i, j]
            if px[0] == px[1] == px[2]:
                continue
            elif i > 0:
                if upper == -1:
                    upper = j
                    left = 0
                lower = j + 1
                right = i
            break

    box = (left, upper, right, lower)
    # print box
    samplesize = ((right - left + 1) / 7, 1)
    text = im.crop(box).convert('L').resize(samplesize).tostring()
    return "".join([chr(int(x)) for x in re.findall(r'\d+', text)])


if __name__ == "__main__":
    text = catch(url)
    answer = solve(text)
    # integrity
    print PREFIX + answer + '.html'
    # url: http://www.pythonchallenge.com/pc/def/integrity.html
