"""
Word Search

Created on Thu Sep 24 15:24:52 2020

@author: Matthew
"""
import random

words = ["mercury", "Venus", "earth", "Mars", "saturn", "Uranus", "Jupiter", "Neptune", "Pluto"]
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
List = list

def puzzle_word_starts_at(puzzle, row_num: int, col_num: int, word: str) -> bool:
    """
    >>> puzz1 = [[' ', 'B', 'C'], [' ', 'A', ' '], ['T', 'F', ' ']]
    >>> puzzle_word_starts_at(puzz1, 0, 2, "cat")
    True
    >>> puzzle_word_starts_at(puzz1, 2, 1, "fab")
    True
    >>> puzzle_word_starts_at(puzz1, 0, 0, "nothing")
    False
    """
    for row_chg in (-1, 0, +1):
        for col_chg in (-1, 0, +1):
            if row_chg == 0 and col_chg == 0:
                continue # skip this iteration and move on to the next one
            if (0 <= (row_num + row_chg * (len(word) - 1)) < len(puzzle)) and \
                (0 <= (col_num + col_chg * (len(word) - 1)) < len(puzzle[0])):
                found = True
                for pos in range(len(word)):
                    if puzzle[row_num + row_chg * pos][col_num + col_chg * pos] != \
                        word[pos].upper():
                        found = False
                        break # exit the inner loop
                if found:
                    return True
    return False

def puzzle_contains_word(puzzle, word: str) -> bool:
    """
    >>> puzz1 = [[' ', 'B', 'C'], [' ', 'A', ' '], ['T', 'F', ' ']]
    >>> puzzle_contains_word(puzz1, "cat")
    True
    >>> puzzle_contains_word(puzz1, "FAB")
    True
    >>> puzzle_contains_word(puzz1, "CAB")
    False
    """
    for row_num in range(len(puzzle)):
        for col_num in range(len(puzzle[row_num])):
            if puzzle_word_starts_at(puzzle, row_num, col_num, word):
                return True
    return False


def check_valid_start(key, word, height, width, startx, starty, changex, changey):
    """
    >>> key1 = [[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]
    >>> check_valid_start(key1, "cow", 4, 4, 0, 0, 1, 1)
    True
    >>> check_valid_start(key1, "cow", 4, 4, 1, 1, 0, 1)
    True
    >>> check_valid_start(key1, "cow", 4, 4, 2, 2, 1, 1)
    False
    >>> check_valid_start(key1, "cow", 4, 4, 0, 0, 0, 0)
    False
    >>> check_valid_start(key1, "cow", 4, 4, 3, 0, 1, 0)
    False
    >>> check_valid_start(key1, "cow", 4, 4, 0, 3, 1, 0)
    True
    >>> check_valid_start(key1, "cow", 4, 4, 0, 2, 0, 1)
    False
    >>> key2 = [["A"," "," "," "],["P"," "," "," "],["P"," "," "," "],[" "," "," "," "]]
    >>> check_valid_start(key2, "PING", 4, 4, 0, 1, 1, 0)
    True
    >>> check_valid_start(key2, "PING", 4, 4, 0, 0, 1, 0)
    False
    >>> key3 = [["A","P","P"," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]
    >>> check_valid_start(key3, "PING", 4, 4, 1, 0, 0, 1)
    True
    >>> check_valid_start(key3, "PING", 4, 4, 0, 0, 0, 1)
    False
    """
    if changex == 0 and changey == 0:
        return False
    
    finalx = startx
    finaly = starty
    
    for char in range(len(word) - 1):        
        finalx += changex
        finaly += changey
        
    
    if finalx > (width - 1) or finalx < 0 or finaly > (height - 1) or finaly < 0:
        return False
    
    
    finalx = startx
    finaly = starty
    for char in word:        
        if key[finaly][finalx] != " " and key[finaly][finalx] != char:
            return False
        finalx += changex
        finaly += changey
    
    
    
    return True
    
def place_word(key, word, startx, starty, changex, changey):
    """
    >>> key = [[" "," "," "],[" "," "," "],[" "," "," "]]
    >>> place_word(key, "COW", 0, 0, 1, 0)
    >>> puzzle_contains_word(key, "COW")
    True
    >>> puzzle_contains_word(key, "WOW")
    False
    >>> place_word(key, "WOW", 0, 1, 1, 0)
    >>> puzzle_contains_word(key, "WOW")
    True
    """
    for char in word:
        key[starty][startx] = char
        startx += changex
        starty += changey
        
def fill_puzzle(key):
    """
    >>> key1 = [["C"," "," "],[" ","O"," "],[" "," ","W"]]
    >>> puzzle_contains_word(key1, " ")
    True
    >>> puzzle1 = fill_puzzle(key1)
    >>> puzzle_contains_word(puzzle1, " ")
    False
    >>> puzzle_contains_word(puzzle1, "COW")
    True
    """
    puzzle = key
    for row in range(len(key)):
        for char in range(len(key[row])):
            if key[row][char] == " ":
                puzzle[row][char] = alphabet[random.randint(0,25)]
    return puzzle
                

def generate_key(height, width, words):
    """
    >>> puzzle2 = generate_key(7,5,["yoyo", "yolo", "matches"])
    >>> puzzle_contains_word(puzzle2, "yoyo")
    True
    >>> puzzle_contains_word(puzzle2, "yolo")
    True
    >>> puzzle_contains_word(puzzle2, "matches")
    True
    >>> puzzle_contains_word(puzzle2, " ")
    True
    >>> len(puzzle2)
    7
    >>> len(puzzle2[0])
    5
    >>> puzzle3 = generate_key(4,4,["yoyo", "yolo", "matches"])
    >>> puzzle3 == None
    True
    """
    key = [[" " for i in range(width)] for i in range(height)]
    
    words.sort(key = len)
    words = words[::-1]
    
    print(words)
    
    for word in words:
        word = word.upper()
        valid_start = False
        
        check_attempts = 0
        while not valid_start:
            
            if check_attempts > 10000:
                print (word + ": attempts = 10000. Giving up and returning None.")
                return None
            
            start_x = random.randint(0,width-1)
            start_y = random.randint(0,height-1)
            change_x = random.randint(-1,1)
            change_y = random.randint(-1,1)
            
            valid_start = check_valid_start(key, word, height, width, start_x, start_y, change_x, change_y)
            check_attempts += 1
        print (word + ": attempts =",check_attempts, "start_x =", start_x, "start_y +", start_y, "change_x =", change_x, "change_y =", change_y)
        place_word(key, word, start_x, start_y, change_x, change_y)
    
    
    return key
    
def print_key(key):
    for row in key:
        print(row)


import doctest
doctest.testmod()

key = generate_key(10,10,words)
print_key(key)
print()
puzzle = fill_puzzle(key)
print_key(puzzle)