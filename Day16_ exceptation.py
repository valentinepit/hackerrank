# -*- coding: utf-8 -*-
"""
Created on Fri May 10 21:47:01 2019

@author: ValentinePit
"""

import sys

class Calculator(Exception):
    
    def power(self,n, p):
        
        
        try:
            if n < 0 and p < 0:
                raise Calculator("n and p should be non-negative")
        except Calculator as mr:
            print(mr)
        else:
            print(n**p)
            
         
     

#Write your code here

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    
    try:
        ans=myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)       