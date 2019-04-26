# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 17:42:50 2019
It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by  from  at the front of the line to  at the back.

Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if and  bribes , the queue will look like this: .

Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!

Function Description

Complete the function minimumBribes in the editor below. It must print an integer representing the minimum number of bribes necessary, or Too chaotic if the line configuration is not possible.

minimumBribes has the following parameter(s):

q: an array of integers
Input Format

The first line contains an integer , the number of test cases.

Each of the next  pairs of lines are as follows: 
- The first line contains an integer , the number of people in the queue 
- The second line has  space-separated integers describing the final state of the queue.
@author: ValentinePit
"""
  

def minimumBribes(Q):
    """Finding min bribes"""
    Q = [P-1 for P in Q]
    moves = 0
    for i,P in enumerate(Q):
        if P - i > 2:
            return "Too chaotic"
        for j in range(max(P-1,0),i):
            if Q[j] > P:
                moves += 1
   
    return moves

def test_1():
    if minimumBribes([2, 1, 5, 3, 4]) == 3:
        print("test1 - OK")
    else:
        print("test1 is not OK")
     
def test_2():
    if minimumBribes([2, 5, 1, 3, 4]) == "Too chaotic":
        print("test2 - OK")
    else:
        print("test2 is not OK" )
         
    
if __name__ == '__main__':
    t = int(input())

#    test_1()
#    test_2()
    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))
          
        print(minimumBribes(q))
