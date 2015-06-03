__author__ = 'dracz'

url8 = 'http://www.pythonchallenge.com/pc/def/integrity.html'

import urllib.request
import re

page = urllib.request.urlopen(url8).read().decode()

un = re.search(r"un: '(.*)'", page).group(1)
pw = re.search(r"pw: '(.*)'", page).group(1)

# used unix 'file' command to determine that the un and pw fields are bzip2 encoded

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