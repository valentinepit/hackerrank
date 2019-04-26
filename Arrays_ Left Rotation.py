# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 08:22:34 2019

@author: ValentinePit
"""
def rev(a):
    """ reversing an array"""
    N = len(a)
    for i in range(N//2):
        a[i], a[N-1-i] = a[N-1-i], a[i]
    return a

def rotLeft(a, d, n):
    a1 = rev(a[:d])
    a2 = rev(a[d::])
    c = rev(a1+a2)
    
    return(c)
    
n, d = map(int, input().split())

a = list(map(int, input().rstrip().split()))
            

print(rotLeft(a, d, n))