# -*- coding: utf-8 -*-
"""
Numbers to Words
Created on Thu Oct  8 13:58:50 2020

@author: Matthew
"""
digits = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
tens = {1:"ten", 2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
teens = {11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
power_dict = {1:"thousand", 2:"million", 3:"billion", 4:"trillion", 5:"quadrillion", 6:"quintillion", 7:"sextillion", 8:"septillion", 9:"octillion", 10:"nonillion", 11:"decillion", 12:"undecillion", 13:"duodecillion", 14:"tredecillion", 15:"quattuordecillion", 16:"quindecillion", 17:"sexdecillion", 18:"septendecillion", 19:"octodecillion", 20:"novemdecillion", 21:"vigintillion", 22:"centillion"}
#number = input("Enter a number: ")

def words_from_number(number: int) -> str:
    """
    >>> words_from_number(237)
    'two hundred thirty-seven'
    
    >>> words_from_number(0)
    'zero'
    
    >>> words_from_number(1)
    'one'
    
    >>> words_from_number(100)
    'one hundred'
    
    >>> words_from_number(907)
    'nine hundred seven'
    
    >>> words_from_number(1050)
    'one thousand fifty'
    
    >>> words_from_number(10500)
    'ten thousand five hundred'
    
    >>> words_from_number(100001)
    'one hundred thousand one'
    
    >>> words_from_number(987654321)
    'nine hundred eighty-seven million six hundred fifty-four thousand three hundred twenty-one'
    
    """
    
    word_num_list = []
    
    if int(number) < 0:
        number = number * (-1)
    
    string_num = str(number)
    

    
    length = len(string_num)
    starting_power = (length - 1)//3
    power = starting_power
    
    first = 0
    

    second = length - (3 * power)
    
    
    if int(number) == 0:
        return "zero"

    
    while (power > 0):

        if second > length:
            second = length

        
        if (second - first) == 3:
             if (three_digit_converter(int(str(number)[first:second]))) != "":
                 word_num_list.append(three_digit_converter(int(str(number)[first:second])))
                 word_num_list.append(str(power_dict[power]))
        else:
            if (less_than_three_converter(int(str(number)[first:second]))) != "":
                 word_num_list.append(less_than_three_converter(int(str(number)[first:second])))
                 word_num_list.append(str(power_dict[power]))
             
        power = power - 1
        first = second 
        second = second + 3
    
    
    word_num_list.append(three_digit_converter(int(str(number)[-3:])))

    while "" in word_num_list:
        word_num_list.remove("")
    return " ".join(word_num_list)
    
def three_digit_converter(number: int):
    
    """
    >>> three_digit_converter(123)
    'one hundred twenty-three'
    
    >>> three_digit_converter(0)
    ''
    
    >>> three_digit_converter(900)
    'nine hundred'
    
    >>> three_digit_converter(20)
    'twenty'
    
    >>> three_digit_converter(2)
    'two'
    
    >>> three_digit_converter(515)
    'five hundred fifteen'
    
    >>> three_digit_converter(107)
    'one hundred seven'
    """
    
    short_num = ""
    
    string_num = str(number)
    
    if len(string_num) == 3:
        
        short_num = short_num + digits[int(string_num[0])] + " hundred"
        
        if int(string_num[1:3]) < 20 and int(string_num[1:3]) > 10:
            short_num = short_num + " " + teens[int(string_num[1:3])]

        elif int(string_num[1]) == 0 and int(string_num[2]) == 0:
            short_num = short_num    
            
        elif int(string_num[1]) == 0:
            short_num = short_num + " " + digits[int(string_num[2])]
            
        else:
            if int(string_num[2]) != 0:
                short_num = short_num + " " + tens[int(string_num[1])] + "-" + digits[int(string_num[2])]
            else:
                short_num = short_num + " " + tens[int(string_num[1])]
    
    elif number == 0:
        return ""
    
    elif len(string_num) == 0:
        return ""
    else:
        short_num = short_num + less_than_three_converter(number)
        
    
    return short_num


def less_than_three_converter(number: int):
    """
    >>> less_than_three_converter(99)
    'ninety-nine'
    
    >>> less_than_three_converter(9)
    'nine'
    
    >>> less_than_three_converter(0)
    'zero'
    
    >>> less_than_three_converter(13)
    'thirteen'
    
    >>> less_than_three_converter(50)
    'fifty'
    
    >>> less_than_three_converter(23)
    'twenty-three'
    
    """
    word_num = ""
    
    string_num = str(number)
    length = len(string_num)

    if length == 2:
        if int(number) < 20 and int(number) > 10:
            word_num = word_num + teens[int(number)]
        else:
            word_num = tens[int(string_num[0])]
            if int(string_num[1]) != 0:
                word_num = word_num + "-" + digits[int(string_num[1])]
    else:
        word_num = digits[int(string_num[0])]
    return word_num
    
import doctest
doctest.testmod()