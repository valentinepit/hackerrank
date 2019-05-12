# -*- coding: utf-8 -*-
"""
Created on Fri May 10 21:47:01 2019

@author: ValentinePit
"""

import sys

class Calculator(Exception):
    
    def power(self,n, p):
        self.n = n
        self.p = p
        if n < 0 and p < 0:
            raise Exception("n and p should be non-negative")
        else:
            return n**p
            
         
     

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