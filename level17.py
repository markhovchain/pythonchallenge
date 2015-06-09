__author__ = 'dracz'

url17 = "http://www.pythonchallenge.com/pc/return/romance.html"

# title: "eat?"
# image of cookies and in the corner is the image from challenge 4
# look for cookies set from in level4:

import urlhelp

# url4 = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
# f = urlhelp.openurl(url4)
# print(f.info()["Set-Cookie"]) # info=you+should+have+followed+busynothing...;

# let's try following the nothings as we did in level4
nothing = 12345

import re

msg = []

while True:
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={0}".format(nothing)
    print('fetching "{0}"...'.format(url))
    f = urlhelp.openurl(url)

    cookie = f.info()["Set-Cookie"]
    print(cookie)

    info = re.search(r'info=([^;]+)', f.info()["Set-Cookie"]).group(1)
    msg.append(info)

    res = f.read().decode()
    print(res)

    match = re.search(r'the next busynothing is ([0-9]+)', res)
    if match is None:
        break

    nothing = match.group(1)

print("="*80)

s = ''.join(msg)
print(s)

"""
BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EA
i7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%
05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90
"""

# the BZ at the start indicates that it is bz2 encoded, but since it came from cookie it is also
# url encoded. unescape the %XX sequences and replace the "+" with space

print("="*80)

import urllib
unescaped = urllib.parse.unquote_to_bytes(s.replace("+", " "))
print(unescaped)

"""
b'BZh91AY&SY\x94:\xe2I\x00\x00!\x19\x80P\x81\x11\x00\xafg\x9e\xa0 \x00hE=M\xb5#\xd0\xd4\xd1\xe2\x8d\x06\xa9\xfa&S
\xd4\xd3!\xa1\xeai7h\x9b\x9a+\xbf`"\xc5WX\xe1\xadL\x80\xe8V<\xc6\xa8\xdbH&32\x18\xa8x\x01\x08!\x8dS\x0b\xc8\xaf
\x96KO\xca2\xb0\xf1\xbd\x1du\xa0\x86\x05\x92s\xb0\x92\xc4Bc\xf1w$S\x85\t\tC\xae$\x90'
"""

print("="*80)

# now decompress the message

import bz2
print(bz2.decompress(unescaped))
# is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand

print("="*80)

# refers to mozart's birthday from level15. Mozart's father was Leopold.
# to call him, use the xmlprc service from

from xmlrpc.client import ServerProxy

server = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php/")

print(server.phone("Leopold"))
# 555-VIOLIN

print("="*80)

# going to: http://www.pythonchallenge.com/pc/return/violin.html
# page says: "no! i mean yes! but ../stuff/violin.php."

# going to: "http://www.pythonchallenge.com/pc/stuff/violin.php"
# picture of Leopold, and he says: "http://www.pythonchallenge.com/pc/stuff/violin.php"

# need to tell him: "the flowers are on their way"
# use info cookie


import urllib
opener = urllib.request.build_opener()
opener.addheaders.append(('Cookie', 'info=the+flowers+are+on+their+way'))
f = opener.open("http://www.pythonchallenge.com/pc/stuff/violin.php")
print(f.read().decode())


# contains the message: "oh well, don't you dare to forget the balloons"
import prompt
prompt.openurl("http://www.pythonchallenge.com/pc/return/balloons.html")






