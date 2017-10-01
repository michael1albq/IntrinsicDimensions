# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 22:05:55 2017

@author: Kafung
"""

import numpy as np 

# Outputs n sample points from a random plane in R^3 as a matrix of the form nx3.
def sample_plane(n):
    
    normal_vec = 2*(np.random.random(3)-1/2)
    point_plane = 2*(np.random.random(3)-1/2) 
    plane_points = [] 
    
    #Points on the plane must satisfy the equation (n1,n2,n3).(x-p1, y-p2, z-p3) = 0, where . operation 
    #represents the dot product and (n1,n2,n3) is the normal vector and (p1,p2,p3) is a point on the plane.
    #We randomly sample for x and y and solve for z using the above equation. 
    for int in range(n) :
        sample_2coord = 2*(np.random.random(2)-1/2) 
        last_coord = sample_2coord - point_plane[0:2] 
        last_coord = -(np.dot(normal_vec[0:2], last_coord)-
                       normal_vec[2]*point_plane[2])/normal_vec[2] 
        sample_2coord = np.append(sample_2coord, last_coord) 
        plane_points = np.append(plane_points,sample_2coord)
   
    plane_points = np.reshape(plane_points, (n,3))    
         
    return plane_points