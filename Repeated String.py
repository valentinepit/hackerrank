# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:43:20 2019

@author: ValentinePit
"""

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    print("len(s)=", len(s), "n//len(s)=", n//len(s), "count(a) =", s.count("a") )
    if n > len(s):
        x = s.count("a") 
        y =  n//len(s)
        c = x*y
        s = s[:(n%len(s))]
        c +=s.count("a")
        return c
    s = s[:n]
    c = s.count("a")
    return c 

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
