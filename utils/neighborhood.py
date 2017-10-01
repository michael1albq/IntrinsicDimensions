# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 16:36:01 2017

@author: Kafung
"""

import numpy as np
import scipy.spatial as spatial

def neighborhood(data, point, rad) :
    coord_set = list(tuple(row) for row in data)
    tree = spatial.cKDTree(coord_set)
    
    return tree.data[tree.query_ball_point(point, rad)]