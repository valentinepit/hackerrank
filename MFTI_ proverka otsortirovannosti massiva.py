# -*- coding: utf-8 -*-
"""
Created on Thu May 16 22:54:52 2019
Проверка отсортированности массива за U(N) БЫСТРО!!!!
@author: ValentinePit
"""
def chek_sorted(A, ascending = True):
    # проверка отсортированности за O(N)
    flag = True
    s = 2*int(ascending) - 1 #это дает s=-1 если ascending =False и s=1 при True
    for i in range(0, n-1):
        if s*A[i] > s*A[i+1]: # умножение на s меняет сортировку по возрастанию и убыванию 
            return False