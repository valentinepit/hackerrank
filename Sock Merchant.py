# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 22:20:21 2019
ohn works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock
Input Format

The first line contains an integer , the number of socks represented in . 
The second line contains  space-separated integers describing the colors  of the socks in the pile.
@author: ValentinePit
"""

def sockMerchant(n, ar):
    a = set(ar)
    sm = 0
    for i in a:
        x = ar.count(i)//2
        sm += x
    print(sm)    
    return sm      
        
    

def test_1():
    if  sockMerchant(7, [1, 1, 2, 1, 2, 4, 4]) == 3:
        print("Test 1 - OK")
    else:
        print("Test 1 - Not OK")
        
def test_2():
    if  sockMerchant(9, [1, 1, 2, 1, 2, 4, 4, 3, 1]) == 4:
        print("Test 2 - OK")
    else:
        print("Test 2 - Not OK")  
        
test_1()
test_2()        