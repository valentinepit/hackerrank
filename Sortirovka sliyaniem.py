# -*- coding: utf-8 -*-
"""
Created on Sun May 12 23:03:23 201


Сортировка слиянием
Слияние отсортированных массивов
@author: ValentinePit
"""

def merge(A:list, B:list):
    C = [0]*(len(A) + len(B)) #создаем новый список длинной как два исходных
    # задади 3 индекса i, k, n для каждого из списков
    i = k = n =0 
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    
    return C    