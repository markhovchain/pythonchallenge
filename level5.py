__author__ = 'dracz'

import urllib.request
import pickle

url5 = 'http://www.pythonchallenge.com/pc/def/peak.html'

# banner on the page refers to: banner.p

p = pickle.load(urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

# the object is list of list of tuple, where the tup[0] is char '#' or ' '
# the tup[1] contains an int. These can be interpreted and line, character, and number of reps

for l in p:
    s = ""
    for e in l:
        s += e[0]*e[1]
    print(s)


# the result looks like:
"""
              #####                                                                      #####
               ####                                                                       ####
               ####                                                                       ####
               ####                                                                       ####
               ####                                                                       ####
               ####                                                                       ####
               ####                                                                       ####
               ####                                                                       ####
      ###      ####   ###         ###       #####   ###    #####   ###          ###       ####
   ###   ##    #### #######     ##  ###      #### #######   #### #######     ###  ###     ####
  ###     ###  #####    ####   ###   ####    #####    ####  #####    ####   ###     ###   ####
 ###           ####     ####   ###    ###    ####     ####  ####     ####  ###      ####  ####
 ###           ####     ####          ###    ####     ####  ####     ####  ###       ###  ####
####           ####     ####     ##   ###    ####     ####  ####     #### ####       ###  ####
####           ####     ####   ##########    ####     ####  ####     #### ##############  ####
####           ####     ####  ###    ####    ####     ####  ####     #### ####            ####
####           ####     #### ####     ###    ####     ####  ####     #### ####            ####
 ###           ####     #### ####     ###    ####     ####  ####     ####  ###            ####
  ###      ##  ####     ####  ###    ####    ####     ####  ####     ####   ###      ##   ####
   ###    ##   ####     ####   ###########   ####     ####  ####     ####    ###    ##    ####
      ###     ######    #####    ##    #### ######    ###########    #####      ###      ######

"""

import prompt
prompt.openurl('http://www.pythonchallenge.com/pc/def/channel.html')
