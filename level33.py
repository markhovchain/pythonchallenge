__author__ = 'dracz'

url33 = "http://www.pythonchallenge.com/pc/rock/beer.html"

# title: 33 bottles of beer on the wall
# beer1.jpg is of lots of bottles of whiskey aligned on 16 shelves in a sort of pyramid
# actually contains 239 bottles of whiskey with each side containing 19+18+...+13+8
# just one bottle missing in the 3rd position in 4th from bottom shelf on left side
# comment contains:

"""
If you are blinded by the light,
remove its power, with its might.
Then from the ashes, fair and square,
another truth at you will glare.
"""

beer2 = "http://www.pythonchallenge.com/pc/rock/beer2.jpg"
# image says: no, png

beer2 = "http://www.pythonchallenge.com/pc/rock/beer2.png"
# 138x138 grey-scale image with some white noise and an x in the middle

# based on the clue, "if you are blinded by the light, remove it's power":
# we need to remove light pixels, but to throw away pixels we need to resize the image.
# clue says: "fair and square", so maybe the hidden image is also square
# then the square root of the total num of remaining pixels must be integer
# strategy: count pixels by intensity,
# then try to find pixels values that if removed would leave a square image


from PIL import Image

img = Image.open(open("img/beer2.png", "rb"))
data = list(img.getdata())

from collections import Counter
from itertools import accumulate

n = img.size[0] * img.size[1]

# first count the frequency of pixel intensities and order by descending intensity
counts = sorted(Counter(data).most_common(), reverse=True)

from math import sqrt

# now let's see if there are pixels that if removed would leave a square image
print(len([v for v,c in counts if sqrt(n-c).is_integer()]))

# that results in zero. perhaps we need to remove all pixels brighter than certain value?
# compute the cumulative sum of the counts up to each intensity

sums = list(accumulate([c for v,c in counts]))

# now see if there are ranges that if removed would result in square image
print(len([s for s in sums[:-1] if sqrt(s).is_integer()]))

# that results in 0 also, what if we look dark to light? as in "from the ashes"

counts.reverse()
sums = list(accumulate([c for v, c in counts]))
print(len([s for s in sums[:-1] if sqrt(s).is_integer()]))

# aha! 32. Let's try to make an image from each:

for i, c in enumerate(counts):
    sq = sqrt(sums[i])
    if not sq.is_integer():
        continue
    nd = [b for b in data if b <= counts[i][0]]
    mx = max(nd)
    nb = [255 if b == mx else 0 for b in nd]
    nim = Image.frombytes(img.mode, (int(sq), int(sq)), bytes(nb))
    nim.show()


# each image contains a letter
# oslodnidlomeniwragenivx....

# lots of x's, some letters have random dots,
# after a while some are surrounded a solid border:
# g-r-e-m-l-i-n-s

url34 = "http://www.pythonchallenge.com/pc/rock/gremlins.html"

from prompt import openurl
openurl(url34, 34)

"""Temporary End
Thank you for playing the Python Challenge.
More levels will come soon.
"""


