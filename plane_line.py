# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 12:58:08 2017

@author: Kafung
"""

import numpy as np

#Outputs n sample points from a random plane and m sample points from a line intersecting said random plane.
def plane_line(n, m) :
    sample_p = sample_plane(n)
    
    #Construct a random line through point sample_p[0]
    line_point = sample_p[0] 
    dir_vec = np.random.randn(3) 
    parameter = np.transpose(np.random.random(m)[np.newaxis])
    sample_l = line_point + parameter*dir_vec
    
    #The first element is an array of the n sample points from the plane.
    #The second element is an array of the m sample points from the line.
    return [sample_p, sample_l]