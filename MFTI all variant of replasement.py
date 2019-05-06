# -*- coding: utf-8 -*-
"""
Created on Sat May  4 23:29:51 2019
генерация всех перестановок n чисел
@author: ValentinePit
"""
def generate_numbers(N:int, M:int, prefix=None):
    """ Генерирует все числа с лидирующими нулями 
        в N-ричной системе счисления (N<=10)
        длины M"""
        
    prefix = prefix or []
    if M == 0: 
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()
        

generate_numbers(4, 3)
     
        