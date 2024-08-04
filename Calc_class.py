# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 16:02:24 2022

@author: swati
"""

class Calc(): # 3 user defined functions with parameter and return
    
    def __init__(self):
        pass
    
        
    def percent(self, total, max_total):
        self.total = total
        self.max_total = max_total
        
        self.percent = (self.total/self.max_total)*100
        return self.percent
    
    def letter_grade(self, num_grade): 
        
        self.num_grade = num_grade
                
        if 100 >= self.num_grade >=90:
            self.let_grade = "A"
            
        elif  90 > self.num_grade >=80:
            self.let_grade = "B"
            
        elif  80 > self.num_grade >=70:
            self.let_grade = "C" 
            
        elif  70 > self.num_grade >=60:
            self.let_grade = "D"
                   
        else:
            self.let_grade = "F"
            
        return self.let_grade
    
    
    def grade_average(self, grade_list):
        '''takes list paramter and calculates average number grade to 
        later convert to final letter grade'''
        
        self.grade_list = grade_list
        
        self.final_average = sum(self.grade_list)/len(grade_list) 
        
        return self.final_average

#unit test 1 for percent method with assert

test1 = Calc().percent(80,100)

assert test1 == 80, "percent function not working"     

#print(test1)

# unit test 2 for grade_average method with assert

test_list = [10,20,10,20]   
     
test2 = Calc().grade_average(test_list)

#print(test2)        
         
assert test2 == 15, "grade_average function not working"    
        
        
        
        











            
    
            