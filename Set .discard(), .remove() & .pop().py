# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 22:17:45 2019
You have a non-empty set , and you have to execute  commands given in  lines.

The commands will be pop, remove and discard.

Input Format

The first line contains integer , the number of elements in the set . 
The second line contains  space separated elements of set . All of the elements are non-negative integers, less than or equal to 9. 
The third line contains integer , the number of commands.
The next  lines contains either pop, remove and/or discard commands followed by their associated value.

@author: ValentinePit
"""
n = int(input())
s = set(map(int, input().split()))
n = int(input())
for i in range(n):
    ls = input().split()
    if ls[0] == "pop":
        s.pop()
    elif ls[0] == "discard":
        s.discard(int(ls[1])) 
    elif ls[0] == "remove":
        s.remove(int(ls[1]))
    else:
        print("wrong command")
k = 0
for i in s:
    k +=i
print(k)
