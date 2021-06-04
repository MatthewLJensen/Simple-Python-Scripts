# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:34:29 2020

@author: Matthew
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"

def letter_value(letter):
    value = alphabet.find(letter)        
    return value

def caesar_cipher(offset, message):
    message=message.lower()
    cipher = ""
    for char in message:
        print("char: " + char + ". value + offset: " + str(letter_value(char) + offset) + ". modulo: " + str((letter_value(char) + offset)%25))
        if (letter_value(char) + offset) < 26 and (letter_value(char) + offset) > -1:
            cipher = cipher + alphabet[letter_value(char) + offset]
        else:
            cipher = cipher + alphabet[(letter_value(char) + offset)%26]
    return cipher
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    print(caesar_cipher(100,"matthew"))
    print(caesar_cipher(-100, caesar_cipher(100, "matthew")))