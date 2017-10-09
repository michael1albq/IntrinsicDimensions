# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 13:06:35 2017

@author: Kafung
"""

import numpy as np
import math
import neighborhood as nbh
import center_data as cd
import svd
import sample_sphere as ss
import time


#Input a matrix data, a threshold K to determine the min number  
#of points in each neighborhood, a threshold thres for percentage of variance 
#to exhibit and num, the number of radii.
#This computes the intrinsic dimension of a list of data points
def intrinsic_dim(data, K, thres, num) :
    rads = [(1/2.)**(i) for i in range(num)] 
    dims = np.zeros((len(data), num))
    elem_ind = 0 
    #density = []
    for elem in data :         
        rad_ind = 0
        for radius in rads :
            D_n = nbh.neighborhood(data, elem, radius)
            D_nset = set(tuple(row) for row in D_n)            
            if len(D_nset) < K*math.log(K):
                #density.append(0)
                dims[elem_ind, rad_ind] = -1
                break
            else:
                #density.append(1)
                D_n0 = cd.centered(D_n)
                D_n0 = (1/(len(D_n0)-1)**(1/2.))*D_n0
                S = svd.svd(D_n0)
                S_2 = np.multiply(S,S)
                TV = sum(S_2)
                CRV =np.asarray([ (1/TV)*sum(S_2[0:i]) for i in range(len(S_2)+1)][1:])
                CRV_bool = CRV > thres
                ind = [i for i,x in enumerate(CRV_bool) if x]  
                dims[elem_ind, rad_ind] = ind[0]+1 
                rad_ind += 1
                if ind[0]==0 :
                    break
        #int_dim[elem_ind] = min(i for i in dims[elem_ind, :] if i>-1 )
        elem_ind += 1
    return dims

if __name__ == '__main__':
    data = ss.sample_sphere(5000, [0,0,0])
    start = time.time()
    results = intrinsic_dim(data, 3, .95, 5)
    end = time.time()
    print("Took", end - start, "sec")
