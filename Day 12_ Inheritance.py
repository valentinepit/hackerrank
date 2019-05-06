# -*- coding: utf-8 -*-
"""
Created on Sat May  4 10:33:53 2019

@author: ValentinePit
"""

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):#   Class Constructor
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
        self.average = 0
    #   Parameters:
    #self.firstName = first.Name #   firstName - A string denoting the Person's first name.
    #self.lastName = lastName #   lastName - A string denoting the Person's last name.
    #self.idNumber = idNumber #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    def calculate(self):#   Function Name: calculate
        
        for i in range(len(self.scores)): #   Return: A character denoting the grade.
            self.average = self.average + self.scores[i]
        self.average = self.average / len(self.scores)
        
        if self.average >= 90:
            return "O"
        elif self.average >= 80:
            return "E"
        elif self.average >= 70:
            return "A"
        elif self.average >= 55:
            return "P"
        elif self.average >= 40:
            return "D"
        else:
            return "T"
    # Write your function here
def test_1():

    firstName = "Doshi"
    lastName = "Aakansha"
    idNum = 7825621
    scores = [31, 32, 34, 35]
    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print("Grade:", s.calculate())

test_1()    