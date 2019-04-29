# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:27:51 2019

@author: ValentinePit
"""

def substrCount(n, s):
    
    num_of_pos = 0
    ln_1 = 0
    X = 0
    f = 0 # индикатор границы проверенной области
    for i in range(n):
        s1 = s[::-1] #начали перебирать символы
        num_of_char = s.count(s[i])
        if num_of_char > 1: # если встречается более 1 раза
            num_of_pos1 = s1.index(s[i])
            
            
            num_of_pos = len(s1) - num_of_pos-1 #номер последнего элемента 
            for j in range(f, num_of_char):
                ln_1 = i + num_of_pos #длинна отрезка  
                if ln_1 % 2 == 1:
                    
                    if s[i : ((i+num_of_pos)//2)] == s[(i + num_of_pos)//2 : num_of_pos]:
                        
                        X += len((s[num_of_pos] - s[i]) // 2)
                        f = num_of_pos
                        
                        break
                else:
                    if s[i :(i + num_of_pos)//2 -1] == s[(i + num_of_pos)//2 +1 : num_of_pos]:
                        X += len((s[ num_of_pos] - s[i]) // 2)
                        f = num_of_pos
                        break
                s1 =  s1[num_of_pos1+1:]  
                num_of_pos1 = s1.index(s[i])
                num_of_pos = len(s1) - num_of_pos1
                

def test_1():
    if  substrCount(5, "abbaca") == 10:
        print("Test 1 - OK")
    else:
        print("Test 1 - Not OK")
        
def test_2():
    if  substrCount(7, 'abcbaba') == 10:
        print("Test 2 - OK")
    else:
        print("Test 2 - Not OK")  

test_1()
test_2()