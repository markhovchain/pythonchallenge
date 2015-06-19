__author__ = 'dracz'

url29 = "http://www.pythonchallenge.com/pc/ring/guido.html"

# title: silence!
# who is it?

from urlhelp import openurl

html = openurl(url29, "repeat", "switch").read()

# printing the html reveals that there are lots of extra spaces and newlines at the end of the file
# each newline has different number of spaces

import re
sp = re.search("</html>(.*)", html.decode(), re.S).group(1)


bb = bytes([len(line) for line in sp.split("\n")])
# b'\x00BZh91AY&SY\xd9\xc...
# looks like a bz2, with leading zero

from bz2 import decompress

print(decompress(bb[1:]))
# "Isn't it clear? I am yankeedoodle!"

url30 = "http://www.pythonchallenge.com/pc/ring/yankeedoodle.html"

from prompt import openurl
openurl(url30)


