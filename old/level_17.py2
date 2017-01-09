#!/bin/env python
# coding=utf-8
# http://huge:file@www.pythonchallenge.com/pc/return/romance.html
# Cookie is new but busynothing is in the past.
import urllib
import urllib2
import Cookie
import contextlib
import re

PREFIX = "http://www.pythonchallenge.com/pc/def/"
PREFIX_AUTH = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + 'linkedlist.php'
NOTHING = 12345


def solve(url, pattern):
    reo = re.compile(pattern)
    nothing = NOTHING

    info = ""
    cookie = Cookie.SimpleCookie()
    print "Following the busynothing chain and picking up the crumbs!"
    for i in range(400):
        url1 = "{}?busynothing={}".format(url, nothing)
        with contextlib.closing(urllib.urlopen(url1)) as page:
            text = page.read()
            cookie_string = page.info().getheader('Set-Cookie')
            cookie.load(cookie_string)
        info += cookie['info'].value
        m = reo.search(text)
        print '{}:{}'.format(i, text)
        if m:
            nothing = m.group(1)
        else:
            break
    print "Done\n"

    print "Decompressing the message:"
    import bz2

    hidden = bz2.decompress(urllib.unquote_plus(info))
    print hidden
    # is it the 26th already? call his father and inform him that "the flowers
    # are on their way". he'll understand.
    message = re.findall(r'"(.+)"', hidden)[0]
    # the flowers are on their way
    print

    print "Looking up Mozart's father (Leopold):",
    import xmlrpclib

    url2 = PREFIX + '../phonebook.php'
    phonebook = xmlrpclib.ServerProxy(url2)
    response = phonebook.phone('Leopold')
    whom = re.findall(r'[A-Z]+', response)[0].lower()
    print whom  # violin

    print "Calling Leopold and sending him the mssage"
    url3 = PREFIX_AUTH + whom + '.html'
    with contextlib.closing(urllib.urlopen(url3)) as page:
        address = re.findall(r'(\S+?)\.$', page.read())[0]
    url4 = PREFIX + address  # violin.php
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', 'info=' + message))
    with contextlib.closing(opener.open(url4)) as page:
        answer = re.findall(r'(.+)</font>', page.read())[0]
        print "His response is: {}\n".format(answer)
        return re.findall(r'(\S+)\.$', answer)[0]


if __name__ == "__main__":
    pattern = r'and the next busynothing is ([0-9]+)'
    answer = solve(url, pattern)
    # balloons
    print PREFIX_AUTH + answer + '.html'
    # http://huge:file@www.pythonchallenge.com/pc/return/balloons.html
