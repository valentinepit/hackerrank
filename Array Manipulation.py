# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:08:46 2019

@author: ValentinePit
"""

def input_array():
    pass

def multi_array(ar, a, b, k):
    
    for i in range(a-1, b):
        ar[i] += 1
    
    return ar

n, m = map(int, input().split())

ar = [0 for i in range(n)] 
ls = []
for i in range(m):
    ls = list(map(int, input().split()))
    ar = multi_array(ar, ls[0], ls[1], ls[2])
    print(max(ar))
#print(ar)