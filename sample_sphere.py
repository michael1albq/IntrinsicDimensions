# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 11:07:48 2017

@author: Kafung
"""

import numpy as np


def sample_sphere(n, c):
    """
    Outputs sample points from a random sphere in R^3 centered at c as a matrix of the form nx3

    :param n: No. of points to be sampled
    :param c: Vector - Coordinates for Center of sphere [x,y,z]
    :return: Coordinates of the n points on the sphere [x,y,z]

    Note: We use the last construction found in http://mathworld.wolfram.com/SpherePointPicking.html
    """
    vec = np.random.randn(3, n)
    vec /= np.linalg.norm(vec, axis=0)
    recenter = np.repeat(c, n)
    recenter = np.reshape(recenter, (3, n))
    vec = vec + recenter
    return np.transpose(vec)

if __name__ == "__main__":
    print(sample_sphere(10, [-0.45037415,  0.75855613,  2.88560308]))
