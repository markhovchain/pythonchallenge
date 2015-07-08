__author__ = 'dracz'

url0 = 'http://www.pythonchallenge.com/pc/def/0.html'

import prompt
prompt.openurl(url0, 0)

# title: warming up
# image contains: 2^38
# hint: Hint: try to change the URL address.

ans = 2**38 # 274877906944

url1 = "http://www.pythonchallenge.com/pc/def/274877906944.html"

print("""
2^38 = {0}
URL 0: {1}
URL 1: {2}
""".format(ans, url0, url1))

import prompt
prompt.openurl(url1, 1)
