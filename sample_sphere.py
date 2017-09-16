# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 11:07:48 2017

@author: Kafung
"""

import numpy as np
from numpy import linalg as la

def sample_sphere(n):
    vec = np.random.randn(3, n)
    vec /= np.linalg.norm(vec, axis=0)
    return np.transpose(vec)