# -*- coding: utf-8 -*-
"""
Pandigital
Created on Thu Oct 22 13:37:58 2020

@author: Matthew
"""



def check_pangram(number):
    """
    >>> check_pangram("0123456789")
    True
    >>> check_pangram("123023413452456356746785789689079089")
    True
    >>> check_pangram("012345678")
    False
    >>> check_pangram("")
    False
    >>> check_pangram("12345")
    False
    """
    check = 0
    while check < 10:
        if str(check) in number:
            check += 1
        else:
            check = 10
            return False
            break
        if check == 10:
            return True

    
    
import doctest
doctest.testmod()


number = input("Enter a whole number: ")
is_pangram = check_pangram(number)
if is_pangram:
    print("number is a pangram")
else:
    print("number is not a pangram") 