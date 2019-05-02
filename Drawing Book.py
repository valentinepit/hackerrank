# -*- coding: utf-8 -*-
"""
Created on Wed May  1 22:48:55 2019

@author: ValentinePit
"""

def pageCount(n, p):
    if n - p == 1 and n % 2 == 0 and n != 2:
        return 1
    if n - p == 1 and n ==2:
        return 0
    if p - 1 < n - p:
        return p // 2
    else:
        
        return (n-p) // 2
      
    
def test_1():
    print("OK" if pageCount(6, 5) == 1 else "Not Ok")
    
def test_2():
    print("OK" if pageCount(2, 1) == 0 else "Not Ok")    


test_1()
test_2()    