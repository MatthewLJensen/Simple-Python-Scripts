def counter(element, iterable) -> int:
    """
    Takes a list and an item to count and returns the number of times that item appears in the list
    >>> counter(3,[1,3,6,9,3,4,3])
    3
    >>> counter("a", [1,2,3,4,"a",4,3,"b", 3])
    1
    >>> counter(1378, [1234,2345,3456,4567,91234])
    0
    """
    count = 0
    for item in iterable:
        if item == element:
           count += 1
    return count
        
import doctest
doctest.testmod()