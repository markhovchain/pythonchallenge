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
"""
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


# "brightness works"
url18 = "http://www.pythonchallenge.com/pc/return/brightness.html"

# same image is returned, with same title: "can you tell the difference?"
# hint: maybe consider deltas.gz
"""
gzurl = "http://www.pythonchallenge.com/pc/return/deltas.gz"

import gzip

gz = gzip.decompress(openurl(gzurl, "huge", "file").read())
print(gz.decode())