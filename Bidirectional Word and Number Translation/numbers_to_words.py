# -*- coding: utf-8 -*-
"""
Numbers to Words
Created on Thu Oct  8 13:58:50 2020

@author: Matthew
"""
digits = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
tens = {1:"ten", 2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
teens = {11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
power_dict = {1:"thousand", 2:"million", 3:"billion", 4:"trillion", 5:"quadrillion", 6:"quintillion", 7:"sextillion"}
#number = input("Enter a number: ")

def words_from_number(number: int) -> str:
    """
    >>> convert_to_word(237)
    two hundred thirty-seven

    """
    word_num_list = []
    word_num = ""
    
    string_num = str(number)
    
    if "-" in string_num:
        return None
    
    length = len(string_num)
    starting_power = (length - 1)//3
    power = starting_power
    
    first = 0
    
    #if length-3 > 3:
    #    second = 3
    #else:
    
    second = length - (3 * power)
    
    
    if number == 0:
        return "zero"
    
    if length < 3:
        word_num_list.append(less_than_three_converter(number))
        word_num = word_num + less_than_three_converter(number)
        return word_num
    
    
    while (power > 0):

        if second > length:
            second = length
            
        #print("power: " + str(power) + ", first: " + str(first), ", second: " + str(second))
        
        if (second - first) == 3:
             if (three_digit_converter(int(str(number)[first:second]))) != "":
                 word_num_list.append(three_digit_converter(int(str(number)[first:second])))
                 word_num_list.append(str(power_dict[power]))
                 word_num = word_num + three_digit_converter(int(str(number)[first:second])) + " " + str(power_dict[power])
        else:
            if (less_than_three_converter(int(str(number)[first:second]))) != "":
                 word_num_list.append(less_than_three_converter(int(str(number)[first:second])))
                 word_num_list.append(str(power_dict[power]))
                 word_num = word_num + less_than_three_converter(int(str(number)[first:second])) + " " + str(power_dict[power])
             
        if (power > 1):
            word_num = word_num + " "
        power = power - 1
        first = second 
        second = second + 3
    
    
    word_num_list.append(three_digit_converter(int(str(number)[-3:])))
    word_num = word_num + " " + three_digit_converter(int(str(number)[-3:]))
    
    while word_num[-1] == " ":
        word_num = word_num[:-1]
        
    while word_num[0] == " ":
        word_num = word_num[1:]
    
    while "" in word_num_list:
        word_num_list.remove("")
    return " ".join(word_num_list)
    
def three_digit_converter(number: int):
    print("converting 3 digits: " + str(number))
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
    print("converting less than 3 digits: " + str(number))
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
    
while(True):
    print(words_from_number(input("enter number: ")))