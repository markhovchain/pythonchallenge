__author__ = 'dracz'

url1 = "http://www.pythonchallenge.com/pc/def/map.html"

# title: what about making trans
# image of: K->M , O->Q, E->G
# clue: everybody thinks twice before solving this.

# translate each character by 2

# contains the string
w = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

# Translated string: "i hope you didnt translate it by hand. thats what computers are for. doing it in by hand
# is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url."

# map -> ocr

def trans_word(s):
    t = ""
    for c in s:
        if not str.isalpha(c):
            t += c
            continue

        o = ord(c)
        if o >= 121:
            o -= 26

        t += chr(o + 2)
    return t

def trans_string(s):
    return ' '.join([trans_word(word) for word in s.split()])


url2 = "http://www.pythonchallenge.com/pc/def/{0}.html".format(trans_word("map"))

print("""
Original string:   "{0}"

Translated string: "{1}"

URL 1: {2}
URL 2: {3}
""".format(w, trans_string(w), url1, url2))

import prompt
prompt.openurl(url2)