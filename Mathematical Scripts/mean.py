def mean(numbers: list) -> float:
    """
    >>> type(mean([]))
    <class 'NoneType'>
    
    >>> mean([1,2,3,4,5])
    3.0
    
    >>> mean([100,500,1000,1100])
    675.0
    
    >>> mean([-3,4,-2,5])
    1.0

    """
    if len(numbers) == 0:
        return None
    total = 0
    for number in numbers:
        total += number
    mean = total/len(numbers)
    return mean

import doctest
doctest.testmod()
    