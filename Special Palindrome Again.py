# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:27:51 2019

@author: ValentinePit
"""

def substrCount(n, s):
    s1 = reversed(s)
    X = 0
    f = 0 # индикатор границы проверенной области
    for i in range(n): #начали перебирать символы
        num_of_char = s.count(s[i])
        if num_of_char > 1: # если встречается более 1 раза
            num_of_pos = s1.index(s[i])
            num_of_pos = len(s1) - num_of_pos #номер последнего элемента 
            for j in range(f, num_of_char):
                if (s[i] + s[ num_of_pos]) % 2 == 1:
                    if (s[i]: s[(i + num_of_pos)//2]) == (s[(i + num_of_pos)//2]:s[num_of_pos]):
                        X += (s[ num_of_pos] - s[i]) // 2
                        f = num_of_pos
                        break
                else:
                    if (s[i]: s[(i + num_of_pos)//2 -1]) == (s[(i + num_of_pos)//2 +1]:s[num_of_pos]):
                        X += (s[ num_of_pos] - s[i]) // 2
                        f = num_of_pos
                        break
                num_of_pos = s1[num_of_pos:].index(s[i])
                num_of_pos = len(s1) - num_of_pos
                

def test_1():
    if  substrCount("aaaaa") == 10:
        print("Test 1 - OK")
    else:
        print("Test 1 - Not OK")
        
def test_2():
    if  substrCount('abcbaba') == 10:
        print("Test 2 - OK")
    else:
        print("Test 2 - Not OK")  

test_1()
test_2()