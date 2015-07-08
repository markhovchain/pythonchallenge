__author__ = 'dracz'

# some helper functions for fetching urls

import urllib.request

def openurl(url, username=None, password=None, brange=None):
    """return the contents of the url"""
    print("\nopening {}...".format(url))

    if username is None or password is None:
        return urllib.request.urlopen(url)

    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, username, password)

    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(handler)

    req = urllib.request.Request(url)
    if brange is not None:
        req.add_header("Range", brange)

    return opener.open(req)


