# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 23:47:59 2019
Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.

For example, if , it is a valid string because frequencies are . So is  because we can remove one  and have  of each character in the remaining string. If  however, the string is not valid as we can only remove  occurrence of . That would leave character frequencies of .

Function Description

Complete the isValid function in the editor below. It should return either the string YES or the string NO.

isValid has the following parameter(s):

s: a string
Input Format

A single string .

Constraints

Each character 
Output Format

Print YES if string  is valid, otherwise, print NO.
@author: ValentinePit
"""

import string

def isValid(s):
    cont = s.count(s[0])
    flag1 = False 
    flag2 = False
    for i in string.ascii_lowercase:
        a = s.count(i)
        if abs(cont - s.count(i)) > 1 and s.count(i) != 0:
            if s.count(i) == 1 and flag1 == True:  
                return "NO"
            if s.count(i) == 1 and flag1 == False:
                flag1 =True     
            if s.count(i) != 1:
                return "NO"

        elif cont - s.count(i) == 1 and flag2 == False and s.count(i) != 0:
            flag2 = True
         
        elif cont - s.count(i) == 1 and flag2 == True and s.count(i) != 0:
            return "NO"
         
            
    return "YES"     


def test_1():
    if  isValid("aaaaabc") == "YES":
        print("Test 1 - OK")
    else:
        print("Test 1 - Not OK")
        
def test_2():
    if  isValid('aabbccddeefghi') == "NO":
        print("Test 2 - OK")
    else:
        print("Test 2 - Not OK")  

test_1()
test_2()