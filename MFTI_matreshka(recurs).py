# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 23:00:27 2019

@author: ValentinePit
"""



def matreshka(n):
    if n == 1:
        print("Матрешечка")
    else:
        print("Верх матрешки n= ", n)
        matreshka(n-1)
        print("Низ матрешки n=", n)

matreshka(5)        
        
        