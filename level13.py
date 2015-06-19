__author__ = 'dracz'

"""
http://www.pythonchallenge.com/pc/return/disproportional.html

Clue is: "phone him" and "call the evil"
Remember clue from last level, said: "Bert is evil"
Clicking on the phone leads to: "http://www.pythonchallenge.com/pc/phonebook.php"
Which yields an xml error page containing: "XML error: Invalid document end at line 1, column 1"
So the php service is expecting an xml body. perhaps its an xmlrpc service?
"""

from xmlrpc.client import ServerProxy

server = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php/")

print(server.system.listMethods())
# ['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature',
# 'system.multicall', 'system.getCapabilities']

print(server.system.methodSignature('phone'))
# [['string', 'string']] # takes a string parameter and returns a string

print(server.phone("bert"))
# He is not the evil

print(server.phone("Bert"))
# 555-ITALY

url14 = "http://www.pythonchallenge.com/pc/return/555-ITALY.html"
# Not Found

url14 = "http://www.pythonchallenge.com/pc/return/ITALY.html"
# SMALL letters

url14 = "http://www.pythonchallenge.com/pc/return/italy.html"

import prompt
prompt.openurl(url14)