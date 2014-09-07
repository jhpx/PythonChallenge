# coding=utf-8
#!/bin/env python
import urllib
import re
import bz2

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'integrity.html'

text = re.findall(r'<!--(.*?)-->', urllib.urlopen(url).read(), re.DOTALL)[0]
un = re.findall(r'un: \'(.*?)\'', text)[0].decode('string-escape')
pw = re.findall(r'pw: \'(.*?)\'', text)[0].decode('string-escape')
answer = bz2.decompress(un), bz2.decompress(pw)
print answer
# huge, file
