__author__ = 'dracz'

import sys, os

LAST_LEVEL = 33

def print_usage():
    print("""
NAME
     solve.py

DESCRIPTION
     solve one or more stages of http://www.pythonchallenge.com/

USAGE
     python3.4 solve.py [from_level [to_level]]

ARGS
     if no levels, are specified then all are solved in sequence.
     if just from_level is specified, then only that level is solved.
     if to_level is also specified, then levels within the range are solved
""")

def main():
    if len(sys.argv) == 1:
        start = 0
        end = LAST_LEVEL + 1

    elif len(sys.argv) == 2:
        if sys.argv[1] == "?" or sys.argv[1] == "help":
            return print_usage()

        start, end = int(sys.argv[1]), int(sys.argv[1])+1

    elif len(sys.argv) > 2:
        start, end = int(sys.argv[1]), int(sys.argv[2])+1

    for i in range(start, end):
        print("solving level", i, "...")
        os.system("python3.4 level{}.py".format(i))

if __name__ == "__main__":
    main()
