# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:55:54 2019

@author: ValentinePit
"""

def schet_edenic(S):
     k = 0
     f = 0
     m = 0
     for i in range(len(S)):
         if S[i] == '1':
             if f == 1:
                 k += 1
             else:
                 k = 1
                 f = 1
         else:
             k = 0
             f = 0
         if m < k: 
             m = k
     return m
N = int(input())
print(bin(N))
S = list(bin(N))

print(schet_edenic(S))
 