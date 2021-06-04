def largest(num_list):
    """Given a list of numbers, this function will return the largest value
    >>> largest([0,1,2,3])
    3
    >>> largest([-1,-2,-3,-80])
    -1
    >>> largest([10,9,-1,4.3])
    10
    """
    large = num_list[0]
    for number in num_list:
        if number > large:
            large = number
    return large

import doctest
doctest.testmod()