#!/bin/env python
# coding=utf-8
# http://butter:fly@www.pythonchallenge.com/pc/hex/ambiguity.html
# Find a path in the maze.
import zipfile
from io import BytesIO

import networkx as nx
import requests
from PIL import Image

PREFIX = "http://butter:fly@www.pythonchallenge.com/pc/hex/"
url = PREFIX + 'maze.png'


# White is the wall. Black is the path. Red is the hidden data.
def build_graph(im):
    width, height = im.size
    G = nx.Graph()
    for i in range(width):
        for j in range(height):
            if im.getpixel((i, j)) not in {(255, 255, 255, 255), (127, 127, 127, 255)}:
                G.add_node((i, j))
                if j == 0:
                    start = (i, j)  # (639,0)
                elif j == height - 1:
                    end = (i, j)  # (1,640)

    for i in range(width):
        for j in range(height):
            if not G.has_node((i, j)):
                continue
            dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for dir in dirs:
                neighbor = (i + dir[0], j + dir[1])
                if G.has_node(neighbor):
                    G.add_edge((i, j), neighbor)

    return G, start, end


def solve(something):
    im = Image.open(BytesIO(something))
    print("Building Maze Graph...")
    Maze, start, end = build_graph(im)
    print("Searching Shortest path...")
    path = nx.astar_path(Maze, start, end)
    #
    print("Showing Shortest path...")
    im2 = im.copy()
    for coord in path:
        im2.putpixel(coord, (0, 255, 0, 255))
    im2.show()
    #
    print("Extracting hidden data...")
    hidden = bytes([im.getpixel(coords)[0] for coords in path[1::2]])
    with zipfile.ZipFile(BytesIO(hidden), 'r') as zip:
        for name in zip.namelist():
            if name.endswith('.jpg'):
                Image.open(BytesIO(zip.read(name))).show()
            elif name.endswith('.zip'):
                # Generate 'mybroken.zip' in current folder
                zip.extract(name)

    return


if __name__ == "__main__":
    r = requests.get(url)
    something = r.content
    answer = solve(something)
    # lake

    # http://butter:fly@www.pythonchallenge.com/pc/hex/lake.html
