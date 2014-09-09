# coding=utf-8
#!/bin/env python
# Jan.26th, 1??6 (Mon)
import urllib
import re
import calendar
from datetime import date

PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + 'uzi.html'


def catch(url, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, urllib.urlopen(url).read(), re.DOTALL)[cnt]


def solve():
    years = []
    for yr in range(1006, 1996, 10):
        if calendar.isleap(yr) and 0 == date(yr, 1, 26).weekday():
            years.append(str(yr))
    year = years[-2]
    print year + '/01/27'
    # 1756/01/27

    wikiurl = 'http://en.wikipedia.org/wiki/January_27'
    text = catch(wikiurl, '<li><a href="/wiki/' + year + '.*?</a>(.*?)</li>')
    text = re.findall(r'<a.*?>(.+?)</a>', text)[0]
    print text
    # Wolfgang Amadeus Mozart
    return text.split()[-1].lower()


if __name__ == "__main__":
    answer = solve()
    # mozart
    print PREFIX + answer + '.html'
    # url: http://huge:file@www.pythonchallenge.com/pc/return/mozart.html
