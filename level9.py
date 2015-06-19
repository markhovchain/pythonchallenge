__author__ = 'dracz'

import urlhelp
import re

url9 = 'http://www.pythonchallenge.com/pc/return/good.html'

page = urlhelp.openurl(url9, 'huge', 'file').read().decode()

match = re.search(r'first:\n(.*)\n\nsecond:\n(.*)\n\n-->', page, re.S)

first = [int(n) for n in match.group(1).replace('\n', '').split(',')]
second = [int(n) for n in match.group(2).replace('\n', '').split(',')]

# these are two lists of ints
# first has 442 numbers in the range 77-403
# second has 112 numbers in the range 77-220

# clue is connect the dots, so assume these are lists of line coordinates
# and draw them

import turtle

def draw(coords, color="black", speed=10):
    t = turtle.Turtle()
    t.pencolor(color)
    t.speed(speed)
    t.penup()
    t.setpos(coords[0][0], coords[0][1])
    t.pendown()
    for x, y in coords[1:]:
        t.setpos(x, y)
    t.ht()

line1 = list(zip(first[0::2], first[1::2]))
line2 = list(zip(second[0::2], second[1::2]))

turtle.setworldcoordinates(max(first), max(first)+10, 0, 0)

draw(line1, "brown")
draw(line2, "black")

# it's a cow!
url10 = 'http://www.pythonchallenge.com/pc/return/cow.html'

# clue: "hmm. it's a male."
# oh, it's actually a bull
url10 = 'http://www.pythonchallenge.com/pc/return/bull.html'

import prompt
prompt.openurl(url10)
