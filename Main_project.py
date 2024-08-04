# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 10:03:34 2022

@author: swati
"""

import sys
import string
import math
import os
import Calc_class
import Quiz_class
import File_class


category_tuple = ("A", "Q", "E", "P") # tuple
final_grade_list =[] #list
grade_set = {"A", "B", "C", "D"} #set

print("The categories and their codes are: \nA: Assignment/Homework/Lab\n"
      "Q: Quiz/Test\nE: Final exams\nP: Project\n")
print("The grades are: 'A' 'B' 'C' and 'D'")

# enter target and passing grades
while True: #while loop
    target_grade=input(
        "Enter your target grade for this semester: ")
    passing_grade = input(
        "Enter passing grade for this semester: ")    
    target_grade = target_grade.upper()
    passing_grade = passing_grade.upper()
                              
    if target_grade and passing_grade not in grade_set:   #if loop     
        print("Enter a grade A,B,C or D")
        
    elif passing_grade < target_grade:
        print ("\nEnter a target grade above passing grade please.")
        
    else : break

while True: 
    cat_list = list(category_tuple) #zip into dict keys: A Q E P
    w_list = []                     #zip into dict values: weightage
    for i in cat_list:
        w_val = int(input("Enter weightage of " + i + ": "))
        w_list.append(w_val)   
    if sum(w_list) != 100:            
        print("Weightage must be out of total 100")        
    else:
        break
   

def target(current_grade): #user defined function
    '''assess if grades are on track'''    
    current_grade= current_grade.upper()    
    # print(passing_grade, target_grade)    
    if passing_grade < current_grade:
        print("\nGrades are below passing grade, try to improve!")    
    elif target_grade < current_grade:
        print("\nYou are below target grade but you are passing, try to catch up!")
    else:
        print("\nGrades are on track, keep it up!")
        

# input category for which you want to enter marks
print("\nChoose category of submissions  \nA: Assignment/Homework/Lab\n"
      "Q: Quiz/Test\nE: Final exams\nP: Project")

#choose category and input marks. Goes on till you exit by entering x or X 
#calls Quiz_class file's classes   
while True:
    inp_cat = input("Enter category: ")      
    inp_cat = inp_cat.upper()    
            
    if inp_cat in category_tuple:        
        if inp_cat =="A":
            
            grade_stats = Quiz_class.Assignment()               
            grade_stats.get_assign_marks()   
            assign_percentage = grade_stats.assign_percent()  
            final_grade_list.append(assign_percentage)            
            cur_assign_letter = grade_stats.assign_letter()   
            print(grade_stats.__str__())
            leave = input("Enter X to exit and ENTER key to continue:  ")
            if leave.upper() =="X":
                break
        
        if inp_cat =="Q" :
            
            quiz_stats = Quiz_class.Quiz()        
            quiz_stats.get_quiz_marks()   
            quiz_percentage = quiz_stats.quiz_percent()
            final_grade_list.append(quiz_percentage)              
            cur_quiz_letter = quiz_stats.quiz_letter()     
            print(quiz_stats.__str__())
            leave = input("Enter X to exit and ENTER key to continue:  ")
            if leave.upper() =="X":
                break
                       
    
        if inp_cat == "E":            
            exam_grade = Calc_class.Calc()  
            exam_marks = int(input("Enter final exam grade or enter hypothetical "
                                    "grade to check all grade stats: "))
            max_marks = int(input("Enter maximum marks of final exam: "))
            
            exam_percent = exam_grade.percent(exam_marks,max_marks)            
            final_grade_list.append(exam_percent)            
            exam_letter = exam_grade.letter_grade(exam_percent)            
            print(f'\nYour exam percentage and grade are: {exam_percent:.2f} %,'
                  f' {exam_letter}')
            
            leave = input("Enter X to exit and ENTER key to continue:  ")
            if leave.upper() =="X":
                break
            
            
        if inp_cat == "P":
            
            project_grade = Calc_class.Calc()  
            project_marks = int(input("Enter final project grade or enter "
                                      "hypothetical grade to check all grade stats: "))
            max_project_marks = int(input("Enter maximum marks of project: "))
            
            project_percent = project_grade.percent(
                project_marks,max_project_marks)            
            final_grade_list.append(project_percent)
            project_letter = project_grade.letter_grade(project_percent)            
            print(f'\nYour project percentage and grade are: {project_percent:.2f} %,'
                  f' {project_letter}')
            
            leave = input("Enter X to exit and ENTER key to continue:  ")
            if leave.upper() =="X":
                break
       
    else :
        print("Please choose from above categories")
        True

#calculating final grades, calling methods from other classes (Calc)
final_percentage = Calc_class.Calc().grade_average(final_grade_list)
final_letter = Calc_class.Calc().letter_grade(final_percentage)

x = target(final_letter)
w_dict = dict(zip(cat_list, w_list)) # dictionary
assign_section = (assign_percentage/100) *w_dict["A"]    
quiz_section = (quiz_percentage/100)*w_dict["Q"]
exam_section = (exam_percent/100)*w_dict["E"]
project_section = (project_percent/100)*w_dict["P"]


assign_and_quiz_grades = assign_section + quiz_section 
assign_and_quiz_total = w_dict["A"]+ w_dict["Q"] 
remaining_total = 100- assign_and_quiz_total 

# calculating remaining grade 

def need_to_get(grades):
    if grades == "A":    
        need_marks = 90 - assign_and_quiz_grades 
        
    elif grades =="B":    
        need_marks = 80 - assign_and_quiz_grades 
        
    elif grades == "C":    
        need_marks = 70 - assign_and_quiz_grades 
    
    else:
        need_marks = 60 - assign_and_quiz_grades
        
    return need_marks

remaining_grade = need_to_get(target_grade)
need_to_pass =  need_to_get(passing_grade)
    
need_grade_exam = w_dict["E"]/remaining_total * remaining_grade
need_exam_pass = w_dict["E"]/remaining_total * need_to_pass
need_grade_project = w_dict["P"]/remaining_total * remaining_grade
need_project_pass = w_dict["P"]/remaining_total * need_to_pass
need_exam_per = need_grade_exam/w_dict["E"]*100
need_project_per = need_grade_project/w_dict["P"]*100


if remaining_grade > remaining_total:
    print("That's not likely, try with a different target grade")

#final output
final_output = f'\nYour target grade is: {target_grade}\n\
Your passing grade is: {passing_grade}\n\
Your final percentage is: {final_percentage:.2f} %\n\
Your final letter grade is: {final_letter}\n\
\nAssuming correct grades in all categories, weightage-proportionate marks are:\n\
\nAssignment: {assign_section:.2f}/{w_dict["A"]} ({assign_percentage:.2f} %, {cur_assign_letter}) \n\
Quiz: {quiz_section:.2f}/{w_dict["Q"]} ({quiz_percentage:.2f} %, {cur_quiz_letter})\n\
Exam: {exam_section:.2f}/{w_dict["E"]} ({exam_percent:.2f}%, {exam_letter})\n\
Project: {project_section:.2f}/{w_dict["P"]} ({project_percent:.2f} %, {project_letter})\n\
\nAssuming hypothetical marks for Project and Exam categories, here are the required grades:\n\
\nRemaining total marks: {remaining_total}\n\
Marks you need to get out of {remaining_total}: {remaining_grade:.2f}\n\
\nMarks you need to get in EXAM out of {w_dict["E"]}: {need_grade_exam:.2f}\n\
Marks you need to get in PROJECT out of {w_dict["P"]}: {need_grade_project:.2f}\n\
The percentage you need to get in EXAM: {need_exam_per:.2f} %\n\
The percentage you need to get in PROJECT: {need_project_per:.2f} %\n\
\nMinimum marks needed for passing EXAM out of {w_dict["E"]}: {need_exam_pass:.2f}\n\
Minimum marks needed for passing PROJECT out of {w_dict["P"]}: {need_project_pass:.2f}\n'


print(final_output)

#calling class method to read input file and output to a text file.

result_print = File_class.File_in_out()
result_print.write_file(final_output)







