# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 09:16:15 2019

@author: ValentinePit
"""
def rev_array(n, a):
    
    
    for i in range(len(a)-1, -1, -1):
        print(a[i], end=" ")
        
    
    

def test_1():
    if  rev_array(4, [1, 4, 3, 2]) == "2 3 4 1":
        print("Test 1 - OK")
    else:
        print("Test 1 - Not OK")
        
def test_2():
    if  rev_array(6, [1, 3, 5, 2, 4, 6]) == "6 4 2 5 3 1":
        print("Test 2 - OK")
    else:
        print("Test 2 - Not OK")  

rev_array(6, [1, 3, 5, 2, 4, 6])
#test_1()
#test_2()