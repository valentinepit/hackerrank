# -*- coding: utf-8 -*-
"""
Created on Sun May 12 23:48:39 2019
Сортировка Тони Хоара (Быстрая сортировка)
@author: ValentinePit
"""

def HoarSort(A):
    
    if len(A) <= 1:
        return
    barrier = A[0] #барьерный элемент для сравнений
    L = []
    R = []
    M = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x > barrier:
            R.append(x)
        else:
            M.append(x)
    
    HoarSort(L)
    HoarSort(R)
    
    k = 0
    
    for x in L + M + R:
        A[k] = x
        k += 1        
