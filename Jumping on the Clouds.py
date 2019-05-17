# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:15:32 2019
Emma is playing a new mobile game that starts with consecutively numbered clouds. 
Some of the clouds are thunderheads and others are cumulus.
 She can jump on any cumulus cloud having a number that is equal to the number 
 of the current cloud plus  or . She must avoid the thunderheads. Determine 
the minimum number of jumps it will take Emma to jump
from her starting postion to the last cloud. It is always possible to win the game.
@author: ValentinePit
"""

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count = i = 0
    while i < len(c)-2:
        if c[i+2] == 0:
            i += 2
            
        elif c[i+1] == 1:
            print("wrong way")
        else:
            i += 1
        count += 1
        print("i=", i)
    if i == len(c) - 2:
        count += 1
    return count    
            

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()