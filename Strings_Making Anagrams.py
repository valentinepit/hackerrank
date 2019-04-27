# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 23:09:32 2019
Check out the resources on the page's right side to learn more about strings. The video tutorial is by Gayle Laakmann McDowell, author of the best-selling interview book Cracking the Coding Interview.

Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?

Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

For example, if  and , we can delete  from string  and  from string  so that both remaining strings are and  which are anagrams.

Function Description

Complete the makeAnagram function in the editor below. It must return an integer representing the minimum total characters that must be deleted to make the strings anagrams.

makeAnagram has the following parameter(s):

a: a string
b: a string
Input Format

The first line contains a single string, . 
The second line contains a single string, .

Constraints

The strings  and  consist of lowercase English alphabetic letters ascii[a-z].
Output Format

Print a single integer denoting the number of characters you must delete to make the two strings anagrams of each other.
@author: ValentinePit
"""
import string

def makeAnagram(a, b):
    count = 0
    
    for i in string.ascii_lowercase:

        ac = a.count(i)
        bc = b.count(i)
        count += abs(ac - bc)
    print(count)   
    return count    

def test_1():
    if  makeAnagram('abc', 'cde') == 4:
        print("Test 1 - OK")
    else:
        print("Test 1 - Not OK")
        
def test_2():
    if  makeAnagram('make', 'kredo') == 5:
        print("Test 2 - OK")
    else:
        print("Test 2 - Not OK")  

test_1()
test_2()

        

