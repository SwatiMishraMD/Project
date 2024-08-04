# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 10:44:49 2022

@author: swati
"""
import sys
import string
import math
import os
import Calc_class

# classes to take marks and do calculations with Calc class methods

class Assignment():
    
    def __init__(self):
        pass
    
    def get_assign_marks(self):        
        self.marks_list =[]
        self.max_list=[]
        
        while True:   # enter as many marks as needed  
                        #try except 
            try:
                self.marks,self.max_assign =input(
                    "Enter marks received for assignment: "), input(
                        "Enter maximum marks for assignment: ") 
                                                       
                self.marks,self.max_assign = [int(self.marks), int(self.max_assign)]
                
                if self.marks>self.max_assign:    
                    print("Marks cannot be more than maximum marks, try again")
                    break
                                
                self.marks_list.append(self.marks) 
                self.max_list.append(self.max_assign)
                
                print("\nEnter any letter to exit and marks to continue")
                      
            except ValueError:
                break   
         
        return self.marks_list, self.max_list
    
    def __assign_totals__(self): #private method not called outside class    
        self.__assign_sum__ = 0  #private attribute not called outside class
        for i in self.marks_list:
            self.__assign_sum__ += i
        return self.__assign_sum__     
            
    def __add__(self):     #magic method           
        self.__max_sum__ = 0
        for i in self.max_list:
            self.__max_sum__ += i
            
        return self.__max_sum__
    
    def assign_percent(self):   #public method1 with public attribute1
        self.__assign_totals__()
        self.__add__()
        self.assign_percentage = Calc_class.Calc().percent(self.__assign_sum__,
                                                          self.__max_sum__)
        return self.assign_percentage
    
    def assign_letter(self): #public method2 with public attribute2
        self.assign_let_grade = Calc_class.Calc().letter_grade(self.assign_percentage)
        return self.assign_let_grade
    
    def __str__(self): #__str__ method
        return f'\nAssignment percentage is: {self.assign_percentage:.2f} % \
and the letter grade is: {self.assign_let_grade}'
    
        

            
class Quiz():
    
    def __init__(self):
        pass
    
    def get_quiz_marks(self):        
        self.quiz_list =[]
        self.max_quiz_list=[]
        
        while True:             
            try:
                self.quiz,self.max_quiz =input(
                    "Enter marks received for quiz: "), input(
                        "Enter maximum marks for quiz: ") 
                
                self.quiz,self.max_quiz = [int(self.quiz), int(self.max_quiz)]
                
                if self.quiz>self.max_quiz:    
                    print("Marks cannot be more than maximum marks, try again")
                    break     
                   
                self.quiz_list.append(self.quiz) 
                self.max_quiz_list.append(self.max_quiz)
                                                             
                print("\nEnter any letter to exit and marks to continue")
                                               
            except ValueError:
                break
            
        return self.quiz_list, self.max_quiz_list
    
    def __quiz_totals__(self):         
        self.__quiz_sum__ = 0
        for i in self.quiz_list:
            self.__quiz_sum__ += i
                
        self.__max_quiz__ = 0
        for i in self.max_quiz_list:
            self.__max_quiz__ += i
            
        return self.__quiz_sum__ , self.__max_quiz__
    
    def quiz_percent(self):  
        self.__quiz_totals__()
        self.quiz_percentage = Calc_class.Calc().percent(self.__quiz_sum__,
                                                          self.__max_quiz__)
        return self.quiz_percentage
    
    def quiz_letter(self):
        self.quiz_let_grade = Calc_class.Calc().letter_grade(self.quiz_percentage)
        return self.quiz_let_grade
    
    def __str__(self):
        return f'\nQuiz percentage is: {self.quiz_percentage:.2f} % \
and the letter grade is: {self.quiz_let_grade}'


    
    