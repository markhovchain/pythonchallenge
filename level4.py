__author__ = 'dracz'

import urllib.request
import re

url4 = "http://www.pythonchallenge.com/pc/def/linkedlist.html"
# page says: linkedlist.php

url4 = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
#image link contains a url parameter: nothing=12345

nothing = 12345

# after awhile nothing = 16044, and the message says to divide by two
nothing = 8022


while True:
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={0}".format(nothing)
    print('fetching "{0}"...'.format(url))

    f = urllib.request.urlopen(url)
    res = f.read().decode()

    print(res)
    match = re.search(r'the next nothing is ([0-9]+)', res)
    if match is None:
        break

    nothing = match.group(1)


# after many iterations the result is:
# peak.html

import prompt
prompt.openurl('http://www.pythonchallenge.com/pc/def/peak.html')

