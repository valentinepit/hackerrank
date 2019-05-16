# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:28:22 2019
Task 
The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. You are given a pointer, , pointing to the root of a binary search tree. Complete the getHeight function provided in your editor so that it returns the height of the binary search tree.

Input Format

The locked stub code in your editor reads the following inputs and assembles them into a binary search tree: 
The first line contains an integer, , denoting the number of nodes in the tree. 
Each of the  subsequent lines contains an integer, , denoting the value of an element that must be added to the BST.

Output Format

The locked stub code in your editor will print the integer returned by your getHeight function denoting the height of the BST.
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