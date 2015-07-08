__author__ = 'dracz'

# title: what are you looking at?
# clue: a[30] = ?
# image of a bull

url10 = 'http://www.pythonchallenge.com/pc/return/bull.html'

# link on bull points to:
sequence_url = 'http://www.pythonchallenge.com/pc/return/sequence.txt'

# clue: a = [1, 11, 21, 1211, 111221,
# a web search reveals that this is the "look-and-say sequence"
# https://en.wikipedia.org/wiki/Look-and-say_sequence

from lookandsay import lookandsay

ans = len(lookandsay(31))

print(ans)
# 5808

import prompt

prompt.openurl('http://www.pythonchallenge.com/pc/return/5808.html', 11)
