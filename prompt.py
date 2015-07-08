__author__ = 'dracz'

import webbrowser

def openurl(url, level=None):
    s = "Press enter to open level {}: '{}'...\n".format(level, url)
    prompt(s)
    webbrowser.open(url)

def prompt(s="Press enter to continue..."):
    try:
        return raw_input(s) # python 2
    except NameError:
        return input(s)     # python 3
