__author__ = 'dracz'

url20 = 'http://www.pythonchallenge.com/pc/hex/idiot2.html'

# title: "go away!"
# image of sign that says: "PRIVATE PROPERTY BEYOND THIS FENCE"
# clue says: "but inspecting it carefully is allowed"

# does it require authentication?

import urlhelp
import re

def openrange(url, rangefrom=None):
    rng = "bytes={}-".format(rangefrom) if rangefrom is not None else None
    if rng is not None:
        print("requesting range: {}...".format(rng))

    s = urlhelp.openurl(url, 'butter', 'fly', rng)
    print("Status: {}".format(s.getcode()))
    print(s.info()["Content-Range"])
    return s

url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'

openrange(url)

# Response header contains:
# Content-Range: bytes 0-30202/2123456789
# indicating that there is more to the image.

# try to get data from subsequent ranges

import urllib.request

n = 30203  # offset

while True:
    try:
        s = openrange(url, n)
        cr = s.info()["Content-Range"]
        n = int(re.search(r'-(\d+)/', cr).group(1)) + 1
        print("\n--> {}".format(s.read().decode()))
    except urllib.request.HTTPError as err:
        print("request failed: {}".format(err))
        break

# there are several iterations before error 416 Requested Range Not Satisfiable is returned
# "Why don't you respect my privacy?"
# "we can go on in this way for really long time."
# "stop this!"
# "invader! invader!"
# "ok, invader. you are inside now."

# try: 'http://www.pythonchallenge.com/pc/hex/invader.html'
# "Yes! that's you!"

# how about the end of the range?

r = openrange(url, 2123456789).read().decode()
print("\n{}\n{}\n".format(r, r[::-1]))


# bytes 2123456744-2123456788/2123456789
# "esrever ni emankcin wen ruoy si drowssap eht"

# reverse it: "the password is your new nickname in reverse"

pwd = "invader"[::-1]
print(pwd)
# redavni

# got all the bytes at the end and beginning, try to walk backwards now
print(openrange(url, 2123456743).read().decode())
# "and it is hiding at 1152983631."

r = openrange(url, 1152983631).read()
print(r[:8])
# PK\x03\x04\x14\x00\t\x00
# first 3 bytes are gzip magic number


import gzip

with gzip.open(r, 'rb') as f:
    print(f.read())

# FAIL: TypeError: embedded NUL character
# gzip module does not support pwd protection

with open("img/invader.zip", "wb") as f:
    print("writing {}...".format(f.name))
    f.write(r)

"""
$ cd img
$ unzip invader.zip
Archive:  invader.zip
[invader.zip] readme.txt password: redavni

inflating: readme.txt
inflating: package.pack

$ less readme.txt
Yes! This is really level 21 in here.
And yes, After you solve it, you'll be in level 22!

Now for the level:

* We used to play this game when we were kids
* When I had no idea what to do, I looked backwards.
"""

# so level 21 is in contained in the package.pack