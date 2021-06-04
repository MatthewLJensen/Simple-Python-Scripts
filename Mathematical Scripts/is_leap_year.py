def is_leap_year(year):
    """Enter a year and the function should return true if it is a leap year, and false if not
    >>> is_leap_year(2000)
    True
    >>> is_leap_year(2004)
    True
    >>> is_leap_year(2016)
    True
    >>> is_leap_year(1700)
    False
    >>> is_leap_year(2003)
    False
    >>> is_leap_year(2020)
    True
    >>> is_leap_year(2021)
    False
    """
    if year%4 == 0:
        if year%100 ==0:
            return year%400 == 0
        else:  
            return True
    else:
        return False
    
import doctest
doctest.testmod()