# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 21:22:49 2019
If we want to add a single element to an existing set, we can use the .add() operation. 
It adds the element to the set and returns 'None'.
@author: ValentinePit
"""
n = int(input())
l = []
c = set(l)
for i in range(n):
    c.add(input())
print(len(c))

