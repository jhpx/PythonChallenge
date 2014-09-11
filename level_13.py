# coding=utf-8
#!/bin/env python
# Phone that (remote) evil.
import re
import xmlrpclib

PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + '../phonebook.php'


def solve(url):
    phonebook = xmlrpclib.ServerProxy(url)
    return phonebook.phone('Bert')


if __name__ == "__main__":
    answer = solve(url)
    # 555-ITALY
    print PREFIX + re.findall(r'[A-Z]+', answer)[0].lower() + '.html'
    # url: http://huge:file@www.pythonchallenge.com/pc/return/italy.html
