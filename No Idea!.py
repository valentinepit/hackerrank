# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:03:39 2019
There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints 
 
 

Input Format

The first line contains integers  and  separated by a space. 
The second line contains  integers, the elements of the array. 
The third and fourth lines contain  integers,  and , respectively.

Output Format

Output a single integer, your total happiness.
@author: ValentinePit
"""
"""
def inc(arr, one_set):
    """ counting inclusions"""
    p = 0
    for i in one_set:
        p += ls.count(i)
        #print(i, p)
    return p    

m, n = map(int, input().split())
ls  = []
ls = input().split()
a = set(input().split())
b = set(input().split())
#print(ls, a, b)
c = a - b
d = b - a 
#print(c)
per = inc(ls, c)
per -= inc(ls, d)
print(per) """

n, m = input().split()

sc_ar = input().split()

A = set(input().split())
B = set(input().split())
print (sum([(i in A) - (i in B) for i in sc_ar]))