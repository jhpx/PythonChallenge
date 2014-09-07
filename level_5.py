# coding=utf-8
#!/bin/env python
import urllib
import re
import pprint
import pickle

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'peak.html'

src = re.findall(
    r'<peakhell src="(.*?)"/>', urllib.urlopen(url).read(), re.DOTALL)[0]
banner = pickle.load(urllib.urlopen(PREFIX + src))
# pprint.pprint(banner)
for line in banner:
    print "".join(ch * count for ch, count in line)
# channel

# url: http://www.pythonchallenge.com/pc/def/channel.html
