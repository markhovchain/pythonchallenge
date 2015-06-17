__author__ = 'dracz'

url23 = "http://www.pythonchallenge.com/pc/hex/bonus.html"

"""
title: what is this module?

comments:

TODO: do you owe someone an apology? now it is a good time to
tell him that you are sorry. Please show good manners although
it has nothing to do with this level.

msg: 'it can't find it. this is an undocumented module.'

msg: 'va gur snpr bs jung?'
"""

"""
I guess we called leopold an idiot in level19:
'http://www.pythonchallenge.com/pc/hex/idiot.html'
He told us to apologize and level19 also contained an email from him:

From: leopold.moz@pythonchallenge.com

So I sent an email, and he replies:

Never mind that.

Have you found my broken zip?

md5: bbb8b499a0eef99b52c7f13f4e78c24b

Can you believe what one mistake can lead to?
"""


# let's try to decode the msg using various length rotations

from rot import rots

for i in range(1, 27):
    print(i, rots('va gur snpr bs jung?', i))

# inspecting the output, there is one sensible string in the 13th rotation:
# "in the face of what?"

# apparently this is the caeser cipher aka rot13, which is documented here:
# https://docs.python.org/3/library/codecs.html

# trying: adversity, death, god, time, isnecessary, necessary..
# no luck. think about the clue again" 'this' is an undocumented module:

"""
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# there it is: "In the face of ambiguity..."

import prompt
prompt.openurl("http://www.pythonchallenge.com/pc/hex/ambiguity.html")


