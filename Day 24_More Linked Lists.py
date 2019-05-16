# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:57:42 2019

@author: ValentinePit
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        
        if head == None:            
            return head
        old = cur = head
        while cur != None:
            
            if cur.next != None:
                print(cur.next.data)
                if cur.data == cur.next.data:
                    cur.next = cur.next.next 
                    head=mylist.removeDuplicates(head)                       
                
            cur = cur.next
                    
            '''if old.data == cur.next.data:
                    cur.next = cur.next.next
            else:
                old =  cur = old.next
                
            cur = cur.next'''    
        return head    

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 