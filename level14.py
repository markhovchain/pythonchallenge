__author__ = 'dracz'

# page title is: "walk around"
# clue: "remember: 100*100 = (100+99+99+98) + (..."
# image is of a spiral pastry

# wire.png is 10000 x 1 png
# seems like we need to wrap the pixels around in a spiral pattern to form new 100x100 img

# ... + (98+97+97+96) + (96+95+95+94) + ...

from urlhelp import openurl
from PIL import Image


wire = Image.open(openurl("http://www.pythonchallenge.com/pc/return/wire.png", "huge", "file"))

# width and height of new image
edge = 100

# the new image
img = Image.new(wire.mode, (edge, edge))

# how far along the 10000 x 1 pixel input image we have travelled
pos = 0

ps = []

# t, b, r, l are length of top, right, bottom, left, edges of each iteration
for i, (t, r, b, l) in enumerate([(i, i-1, i-1, i-2) for i in range(edge, 1, -2)]):

    # top-side of this spiral iteration
    for j in range(t):
        img.putpixel((j+i, i), wire.getpixel((pos+j, 0)))
    pos += t

    # right-side of this spiral iteration
    for j in range(r):
        img.putpixel((edge-1-i, j+i+1), wire.getpixel((pos+j, 0)))
    pos += r

    # bottom-side of this spiral iteration
    for j in range(b):
        img.putpixel((edge-2-i-j, edge-1-i), wire.getpixel((pos+j, 0)))
    pos += b

    # left-side of this spiral iteration
    for j in range(l):
        img.putpixel((i, edge-2-i-j), wire.getpixel((pos+j, 0)))
    pos += l

f = "./img/uzi.png"
print("writing {}...".format(f))
img.save(f)
img.show()

import prompt
prompt.openurl("http://www.pythonchallenge.com/pc/return/cat.html")

# his name is uzi
prompt.openurl("http://www.pythonchallenge.com/pc/return/uzi.html")