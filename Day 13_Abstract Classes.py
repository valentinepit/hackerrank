# -*- coding: utf-8 -*-
"""
Created on Mon May  6 22:05:32 2019

@author: ValentinePit
"""

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title 
        self.author=author
        
    @abstractmethod
    def display(self): pass
        
#Write MyBook class

class MyBook(Book):
    def __init__(self, title, author, price):
        self.price = price
        self.title=title 
        self.author=author
        
    def display(self):
        print('Title:', self.title)
        print('Author:', self.author)
        print('Price:', self.price)  
        
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()