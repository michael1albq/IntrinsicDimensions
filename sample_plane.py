# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 22:05:55 2017

@author: Kafung
"""

import numpy as np 


def sample_plane(n):
    
    normal_vec = np.random.randn(3)
    point_plane = np.random.randn(3)
    sample_points = []

    for int in range(0, n):
        sample_2coord = np.random.randn(2)
        last_coord = sample_2coord - point_plane[0:2]
        last_coord = -(np.dot(normal_vec[0:2], last_coord)-normal_vec[2] * point_plane[2])/normal_vec[2]
        sample_2coord = np.append(sample_2coord, last_coord)
        sample_points = np.append(sample_points, sample_2coord, axis=0)

    sample_points = np.reshape(sample_points, (n,3))

    return sample_points

if __name__ == "__main__":
    print(sample_plane(10))

