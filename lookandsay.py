__author__ = 'dracz'

def lookandsay(k):
    """Return the k-th item in the look-and-say sequence as a string.

    http://en.wikipedia.org/wiki/Look-and-say_sequence

    >>> list([lookandsay(i) for i in range(1,8)]) == ["1", "11", "21", "1211", "111221", "312211", "13112221"]
    True

    >>> lookandsay(0)
    Traceback (most recent call last):
    ...
    ValueError: k must be > 0
    """

    if k < 1:
        raise ValueError("k must be > 0")
    if k == 1:
        return "1"
    if k == 2:
        return "11"

    s = "11"
    n = 2
    while n < k:
        c = s[0]
        count = 1
        t = ""
        for d in s[1:]:
            if d == c:
                count += 1
            else:
                t += str(count)
                t += c
                c = d
                count = 1
        s = t + str(count) + c
        n += 1
    return s

