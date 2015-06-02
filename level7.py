__author__ = 'dracz'

url7 = 'http://www.pythonchallenge.com/pc/def/oxygen.html'
# title: "smarty"

hurl = 'http://www.pythonchallenge.com/pc/def/pants.html'

import urllib.request
hint = urllib.request.urlopen(hurl).read().decode()

print('\n{0} says: {1}'.format(hurl, hint))

f = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png')

import png
width, height, pixels, metadata = png.Reader(file=f).asDirect()

n = 0

for row in pixels:
    n += 1
    s = []
    # look for the band in the middle
    if n == height//2:
        for i in range(0, width*4, 7*4):
            if not row[i] == row[i+1] or not row[i] == row[i+2]:
                break
            s.append(row[i])
        break

print(''.join([chr(i) for i in s]))

# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

print(''.join([chr(i) for i in [105, 110, 116, 101, 103, 114, 105, 116, 121]]))

# integrity

import prompt
url8 = 'http://www.pythonchallenge.com/pc/def/integrity.html'
prompt.openurl(url8)