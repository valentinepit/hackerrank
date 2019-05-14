# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:42:40 2019

@author: ValentinePit
"""

import sys

                
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
def bubble_sort(A):
    """пузырьковый метод сортировки списка А"""
    swap = 0
    N = len(A)
    for bypass in range(1, N):
        for k in range(N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
                swap += 1
    print("Array is sorted in", swap,"swaps.")
    print("First Element:", A[0])
    print("Last Element:", A[N-1])
            
bubble_sort(a)               

                