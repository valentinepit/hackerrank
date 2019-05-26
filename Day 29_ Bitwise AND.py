# -*- coding: utf-8 -*-
"""
Created on Sat May 25 22:55:02 2019

@author: ValentinePit
"""


import math
import os
import random
import re
import sys

def finde(n,k):
    m = 0
    for i in range(n):
        for j in range(1, n):
            if i!=j:
                if i&j < k and i&j > m:
                    m = i&j
    print(m)                

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        
       
       finde(n, k)      
        
