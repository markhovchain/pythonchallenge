__author__ = 'dracz'

url28 = "http://www.pythonchallenge.com/pc/ring/bell.html"
# username: repeat
# password: switch

# title: many pairs ring-ring
# RING-RING-RING
# say it out loud

# when i do i hear, GREEN
# image has a lot of green

from urlhelp import openurl
from PIL import Image, ImageShow

img = Image.open(open("img/bell.png", "rb"))
w, h = img.size

bb = img.getdata()

from collections import defaultdict
from operator import itemgetter


def get_pairs():
    # look into the colors
    # return a dict where keys are counts, and val is a pair of green channel colors with that count

    counts = defaultdict(int)
    greens = defaultdict(int)

    for rgb in bb:
        counts[rgb] += 1
        greens[rgb[1]] += 1

    print("number colors:", len(counts))
    print("distinct green channels:", len(greens), "\n")

    # show top pixels by color
    # for k, v in sorted(counts.items(), key=itemgetter(1), reverse=True)[:100]:
    #    print(k, v)

    """
    (10, 45, 11) 145
    (6, 3, 7) 142
    (9, 3, 10) 140
    (8, 3, 9) 139
    (10, 3, 0) 133
    (10, 3, 11) 127
    (11, 45, 12) 127
    (4, 3, 5) 126
    (6, 45, 7) 125
    (7, 45, 8) 123
    (7, 3, 8) 122
    (5, 3, 4) 119
    (8, 3, 7) 116
    ...
    """

    # find counts that come in pairs
    gcounts = defaultdict(int)
    for v in greens.values():
        gcounts[v] += 1

    gpc = [k for k, v in gcounts.items() if v == 2]
    print("counts that occur in pairs:", gpc, "\n")

    gc = defaultdict(list)

    for c in gpc:
        for k, v in greens.items():
            if v == c:
                gc[c].append(k)

    print("green channel pairs:", ", ".join(["{}:{}".format(k,v) for k,v in gc.items()]), "\n")
    # there are 23
    return gc


import itertools

def render_pairs():
    """ draw the pixels in which the counts of that pixel green channel were the same as one other green channel """
    gs = list(itertools.chain.from_iterable(get_pairs().values()))
    nimg = Image.new(img.mode, img.size)
    for xy in [(x,y) for x in range(w) for y in range(h)]:
        r,g,b = img.getpixel(xy)
        if g in gs:
            nimg.putpixel(xy, (r,g,b))
    ImageShow.show(nimg)
    # nope


def pairs():
    # look at pairs of consecutive green channel values
    greens = [g for r,g,b in bb]
    ps = [(greens[i], greens[i+1]) for i in range(0, len(greens), 2)]
    # look at the absolute value of the difference of these
    d = [abs(p[1] - p[0]) for p in ps]
    # lots of 42's # the meaning of life is ...
    print(bytes([n for n in d if n != 42]))
    # b'whodunnit().split()[0] ?'
    # idk: nadav? guido?

pairs()

from prompt import openurl
openurl("http://www.pythonchallenge.com/pc/ring/guido.html")




