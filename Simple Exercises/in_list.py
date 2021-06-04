def in_list(lst, obj):
    """
    Takes a list and an object and returns true if the object is in the list and false if it is not
    >>> in_list([1,2,3,4,5,6,6,6,7], 6)
    True
    >>> in_list([1,2,3,4,5,6,6,6,7], 8)
    False
    >>> in_list(["a", "b", "c", "d", 1,2,3,6], 6)
    True
    >>> in_list(["a", "b", "c", "d", 1,2,3,6], "b")
    True
    >>> in_list([], 6)
    False
    """
    count = 0
    while count < len(lst):
       if lst[count] == obj:
            return True
       count += 1
    return False    

import doctest
doctest.testmod()
