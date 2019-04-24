# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 12:10:27 2019
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands. 
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
@author: ValentinePit
"""

if __name__ == '__main__':
    N = int(input())
    com = []
    ls = []
    for i in range(N):
        com = input().split()
        if com[0] == "insert":
            ls.insert(int(com[1]), int(com[2]))
        elif com[0] == "print":
            print(ls)
        elif com[0] == "append": 
            ls.append(int(com[1]))
        elif com[0] == "remove":
            ls.remove(int(com[1]))
        elif com[0] == "sort":
            ls.sort()
        elif com[0] == "pop":
            ls.pop()
        elif com[0] == "reverse":
            ls.reverse()
        else:
            print("Wrong command")                            
