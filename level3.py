__author__ = 'dracz'

# title: re
# hint: One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

import urllib.request
import re

url3 = "http://www.pythonchallenge.com/pc/def/equality.html"

page = urllib.request.urlopen(url3).read().decode()

# page source has a comment with lots of upper and lower chars

gibberish = re.search(r'<!--(.*)-->', page, re.DOTALL).group()

# look for lower case with exactly 3 upper case on both sides
ans = ''.join(re.findall(r'(?<![A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?![A-Z])', gibberish))

# linkedlist

url4 = "http://www.pythonchallenge.com/pc/def/{0}.html".format(ans)

print("""
Found characters: "{0}"
URL 3: {1}
URL 4: {2}
""".format(ans, url3, url4))

import prompt
prompt.openurl(url4)

# url4 = "http://www.pythonchallenge.com/pc/def/linkedlist.html"
