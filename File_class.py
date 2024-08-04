# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:45:52 2022

@author: swati
"""

import sys
import string
import math
import os

class File_in_out():
    '''use text file to output text'''
    
    #__init__ method with paramters
    def __init__(self, file1 = "cs521_project_input.txt", 
                 file2 = "cs521_project_output.txt"):
        
        self.file1 = file1
        self.file2 = file2
    
    def write_file(self, output):
        
        self.output = output
        a = os.getcwd()
        b = os.path.join(a, self.file1 )
        c = os.path.join(a, self.file2)
        # print(b)
        
        file_in = open(b,'r')
        file_out = open(c, 'w')
        
        d = file_in.readline()         
        
        file_out.write(d + output)            
        file_in.close()        
        file_out.close()

