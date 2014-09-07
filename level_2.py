# coding=utf-8
#!/bin/env python
import urllib
import re

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'ocr.html'

text = re.findall(r'<!--(.*?)-->', urllib.urlopen(url).read(), re.DOTALL)[1]
answer = "".join(re.findall(r'[a-z]+', text))
# equality
print PREFIX + answer + '.html'
# url: http://www.pythonchallenge.com/pc/def/equality.html
