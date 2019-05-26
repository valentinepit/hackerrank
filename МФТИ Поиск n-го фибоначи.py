# -*- coding: utf-8 -*-
"""
Created on Sun May 26 23:02:02 2019

@author: ValentinePit
"""

def fib_n(n):
    """Поиск n-го числа фибоначию. Фибиначивое дерево О(Fib n)"""
    if n<=1:
        return n
    return(fib(n-1)+fib(n-2))
    
    
    
 """Простой поиск всех чисел фибоначи до n"""   
fib = [0, 1]+[0]*(n-1)
for i in range(2, n+1):
    fib[i] = fib[i-1] + fib[i-2]    