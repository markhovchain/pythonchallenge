__author__ = 'dracz'

url31 = "http://www.pythonchallenge.com/pc/ring/grandpa.html"

# title: where am i?
# hint: <!-- short break, this ***REALLY*** has nothing to do with Python -->
# image of a phallic looking rock on the sea
# link leads to pwd protected page with domain: island: country

url = "http://www.pythonchallenge.com/pc/rock/grandpa.html"

# using google image search, reveals that this is
# grandmother and grandfather rock in Koh Samui, Thailand

print("""
http://www.pythonchallenge.com/pc/rock/grandpa.html
username: kohsamui
password: thailand
""")

import prompt
#prompt.openurl(url)

# title: UFOs?
# msg: That was too easy, you are still on 31...
# image of blue mandelbrot set in the image:

# inside the img tag is
"""
<window left="0.34" top="0.57" width="0.036" height="0.027"/>
<option iterations="128"/>
"""

# these values seem like the parameters of a mandelbrot set

from PIL import Image
import urlhelp

# mb_url = "http://www.pythonchallenge.com/pc/rock/mandelbrot.gif"
# mb1 = Image.open(urlhelp.openurl(mb_url, "kohsamui", "thailand"))

mb1 = Image.open("img/mandelbrot.gif")
w, h = mb1.size

import mandelbrot

mb2 = mandelbrot.render(w, h, 128, 0.34, 0.34+0.036, 0.57, 0.57+0.027)
mb2.putpalette(mb1.getpalette())
mb2.save("img/mandelbrot_2.gif")
mb2.show()

mb1_data = mb1.getdata()
mb2_data = mb2.getdata()

print(min(mb1_data), max(mb1_data))
print(min(mb2_data), max(mb2_data))

# mb1 data is in range (0, 114)
# mb2 data is in range (13, 127)

# The image looks identical to the original, but is it?
# Looks like the min value was subtracted out of mb1
# For comparison, lets subtract min from mb2 as well

diffs = [d1 - d2 - 13 for d1, d2 in zip(mb1.getdata(), mb2.getdata())]
# rendering these in the original image w, h does not reveal anything
# try using only the nonzero diffs

nz_diffs = [d for d in diffs if d != 0]
print(len(nz_diffs))
# 1679
# can we interpret these as an image?
# what shapes will work?

def factors(n):
    return set(x for t in ([i, n//i] for i in range(2, int(n**0.5)+1) if n % i == 0) for x in t)

print(factors(1679))
# {73, 23} # semi-prime: unique product of 2 primes

print(set(nz_diffs))
# {-16, 16}
# only two values, so it can be rendered as one bit black and white image 23 x 73

dimg = Image.new("1", (23, 73))
dimg.putdata([d > 0 for d in nz_diffs])
dimg = dimg.resize((230,730))
dimg.save("img/arecibo.gif")
dimg.show()

# image search reveals that it's the arecibo message sent by SETI in 1974
# https://en.wikipedia.org/wiki/Arecibo_message

url32 = "http://www.pythonchallenge.com/pc/rock/arecibo.html"
import prompt
prompt.openurl(url32)

