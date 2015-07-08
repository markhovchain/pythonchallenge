__author__ = 'dracz'

url22 = 'http://www.pythonchallenge.com/pc/hex/copper.html'

# picture: atari joystick
# title: "emulate"
# hint: "or maybe white.gif would be more bright"

url = 'http://www.pythonchallenge.com/pc/hex/white.gif'

from urlhelp import openurl
from PIL import Image, ImageSequence


img = Image.open(openurl(url, "butter", "fly"))

# image contains only one non-zero pixel color 8 at pixel 100,100
# maybe it's animated gif?
# iterate through the frames and observe the positions

log = []

for frame in ImageSequence.Iterator(img):
    for x, y in [(x, y) for x in range(img.size[0]) for y in range(img.size[1])]:
        p = img.getpixel((x, y))
        if p != 0:
            log.append((x,y))

# print(set(log))

# {(102, 100), (98, 102), (100, 102), (102, 102), (100, 100), (102, 98), (98, 98), (100, 98), (98, 100)}
# there are 9 distinct positions which can be interpreted as joystick movements
# let's draw the movements


# map coordinates to angle
headings = {
    (98, 98): 135,
    (100, 98): 90,
    (102, 98): 45,
    (98, 100): 180,
    (100, 100): None,
    (102, 100): 0,
    (98, 102): 225,
    (100, 102): 270,
    (102, 102): 315
}

import turtle

t = turtle.Turtle()
t.speed(100)
t.penup()
t.screen.setup(600, 400)
t.setpos(-300, 0)
t.pendown()

for h in [headings[c] for c in log]:
    if h is None:
        t.penup()
        t.setpos(t.pos()[0] + 75, t.pos()[1])
        t.pendown()
        continue
    t.setheading(h)
    t.forward(5)
t.hideturtle()

# it spells "bonus"

import prompt
prompt.openurl("http://www.pythonchallenge.com/pc/hex/bonus.html", 23)


















