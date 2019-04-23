# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:23:59 2019
You have a record of  students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer  followed by the names and marks for students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

Input Format

The first line contains the integer , the number of students. The next  lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.

Constraints

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
@author: ValentinePit
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    
    av = 0
    for i in range(len(student_marks[query_name])):
        av += student_marks[query_name][i]
        
    print(format(av/(i+1), '.2f'))
    
        
