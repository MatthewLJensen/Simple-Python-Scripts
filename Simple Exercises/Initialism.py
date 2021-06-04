# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:12:32 2020

@author: Matthew
"""

def initialism(phrase):
    first_letters = ""
    words = phrase.split()
    for word in words:
        first_letters = first_letters + word[0].upper()
    return first_letters

print(initialism("this is a test of the emergency broadcast system"))

        