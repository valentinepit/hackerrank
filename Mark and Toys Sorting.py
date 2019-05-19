# -*- coding: utf-8 -*-
"""
Created on Fri May 17 19:48:03 2019

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

def mergeSort(A:list):
    if len(A)<=1: return
    middle = len(A)//2
    L = [A[i] for i in range(middle)]
    R = [A[i] for i in range (middle, len(A))]
    mergeSort(L)
    mergeSort(R)
    C = merge(L, R)
    for i in range(len(A)): #нельзя просто написать А=С это только ссылку на объект поменят
        A[i] = C[i]
    return A    
        
def maximumToys(prices, k):
    
    m = i = 0
    while m <= k:
        print(prices[i])
        m += prices[i]
        i +=1
    return i - 1    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))
    
    prices = mergeSort(prices)
    result = maximumToys(prices, k)    
    print(result)    