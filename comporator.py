# -*- coding: utf-8 -*-
"""
Created on Fri May 17 21:34:29 2019

@author: ValentinePit
"""

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        pass
        
    def comparator(a, b):
        if a > b:
            return a.name, b.name
        else:
            return b.name, a.name

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)