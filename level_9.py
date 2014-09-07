# coding=utf-8
#!/bin/env python
import re
import urllib2
import Image
import ImageDraw

PREFIX = "http://www.pythonchallenge.com/pc/return/"
url = PREFIX + 'good.html'

username = 'huge'
password = 'file'

passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
auth_handler = urllib2.HTTPBasicAuthHandler(passman)
auth_handler.add_password(None, url, username, password)
opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(opener)
page = urllib2.urlopen(url).read()

text = re.findall(r'<!--(.*?)-->', page, re.DOTALL)[1].replace('\n', '')
first, second = re.findall(r'first:(.*?)second:(.*)', text)[0]

L1 = map(int, first.split(','))
L2 = map(int, second.split(','))

im = Image.new("RGB", (480, 480))
draw = ImageDraw.Draw(im)
draw.polygon(L1)
draw.polygon(L2)

im.show()
# bull

# url: http://www.pythonchallenge.com/pc/return/bull.html
