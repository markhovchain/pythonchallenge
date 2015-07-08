__author__ = 'dracz'

url32 = "http://www.pythonchallenge.com/pc/rock/arecibo.html"

# title: etch-a-scetch

# it shows a Nonogram puzzle: https://en.wikipedia.org/wiki/Nonogram
# the numbers in the margin show the length of contiguous blocks in the rows/columns

# in the page source:  Fill in the blanks <!-- for warmup.txt -->
# try warmup.txt

warmup = "http://www.pythonchallenge.com/pc/rock/warmup.txt"

# this file contains lines with the dimensions and horizontal/vertical clues for a nonogram
# looks like we need to solve the puzzle


# characters to use for marking and visualizing puzzle/solution
SPACE = " "
MARK = "X"
UNKNOWN = "?"


def runs(l, w, space=SPACE, mark=MARK):
    """
    Generate list of possible runs
    :param l: list of ints specifying run lengths
    :param w: the width of the puzzle
    :param space: character to use for spaces
    :param mark: character to use for marks
    :return: list of list of bool specified whether box is marked

    >>> runs([2,1], 5, space="O", mark="X") == ['XXOXO', 'XXOOX', 'OXXOX']
    True
    >>> runs([1,1,1], 5, space=[False,], mark=[True,])
    [[True, False, True, False, True]]
    """
    res = []
    for i in range(w - sum(l) - len(l) + 2):
        head = space*i + mark*l[0]
        if len(l) == 1:
            res.append(head + space*(w-len(head)))
        else:
            tails = [space + tail for tail in runs(l[1:], w - len(head) - 1, space, mark)]
            res.extend([head + tail for tail in tails])
    return res


def solve(hor, ver, max_iters=1000):
    """ solve a puzzle specified by the horizontal and vertical clues
    :param hor: list of list of integer clues for each row of the puzzle
    :param ver: list of list of integer clues for each column of the puzzle
    :return: a list of the rows of the puzzle solution as characters
    """
    w, h = len(ver), len(hor)
    total = w*h

    # generate all possible runs for row and column clues
    hc = [runs(r, w) for r in hor]
    vc = [runs(r, h) for r in ver]

    res = [[UNKNOWN for i in range(w)] for j in range(h)]
    iters, filled = 0, 0

    # iterate until all boxes are filled in or we reach max number of iterations
    print("\nsolving...\n")
    while total - filled > 0:
        iters += 1
        iterate(hc, vc, res, col=False)
        iterate(vc, hc, res, col=True)
        filled = len([x for row in res for x in row if x != UNKNOWN])
        print("filled", filled, "after", iters, "iterations")

    print("\nsolved:\n")
    print_solution(res)
    return res



def iterate(hc, vc, res, col=False):
    """ iterate through one pass of the puzzles rows and columns
    :param hc: list of current possible solutions for first dimension
    :param vc: list of current possible solutions for second dimension
    :param res: the list of rows of the current solution
    :param col: whether iterating over columns or rows
    """
    for i in range(len(hc)):
        cs = hc[i]  # candidates for this row/col
        for j in [j for j in range(len(vc))]:
            r = res[i][j] if not col else res[j][i]
            if not r == UNKNOWN:
                continue
            if [c[j] for c in cs].count(cs[0][j]) == len(cs):
                if not col:
                    res[i][j] = cs[0][j]  # fill in the row
                else:
                    res[j][i] = cs[0][j]  # fill in the col
                vc[j] = prune(vc[j], i, cs[0][j])  # prune cols/rows

def prune(cs, i, val):
    """ prune the list of list in cs to contain only those that have the specified val at index i """
    return [c for c in cs if c[i] == val]


def print_solution(res):
    """ print the solution to console """
    print("\n".join(["".join(r) for r in res]))


import re

def solve_puzzle(f):
    """ Solve the puzzle specified in the file-like obj f """

    def parse(s):
        """parse lines of run length clues into list of list of int"""
        return [[int(i) for i in l.split()] for l in s.split("\n") if l]

    lines = f.read().decode()
    hor = parse(re.search(r'# Horizontal(?: lines)?(.*)#', lines, re.S).group(1))
    ver = parse(re.search(r'# Vertical(?: lines)?(.*)', lines, re.S).group(1))
    return solve(hor, ver)


solve_puzzle(open("img/warmup.txt", "rb"))

"""
filled 81 after 2 iterations:

XX  X  XX
X  XXX  X
  XXXXX
 XXXXXXX
XXXXXXXXX
   XXX
XX XXX XX
XX XXX XX
XX XXX XX
"""

up = "http://www.pythonchallenge.com/pc/rock/up.txt"
up_sol = solve_puzzle(open("img/up.txt", "rb"))

"""
filled 1024 after 13 iterations:

                   XXX XX
                  XXXXXXXX
                 XXXXXXXXXX
                 XXX   X  X
                 XXXXX XX X
                 XXXXX XX X
                XXXX   X  X
             XXXXXXXXXXXXXXX
           XXXXXXXXXXXXXXXXXXX
          XXXXXX XXXXXXXXXXXXXX
         XXXXXX   X XXXXXXXXXXXX
         XXXXXX     X XXXXXXXXXX
        XXXXXXX   XX  X XXXXXXXX
        XXXXXX X X XX   X X X  X
        XXXXX   X  XXXX        X
        XXXXX XXXX X XXXX X X X
        XXXXX   X X   XXXXXXXX
         XXXXX XX  X   XXXXXXXX
         XXXXXX  X  XX   X XXX
          XXXXXX XXX  XX     X
           XXXXXX   X   XXXXX
X           XXXXXX  XXX
XX           XXXXXXX   XX
XXX  XXX   XXXXXXXXXX XXXX
XXXXXXXXX XXXXXXXXXXXX    X
XXXXXXXXXXXXXXXXXXXXXX    X
 XXXXXXXXXXXXXXXXXXXXX XXXX
  X  XXXXXXXXXXXXXXXXX    X
   XX  XXXXXXXX XXXXX     X
        XX     XX     XXXX
          XXXXX  XX X   X
                   XXXXX
"""

from PIL import Image

bs = bytes([0 if x == MARK else 255 for row in up_sol for x in row])

img = Image.frombytes("P", (len(up_sol[0]), len(up_sol)), bs)
img.save("img/up.png")

# from the image we can see it's the python mascot
"http://www.pythonchallenge.com/pc/rock/python.html"

# the page shows the solution of the up.txt nonogram and contains:
# Congrats! You made it through to the smiling python.
# title: here we go
# Congrats! You made it through to the smiling python.
# hint:	"Free" as in "Free speech", not as in "free...

url33 = "http://www.pythonchallenge.com/pc/rock/beer.html"

from prompt import openurl
openurl(url33, 33)



