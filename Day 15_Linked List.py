# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:46:06 2019

@author: ValentinePit
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
        
        
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next
    
    def insert(self,head,data):
      if (head == None):
          head = Node(data)
      elif (head.next == None):
          head.next = Node(data)
      else: 
          self.insert(head.next, data)
      return head
        
        
"""            
def add(self, x):
        self.length+=1
        if self.first == None:
            #self.first и self.last будут указывать на одну область памяти
            self.last = self.first = Node(x, None)
        else:
            #здесь, уже на разные, т.к. произошло присваивание
            self.last.next = self.last = Node(x, None)
"""

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
       
mylist.display(head); 	  