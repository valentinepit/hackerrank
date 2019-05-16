# -*- coding: utf-8 -*-
"""
Created on Wed May 15 21:19:37 2019

@author: ValentinePit
"""

import sys

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

    # /* функция для распечатки элементов на определенном уровне дерева */
    def printGivenLevel(self, root, level):
      if root == None:
        return
      if level == 1:
        print ("%d " % root.data, end=" ")
      elif level > 1:
          self.printGivenLevel(root.left, level-1);
          self.printGivenLevel(root.right, level-1);

    def getHeight(self, root):
        if root == None: return -1
        return 1 + max(myTree.getHeight(root.right), myTree.getHeight(root.left))
         
# /* функция для распечатки дерева */
    def LevelOrder(self, root):
      h = self.getHeight(root) + 1
      i=1
      while(i<=h):
        self.printGivenLevel(root, i)
        i +=1
    
    '''def levelOrder(self,root):
        global flag
        if root == None: return
        
        print(root.data, end= " ")
        if flag > 0:
            myTree.levelOrder(root.left)
            flag *= -1
            myTree.levelOrder(root.right)
        else:
            myTree.levelOrder(root.right)
            flag *= -1'''
        #Write your code here
flag = 1
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.LevelOrder(root)