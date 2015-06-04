__author__ = 'dracz'

# some helper functions for fetching urls

import urllib.request

def openurl(url, username=None, password=None):
    """return the contents of the url"""

    if username is None or password is None:
        return urllib.request.urlopen(url)

    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, username, password)

    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(handler)

    return opener.open(url)

