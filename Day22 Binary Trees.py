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

    '''def getHeight(self,root):
        global heightL 
        global heightR
        if root.left == None and root.right == None:
            return heightL if heightL > heightR else heightR
        heightL = 0
        heightR = 0
        if root.left != None:
            heightL += myTree.getHeight(root.left)
        if root.right != None:
            heightR += myTree.getHeight(root.right )
        if heightL > heightR:
            return heightL+ 1
        return heightR + 1'''
        
    def getHeight(self, root):
        if root == None: return -1
        return 1 + max(myTree.getHeight(root.right), myTree.getHeight(root.left))
         
                
height = 0
heightL = heightR = 0
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)  