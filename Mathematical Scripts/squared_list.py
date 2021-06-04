def square_list(list):
    """Given a list, this function will return another list with the values in the new list equal to their respective values in the original list squared
    >>> square_list([10,20,30,40])
    [100, 400, 900, 1600]
    >>> square_list([1,2,5,8,12,3])
    [1, 4, 25, 64, 144, 9]
    >>> square_list([.5,1.5,3.86,8.4])
    [0.25, 2.25, 14.8996, 70.56]
    """
    squared = []
    for val in list:
        squared.append(val**2)
    return squared
        
import doctest
doctest.testmod()