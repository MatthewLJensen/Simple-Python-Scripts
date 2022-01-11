def first_letters(sentence):
    """Given a string, this function will return a dictionary with the a letter as the key, and the number of times that letter started a word in the string.
    >>> first_letters("apples armadillos bats boys bombs zebra zoology zing zang zest")
    {'a': 2, 'b': 3, 'z': 5}
    >>> first_letters("Will this test work with Capital LEtters and punctuation?")
    {'w': 3, 't': 2, 'c': 1, 'l': 1, 'a': 1, 'p': 1}
    >>> first_letters("")
    {}
    """
    sentence = sentence.lower()
    if len(sentence) == 0:
        return {}
    words = sentence.split(" ")
    letter_counts = {}
    for word in words:
        if word[0] not in letter_counts:
            letter_counts[word[0]] = 0
        letter_counts[word[0]] = letter_counts[word[0]] + 1
    return letter_counts

import doctest
doctest.testmod()