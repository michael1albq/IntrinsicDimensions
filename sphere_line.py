# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:07:19 2017

@author: Kafung
"""
import numpy as np 

#Outputs n sample points from a random sphere and m sample points from a line intersecting said random sphere.
def sphere_line(n, c, m) :
    sample_s = sample_sphere(n, c)
    
    #Construct a random line through point sample_s[0]
    line_point = sample_s[0] 
    
    parameter =np.transpose(2*(np.random.random(m)-1/2)[np.newaxis])
    sample_l = line_point + parameter*line_point
    
    #The first element is an array of the n sample points from the sphere. 
    #The second element is an array of the m sample points from the line.
    return [sample_s, sample_l]

    