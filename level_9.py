# coding=utf-8
#!/bin/env python
# Connect the dots.
import re
import urllib
import Image
import ImageDraw

PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + 'good.html'


def catch(url, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, urllib.urlopen(url).read(), re.DOTALL)[cnt]


def solve(text):
    first, second = re.findall(
        r'first:(.*?)second:(.*)', text.replace('\n', ''))[0]
    L1 = map(int, first.split(','))
    L2 = map(int, second.split(','))

    im = Image.new("RGB", (640, 480))
    draw = ImageDraw.Draw(im)
    draw.polygon(L1)
    draw.polygon(L2)

    im.show()

if __name__ == "__main__":
    text = catch(url, cnt=1)
    answer = solve(text)
    # bull graph

    # url: http://www.pythonchallenge.com/pc/return/bull.html
