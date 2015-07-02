__author__ = 'dracz'

url32 = "http://www.pythonchallenge.com/pc/rock/arecibo.html"

# title: etch-a-scetch
# text:  Fill in the blanks <!-- for warmup.txt -->

# it shows a Nonogram puzzle
# the numbers in the margin show the length of contiguous blocks in the rows/columns

warmup = "http://www.pythonchallenge.com/pc/rock/warmup.txt"

# strategy: for each row, generate all possible configurations of boxes
# then check the permutations until the column constraints are met


def lpos(l, start, w):
    """ generate list of possible positions for the run length in l[0]
    in a puzzle of width w, starting from start pos
    >>> lpos([2,1], 0, 5)
    [[0, 1], [1, 2]]
    >>> lpos([2,1], 1, 5)
    [[1, 2]]
    >>> lpos([2,2], 0, 5)
    [[0, 1]]
    >>> lpos([1,1], 0, 5)
    [[0], [1], [2]]
    """
    end = w - sum(l) - len(l) + 2
    return [list(range(p, p+l[0])) for p in range(start, end)]


def pos(l, w):
    """ generate list of possible positions for list of run lengths
    in puzzle of width w
    >>> pos([2,1], 5)
    [[0, 1, 3], [0, 1, 4], [1, 2, 4]]
    >>> pos([1,1,1], 5)
    [[0, 2, 4]]
    """
    res = lpos(l, 0, w)
    while len(l[1:]) > 0:
        l = l[1:]
        new_res = []
        for r in res:
            for t in lpos(l, r[-1] + 2, w):
                new_res.append(r+t)
        res = new_res
    return res


def pprint_runs(boxes, w):
    """ visualize the run length boxes in puzzle of width w """
    s = ""
    for row in boxes:
        print(row)
        s += "\n"
        for i in range(w):
            if i in row:
                s += "X"
            else:
                s += " "
    print(s)


def calc(rows, w):
    """ calculate run length col value for each sequence of row click positions
    >>> calc([[0,1,3], [0,2,3,4], [1,3,4]], 5)
    [[2], [1, 1], [1], [3], [2]]
    """
    m = []
    for row in rows:
        b = [i in row for i in range(w)]
        m.append(b)
    r = []
    for j in range(w):
        c = []
        n = 0
        for i in range(len(m)):
            if m[i][j]:
                n += 1
            elif n > 0:
                c.append(n)
                n = 0
        if n > 0:
            c.append(n)
        r.append(c)
    return r


import itertools

def solve(rows, cols, brute_force=False):
    """ solve the puzzle
    for each row, generate possible solutions
    then check permutations of solutions until match found in the columns
    """
    w = len(cols)
    h = len(rows)

    # list of list of possible solutions for each row, col
    row_sols = [pos(row, w) for row in rows]
    col_sols = [pos(col, h) for col in cols]

    if not brute_force:
        print("pruning...")
        row_sols, col_sols = prune(row_sols, col_sols)

    perms = itertools.product(*row_sols)  # all permutations of row solutions

    n = 0
    for perm in perms:
        if n % 10000 == 0:
            print("checking {}...".format(n))
        n += 1
        sol = calc(perm, w)
        if check(sol, cols):
            print("Found solution:", perm)
            pprint_runs(perm, w)
            print("After", n, "permutations")
            return
    print("No solution found after", n, "permutations")


DEBUG = True

def prune(row_sols, col_sols):
    w = len(col_sols)
    h = len(row_sols)

    marked_rows = mark_boxes(row_sols, w)

    marked_cols = mark_boxes(col_sols, h)

    rows_as_cols = transpose(marked_rows, w)
    cols_as_rows = transpose(marked_cols, h)

    pruned_rows = prune_sol(row_sols, cols_as_rows)
    pruned_cols = prune_sol(col_sols, rows_as_cols)

    return pruned_rows, pruned_cols


def prune_sol(sol_set, constraints):
    filtered = []
    for c, sols in enumerate(sol_set):
        filtered.append([sol for sol in sols if not reject(sol, constraints[c])])
        if DEBUG:
            print("pruning ", c, "...")
            print("filtered {}/{}".format(len(sols) - len(filtered[c]), len(sols)))
            print(sols)
            print(filtered[c])
    len_before = sum([len(l) for l in sol_set])
    len_after = sum([len(l) for l in filtered])
    print("before:", len_before)
    print("after:", len_after)
    return filtered


def reject(sol, constraint):
    for r in constraint:
        if r not in sol:
            if DEBUG:
                ("rejecting", sol, "is missing", r)
            return True
    return False


def print_rows(rows):
    for i, row in enumerate(rows):
        print(i, ":", row)


def transpose(rows, w):
    cols = [[] for i in range(w)]
    for i, l in enumerate(rows):
        for j in l:
            cols[j].append(i)
    return cols


def mark_boxes(rows, w):
    marked = []
    for r, sols in enumerate(rows):
        m = [True,]*w
        for sol in sols:
            for i in range(w):
                if i not in sol:
                    m[i] = False
        marked.append([c for c, v in enumerate(m) if v])
    return marked


def print_marked(rows, w):
    print(" " + "-"*w + " ")
    for row in rows:
        print("|" + "".join(["X" if i in row else " " for i in range(w)]) + "|")
    print(" " + "-"*w + " ")


def check(sol, cols):
    """ check if the solution is contained in the cols """
    for i in range(len(cols)):
        if sol[i] != cols[i]:
            return False
    return True


def solve1():
    """ solve the warmup """
    rows = [[2,1,2], [1,3,1], [5], [7], [9], [3], [2,3,2], [2,3,2], [2,3,2]]
    cols = [[2,1,3], [1,2,3], [3], [8], [9], [8], [3], [1,2,3], [2,1,3]]
    solve(rows, cols)


"""
[0, 1, 4, 7, 8]
[0, 3, 4, 5, 8]
[2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[3, 4, 5]
[0, 1, 3, 4, 5, 7, 8]
[0, 1, 3, 4, 5, 7, 8]
[0, 1, 3, 4, 5, 7, 8]

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

urlnext = "http://www.pythonchallenge.com/pc/rock/up.txt"

# Horizontal lines
hl = """
3 2
8
10
3 1 1

5 2 1
5 2 1
4 1 1
15

19
6 14
6 1 12
6 1 10

7 2 1 8
6 1 1 2 1 1 1 1
5 1 4 1
5 4 1 4 1 1 1

5 1 1 8
5 2 1 8
6 1 2 1 3
6 3 2 1

6 1 5
1 6 3
2 7 2
3 3 10 4

9 12 1
22 1
21 4
1 17 1

2 8 5 1
2 2 4
5 2 1 1
5
"""

# Vertical lines
vl = """
5
5
5
3 1

3 1
5
5
6

5 6
9 5
11 5 1
13 6 1

14 6 1
7 12 1
6 1 11 1
3 1 1 1 9 1

3 4 10
8 1 1 2 8 1
10 1 1 1 7 1
10 4 1 1 7 1

3 2 5 2 1 2 6 2
3 2 4 2 1 1 4 1
2 6 3 1 1 1 1 1
12 3 1 2 1 1 1

3 2 7 3 1 2 1 2
2 6 3 1 1 1 1
12 3 1 5
6 3 1

6 4 1
5 4
4 1 1
5
"""

def parse_lines(s):
    return [[int(i) for i in l.split()] for l in s.split("\n") if l]

def solve2():
    """ solve the second puzzle """
    rows = parse_lines(hl)
    cols = parse_lines(vl)
    solve(rows, cols)

solve1()







