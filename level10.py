__author__ = 'dracz'

# clue: a[30] = ?
url10 = 'http://www.pythonchallenge.com/pc/return/bull.html'

# link points to:
sequence_url = 'http://www.pythonchallenge.com/pc/return/sequence.txt'

# clue: a = [1, 11, 21, 1211, 111221,
# a web search reveals that this is the "look-and-say sequence"
# https://en.wikipedia.org/wiki/Look-and-say_sequence

from lookandsay import lookandsay

ans = len(lookandsay(31))

print(ans) #5808

import prompt

prompt.openurl('http://www.pythonchallenge.com/pc/return/{}.html'.format(ans))
