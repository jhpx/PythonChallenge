# coding=utf-8
#!/bin/env python

PREFIX = "http://www.pythonchallenge.com/pc/def/"

if __name__ == "__main__":
    answer = str(2 ** 38)
    # 274877906944
    print PREFIX + answer + '.html'
    # url: http://www.pythonchallenge.com/pc/def/274877906944.html
