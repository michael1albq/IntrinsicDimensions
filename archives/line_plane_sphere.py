# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:07:19 2017

@author: Kafung
"""
import numpy as np
from numpy import linalg as LA
def line_plane_sphere(k, n, c, m) :
    
    ps = plane_sphere(n, c, m) 
    plane = ps[0] 
    sphere = ps[1] 
    #combin_ps = np.reshape(np.append(sphere, plane), (-1,3)) 
    plane_tup = list(tuple(row) for row in plane)
    sphere_tup = list(tuple(row) for row in sphere)
    intersection = np.array([list(item) for item in 
                    set(plane_tup).intersection(sphere_tup)]) 
    if len(intersection) == 0 :
        return ["intersection empty", intersection]
    line = sample_line(k, intersection[0])
    
    #We remove any points on the plane that is inside the unit sphere.
    rel_line_pts = []
    for i in range(k) :
        if LA.norm(line[i]-c)>=1 :
            rel_line_pts = np.append(rel_line_pts, line[i])
        
    rel_line_pts =np.reshape(rel_line_pts, (-1,3))
    
    return [rel_line_pts, plane, sphere]