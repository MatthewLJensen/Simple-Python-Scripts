#Created by Matthew Jensen and edited most recently on December 3, 2020

from bottle import default_app, route
import json
import math
import operator


sauUsername = 'matthewljensen'
paUsername = 'matthewljensen'


@route('/')
def hello_world():
    return 'Hello from Bottle!'

#Start Leap Year

@route('/misc/is_leap_year/<year>')
def is_leap_year(year):
    return json.dumps(leap_year(year))
    
def leap_year(year):
    """Enter a year and the function should return true if it is a leap year, and false if not
    >>> leap_year(2000)
    True
    >>> leap_year(2004)
    True
    >>> leap_year(2016)
    True
    >>> leap_year(1700)
    False
    >>> leap_year(2003)
    False
    >>> leap_year(2020)
    True
    >>> leap_year(2021)
    False
    """
    year = int(year)
    if year%4 == 0:
        if year%100 ==0:
            return (year%400 == 0)
        else:
            return True
    else:
        return False

#End Leap Year


#Start Day of Week

weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Sabbath"]



@route('/misc/day_of_week/<year>/<month>/<day>')
def day_of_week(year,month,day):
    return json.dumps(weekdays[dow(year, month, day)])


def dow(year, month, day):
    """Enter a year, month, and day, and it will return the day of the week in the form of a number
    (0 = Su, 1 = Mo, ... 6 = Sa).
    >>> dow(2020,9,7)
    1
    >>> dow(1999,11,5)
    5
    >>> dow(2022,10,1)
    6
    >>> dow(2000,2,29)
    2
    >>> dow(2020,9,17)
    4
    >>> dow(2020,9,16)
    3
    >>> dow(1928,1,1)
    0
    """
    year = int(year)
    month = int(month)
    day = int(day)
    if month < 3:
        month += 12
        year -= 1
    month_day = (day + math.floor((13*(month+1))/5) + year + math.floor(year/4) - math.floor(year/100) + math.floor(year/400)) % 7 #Zeller's Congruence: https://en.wikipedia.org/wiki/Zeller%27s_congruence
    if month_day == 0:
        month_day = 6
    else:
        month_day -= 1
    return month_day

#End Day of Week


#This next section is for the calendar

@route('/misc/month_calendar/<year:int>/<month:int>')
def month_calendar(year, month):
    month_list = create_month_list(year, month, 0)

    month_string = "\n".join(month_list)
    return json.dumps(month_string)

weekdays_cal = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
month_length = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
month_names = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October",11:"November", 12:"December"}


def is_leapyear(year):
    """Enter a year and the function should return true if it is a leap year, and false if not
    >>> is_leapyear(2000)
    True
    >>> is_leapyear(2004)
    True
    >>> is_leapyear(2016)
    True
    >>> is_leapyear(1700)
    False
    >>> is_leapyear(1900)
    False
    >>> is_leapyear(2003)
    False
    """
    if year%4 == 0:
        if year%100 ==0:
            return year%400 == 0
        else:
            return True
    else:
        return False



def day_of_week_cal(year,month,day):
    """Enter a year, month, and day, and it will return the day of the week in the form of a number
    (0 = Su, 1 = Mo, ... 6 = Sa).
    >>> day_of_week_cal(2020,9,7)
    1
    >>> day_of_week_cal(1999,11,5)
    5
    >>> day_of_week_cal(2022,10,1)
    6
    >>> day_of_week_cal(2000,2,29)
    2
    >>> day_of_week_cal(2020,9,17)
    4
    >>> day_of_week_cal(2020,9,16)
    3
    >>> day_of_week_cal(1928,1,1)
    0
    """
    year = int(year)
    month = int(month)
    day = int(day)
    if month < 3:
        month += 12
        year -= 1
    month_day = (day + math.floor((13*(month+1))/5) + year + math.floor(year/4) - math.floor(year/100) + math.floor(year/400)) % 7 #Zeller's Congruence: https://en.wikipedia.org/wiki/Zeller%27s_congruence
    if month_day == 0:
        month_day = 6
    else:
        month_day -= 1
    return month_day



