__author__ = 'dracz'

# the clue in the page src is: <-- zip -->, so look for:
# channel.zip

url6 = 'http://www.pythonchallenge.com/pc/def/channel.html'

import urllib.request, io
from zipfile import ZipFile

zurl = 'http://www.pythonchallenge.com/pc/def/channel.zip'

zip = ZipFile(io.BytesIO(urllib.request.urlopen(zurl).read()))

with zip.open('readme.txt') as readme:
    print(readme.read().decode())

"""
welcome to my zipped list.

hint1: start from 90052
hint2: answer is inside the zip
"""

import re

fn = "90052.txt"
chars = []

while True:
    chars.append(zip.getinfo(fn).comment.decode())
    with zip.open(fn) as f:
        s = f.read().decode()
        print(s)
        match = re.search(r'Next nothing is ([0-9]+)', s)
        if match is None:
            break
        fn = "{0}.txt".format(match.group(1))

# Clue inside 46145.txt is: "Collect the comments"

print(''.join(chars))

"""
****************************************************************
****************************************************************
**                                                            **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
**                                                            **
****************************************************************
 **************************************************************
"""

import prompt
prompt.openurl('http://www.pythonchallenge.com/pc/def/hockey.html', 7)

# Clue: "it's in the air. look at the letters."
# the letters are written other letters: H->O, O->X, C->Y, K->G, E->E, Y->N

prompt.openurl('http://www.pythonchallenge.com/pc/def/oxygen.html', 7)
