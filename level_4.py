# coding=utf-8
#!/bin/env python
import urllib
import re

urlbase = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
PREFIX = "http://www.pythonchallenge.com/pc/def/"
nothing = 12345
p = re.compile(r'and the next nothing is ([0-9]+)')
while(True):
    params = urllib.urlencode({'nothing': nothing})
    text = urllib.urlopen("{}?{}".format(urlbase, params)).read()
    m = p.search(text)
    if m:
        nothing = m.group(1)
    elif text.find(r'Yes. Divide by two and keep going.') > -1:
        nothing = int(nothing) / 2
    else:
        # print nothing
        # print text
        break
answer = text
# peak.html
print PREFIX + answer
# url: http://www.pythonchallenge.com/pc/def/peak.html
