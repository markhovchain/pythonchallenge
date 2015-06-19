__author__ = 'dracz'

url27 = "http://www.pythonchallenge.com/pc/hex/speedboat.html"

# title: between the tables
# image: row boat on lake with up-down zig zag strokes near the oar
# link: http://www.pythonchallenge.com/pc/ring/bell.html
# it's pw protected and previous passwords don't work
# login page says: "the order matters"
# hint: did you say gif?
# hint: oh, and this is not a repeat of 14

from PIL import Image
from urlhelp import openurl

# based on the 'did you say gif?' clue, try to open zigzag.gif
img = Image.open(openurl("http://www.pythonchallenge.com/pc/hex/zigzag.gif", "butter", "fly"))

# it looks like random grey-scale noise

w, h = img.size

# try reshaping based on zigzag patterns

def reshape_du():
    """ reshape the image based on down-up zigzag """
    img2 = Image.new(img.mode, (int(w*2), h//2))
    for y in range(0, h, 2):
        for x in range(w):
            img2.putpixel((x, y//2), img.getpixel((x, y)))
            img2.putpixel((x+w, y//2), img.getpixel((w-x-1, y+1)))
    return img2


def reshape_lr():
    """ reshape based on left-right zigzag """
    img2 = Image.new(img.mode, (w//2, int(h*2)))
    for x in range(0, w, 2):
        for y in range(h):
            img2.putpixel((x//2, y), img.getpixel((x, y)))
            img2.putpixel((x//2, y+h), img.getpixel((x+1, h-y-1)))
    return img2


# try looking at the differences in columns
# try starting from the bottom-left, then zig zag up and down

def get_cols(zigzag=True):
    # get columns of the image and optionally flip each column
    cols = []
    for x in range(w):
        col = []
        for y in range(h):
            col.append(img.getpixel((x,y)))
        if zigzag and x % 2 == 0:
            col = list(reversed(col))
        cols.append(col)
    return cols


def img_to_rgb():
    # convert the grey scale to rgb
    cols = get_cols(False)
    nimg = Image.new("RGB", (len(cols), len(cols[0])//3))
    for x in range(len(cols)):
        c = cols[x]
        for i in range(0, len(c), 3):
            r, g, b = c[i], c[i+1], c[i+2]
            nimg.putpixel((x, i//3), (r, g, b))
    nimg.show()


def col_diffs(zigzag=True):
    # compute differences between columns
    cols = get_cols(zigzag)
    even = cols[::2]
    odd = cols[1::2]
    diffs = []
    for i in range(len(even)):
        diff = [e - o for e in even[i] for o in odd[i]]
        diffs.append(diff)

import binascii

def convert_color():
    mode, ba = img.palette.getdata()
    print(mode)
    # the palette is RGB, but the image is grey scale

    print(ba[:100])
    # b'%%%\xe5\xe5\xe5\xa2\xa2\xa2\x88\x88\x88;;;

    print(ba[::3] == ba[1::3] == ba[2::3])  #True
    # each consecutive triplet of bytes the same value

    print(len(ba[::3])) #256

    # use the color palette to convert greyscale byte into rgb
    nb = [img.palette.getcolor((b)) for b in img.getdata()]
    nimg = Image.frombytes("P", (w, h), bytes(nb))
    nimg.save("img/zigzag_color.gif")

    # now we can start to see something there
    # it's a key and text "not" "word", but it's very unclear
    # entering these in the auth box, don't seem to work
    # there are bands of ascending numbers interspersed with the img data
    # "the order matters?"
    return nb


def between_tables():
    mode, palette = img.palette.getdata()
    table = bytes.maketrans(bytes(range(256)), palette[::3])
    bb = bytes(img.getdata())
    cb = bb.translate(table)

    # print(bb[:100])
    # b'\xd7\xd0\xcb\x0c\xfe<\x8bHB\xbd\x7f\xb0\xadF\xaa\xcf\...'

    # print(cb[:100])
    # '\xd0\xcb\x0c\xfe<\x8bHB\xbd\x7f\xb0\xadF\xaa\xcf\...

    # Look the same, but misaligned

    print(bb[1:] == cb[0:-1])
    # False: There are other differences. lets see

    same = bytes([bb[i] for i in range(1, len(bb)) if bb[i] == cb[i-1]])
    print(same[:100])
    # b'\xd0\xcb\x0c\xfe<\x8bHB\xbd\x7f\xb0\xadF\xaa\xcf\' ~\
    # bytes that are the same looks like an image,
    # however we will need to keep the same dims as original

    b1 = []
    for i in range(1, len(bb)):
        if bb[i] == cb[i-1]:
            b1.append(0)
        else:
            b1.append(255)

    nimg = Image.frombytes("L", (w,h), bytes([0]+b1+[0]))
    nimg.save("img/zigzag_translated.gif")
    nimg.show()

    # now we can see it better:
    # "not", "word", "busy?"

    diff = bytes([bb[i] for i in range(1, len(bb)) if bb[i] != cb[i-1]])
    print(diff[:100])
    # b'BZh91AY&SY\xe0\xaaYF\x00\x17\x9a\x11\x80@\
    # bytes that differ look like bz2

    from bz2 import decompress

    words = decompress(diff)
    # print(words)
    # lots of python keywords and ../ring/bell.html

    from keyword import kwlist
    for s in set(words.split()):
        if s.decode() not in kwlist:
            print(s)

    """
    b'../ring/bell.html'
    b'print'
    b'switch'
    b'exec'
    b'repeat'
    """

    # print and exec were removed in python 3. so the python2.7 list just includes switch and repeat

    url28 = "http://www.pythonchallenge.com/pc/ring/bell.html"

    from prompt import openurl
    openurl(url28)


between_tables()


