#!/bin/env python
# coding=utf-8
# http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/arecibo.html
import re

import requests

PREFIX = "http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/"
url = PREFIX + 'warmup.txt'


def catch(text, pattern=r'<a href="(.*?)">', cnt=0):
    return re.findall(pattern, text, re.DOTALL)[cnt]


# ----------------------------------------------------------------------------------------------
# Adapted from https://ruoyu0088.github.io/thinking_code/ortools-sat_nonogram.html
# By 株式会社フォン
# © Copyright 2024.
from ortools.sat.python import cp_model
import string


def place_numbers(model, numbers, width, prefix=""):
    locations = [model.new_int_var(0, width - 1, f"{prefix}{name}") for _, name in zip(numbers, string.ascii_uppercase)]
    for n1, n2, c in zip(locations[:-1], locations[1:], numbers):
        model.add(n2 > n1 + c)
    model.add(locations[-1] <= width - numbers[-1])
    return locations


def fill_pattern(model, numbers, targets, prefix=""):
    width = len(targets)
    count = len(numbers)
    locations = place_numbers(model, numbers, width, prefix)

    fills = {}
    for i in range(width):
        for j in range(count):
            fills[i, j] = model.new_bool_var(f'{locations[j].name}_{i}')

    for j, n in enumerate(locations):
        for i in range(width - numbers[j] + 1):
            # b is equal to locations[j] == i
            b = model.new_bool_var(f'{n.name}_{i}')
            model.add(n == i).only_enforce_if(b)
            model.add(n != i).only_enforce_if(~b)

            # fill fills by b
            tmp = [fills[x, j] if i <= x < i + numbers[j] else ~fills[x, j] for x in range(width)]
            model.add_bool_and(tmp).only_enforce_if(b)

    for i, t in enumerate(targets):
        bools = [fills[i, j] for j in range(count)]
        # if target is True then fills[i, *] must have one True
        model.add_bool_or(bools).only_enforce_if(t)
        # if target is False then all fills[i, *] must be False
        model.add_bool_and([~v for v in bools]).only_enforce_if(~t)


def solve_nonogram(row_clues, col_clues):
    model = cp_model.CpModel()
    width = len(col_clues)
    height = len(row_clues)
    cells = [[model.new_bool_var(f"T_{r}_{c}") for c in range(width)] for r in range(height)]
    for r, numbers in enumerate(row_clues):
        line = cells[r]
        fill_pattern(model, numbers, line, f"R{r}")

    for c, numbers in enumerate(col_clues):
        line = [cells[i][c] for i in range(height)]
        fill_pattern(model, numbers, line, f"C{c}")

    solver = cp_model.CpSolver()
    solver.solve(model)
    return [[solver.value(c) for c in row] for row in cells]


def print_nonogram(result):
    print("\n".join([" ".join([" #"[c] for c in row]) for row in result]))


# ----------------------------------------------------------------------------------------------

def parse(text):
    # Split into non-empty, stripped lines
    lines = [line.strip() for line in text.strip().split('\n') if line.strip()]
    # Find the indices of each section
    i_dim = next(i for i, line in enumerate(lines) if line.startswith('# Dimensions'))
    i_hor = next(i for i, line in enumerate(lines) if i > i_dim and line.startswith('# Horizontal'))
    i_ver = next(i for i, line in enumerate(lines) if i > i_hor and line.startswith('# Vertical'))
    # Parse rows and columns
    rows, cols = map(int, lines[i_dim + 1].split())
    # Extract horizontal and vertical constraints
    row_clues = [list(map(int, line.split())) for line in lines[i_hor + 1:i_ver]]
    col_clues = [list(map(int, line.split())) for line in lines[i_ver + 1:]]
    return rows, cols, row_clues, col_clues


def solve(row_clues, col_clues):
    print_nonogram(solve_nonogram(row_clues, col_clues))
    # See an up arrow

    url = PREFIX + 'up.html'
    # http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/up.html"

    url2 = PREFIX + catch(requests.get(url).text)
    # http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/up.txt"

    rows, cols, row_clues, col_clues = parse(requests.get(url2).text)
    print_nonogram(solve_nonogram(row_clues, col_clues))
    # See a python

    url3 = PREFIX + 'python.html'
    something = catch(requests.get(url3).text, pattern=r'<br/>\s*<br/>\s*(.*?)\s*</font>', cnt=0)
    return something


if __name__ == "__main__":
    r = requests.get(url)
    something = r.text
    rows, cols, row_clues, col_clues = parse(something)
    answer = solve(row_clues, col_clues)
    print(answer)
    # "Free" as in "Free speech", not as in "free...
    # Google this sentence and the answer is beer

    # http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/beer.html
