def count(string):
    """
    >>> count("abc")
    {'a': 1, 'b': 1, 'c': 1}
    
    >>> count("cba")
    {'c': 1, 'b': 1, 'a': 1}
    
    >>> count("abcabc")
    {'a': 2, 'b': 2, 'c': 2}
    
    >>> count("abcabcd")
    {'a': 2, 'b': 2, 'c': 2, 'd': 1}
    
    >>> count("abc123xyza")
    {'a': 2, 'b': 1, 'c': 1, 'x': 1, 'y': 1, 'z': 1}
    
    >>> count("McDonald's restaurants")
    {'m': 1, 'c': 1, 'd': 1, 'o': 1, 'n': 2, 'a': 3, ''}
    """
    
    dict = {}
    string = string.lower()
    for char in string:
        if char.isalpha():
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
    return dict

def are_anagrams(string1, string2):
    """
    >>> are_anagrams("abcdefghijklmnopqrstuvwxyz","acbdefghijklmnopqrstuvwxyz")
    True
    
    >>> are_anagrams("dog","god")
    True
    
    >>> are_anagrams("hannah","aannhh")
    True
    
    >>> are_anagrams("dormitory","dirty room")
    True
    
    >>> are_anagrams("abcdefghijklmnopqrstuvwxy","acbdefghijklmnopqrstuvwxyz")
    False
    
    >>> are_anagrams("abcdefghijklmnopqrstuvwxyz","acbdefghijklmnopqrstuvwxy")
    False
    
    >>> are_anagrams("the eyes", "they see")
    True
    
    >>> are_anagrams("McDonald's restaurants", "Uncle Sam's standard rot")
    False
    """
    dict1 = count(string1)
    dict2 = count(string2)
    
    print (dict1)
    print (dict2)
    
    for key in dict1:
        if key not in dict2:
            return False
        if dict1[key] is not dict2[key]:
            return False
    
    for key2 in dict2:
        if key2 not in dict1:
            return False
        if dict1[key2] is not dict2[key2]:
            return False        
        
    return True
    

import doctest
doctest.testmod()
            