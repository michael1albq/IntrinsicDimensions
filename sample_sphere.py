# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 11:07:48 2017

@author: Kafung
"""

import numpy as np
# Outputs n sample points from a random sphere in R^3 centered at c as a matrix of the form nx3.
#Note: We use the last construction found in http://mathworld.wolfram.com/SpherePointPicking.html.

def sample_sphere(n, c):
    vec = np.random.randn(3, n)
    vec /= np.linalg.norm(vec, axis=0)
    recenter = np.repeat(c,n)
    recenter = np.reshape(recenter, (3,n))
    vec = vec + recenter
    return np.transpose(vec)

if __name__ == "__main__":
    print(sample_sphere(10))
