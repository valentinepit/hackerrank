# -*- coding: utf-8 -*-
"""
Created on Sat May 18 15:58:50 2019

@author: ValentinePit
"""

def book_back(d:list, d1:list):
    
    if d[2] < d1[2]: #if book was returned in year befor
        return 0
    
    
    if d[2] > d1[2]: #if book was returned a year after
        return 1000
    
    if d[1] < d1[1]: #if book was returned in month or few ago
     
        return 0

    if d[1] > d1[1]: #if book was returned in month or few after
        return (d[1] - d1[1])*500
    
    if d[0] > d1[0]:
        return (d1[0] - d[0])*15

    return 0

d = list(map(int, input().split()))
d1 = list(map(int, input().split()))

'''d = map(int, d)
print(d)
d1 = map(int, d1)


for i in range(3):
    d[i] = int(d[i])
    d1[i] = int(d1[i])
'''

print(book_back(d, d1))


    