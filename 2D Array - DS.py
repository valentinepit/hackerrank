# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 09:06:39 2019
Given an 6*6 2D Array, :
    We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:
@author: ValentinePit
"""

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
     """ count of hourlasses sum and peak it into a list"""
     
      m = arr[0][0] +arr[0][1] + arr[0][2] + arr[1][1] + arr[2][0] + arr[2][1] + arr[2][2]
     
     for i in range(4):
         for k in range(4):
             c = 0
             c += arr[i][k]
             c += arr[i][k+1]
             c += arr[i][k+2]
             c += arr[i+1][k+1]
             c += arr[i+2][k]
             c += arr[i+2][k+1]
             c += arr[i+2][k+2]
             if c > m: m =c
     return m       

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)

   #fptr.write(str(result) + '\n')

    #fptr.close()