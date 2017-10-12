# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 04:39:47 2017

@author: Kafung
"""
import numpy as np
import math

#Input a matrix data, a threshold K to determine the min number  
#of points in each neighborhood, a threshold thres for percentage of variance 
#to exhibit and num, the number of radii
def intrinsic_dim(data, K, thres, num) :
    #Construct radius vector
    rads = [2**(i) for i in range(num)] 
    dims = np.zeros((len(data), num))
    int_dim = np.zeros(len(data))
    elem_ind = -1 
    for elem in data :
        density = []
        elem_ind += 1
        rad_ind = -1
        for radius in rads :
            D_n = neighborhood(data, elem, radius )
            rad_ind += 1
            if len(D_n) < math.log(K*math.log(K,10)):
                density.append(0)
                dims[elem_ind, rad_ind] = -1
            else:
                density.append(1)
                D_n0 = D_n - np.mean(D_n, axis = 0)
                S = svd(D_n0)
                S_2 = np.multiply(S,S)
                TV = sum(S_2)
                CRV = np.multiply(1/TV, 
                      [sum(S_2[0:i]) for i in range(len(S_2)+1)])[1:]
                CRV_bool = CRV>thres
                ind = [i for i,x in enumerate(CRV_bool) if x]
                dims[elem_ind, rad_ind] = ind[0] 
 
        int_dim[elem_ind] = min(i for i in dims[elem_ind, :] if i>-1 )
    
    return [int_dim, dims]

                
                
                
                