__author__ = 'dracz'

import urllib.request
import re

url2 = 'http://www.pythonchallenge.com/pc/def/ocr.html'

page = urllib.request.urlopen(url2).read().decode()
gibberish = re.search(r'(%%\$.*\$\}\*)', page.replace('\\n', ''), re.DOTALL).group()
word = ''.join(re.findall(r'[a-z]', gibberish))

url3 = 'http://www.pythonchallenge.com/pc/def/{0}.html'.format(word)

print("""
Found rare characters: {0}
URL 2: {1}
URL 3: {2}
""".format(word, url2, url3))

import prompt
prompt.openurl(url3)


