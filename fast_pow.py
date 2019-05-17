# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:07:16 2019

@author: ValentinePit
"""

def fastExp(b, n):
    #быстрое возведение b в степень n
    def even(n):#проверка четности
        if n%2==0:
            return 1
        return 0
    
    if n==0:
        return 1
    if even(n):
        return fastExp(b, n/2)**2
    return b*fastExp(b, n-1)

def divider(n):
    i = 2
    j = 0 # флаг
    while i**2 <= n: 
        if n%i == 0:
            return 1
        i += 1
    return 0    
    

n = int(input("n="))

if divider(n):
    print ("Это составное число")
else:
    print ("Это простое число")