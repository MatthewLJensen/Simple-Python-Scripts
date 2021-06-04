def word_count(string):
    """
    Takes a string and returns a dictionary with the number of times each word appears
    >>> word_count("this is a test")
    {'this': 1, 'is': 1, 'a': 1, 'test': 1}
    
    >>> word_count("this is a test. Can't you see?")
    {'this': 1, 'is': 1, 'a': 1, 'test.': 1, "can't": 1, 'you': 1, 'see?': 1}
    
    >>> word_count("this is a  a test  ")
    {'this': 1, 'is': 1, 'a': 2, 'test': 1}
    
    >>> word_count("")
    {}
    
    
    """
    count = {}
    
    if string == "":
        return count
    
    string = string.lower()
    word_list = string.split()
    for word in word_list:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    return count

import doctest
doctest.testmod()