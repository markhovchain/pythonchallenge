__author__ = 'dracz'

ans = 2**38

url0 = 'http://www.pythonchallenge.com/pc/def/0.html'
url1 = 'http://www.pythonchallenge.com/pc/def/{0}.html'.format(ans)

print("""
2^38 = {0}
URL 0: {1}
URL 1: {2}
""".format(ans, url0, url1))

import prompt
prompt.openurl(url1)
