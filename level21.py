__author__ = 'dracz'

data = open("img/package.pack", "rb").read()

# starts with: x\x9c\x00 (zlib)
# after zlib decompress, still starts with: x\x9c\x00
# after a bunch of decompress, now starts with: BZh
# ...

import zlib
import bz2

# return True if the bytes look like bz2
def is_bz(bs):
    return bs[:3] == b'BZh'

# return True if bytes look like zlib
def is_zlib(bs):
    return bs[:2] == b'x\x9c'

log = []
while True:
    print(data[:32])
    if is_zlib(data):
        data = zlib.decompress(data)
        log.append("Z")
    elif is_bz(data):
        data = bz2.decompress(data)
        log.append("B")
    else:
        # \x80\x8d\x96\xcb\xb5r\xa7\x00\x06Xz\xdafO\x19\xee...
        # can't find a magic number for this
        # clue was: "When I had no idea what to do, I looked backwards"
        # reverse the bytes
        rev = data[::-1]
        if is_zlib(rev):
            print("reversed: {}".format(rev[:32]))
            data = rev
            log.append("R")
        else:
            break

print(data[::-1])
# look at your log

print("Z", log.count("Z"))
print("B", log.count("B"))
print("R", log.count("R"))

# Z 432
# B 300
# R  9

# a little trial and error reveals a bitmap where R are line seps, Z are spaces, and B pen strokes
print(''.join(log).replace("B", "*").replace("R", "\n").replace("Z", " "))

"""
      ***          ***      ********    ********    **********  ********
    *******      *******    *********   *********   *********   *********
   **     **    **     **   **      **  **      **  **          **      **
  **           **       **  **      **  **      **  **          **      **
  **           **       **  *********   *********   ********    *********
  **           **       **  ********    ********    ********    ********
  **           **       **  **          **          **          **   **
   **     **    **     **   **          **          **          **    **
    *******      *******    **          **          *********   **     **
      ***          ***      **          **          **********  **      **
"""

import prompt
prompt.openurl('http://www.pythonchallenge.com/pc/hex/copper.html')


