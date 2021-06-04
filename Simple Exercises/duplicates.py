# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:38:50 2020

@author: Matthew
"""

def contains_duplicates(checkList):
    """
    >>> contains_duplicates([1,2,3,4])
    False
    >>> contains_duplicates([1,2,3,4,1])
    True
    >>> contains_duplicates([1,2,3,4,5,5])
    True
    >>> contains_duplicates(["1",1,2,3,4,5])
    False
    >>> contains_duplicates([])
    False
    """
    for item in checkList:
        counter = 0
        for i in checkList:
            if (item == i):
                counter += 1
        if counter > 1:
            return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
                