#!/bin/env python
# coding=utf-8
# http://huge:file@www.pythonchallenge.com/pc/return/disproportional.html
# Phone that (remote) evil.
import re
import xmlrpc.client
from ftplib import print_line

PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + '../phonebook.php'


def solve(url):
    print("Looking up Bert(Evil):")
    phonebook = xmlrpc.client.ServerProxy(url)
    # This line will raise an exception if you're within the Great Firewall (GFW).
    response = phonebook.phone('Bert')
    whom = re.findall(r'[A-Z]+', response)[0].lower()
    print_line(whom)

    return whom


if __name__ == "__main__":
    answer = solve(url)
    # 555-ITALY
    print(PREFIX + answer + '.html')
    # http://huge:file@www.pythonchallenge.com/pc/return/italy.html
