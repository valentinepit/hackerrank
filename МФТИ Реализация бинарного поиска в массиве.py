# -*- coding: utf-8 -*-
"""
Created on Sun May 26 22:42:14 2019
Алгоритм ищет элемент в массиве.

@author: ValentinePit
"""

def left_bound(A, key):
    """Функция ищет в массиве А левую границу вхождения ключа
       делит попалам массив и проверяет больше ли значения ключа.
       Если нет то сдвигает левую границу на средину области. Иначе правую. 
       Все это до тех пор, пока расстояние между границами больше 1""" 
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right)//2
        if A[middle] < key:
            left = middle
        else: 
            right = middle
    return left      

def right_bound(A, key):
    """ТО же но для правой границы"""
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right)//2
        if A[middle] <= key:
            left = middle
        else: 
            right = middle
    return right    

"""Между этими двумя значениями и будет находиться искомое если разница 
между ними больше 1"""