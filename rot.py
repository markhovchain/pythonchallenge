__author__ = 'dracz'

def rotc(c, n):
    """rotate character by n places
    >>> rotc('a', 1)
    'b'
    >>> rotc('a', -1)
    'z'
    >>> rotc('c', 13)
    'p'
    >>> rotc('m', 27)
    'n'
    >>> rotc('C', 5)
    'H'
    """
    if len(c) > 1:
        raise ValueError('expected a single character')
    if c.isupper():
        start = ord('A')
    elif c.islower():
        start = ord('a')
    else:
        return c
    return chr((ord(c) - start + n) % 26 + start)


def rots(s, n):
    """rotate string s by n places
    >>> rots('Why did the chicken cross the road?', 13)
    'Jul qvq gur puvpxra pebff gur ebnq?'
    """
    return ''.join([rotc(c, n) for c in s])
