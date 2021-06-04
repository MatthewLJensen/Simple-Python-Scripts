def counter(string) -> dict:
    """
    Takes a string and returns a dictionary with 2 keys, upper and lower, that signify how many upper and lowercase characters were in the string
    >>> counter("TTTDDDFFFtttdddfff")
    {'lower': 9, 'upper': 9}
    >>> counter("abcdefghijklmnopqrstuvwxyz")
    {'lower': 26, 'upper': 0}
    >>> counter("ABCDEFGHIJKLMNOPQW")
    {'lower': 0, 'upper': 18}
    >>> counter("")
    {'lower': 0, 'upper': 0}
    """
    uplow = {'lower': 0, 'upper': 0}
    string = string.replace(" ", "")
    for character in string:
        if character.isupper():
            uplow['upper'] += 1
        else:
            uplow['lower'] += 1
    return uplow

import doctest
doctest.testmod()