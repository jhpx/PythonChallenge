#!/bin/env python
# coding=utf-8
# http://huge:file@www.pythonchallenge.com/pc/return/uzi.html
# Jan.26th, 1??6 (Mon)
import calendar
import re
from datetime import date

import requests

PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + 'uzi.html'


def catch(text, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, text, re.DOTALL)[cnt]


def analysis():
    years = []
    for yr in range(1006, 1996, 10):
        if calendar.isleap(yr) and 0 == date(yr, 1, 26).weekday():
            years.append(str(yr))
    return years[-2]


def solve(year):
    print('The given date: ' + year + '/01/27')
    # 1756/01/27

    wikiurl = 'https://en.wikipedia.org/wiki/January_27'
    # This line will raise an exception if you're within the Great Firewall (GFW).
    r = requests.get(wikiurl)
    text = catch(r.text, '<li><a href="/wiki/' + year + '.*?</a>(.*?)</li>')
    text = re.findall(r'<a.*?>(.+?)</a>', text)[0]
    print("The great man: {}\n".format(text))
    # Wolfgang Amadeus Mozart
    return text.split()[-1].lower()


if __name__ == "__main__":
    year = analysis()
    answer = solve(year)
    # mozart
    print(PREFIX + answer + '.html')
    # http://huge:file@www.pythonchallenge.com/pc/return/mozart.html
