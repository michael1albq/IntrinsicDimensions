# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:07:19 2017

@author: Kafung
"""
import numpy as np


def sample_sphere(n, c):
    """
    Outputs sample points from a random sphere in R^3 centered at c as a matrix 
    of the form nx3
    :param n: No. of points to be sampled
    :param c: Vector - Coordinates for center of sphere [x,y,z]
    :return: Coordinates of the n points on the sphere [x,y,z]
    Note: We use the last construction found in http://mathworld.wolfram.com/SpherePointPicking.html
    """
    vec = 2*(np.random.random((3, n))-1/2)
    vec /= np.linalg.norm(vec, axis=0)
    recenter = np.repeat(c, n)
    recenter = np.reshape(recenter, (3, n))
    vec = vec + recenter
    
    return np.transpose(vec)

    