def center(message, width):
    """Pad message with spaces on both sides
    so it's centered in a string
    width characters long.
    >>> center("May 2020", 21)
    '      May 2020       '
    >>> center("hello", 9)
    '  hello  '
    >>> center("this is a test", 30)
    '        this is a test        '

    >>> center("this is a test", 31)
    '        this is a test         '
    """
    padding = width - len(message)
    return (" " * (padding // 2)) + message + (" " * ((padding + 1) // 2))



def create_month_list(year, month, day):
    """
    Returns a list of strings, each representing one line in the calendar for the specified month.
    >>> create_month_list(2020,9,15)
    ['   September 2020    ', 'Su Mo Tu We Th Fr Sa ', '       1  2  3  4  5 ', ' 6  7  8  9 10 11 12 ', '13 14 15 16 17 18 19 ', '20 21 22 23 24 25 26 ', '27 28 29 30          ', '                     ']
    >>> create_month_list(1800,9,15)[1]
    'Su Mo Tu We Th Fr Sa '

    >>> len(create_month_list(2000,2,29))
    8
    >>> len(create_month_list(2030,2,15))
    8
    >>> len(create_month_list(1776,6,4))
    8


    >>> len(create_month_list(2000,2,29)[0])
    21
    >>> len(create_month_list(2000,8,29)[1])
    21
    >>> len(create_month_list(2000,7,29)[2])
    21
    >>> len(create_month_list(2000,6,29)[3])
    21
    >>> len(create_month_list(2000,5,29)[4])
    21
    >>> len(create_month_list(2000,4,29)[5])
    21
    >>> len(create_month_list(2000,2,28)[6])
    21
    >>> len(create_month_list(2000,3,29)[7])
    21
    """

    cal_string = ""

    month_start_day_num = day_of_week_cal(year,month,1)

    month_length[2] = 28
    if is_leapyear(year) == True:
        month_length[2] = 29


    #if day==0:
    #    header = month_names[month]
    #else:
    header = month_names[month] + " " + str(year)

    cal_string += center(header, 21) + "\n"


    for day_name in weekdays_cal:
         cal_string += day_name + " "
    cal_string += "\n"


    cal_string += "   " * month_start_day_num
    for day_num in range(month_length[int(month)]):
        if (day_num+month_start_day_num)%7 == 0 and day_num+month_start_day_num > 0:
            cal_string += "\n"

        #if day_num + 1 == int(day): #This chunck highlights today on the calendar
        #        cal_string += '\x1b[0;30;47m'

        if day_num+1 < 10:
            cal_string += " "
        cal_string += str(day_num + 1)

        #if day_num + 1 == int(day): #This chunck highlights today on the calendar
        #    cal_string += '\x1b[0m'

        cal_string += " "


    cal_list = cal_string.split("\n")

    end_padding = 21 - len(cal_list[-1])
    cal_list[-1] += end_padding * " "

    for empty_line in range(8-len(cal_list)):
        cal_list.append(" " * 21)

    return cal_list



#End calendar




#Start Caesar


alphabet = "abcdefghijklmnopqrstuvwxyz"

@route('/misc/caesar_cipher/<offset:int>/<message>')
def caesar_cipher(offset, message):
    return json.dumps(caes_ciph(offset, message))

def caes_ciph(offset, message):
    """
    >>> caes_ciph(1, 'matthew')
    'nbuuifx'
    >>> caes_ciph(26, 'matthew')
    'matthew'
    >>> caes_ciph(52, 'matthew')
    'matthew'
    >>> caes_ciph(-1, 'nbuuifx')
    'matthew'
    >>> caes_ciph(1, 'matt-hew')
    'nbuu-ifx'
    >>> caes_ciph(0, '')
    ''
    >>> caes_ciph(0, 'matthew')
    'matthew'
    
    """
    message=message.lower()
    cipher = ""
    for char in message:
        if (alphabet.find(char) == -1):
            cipher = cipher + char
        elif (alphabet.find(char) + offset) < 26 and (alphabet.find(char) + offset) > -1:
            cipher = cipher + alphabet[alphabet.find(char) + offset]
        else:
            cipher = cipher + alphabet[(alphabet.find(char) + offset)%26]
    return cipher

#End Caesar


#start Roman Numerals


@route('/misc/roman_math/<rn1>/<op>/<rn2>')
def roman_math(rn1, op, rn2):
    """
    >>> roman_math('X', '+', 'X')
    '"XX"'
    >>> roman_math('IV', '+', 'XV')
    '"XIX"'
    >>> roman_math('XCIX', '-', 'X')
    '"LXXXIX"'
    >>> roman_math('XCI', '-', 'X')
    '"LXXXI"'
    >>> roman_math('X', 'x', 'X')
    '"C"'
    >>> roman_math('X', '*', 'X')
    '"C"'
    >>> roman_math('', '*', 'X')
    '""'
    """
    ops = { "+": operator.add, "-": operator.sub, "x": operator.mul, "*": operator.mul }
    return json.dumps(convert_to_rn(ops[op](convert_from_rn(rn1), convert_from_rn(rn2))))

rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def convert_from_rn(rn):
    # Used this site as a resource for this function:
    # https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-2.php
    """
    >>> convert_from_rn('X')
    10
    >>> convert_from_rn('IV')
    4
    >>> convert_from_rn('XXIV')
    24
    >>> convert_from_rn('MCXVI')
    1116
    >>> convert_from_rn('')
    0
    >>> convert_from_rn('XCIX')
    99
    >>> convert_from_rn('MMMMMMMMMMM')
    11000
    """
    val = 0
    for index in range(len(rn)):
        if index > 0 and rom_val[rn[index]] > rom_val[rn[index - 1]]:
            val += rom_val[rn[index]] - 2 * rom_val[rn[index - 1]]
        else:
            val += rom_val[rn[index]]
    return val
    
roman_complete = [
    (1000, "M"),
    ( 900, "CM"),
    ( 500, "D"),
    ( 400, "CD"),
    ( 100, "C"),
    (  90, "XC"),
    (  50, "L"),
    (  40, "XL"),
    (  10, "X"),
    (   9, "IX"),
    (   5, "V"),
    (   4, "IV"),
    (   1, "I"),
]

def convert_to_rn(number):
    # Used this page from user Aristide as a resource for this function:
    # https://stackoverflow.com/questions/28777219/basic-program-to-convert-integer-to-roman-numerals
    """
    >>> convert_to_rn(10)
    'X'
    >>> convert_to_rn(4)
    'IV'
    >>> convert_to_rn(24)
    'XXIV'
    >>> convert_to_rn(1116)
    'MCXVI'
    >>> convert_to_rn(0)
    ''
    >>> convert_to_rn(99)
    'XCIX'
    >>> convert_to_rn(11000)
    'MMMMMMMMMMM'
    """
    result = []
    for (arabic, roman) in roman_complete:
        (factor, number) = divmod(number, arabic)
        result.append(roman * factor)
        if number == 0:
            break
    return "".join(result)
    
    

application = default_app()

if __name__ == "__main__":
    import doctest
    doctest.testmod()