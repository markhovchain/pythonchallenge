__author__ = 'dracz'

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
    return ' '.join([trans_word(w) for w in s.split()])


w = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

url1 = "http://www.pythonchallenge.com/pc/def/map.html"
url2 = "http://www.pythonchallenge.com/pc/def/{0}.html".format(trans_word("map"))

print("""
Original string:   "{0}"

Translated string: "{1}"

URL 1: {2}
URL 2: {3}
""".format(w, trans_string(w), url1, url2))

import prompt
prompt.openurl(url2)