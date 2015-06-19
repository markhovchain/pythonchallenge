__author__ = 'dracz'

import urllib.request
import re

url2 = 'http://www.pythonchallenge.com/pc/def/ocr.html'

# title: ocr
# hint: recognize the characters. maybe they are in the book,
# but MAYBE they are in the page source.

# page source contains:
# find rare characters in the mess below:
"""
%%$@_$^__#)^)&!_+]!*@&^}@[@%]()%+$&[(_@%+%$*^@$^!+]!&_#)_*}{}}!}_]$[%}@[{_@#_^{*
@##&{#&{&)*%(]{{([*}@[@&]+!!*{)!}{%+{))])[!^})+)$]#{*+^((@^@}$[**$&^{$!@#$%)!@(&
+^!{%_$&@...
"""

# look for word characters in the mess"
page = urllib.request.urlopen(url2).read().decode()
gibberish = re.search(r'(%%\$.*\$\}\*)', page.replace('\\n', ''), re.DOTALL).group()
word = ''.join(re.findall(r'[a-z]', gibberish))

# equality

url3 = 'http://www.pythonchallenge.com/pc/def/{0}.html'.format(word)

# http://www.pythonchallenge.com/pc/def/equality.html

print("""
Found rare characters: {0}
URL 2: {1}
URL 3: {2}
""".format(word, url2, url3))

import prompt
prompt.openurl(url3)


