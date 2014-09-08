# coding=utf-8
#!/bin/env python
import urllib
import re
import zipfile

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'channel.zip'
NOTHING = 90052


def catch(url, cnt=0):
    return urllib.urlretrieve(url)[cnt]


def solve(fname, pattern):
    reo = re.compile(pattern)
    nothing = NOTHING
    with zipfile.ZipFile(fname, 'r') as channel:
        comments = []
        for i in range(1000):
            name = '{}.txt'.format(nothing)
            text = channel.read(name)
            comments.append(channel.getinfo(name).comment)
            m = reo.search(text)
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

if __name__ == "__main__":
    pattern = r'nothing is ([0-9]+)'
    text = catch(url)
    answer = solve(text, pattern)
    # oxygen

    # url: http://www.pythonchallenge.com/pc/def/oxygen.html
