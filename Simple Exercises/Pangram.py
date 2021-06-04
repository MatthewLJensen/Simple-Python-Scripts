def is_pangram(sentence):
    """
    >>> is_pangram("abcdefghijklmnopqrstuvwxyz")
    True
    
    >>> is_pangram("abcdefghijklmn opqrst uvwxyz 3456 asdfsaarsdf")
    True
    
    >>> is_pangram("jklmno 234 asdf")
    False
    
    >>> is_pangram("Pack my box with five dozen liquor jugs")
    True
    
    >>> is_pangram("Sphinx of black quartz, judge my vow")
    True
    
    >>> is_pangram("Sphinchs of black quartz, judge my vow")
    False
    
    >>> is_pangram("")
    False
    """
    dict = {}
    string = sentence.lower()
    for char in string:
        if char.isalpha():
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
    if len(dict) == 26:
        return True
    else:
        return False
    

import doctest
doctest.testmod()