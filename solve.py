__author__ = 'dracz'

import sys, os

LAST_LEVEL = 33

if len(sys.argv) == 1:
    start = 0
    end = LAST_LEVEL + 1

elif len(sys.argv) == 2:
    start, end = int(sys.argv[1]), int(sys.argv[1])+1

elif len(sys.argv) > 2:
    start, end = int(sys.argv[1]), int(sys.argv[2])+1

for i in range(start, end):
    print("solving level", i, "...")
    os.system("python3.4 level{}.py".format(i))
