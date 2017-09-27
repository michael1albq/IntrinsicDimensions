# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 12:56:27 2017

@author: Kafung
"""

import numpy as np
import math
def intrinsic_dim(data, K, thres, num) :
    rads = [(1/2.)**(i) for i in range(num)] 
    dims = np.zeros((len(data), num))
    int_dim = np.zeros(len(data))
    elem_ind = -1 
    print("Our radius vector is:")
    print(rads)
    print("")
    for elem in data :     
        density = []
        elem_ind += 1
        rad_ind = -1
        for radius in rads :
            D_n = neighborhood(data, elem, radius )
            rad_ind += 1
            print("The neighborhood around of", elem, "with radius", radius )
            print(D_n)
            print("")
            if len(D_n) < math.log(K*math.log(K)):
                print("The neighborhood does not have enough points.")
                density.append(0)
                dims[elem_ind, rad_ind] = -1
            else:
                density.append(1)
                D_n0 = D_n - np.mean(D_n, axis = 0)
                print("Size of the neighborhood is ")
                print(len(D_n0))
                #D_n0 = (1/(len(D_n0)-1))*np.transpose(D_n0)
                S = svd(D_n0)
                S_2 = np.multiply(S,S)
                TV = sum(S_2)
                print("The total variance is")
                print(TV)
                print("")
                print("The variance is")
                print(S_2)
                print("")
                CRV =np.asarray([ (1/TV)*sum(S_2[0:i]) for i in range(len(S_2)+1)][1:])
                print("The cumulative relative variance is")
                print(CRV)
                print("")
                CRV_bool = CRV > thres
                print("Finding the index when CRV surpasses the threshold")
                print(CRV_bool)
                print("")
                ind = [i for i,x in enumerate(CRV_bool) if x]
                dims[elem_ind, rad_ind] = ind[0]+1 
                print("The dimension of ", elem, "with radius", radius)
                print(dims[elem_ind, rad_ind])
                print("")
                
 
        int_dim[elem_ind] = min(i for i in dims[elem_ind, :] if i>-1 )
        print("The intrinsic dim of ", elem)
        print(int_dim[elem_ind])
        print("")
    return [int_dim, dims, density]