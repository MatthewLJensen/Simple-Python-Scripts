import math
def median(numbers: list) -> float:
    """
    >>> median([1,2,3,4,5])
    3
    
    >>> median([2,1,3,5,4])
    3
    
    >>> median([3,2,1,5,4])
    3
    
    >>> median([1,2,3.5,4,5])
    3.5
    
    >>> median([-3,-9,9,0,179,36])
    4.5

    >>> median([5.5,1.1,2.2,3.3,4.4])
    3.3
    
    >>> type(median([]))
    <class 'NoneType'>
    
    """
    if len(numbers) == 0:
        return None
    numbers.sort()
    length = len(numbers)
    if length%2 == 0:
        median = (numbers[(int(length/2))-1] + numbers[(int((length/2)+1))-1])/2
    else:
        median = numbers[(int(math.ceil(length/2)))-1]
    return median                   

import doctest
doctest.testmod()