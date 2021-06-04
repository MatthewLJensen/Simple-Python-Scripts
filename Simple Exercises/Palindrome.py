# -*- coding: utf-8 -*-
"""
Palindrome
Created on Thu Oct 22 13:46:29 2020

@author: Matthew
"""

def palindrome_check(string_pal):
    """
    >>> palindrome_check("hannah")
    True
    >>> palindrome_check("123hannAh")
    True
    >>> palindrome_check("hanna")
    False
    >>> palindrome_check("")
    True
    >>> palindrome_check("thisIsatesttsetasisiht")
    True
    >>> palindrome_check("thisisatesttsetasisihts")
    False
    >>> palindrome_check("RACEcar")
    True
    """
    string_pal = string_pal.upper()
    string = ""
    
    for char in string_pal:
        if char.isalpha():
            string = string + char
            
    string_pal = string
    
    reverse_pal = string_pal[::-1]
    palindrome = True

    for index in range(len(string_pal)):
        if string_pal[index] is not reverse_pal[index]:
            palindrome = False
    
    return palindrome
        
import doctest
doctest.testmod()


string_pal = input("Enter a string to check if it is a palindrome: ")

palindrome = palindrome_check(string_pal)

if palindrome == True:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")
        
    
    

