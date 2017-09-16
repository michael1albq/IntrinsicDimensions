# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 11:07:48 2017

@author: Kafung
"""

import numpy as np


def sample_sphere(n):
    vec = np.random.randn(3, n)
    vec /= np.linalg.norm(vec, axis=0)
    return np.transpose(vec)

if __name__ == "__main__":
    print(sample_sphere(10))
