__author__ = 'dracz'

import webbrowser

def openurl(url):
    prompt("Press enter to open: '{}'...\n".format(url))
    webbrowser.open(url)

def prompt(s="Press enter to continue..."):
    try:
        return raw_input(s) # python 2
    except NameError:
        return input(s)     # python 3
