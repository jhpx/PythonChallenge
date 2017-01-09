#!/bin/env python
# coding=utf-8
# http://huge:file@www.pythonchallenge.com/pc/return/disproportional.html
# Phone that (remote) evil.
import re
import xmlrpc.client

PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + '../phonebook.php'


def solve(url):
    print("Looking up Bert(Evil):", end=' ')
    phonebook = xmlrpc.client.ServerProxy(url)
    response = phonebook.phone('Bert')
    whom = re.findall(r'[A-Z]+', response)[0].lower()
    print(whom)
    print()
    return whom


if __name__ == "__main__":
    answer = solve(url)
    # 555-ITALY
    print(PREFIX + answer + '.html')
    # http://huge:file@www.pythonchallenge.com/pc/return/italy.html
