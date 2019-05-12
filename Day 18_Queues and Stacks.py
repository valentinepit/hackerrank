# -*- coding: utf-8 -*-
"""
Created on Sun May 12 21:27:41 2019

@author: ValentinePit
"""

import sys

class Solution():
    
    def __init__(self):
        self.st = []
        self.qw = []
    
    def pushCharacter(self, c):
        self.st += c
        
    
    def enqueueCharacter(self, c):
        self.qw += c
    
    def popCharacter(self):
        tmp = self.st.pop()
        #print (tmp)
        return tmp
    
    def dequeueCharacter(self):
        temp = self.qw[0]
        #print(temp)
        for i in range(len(self.qw)-1):
            self.qw[i] = self.qw[i+1]
        return temp    
    # Write your code here

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")  