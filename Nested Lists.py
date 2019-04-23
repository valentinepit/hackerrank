# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 08:05:35 2019
Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, , the number of students. 
The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.
@author: Comp
"""

if __name__ == '__main__':
    clas = []
    
    def min2(lst, val_min):
        """ Returns value next by min"""
        
        for i in lst:
            if i[1] > val_min:
                return i[1]
        return val_min   
   
    for i in range(int(input())):
        name = input()
        score = float(input())
        clas.append([name, score])
     
    clas.sort(key=lambda i: i[1])
    #print(clas)
    
    m = clas[0][1]
    m = min2(clas, m)
    clas.sort()
    
    
    #print("m=", m)
    for i in clas:
        if i[1] == m:
            print(i[0])
        
    ''' print(clas)    
    print("m=", m, "n=", n)
    clas = sorted(clas)
    for i in range(len(clas)):
        if n == clas[i][1]:
            print(clas[i])'''