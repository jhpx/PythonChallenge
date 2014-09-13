#!/bin/env python
# coding=utf-8
# http://huge:file@www.pythonchallenge.com/pc/return/disproportional.html
# Phone that (remote) evil.
import re
import xmlrpclib

PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + '../phonebook.php'


def solve(url):
    phonebook = xmlrpclib.ServerProxy(url)
    response = phonebook.phone('Bert')
    return re.findall(r'[A-Z]+', response)[0].lower()


if __name__ == "__main__":
    answer = solve(url)
    # 555-ITALY
    print PREFIX + answer + '.html'
    # http://huge:file@www.pythonchallenge.com/pc/return/italy.html
