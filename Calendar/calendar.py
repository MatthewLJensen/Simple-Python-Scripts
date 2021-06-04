import math

#Add ability for user to choose first day of calendar.

weekdays = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
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
    
    

def day_of_week(year,month,day):
    """Enter a year, month, and day, and it will return the day of the week in the form of a number
    (0 = Su, 1 = Mo, ... 6 = Sa).
    >>> day_of_week(2020,9,7)
    1
    >>> day_of_week(1999,11,5)
    5
    >>> day_of_week(2022,10,1)
    6
    >>> day_of_week(2000,2,29)
    2
    >>> day_of_week(2020,9,17)
    4
    >>> day_of_week(2020,9,16)
    3
    >>> day_of_week(1928,1,1)
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
    
    month_start_day_num = day_of_week(year,month,1)
        
    month_length[2] = 28
    if is_leapyear(year) == True:
        month_length[2] = 29
    
    
    if day==0:
        header = month_names[month]
    else:
        header = month_names[month] + " " + str(year)

    cal_string += center(header, 21) + "\n"
    

    for day_name in weekdays:
         cal_string += day_name + " "
    cal_string += "\n"


    cal_string += "   " * month_start_day_num
    for day_num in range(month_length[int(month)]):
        if (day_num+month_start_day_num)%7 == 0 and day_num+month_start_day_num > 0:
            cal_string += "\n"

        if day_num + 1 == int(day): #This chunck highlights today on the calendar
                cal_string += '\x1b[0;30;47m'

        if day_num+1 < 10:
            cal_string += " " 
        cal_string += str(day_num + 1)      
        
        if day_num + 1 == int(day): #This chunck highlights today on the calendar
            cal_string += '\x1b[0m'
        
        cal_string += " "
        
        
    cal_list = cal_string.split("\n")
    
    end_padding = 21 - len(cal_list[-1])
    cal_list[-1] += end_padding * " "
    
    for empty_line in range(8-len(cal_list)):
        cal_list.append(" " * 21)
    
    return cal_list



def print_year(year_list, width):
    """
    Takes a list of a list of strings, each list of strings represents 1 month in a calendar year. This function doesn't return anything, it just prints.
    This function also accepts a width parameter to choose how many months show up on each row of the calendar. Doesn't work over 6.
    """
    for row in range(12//width):    
        for line in range(8):
            for month in range(width):                
                    print(year_list[(width*row)+month][line],end=(" "))
            print()
    #for row in range(12%width):
    for last_line in range(8):
        for last_months in range(12%width):                
                print(year_list[last_months+(12-(12%width))][last_line],end=(" "))
        print()
        



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    date = input("Enter date (YYYY-MM-DD): ")
    
    request_year = len(date) == 4
        
    if request_year:
        year = int(date)
        year_cal = []
        for month in range(12):
            year_cal.append(create_month_list(year,month+1,0))
        print_year(year_cal, 4)
            
    else:
        year, month, day = date.split("-")
        year = int(year)
        month = int(month)
        day = int(day)
        month_cal = create_month_list(year, month, day)
        for line in month_cal:
            print(line)
