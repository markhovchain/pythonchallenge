__author__ = 'dracz'

url27 = "http://www.pythonchallenge.com/pc/hex/speedboat.html"

# title: between the tables
# image: row boat on lake with up-down zig zag strokes near the oar
# link: http://www.pythonchallenge.com/pc/ring/bell.html
# it's pw protected and previous passwords don't work
# hint: did you say gif?
# hint: oh, and this is not a repeat of 14

from PIL import Image
from urlhelp import openurl

# based on the 'did you say gif?' clue, try to open zigzag.gif
img = Image.open(openurl("http://www.pythonchallenge.com/pc/hex/zigzag.gif", "butter", "fly"))

# it looks like random grey-scale noise

w, h = img.size

for x in range(0, w, 2):
    for y in range(h):
        print(x,y)


