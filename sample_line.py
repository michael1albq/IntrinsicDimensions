# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 22:05:55 2017

@author: Kafung
"""
import random
import numpy as np 


def sample_line(n):
    
    dir_vec = np.random.randn(3) ;
    line_point = np.random.randn(3) ;
    parameter = np.transpose(np.random.randn(n)[np.newaxis]) ;
    line_points = line_point + parameter*dir_vec ;
      
    return line_points
    
    

    
    
    
    

    