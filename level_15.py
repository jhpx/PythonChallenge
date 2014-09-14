#!/bin/env python
# coding=utf-8
# http://huge:file@www.pythonchallenge.com/pc/return/uzi.html
# Jan.26th, 1??6 (Mon)
import urllib
import contextlib
import re
import calendar
from datetime import date

PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + 'uzi.html'


def catch(url, pattern=r'<!--(.*?)-->', cnt=0):
    with contextlib.closing(urllib.urlopen(url)) as page:
        return re.findall(pattern, page.read(), re.DOTALL)[cnt]


def solve():
    years = []
    for yr in range(1006, 1996, 10):
        if calendar.isleap(yr) and 0 == date(yr, 1, 26).weekday():
            years.append(str(yr))
    year = years[-2]
    print 'The given date: ' + year + '/01/27'
    # 1756/01/27

    wikiurl = 'http://en.wikipedia.org/wiki/January_27'
    text = catch(wikiurl, '<li><a href="/wiki/' + year + '.*?</a>(.*?)</li>')
    text = re.findall(r'<a.*?>(.+?)</a>', text)[0]
    print "The great man: {}\n".format(text)
    # Wolfgang Amadeus Mozart
    return text.split()[-1].lower()


if __name__ == "__main__":
    answer = solve()
    # mozart
    print PREFIX + answer + '.html'
    # http://huge:file@www.pythonchallenge.com/pc/return/mozart.html
