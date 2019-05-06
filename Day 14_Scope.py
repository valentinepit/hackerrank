# -*- coding: utf-8 -*-
"""
Created on Mon May  6 23:02:33 2019

@author: ValentinePit
"""

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.__maximumDifference = 0

    def computeDifference(self):
        print(self.__elements)
        i = min(self.__elements)
        k= max(self.__elements)
        self.maximumDifference = k -i
        
        return self.maximumDifference
        
    
    
	# Add your code here

# End of Difference class

#_ = input()
#a = [int(e) for e in input().split(' ')]

def test_1(a):
    d = Difference(a)
    d.computeDifference()

    print( "Ok" if d.maximumDifference == 4 else d.maximumDifference)
    
    
    
test_1([1,3,5])    
    
    



