# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 23:45:16 2019

@author: ValentinePit
"""
import os
import math
def diverseDeputation(m, w):
    # Write your code here
    if w == 0 or m == 0: 
        return 0
    C1 = 0
    C2 = 0
    C3 = 0
    С1 = math.factorial(w+m)/(6*math.factorial(m+w-3))
    print(math.factorial(w+m)/(6*math.factorial(m+w-3)))
    print (C1)
    if m > 2:
        C2 = math.factorial(m)/(6*math.factorial(m-3))
    if w > 2:
        C2 = math.factorial(w)/(6*math.factorial(w-3))
    return int(math.factorial(w+m)/(6*math.factorial(m+w-3)) - C2 - C3)


m = int(input())
n = int(input())

print(diverseDeputation(m, n))