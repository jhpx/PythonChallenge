#!/bin/env python
# coding=utf-8
# 2 to 38 = ?
PREFIX = "http://www.pythonchallenge.com/pc/def/"

if __name__ == "__main__":
    answer = str(2 ** 38)
    # 274877906944
    print PREFIX + answer + '.html'
    # http://www.pythonchallenge.com/pc/def/274877906944.html
