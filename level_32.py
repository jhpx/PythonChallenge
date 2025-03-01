#!/bin/env python
# coding=utf-8
# http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/arecibo.html

import requests
from PIL import Image, ImageDraw

PREFIX = "http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/"
url = PREFIX + 'warmup.txt'


def parse_data(data):
    lines = iter(data.splitlines())
    width, height = 0, 0
    rows, cols = [], []
    for line in lines:
        if line.startswith("#"):
            continue
        if line.strip() == "":
            break
        if width == 0:
            width, height = map(int, line.split())
        else:
            rows.append(list(map(int, line.split())))
    for line in lines:
        if line.strip() == "":
            continue
        cols.append(list(map(int, line.split())))
    return width, height, rows, cols


def solve_nonogram(width, height, rows, cols):
    grid = [[0] * width for _ in range(height)]

    def is_valid_row(row, hints):
        current = []
        count = 0
        for cell in row:
            if cell == 1:
                count += 1
            elif count > 0:
                current.append(count)
                count = 0
        if count > 0:
            current.append(count)
        return current == hints

    def backtrack(y):
        if y == height:
            for x in range(width):
                column = [grid[y][x] for y in range(height)]
                if not is_valid_row(column, cols[x]):
                    return False
            return True
        row_hint = rows[y]
        for candidate in generate_candidates(width, row_hint):
            grid[y] = candidate
            if backtrack(y + 1):
                return True
        return False

    backtrack(0)
    return grid


def generate_candidates(width, hint):
    from itertools import combinations
    blocks = len(hint)
    total = sum(hint) + blocks - 1
    if total > width:
        return []
    positions = width - total
    gaps = [0] + [1] * (blocks - 1) + [0]
    for combo in combinations(range(positions + len(gaps)), len(gaps)):
        gaps_sizes = [combo[i] - combo[i - 1] for i in range(1, len(combo))]
        if any(s < 0 for s in gaps_sizes):
            continue
        row = []
        for i in range(blocks):
            row += [0] * gaps_sizes[i]
            row += [1] * hint[i]
            if i < blocks - 1:
                row += [0] * 1
        row += [0] * (width - len(row))
        yield row


def solve(width, height, rows, cols):
    solution = solve_nonogram(width, height, rows, cols)
    img = Image.new("RGB", (width * 10, height * 10), "white")
    draw = ImageDraw.Draw(img)
    for y in range(height):
        for x in range(width):
            if solution[y][x] == 1:
                draw.rectangle([x * 10, y * 10, (x + 1) * 10, (y + 1) * 10], fill="black")
    img.show()
    return ""


if __name__ == "__main__":
    r = requests.get(url)
    something = r.text
    width, height, rows, cols = parse_data(something)
    answer = solve(width, height, rows, cols)
    # http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/arrow.html
