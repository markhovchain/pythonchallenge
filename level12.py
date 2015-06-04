__author__ = 'dracz'

url12 = "http://www.pythonchallenge.com/pc/return/evil.html"

"""
Clue is: dealing evil
Image is: evil1.jpg
Maybe there are more evils? 666?
Well, there is evil2.jpg, which gives the hint: "not jpg - .gfx"
evil3.jpg says "no more evils" and there is an evil2.gfx
evil4.jpg is not really a jpg, but rather text file that says: "Bert is evil! go back!"
So there were a total of 5 evils and the evil1 image shows a card dealer dealing into 5 piles.
Maybe the image contains 5 shuffled images?
"""

import urlhelp

evil1 = urlhelp.openurl("http://www.pythonchallenge.com/pc/return/evil2.gfx", "huge", "file").read()

# len(evil) % 5 == 0, so let's split the file into 5 images one byte at a time

import imghdr

for i, img in {i: evil1[i::5] for i in range(5)}.items():
    typ = imghdr.what("", h=img) # determine the image type
    with open("level12_{}.{}".format(i, typ), "wb+") as f:
        print("writing {}...".format(f.name))
        f.write(img)

# the images spell: dis-pro-por-tional

import prompt
prompt.openurl("http://www.pythonchallenge.com/pc/return/disproportional.html")