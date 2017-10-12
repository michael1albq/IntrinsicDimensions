# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 14:25:22 2017

@author: Kafung
"""

import numpy as np
from numpy import linalg as LA
#import sample_sphere as ss
#from sample_sphere import *

def plane_sphere(n, c, m) :
    """
    Constructs n sample points from a unit sphere centered at c and
    m sample points from a plane which intersects the unit sphere.
    If there are any k points from the m sample points that is contained
    in the unit sphere, we remove them and outputs only the m-k sample points.
    i.e. we do not produce any sample points inside the unit sphere. 
    """
    sphere = sample_sphere(n, c) 
    
    #We construct the plane containing the first 3 sample points 
    #sample_s[0:3] on the sphere. 
    plane_points = sphere[0:3]
    #Finding the normal vector
    vec1 = plane_points[1]-plane_points[0] 
    vec2 = plane_points[2]-plane_points[0] 
    #Normal vector 
    normal_vec = np.cross(vec1, vec2) 
    
    #Points on the plane must satisfy the equation 
    #(n1,n2,n3).(x-p1, y-p2, z-p3) = 0, where . operation 
    #represents the dot product and (n1,n2,n3) is the normal vector and 
    #(p1,p2,p3) is a point on the plane (we call it p0 in the code below).
    #We randomly sample for x and y and solve for z using the above equation. 
    p0=plane_points[0]
    for int in range(m) :
        sample_coord = 2*(np.random.random(2)-1/2) 
        first_coords = sample_coord - p0[0:2]
        last_coord = -(np.dot(normal_vec[0:2], first_coords)-
                       normal_vec[2]*p0[2])/normal_vec[2] 
        sample_coord = np.append(sample_coord, last_coord) 
        plane_points = np.append(plane_points,sample_coord)
    
    plane_points = np.reshape(plane_points, (m+3,3))
    
    #We remove any points on the plane that is inside the unit sphere.
    relevant_points = []
    for i in range(m+3) :
        if LA.norm(plane_points[i]-c)>=1 :
            relevant_points = np.append(relevant_points, plane_points[i])
        
    relevant_points =np.reshape(relevant_points, (-1,3))
    
    return [sphere, relevant_points]
    
    