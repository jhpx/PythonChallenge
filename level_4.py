# coding=utf-8
#!/bin/env python
import urllib
import re

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'linkedlist.php'
NOTHING = 12345


def solve(url, pattern):
    reo = re.compile(pattern)
    nothing = NOTHING
    for i in range(400):
        print 'nothing: {}'.format(nothing)
        text = urllib.urlopen("{}?nothing={}".format(url, nothing)).read()
        m = reo.search(text)
        if m:
            nothing = m.group(1)
        elif text.find(r'Yes. Divide by two and keep going.') > -1:
            nothing = int(nothing) / 2
        else:
            # print text
            return text

if __name__ == "__main__":
    pattern = r'and the next nothing is ([0-9]+)'
    answer = solve(url, pattern)
    # peak.html
    print PREFIX + answer
    # url: http://www.pythonchallenge.com/pc/def/peak.html
