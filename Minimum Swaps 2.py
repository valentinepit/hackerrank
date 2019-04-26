# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 23:21:28 2019
You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.

For example, given the array  we perform the following steps:
@author: ValentinePit
"""
def minimumSwaps(permutation):
    """Find number of swaps required to convert the permutation into
    identity one.

    """
    # decompose the permutation into disjoint cycles
    nswaps = 0
    seen = set()
    for i in range(1, len(permutation)+1):
        if i not in seen:           
           j = i # begin new cycle that starts with `i`
           while permutation[j-1] != i: # (i σ(i) σ(σ(i)) ...)
               j = permutation[j-1]
               seen.add(j)
               nswaps += 1

    return nswaps

#def minimumSwaps(arr):
 #   pass

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    
    arr = list(map(int, input().rstrip().split()))
    
    res=minimumSwaps(arr)
    print(res)
    
    #res = minimumSwaps(arr)

    #fptr.write(str(res) + '\n')

    #fptr.close()

