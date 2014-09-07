# coding=utf-8
#!/bin/env python
import urllib
import re

PREFIX = "http://www.pythonchallenge.com/pc/def/"
urlbase = PREFIX + 'linkedlist.php'
nothing = 12345

p = re.compile(r'and the next nothing is ([0-9]+)')
for i in range(400):
    params = urllib.urlencode({'nothing': nothing})
    text = urllib.urlopen("{}?{}".format(urlbase, params)).read()
    m = p.search(text)
    if m:
        nothing = m.group(1)
        print 'nothing: ' + nothing
    elif text.find(r'Yes. Divide by two and keep going.') > -1:
        nothing = int(nothing) / 2
        print 'nothing: {}'.format(nothing)
    else:
        # print nothing
        # print text
        break
answer = text
# peak.html
print PREFIX + answer
# url: http://www.pythonchallenge.com/pc/def/peak.html
