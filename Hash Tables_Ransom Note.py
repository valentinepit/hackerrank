# -*- coding: utf-8 -*-
"""
Created on Sun May 26 22:14:37 2019
Harold is a kidnapper who wrote a ransom note, but now he is worried 
it will be traced back to him through his handwriting. 
He found a magazine and wants to know if he can cut out whole words 
from it and use them to create an untraceable replica of his ransom note. 
The words in his note are case-sensitive and he must use only whole words 
available in the magazine. He cannot use substrings or concatenation to create
 the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes 
if he can replicate his ransom note exactly using whole words from the magazine; 
otherwise, print No.

For example, the note is "Attack at dawn". 
The magazine contains only "attack at dawn". 
The magazine has all the right words, but there's a case mismatch. 
The answer is .

Function Description

Complete the checkMagazine function in the editor below. It must print  
if the note can be formed using the magazine, or .

checkMagazine has the following parameters:

magazine: an array of strings, each a word in the magazine
note: an array of strings, each a word in the ransom note
@author: ValentinePit
"""


import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    
    for i in note:
        try:
            magazine.remove(i)
        except ValueError:
            return "No"
    return "Yes"    

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])
    

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))