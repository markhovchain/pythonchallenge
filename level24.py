__author__ = 'dracz'

url24 = 'http://www.pythonchallenge.com/pc/hex/ambiguity.html'

from PIL import Image, ImageShow
from urlhelp import openurl

"""
Image is of a complex maze
clue: 'from top to bottom'
There are openings at top-right and bottom-left.
So we need to solve the maze?
"""


maze = Image.open(openurl('http://www.pythonchallenge.com/pc/hex/maze.png', 'butter', 'fly'))
w, h = maze.size
start = (w-2, 0)
end = (1, h-1)
wall = (255,) * 4


def adjacent(x, y):
    adj = []
    for d in (0, 1), (1, 0), (-1, 0), (0, -1):
        nx, ny = (x + d[0], y + d[1])
        if w > nx >= 0 <= ny < h and maze.getpixel((nx, ny)) != wall:
            adj.append((nx, ny))
    return adj

from collections import deque


def bfs(start_pos, goal_pos):
    print("searching for {}, from {}...".format(goal_pos, start_pos))
    paths = {goal_pos: None}
    q = deque([goal_pos])
    while q:
        v = q.popleft()
        for a in adjacent(v[0], v[1]):
            if a not in paths.keys():
                paths[a] = v
                if a == start_pos:
                    return paths
                q.append(a)
    return paths

maze_solution_img = "img/maze_solution.png"
maze_path_img = "img/maze_path.png"

def solve():
    nexts = bfs(start, end)
    path = []

    print("goal found after visiting {} nodes".format(len(nexts.keys())))
    nxt = nexts[start]

    while nxt is not None:
        path.append(nxt)
        nxt = nexts[nxt]

    print("shortest path length:", len(path))

    maze_path = Image.new(maze.mode, maze.size)
    for xy in [(x,y) for x in range(maze.size[0]) for y in range(maze.size[1])]:
        maze_path.putpixel(xy, (255,)*4)

    for p in path:
        maze_path.putpixel(p, maze.getpixel(p))  # plot the pixels values along the path
        maze.putpixel(p, (160, 32, 240))  # highlight the solution in the maze

    ImageShow.show(maze)
    maze.save(maze_solution_img)

    ImageShow.show(maze_path)
    maze_path.save(maze_path_img)

    # goal found after visiting 194941 nodes
    # shortest path length: 44622

    return path


if __name__ == "__main__":
    path = solve()

    # the solution of the maze does not appear to spell anything,
    # but the pixel values along the path may encode some information

    # When the pixel values are examined, only the red channel is used and every other pixel is black

    """
    (80, 0, 0, 255)
    (0, 0, 0, 255)
    (75, 0, 0, 255)
    (0, 0, 0, 255)
    (3, 0, 0, 255)
    (0, 0, 0, 255)
    (4, 0, 0, 255)
    (0, 0, 0, 255)
    (20, 0, 0, 255)
    ...
    """

    # let's take only the red value from the even pixels and since they are 0-255

    mp = Image.open(maze_path_img)
    pixels = [mp.getpixel(xy) for xy in path]
    b = bytes([r for r,g,b,a in pixels[::2]])

    # from the leading bytes, looks like zip file
    # PK\x03\x04\x14\x00\x00\x00\x08\x00\xc2\x88\xc2\x9a...

    with open("img/maze.zip", "wb") as f:
        f.write(b)

    # > unzip maze.zip
    # Archive:  maze.zip
    # inflating: maze.jpg
    # extracting: mybroken.zip

    # unzip mybroken.zip
    # Archive:  mybroken.zip
    # inflating: mybroken.gif             bad CRC 31eddaa4  (should be 383782e7)

    # so maze.jpg contains an image with the word "lake"
    # and mybroken.gif only partially inflates

    url25 = "http://www.pythonchallenge.com/pc/hex/lake.html"

    # but what about the mybroken.gif?
    # it was a cyclic redundancy check (CRC) checksum error
    # last level we emailed an apology to leopold and he replied:

    """
    Have you found my broken zip?
    md5: bbb8b499a0eef99b52c7f13f4e78c24b
    Can you believe what one mistake can lead to?
    """

