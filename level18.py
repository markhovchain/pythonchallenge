__author__ = 'dracz'

url18 = "http://www.pythonchallenge.com/pc/return/balloons.html"

# title: "can you tell the difference?"
# hint:  "it is more obvious that what you might think"

from urlhelp import openurl
from PIL import Image, ImageShow

img = Image.open(openurl("http://www.pythonchallenge.com/pc/return/balloons.jpg", "huge", "file"))

w, h = img.size

left = img.crop((0, 0, w//2-1, h-1))
right = img.crop((w//2, 0, w-1, h-1))

diff = Image.new(img.mode, left.size)

for x, y in [(x, y) for x in range(0, left.size[0]) for y in range(0, left.size[1])]:
    pl = left.getpixel((x, y))
    pr = right.getpixel((x, y))
    dp = (pl[0]-pr[0], pl[1]-pr[1], pl[2]-pr[2])
    diff.putpixel((x, y), dp)

f = "img/baloons_diff.jpg"
print("saving {}...".format(f))
diff.save(f)

# nothing hidden in this image. must be something more 'obvious':

from urllib.error import HTTPError
import prompt

for s in ['intensity', 'dark', 'darker', 'brighter', 'brightness', 'obvious']:
    url = 'http://www.pythonchallenge.com/pc/return/{}.html'.format(s)
    print("trying {}...".format(url))
    try:
        u = openurl(url, "huge", "file")
        if u.getcode() == 200:
            print("{} works!". format(url))
            prompt.openurl(url)
            break
        else:
            print("{} doesn't work".format(url))
    except HTTPError:
        print("{} doesn't work".format(url))


# "brightness" works
url18 = "http://www.pythonchallenge.com/pc/return/brightness.html"

# same image is returned, with same title: "can you tell the difference?"
# hint: maybe consider deltas.gz


gzurl = "http://www.pythonchallenge.com/pc/return/deltas.gz"

import gzip

gz = gzip.decompress(openurl(gzurl, "huge", "file").read())

"""
89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52 00 00   89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52 00 00
02 8a 00 00 00 c8 08 02 00 00 00 e0 19 57 95 00 00 00   02 8a 00 00 00 c8 08 02 00 00 00 e0 19 57 95 00 00 00
09 70 48 59 73 00 00 0b 13 00 00 0b 13 01 00 9a 9c 18   09 70 48 59 73 00 00 0b 13 00 00 0b 13 01 00 9a 9c 18
00 00 00 07 74 49 4d 45 07 d5 05 07 0c 18 32 98 c6 a0   00 00 00 07 74 49 4d 45 07 d5 05 07 0c 18 32 98 c6 a0
48 00 00 00 1d 74 45 58 74 43 6f 6d 6d 65 6e 74 00 43   48 00 00 00 1d 74 45 58 74 43 6f 6d 6d 65 6e 74 00 43
"""
# the same for a while
"""
56 3b 44 a4 a0 00 04 d8 04 99 55 d6 c3 af 78 59 73 dd   56 3b 44 a4 a0 00 04 d8 04 99 55 d6 c3 af 78 59 73 dd
89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52 00 00   72 6c 41 7d 6b f7 bd a4 41 41 65 46 79 46 79 4f 6c d6
72 6c 41 7d 6b f7 bd a4 41 41 65 46 79 46 79 4f 6c d6   bc d6 30 1d b5 2d b5 f1 a6 7f eb 29 9a b6 48 0a 94 29
bc d6 30 1d b5 2d b5 f1 a6 7f eb 29 9a b6 48 0a 94 29   32 02 49 8a 66 60 12 a4 0d ea 25 e6 0a 3a 5e a5 88 18
32 02 49 8a 66 60 12 a4 0d ea 25 e6 0a 3a 5e a5 88 18   9e bf 18 32 ca 0f f4 d1 81 3e 2a 55 d5 fb 12 34 bc 6e
9e bf 18 32 ca 0f f4 d1 81 3e 2a 55 d5 fb 12 34 bc 6e   d1 12 95 43 b8 eb 70 35 a3 8b 78 52 7f 63 48 29 1d a8
01 50 00 00 00 8f 08 06 00 00 00 ac f7 83 97 00 00 00   e1 48 8d 13 ba 21 0b a2 c4 52 92 72 1a e0 57 bc f8 f8
d1 12 95 43 b8 eb 70 35 a3 8b 78 52 7f 63 48 29 1d a8   9b 1e 2d 2f ee 32 08 a4 a0 44 0b a6 a1 b7 a9 79 f0 f0
"""
# then bunch of inserts and mis-alignments ... then left is much shorter
# the initial byte are PNG hex signature

# use difflib to "find the differences"
# then create separate image for the +, -, and no diff cases

lines = gz.decode().split('\n')
pairs = [(line[:53], line[56:]) for line in lines]
left, right = zip(*pairs)

from difflib import Differ
diff = list(Differ().compare(left, right))

import binascii

for i, c in [(1, '+'), (2, '-'), (3, ' ')]:
    hexs = ''.join([s[2:].replace(' ', '') for s in diff if s[0] == c])
    fname = 'img/deltas{}.png'.format(i)
    print("writing {}...".format(fname))
    with open(fname, 'wb') as f:
        f.write(binascii.unhexlify(hexs))

# the files say: butter - fly - ../hex/bin.html

# http://www.pythonchallenge.com/pc/hex/bin.html
# username: butter
# password: fly







