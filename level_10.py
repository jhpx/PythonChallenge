#!/bin/env python
# coding=utf-8
# http://huge:file@www.pythonchallenge.com/pc/return/bull.html
# Sequence of number.
import re

PREFIX = "http://huge:file@www.pythonchallenge.com/pc/return/"
url = PREFIX + 'bull.html'


def describe(x):
    return "".join([str(len(i + j)) + i
                    for i, j in re.findall(r"(\d)(\1*)", x)])


def solve(n):
    x = "1"
    for each in range(n):
        x = describe(x)
    return str(len(x))


if __name__ == "__main__":
    answer = solve(30)
    # 5808
    print PREFIX + answer + '.html'
    # http://huge:file@www.pythonchallenge.com/pc/return/5808.html
