# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 12:30:17 2017

@author: Kafung
"""

import numpy as np 

def svd(data) :
    
    #dat = data - np.mean(data, axis = 0)
    u, s, v = np.linalg.svd(data, full_matrices=True) ;
    return s
    