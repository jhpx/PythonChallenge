#!/bin/env python
# coding=utf-8
# http://huge:file@www.pythonchallenge.com/pc/return/romance.html
# Cookie is new but busynothing is in the past.
import codecs
import re
import urllib.parse

import requests

PREFIX = "http://www.pythonchallenge.com/pc/def/"
PREFIX_AUTH = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + 'linkedlist.php'


def catch(text, pattern=r'<!--(.*?)-->', cnt=0):
    return re.findall(pattern, text, re.DOTALL)[cnt]


def solve(url):
    reo = re.compile(r'and the next busynothing is ([0-9]+)')

    r = requests.get(url)
    nothing = catch(r.text, r'nothing=([0-9]+)">')
    MAXRANGE = catch(r.text, r'([0-9]+) times is more than enough')

    info = ""
    print("Following the busynothing chain and picking up the crumbs!")
    for i in range(int(MAXRANGE)):
        r = requests.get(url, params={'busynothing': nothing})
        text = r.text
        info += r.cookies['info']
        m = reo.search(text)
        print('{}:{}'.format(i, text))
        if m:
            nothing = m.group(1)
        else:
            break
    print("Done\n")
    # info = 'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'

    print("Decompressing the message:")
    hidden = codecs.decode(urllib.parse.unquote_to_bytes(info.replace('+', ' ')), 'bz2').decode()
    print(hidden)
    # is it the 26th already? call his father and inform him that "the flowers
    # are on their way". he\'ll understand.
    message = catch(hidden, r'"(.+)"')
    # the flowers are on their way
    print()
    #
    print("Looking up Mozart's father (Leopold):", end=' ')
    import xmlrpc.client

    url2 = PREFIX_AUTH + '../phonebook.php'
    phonebook = xmlrpc.client.ServerProxy(url2)
    response = phonebook.phone('Leopold')
    whom = catch(response, r'[A-Z]+').lower()
    # violin

    url3 = PREFIX_AUTH + whom + '.html'
    r3 = requests.get(url3)
    address = catch(r3.text, r'(\S+?)\.$')
    print(address)  # ../stuff/violin.php

    print("Calling Leopold and sending him the mssage")
    url4 = PREFIX_AUTH + address
    cookies = {'info': message}
    r4 = requests.get(url4, cookies=cookies)
    answer = catch(r4.text, r'([^\n]+)</font>')
    print("His response is: {}\n".format(answer))
    return catch(answer, r'(\S+)\.$')


if __name__ == "__main__":
    answer = solve(url)
    # balloons
    print(PREFIX_AUTH + answer + '.html')
    # http://huge:file@www.pythonchallenge.com/pc/return/balloons.html
