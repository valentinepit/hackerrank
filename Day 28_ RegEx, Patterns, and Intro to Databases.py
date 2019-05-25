# -*- coding: utf-8 -*-
"""
Created on Sat May 25 15:15:11 2019
Consider a database table, Emails, which has the attributes First Name and 
Email ID. Given  rows of data simulating the Emails table, 
print an alphabetically-ordered list of people whose email address ends in .
@author: ValentinePit
"""


import math
import os
import random
import re
import sys

def reg(f, e, r):
    lst = re.split(r'@', e)
    if lst[1] == 'gmail.com':
        r.append(f)
    return r    
        
   

def test():
    res =[]
    l = [['riya', 'riya@gmail.com'], ['julia', 'julia@julia.me'], 
         ['julia', 'sjulia@gmail.com'], ['julia', 'julia@gmail.com'], 
         ['samantha', 'samantha@gmail.com'], ['tanya', 'tanya@gmail.com']]
    
    res = reg(l)
        
    goodres = ['riya', 'julia', 'julia', 'samantha', 'tanya']    
    if res == goodres:
        print("Ok")
    '''else:
        print(res)'''
        
    
if __name__ == '__main__':
    N = int(input())
    result = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        
        result =reg(firstName, emailID, result)
    
    result = sorted(result)    
    for i in range(len(result)):
        print (result[i])
    
