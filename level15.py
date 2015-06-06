__author__ = 'dracz'

url15 = "http://www.pythonchallenge.com/pc/return/uzi.html"

"""
Shows a calendar January 1XX9 where the first of the month is a Thursday.
The 26th is circled
Clue: "he ain't the youngest, he is the second"
Clue: "todo: buy flowers tomorrow"
Title: "whom?"
"""

# in what years 1**6 did January 1 fall on thursday?
from datetime import date


for d in [d for d in [date(i, 1, 26) for i in range(1006, 1996, 10)] if d.weekday() == 0]:
    print(d)

"""
1046-01-26
1176-01-26
1226-01-26
1356-01-26
1446-01-26
1576-01-26
1626-01-26
1756-01-26
1846-01-26
1976-01-26
"""

# mozart's birthday is 1756-01-26

import prompt
prompt.openurl("http://www.pythonchallenge.com/pc/return/mozart.html")
