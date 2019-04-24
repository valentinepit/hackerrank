# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 12:20:30 2019
Task 
Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer, , denoting the number of elements in the tuple. 
The second line contains  space-separated integers describing the elements in tuple .



Print the result of  hash(t)
@author: ValentinePit
"""

n = int(input())
tls =[]
tls = (input().split())
t = tuple(tls)
print(hash(t))