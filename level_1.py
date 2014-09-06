# coding=utf-8
#!/bin/env python
import urllib
import re

PREFIX = "http://www.pythonchallenge.com/pc/def/"
url = PREFIX + 'map.html'

ciphertext = re.findall(
    r'<font color="#f000f0">([^<]*)', urllib.urlopen(url).read(), re.DOTALL)[0]


def decrypter(str):
    """just move 2"""
    plaintext = ''
    for c in str:
        if re.match(r'[a-z]', c):
            plaintext += chr(ord('a') + (ord(c) - ord('a') + 2) % 26)
        else:
            plaintext += c
    return plaintext

hint = decrypter(ciphertext)
print hint

answer = decrypter('map')
# ocr
print PREFIX + answer + '.html'
# url: http://www.pythonchallenge.com/pc/def/ocr.html
