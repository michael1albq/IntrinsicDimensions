# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 22:05:55 2017

@author: Kafung
"""

import numpy as np


def sample_line(n):
    """
    Outputs n sample points from a random line in R^3 as a matrix of the form nx3
    :param n: No. of points to be sampled
    :return: Coordinates of the n points on the line [x,y,z]
    """
    # Generate direction vector to be scaled
    dir_vec = np.random.randn(3)
    line_point = np.random.randn(3)

    # Generate random scalars
    parameter = np.transpose(np.random.randn(n)[np.newaxis])

    # Translate dir_vec by random scalars to get points on the same line
    line_points = line_point + parameter * dir_vec

    return line_points


if __name__ == "__main__":
    print(sample_line(10))
