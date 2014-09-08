# coding=utf-8
#!/bin/env python
# Connect the dots.
import re
import urllib2
import Image
import ImageDraw

PREFIX = "http://www.pythonchallenge.com/pc/return/"
url = PREFIX + 'good.html'

username = 'huge'
password = 'file'


def catch(url, pattern=r'<!--(.*?)-->', cnt=0):
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    auth_handler = urllib2.HTTPBasicAuthHandler(passman)
    auth_handler.add_password(None, url, username, password)
    opener = urllib2.build_opener(auth_handler)

    urllib2.install_opener(opener)
    page = urllib2.urlopen(url).read()

    return re.findall(pattern, page, re.DOTALL)[cnt]


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
