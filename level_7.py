# coding=utf-8
#!/bin/env python
import urllib
import re
import Image  # need PIL 1.1.7+

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'oxygen.png'

im = Image.open(urllib.urlretrieve(url)[0])
width, height = im.size
piv = im.load()

upper = -1
for j in range(height):
    for i in range(0, width, 7):
        px = piv[i, j]
        if px[0] == px[1] == px[2]:
            continue
        elif i > 0:
            if upper == -1:
                upper = j
                left = 0
            lower = j + 1
            right = i
        break

box = (left, upper, right, lower)
samplesize = ((right - left + 1) / 7, 1)
# print box
text = im.crop(box).convert('L').resize(samplesize).tostring()
answer = "".join([chr(int(x)) for x in re.findall(r'\d+', text)])
# integrity
print PREFIX + answer + '.html'
# url: http://www.pythonchallenge.com/pc/def/integrity.html
