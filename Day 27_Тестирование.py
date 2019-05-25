# -*- coding: utf-8 -*-
"""
Created on Sat May 25 12:58:12 2019

@author: ValentinePit
"""
import random

def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    #print(seq)
    
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
            #print("min_idx =", i)
    return min_idx

class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        seq = []
        return seq

class TestDataUniqueValues(object):
    
    seq = []
    for i in range(5):
        new = random.randrange(2, 200, 3)
        if new not in seq:
            seq.append(new)
                
    @staticmethod
    def get_array():
       seq = TestDataUniqueValues.seq
       return seq
        

    @staticmethod
    def get_expected_result():
        # complete this function
        seq = TestDataUniqueValues.get_array()
        return seq.index(min(seq))
    
class TestDataExactlyTwoDifferentMinimums(object):
    seq = []
    for i in range(5):
        new = random.randrange(2, 200, 3)
        if new not in seq:
            seq.append(new)
    seq.append(min(seq))
    #print(seq)      
    
    @staticmethod
    def get_array():
        seq = TestDataExactlyTwoDifferentMinimums.seq
        return seq 

    @staticmethod
    def get_expected_result():
        seq = TestDataExactlyTwoDifferentMinimums.get_array()
        #print(seq)
        return seq.index(min(seq))
                
                    
            
            

def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    #print(tmp)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
print("OK")
TestWithUniqueValues()
print("OK")
TestiWithExactyTwoDifferentMinimums()
print("OK")

#два паровых цыпленка 10 яиц кефир