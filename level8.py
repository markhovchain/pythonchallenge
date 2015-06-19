__author__ = 'dracz'

url8 = 'http://www.pythonchallenge.com/pc/def/integrity.html'

# title: working hard?
# hint: can you find the missing link?
# image of a bee on flower

# the bee has a link that leads to pw protected page:
# page contains comment:
# un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

import urllib.request
import re

page = urllib.request.urlopen(url8).read().decode()

un = re.search(r"un: '(.*)'", page).group(1)
pw = re.search(r"pw: '(.*)'", page).group(1)

# unix 'file' command reveals that the un and pw fields are bz2 encoded

import bz2

und = bz2.decompress(un.encode('latin-1').decode('unicode_escape').encode('latin1')).decode()
pwd = bz2.decompress(pw.encode('latin-1').decode('unicode_escape').encode('latin1')).decode()

print("""
found bzip2 compressed fields:
un: '{}'
pw: '{}'

decompressed fields (use these values when prompted):
un: '{}'
pw: '{}'
""".format(un, pw, und, pwd))

# this is the url of the bee
url9 = 'http://www.pythonchallenge.com/pc/return/good.html'

import prompt
prompt.openurl(url9)