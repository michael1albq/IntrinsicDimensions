# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 22:05:55 2017

@author: Kafung
"""
import numpy as np 

# Outputs n sample points from a random line in R^3 containing point p
# as a matrix of the form nx3. 
def sample_line(n, p):
    
    dir_vec = 2*(np.random.random(3)-1/2)
    line_point = p   
    parameter = np.transpose(2*(np.random.random(n)-1/2)[np.newaxis]) 
    line_points = line_point + parameter*dir_vec 
      
    return line_points
    
    

    
    
    
    

    