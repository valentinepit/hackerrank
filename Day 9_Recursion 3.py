# -*- coding: utf-8 -*-
"""
Created on Wed May  1 22:29:27 2019

@author: ValentinePit
"""

def factorial(n, fac):
    if n == 1: return fac
    
    fac = n * factorial(n-1, fac)
    return fac



def test_1():
    print("OK" if factorial(4, 1) == 24 else "Not Ok") 

#N = int(input())
fac = 1
test_1()