# coding=utf-8
#!/bin/env python
import urllib
import re
import zipfile

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'channel.zip'
nothing = 90052

fname = urllib.urlretrieve(url)[0]
p = re.compile(r'nothing is ([0-9]+)')
comments = []
with zipfile.ZipFile(fname, 'r') as channel:
    for i in range(1000):
        name = '{}.txt'.format(nothing)
        text = channel.read(name)
        comments.append(channel.getinfo(name).comment)
        m = p.search(text)
        if m:
            nothing = m.group(1)
            print 'nothing:' + nothing
        elif text.find('comment') > -1:
            print "".join(comments)
            break
        else:
            # print nothing
            # print text
            break
# oxygen

# url: http://www.pythonchallenge.com/pc/def/oxygen.html
