# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 23:27:05 2019
Шашанку нравятся строки, в которых последовательные символы отличаются. Например, ему нравится строка , но не нравится строка . Задняя строка, состоящая только из символов и . Он хочет понравится. Для этого он может удалить из нее символы.

Ваша задача - найти минимальное количество необходимых удалений.

Данный входной формат 
Первая строка Содержит целое Число , количество тестов. 
В следующих строках записано по одной строке.

Выходные Данные формат 
Выведите Минимальное Наименование Количества необходимого удаления для КАЖДОГО теста.
@author: ValentinePit
"""

def alternatingCharacters(s):
    count = 0
    if len(s) % 2 == 0:
        for i in range(1, len(s)-2, 2):
            if s[i] == s[i-1]: 
                count +=1
                #print("true", s[i], "=", s[i+1])
            if s[i] == s[i+1]: count +=1
        if s[i+2] == s[i+1]: count +=1
    else:
        for i in range(1, len(s)-1, 2):
            if s[i] == s[i-1]: count +=1
            if s[i] == s[i+1]: count +=1
       # if s[i+2] == s[i]: count +=1
    #print(count)
    return(count) 

def test_1():
    if  alternatingCharacters('BBBBB') == 4:
        print("Test 1 - OK")
    else:
        print("Test 1 - Not OK")
        
def test_2():
    if  alternatingCharacters('BABABA') == 0:
        print("Test 2 - OK")
    else:
        print("Test 2 - Not OK")  

test_1()
test_2()