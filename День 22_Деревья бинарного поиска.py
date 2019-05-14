# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:28:22 2019

@author: ValentinePit
"""

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        heightL = heightR = 0
        if root.left != None:
            heightL += 1
            getHeight(root.left)
        if root.right != None:
            heightR += 1 
            getHeight(root.right )
        if heightL > heightR:
            return heightL
        return heightR

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)  