# -*- coding: utf-8 -*-
"""
Created on Sat May  4 23:43:59 2019

@author: ValentinePit
"""
def search(x, a):
    """Ищет x в  A и возвращает True если есть False если нет"""
    for i in a:
        if x == i:
            return True
        
    return False
    
def generate_permutations(N:int, M:int=-1, prefix = None):
    """"Функция генерирует перестановок N чисел в M позициях
         с префиксом prefix"""
    
    M = N if M == -1 else M
    prefix = prefix or []
    if M ==0:
        print(prefix)
        return
    for number in range(1, N+1):
        if search(number, prefix) in prefix:
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()
        
        
generate_permutations(3)        