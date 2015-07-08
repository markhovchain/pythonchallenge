__author__ = 'dracz'

url16 = "http://www.pythonchallenge.com/pc/return/mozart.html"

# clue: let me get this straight
# there are 4 pixel-wide horizontal bars on each image row
# make an image twice as large and align the bars along the center

from PIL import Image

import urlhelp

img = Image.open(urlhelp.openurl("http://www.pythonchallenge.com/pc/return/mozart.gif", "huge", "file"))

w, h = img.size

centers = {}

for y in range(h):
    last = None
    count = 1
    for x in range(w):
        p = img.getpixel((x, y))
        if p == last:
            count += 1
            if count == 4:
                centers[y] = x-2
        else:
            count = 0
            last = p


straight = Image.new(img.mode, (2*w, h))

for y, c in centers.items():
    for x in range(w):
        straight.putpixel((w-c+x, y), img.getpixel((x, y)))

f = 'img/romance.png'
print("saving {}...".format(f))
straight.save(f)
straight.show()

# says 'romance'
import prompt
prompt.openurl("http://www.pythonchallenge.com/pc/return/romance.html", 17)
