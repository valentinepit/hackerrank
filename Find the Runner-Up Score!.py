# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 20:22:07 2019
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
"""
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    m = max(arr)
    mi = min(arr)
    cont = m
    
    for i in range(m-1, mi-1, -1):
        if  i in arr:
            cont = i
            break
          
    print(cont)    
    
   
    
    
        
