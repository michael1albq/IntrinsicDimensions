# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 22:05:55 2017

@author: Kafung
"""
import random
from random import randrange, uniform
import numpy as np 
import matplotlib as mpl 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA as sklearnPCA
from sklearn import decomposition
from sklearn import datasets
from numpy import linalg as la

def sample_line(n):
    
    fig = plt.figure() 

    ax = fig.add_subplot(111, projection='3d')

    v_vec = np.asarray(random.sample(range(1,10), 3)) ;
    initial_point = np.asarray(random.sample(range(1,10), 3)) ;
    sample_points = np.transpose(np.asarray([random.sample(range(1,100), n)])) ;
 
    line_points = initial_point + sample_points*v_vec ;
    
    xs = line_points[:, 0] ;
    ys = line_points[:, 1] ;
    zs = line_points[:, 2] ;
    
    ax.scatter(xs,ys,zs) ;
     
   # pca = decomposition.PCA(n_components=1)
   # u,s,v = la.svd(line_points, full_matrices=True);
    
    return line_points
    
    

    
    
    
    

    