__author__ = 'dracz'

url11 = "http://www.pythonchallenge.com/pc/return/5808.html"

# clue is: odd even
# maybe there are messages encoded in the odd and/or even pixels of the image?

from urlhelp import openurl
from PIL import Image, ImageShow

img = Image.open(openurl("http://www.pythonchallenge.com/pc/return/cave.jpg", "huge", "file"))

size = (img.size[0]//2, img.size[1]//2)

even = Image.new(img.mode, size)

for x in range(0, img.size[0], 2):
    for y in range(0, img.size[1], 2):
        even.putpixel((x-x//2, y-y//2), img.getpixel((x,y)))

f = "./img/even.png"
print("saving {}...".format(f))
even.save(f)

ImageShow.show(even)

# if you look closely, you can see a word in the image: evil

import prompt
prompt.openurl("http://www.pythonchallenge.com/pc/return/evil.html")



