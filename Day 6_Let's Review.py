# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 10:49:42 2019

@author: ValentinePit
"""

for i in range(int(input())):
    s = input()
    for k in range(0, len(s), 2):
        print(s[k], end ="")
    print(" ", end="" )    
    for k in range(1, len(s), 2):
        print(s[k], end ="") 
    print()    
    