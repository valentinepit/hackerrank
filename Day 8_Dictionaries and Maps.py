# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 09:24:55 2019

@author: ValentinePit
"""
import sys
fb = {}
N = int(input())
for i in range(N):
    name, num = input().split()
    fb[name] = num


for line in sys.stdin:
    line = line.rstrip('\r\n')
    if line in fb.keys():
        print(line, "=", fb[line], sep="")
    else: 
        print("Not found") 
   






