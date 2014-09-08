# coding=utf-8
#!/bin/env python
# Peak hell pronounced like 'pickle'.
import urllib
import re
import pickle

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'peak.html'


def catch(url, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, urllib.urlopen(url).read(), re.DOTALL)[cnt]


def solve(text):
    banner = pickle.load(urllib.urlopen(PREFIX + text))
    for line in banner:
        print "".join(ch * count for ch, count in line)


if __name__ == "__main__":
    pattern = r'<peakhell src="(.*?)"/>'
    text = catch(url, pattern)
    answer = solve(text)
    # channel

    # url: http://www.pythonchallenge.com/pc/def/channel.html
