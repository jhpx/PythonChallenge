# coding=utf-8
#!/bin/env python
import urllib
import re

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'equality.html'

text = re.findall(r'<!--(.*?)-->', urllib.urlopen(url).read(), re.DOTALL)[0]
answer = "".join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', text))
# linkedlist
print PREFIX + answer + '.php'
# url: http://www.pythonchallenge.com/pc/def/linkedlist.php
