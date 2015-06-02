__author__ = 'dracz'

import urllib.request
import re

url3 = "http://www.pythonchallenge.com/pc/def/equality.html"

page = urllib.request.urlopen(url3).read().decode()
gibberish = re.search(r'<!--(.*)-->', page, re.DOTALL).group()

ans = ''.join(re.findall(r'(?<![A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?![A-Z])', gibberish))

url4 = "http://www.pythonchallenge.com/pc/def/{0}.html".format(ans)

print("""
Found characters: "{0}"
URL 3: {1}
URL 4: {2}
""".format(ans, url3, url4))

import prompt
prompt.openurl(url4)
