__author__ = 'dracz'

url26 = "http://www.pythonchallenge.com/pc/hex/decent.html"

# image of rhesus monkeys
# title: be a man - apologize!
# hint: you've got his email
# hint: hurry up, I'm missing the boat

# this is referring to the email apology sent to leopold in level23
# he responded:

"""
Have you found my broken zip?
md5: bbb8b499a0eef99b52c7f13f4e78c24b
Can you believe what one mistake can lead to?
"""

# in level24, the unzipping of mybroken.zip led to:

# inflating: mybroken.gif             bad CRC 31eddaa4  (should be 383782e7)

# so maybe there is a single bit error in the zip?
# we can try to flip each bit of every byte and see if the checksum works

from hashlib import md5

def flipbit(ba, checksum):
    bb = list(ba)
    for i in range(len(bb)):
        for n in range(8):
            bb[i] = ba[i] ^ 2**n
            if md5(bytes(bb)).hexdigest() == checksum:
                print("found error in bit {} of byte {}".format(n, i))
                return bytes(bb)
        bb[i] = ba[i]  # return to original state
    raise ValueError("Failed to find erroneous bit")

# that didn't work, maybe not single bit error.
# try replace the byte with all possible values

def changebyte(ba, checksum):
    bb = list(ba)
    for i in range(len(bb)):
        for n in range(256):
            bb[i] = n
            if md5(bytes(bb)).hexdigest() == checksum:
                print("found error byte {} ({} --> {})".format(i, ba[i], bb[i]))
                return bytes(bb)
        bb[i] = ba[i]  # return to original state
    raise ValueError("Failed to find erroneous byte")

broken = open("img/mybroken.zip", "rb").read()

fixed = changebyte(broken, "bbb8b499a0eef99b52c7f13f4e78c24b")

with open("img/myfixed.zip", "wb") as f:
    f.write(fixed)

"""
> unzip myfixed.zip
Archive:  myfixed.zip
replace mybroken.gif? [y]es, [n]o, [A]ll, [N]one, [r]ename: r
new name: myfixed.gif
  inflating: myfixed.gif
"""

# it says "speed"

url27 = "http://www.pythonchallenge.com/pc/hex/speed.html"

# nope. clue said: "I am missing the *boat*"

url27 = "http://www.pythonchallenge.com/pc/hex/speedboat.html"

import prompt
prompt.openurl(url27)

