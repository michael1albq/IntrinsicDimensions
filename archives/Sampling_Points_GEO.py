
# coding: utf-8

# ## Sampling a line
# 

# In[1]:

import numpy as np


def sample_line(n):
    #direction vector to be scaled
    dir_vec = np.random.randn(3)
    line_point = np.random.randn(3)
    #generating random scalars
    parameter = np.transpose(np.random.randn(n)[np.newaxis])
    #translating direc_vec by random scalars to get points on the same line
    line_points = line_point + parameter*dir_vec

    return line_points


# # Visual
# 

# In[2]:

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from numpy.random import rand
from pylab import figure


L=sample_line(1000)# m is an array of (x,y,z) coordinate triplets
#test code
print(L)
#n=exits_sorted['name']
#print(m)

fig=figure(figsize=(30,15))
##fig = figure()
ax = Axes3D(fig)


for i in range(len(L)): #plot each point + it's index as text above
 ax.scatter(L[i][0],L[i][1],L[i][2],color='b') 
 #ax.text(m[i][0],m[i][1],m[i][2],  '%s' % (str(i)), size=20, zorder=1,  
 #color='k')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
pyplot.show()


# ## Sampling a Plane

# In[3]:

import numpy as np 


def sample_plane(n):
    #normal vector dot vector on a plane is equal to zero
    #random normal vector
    normal_vec = np.random.randn(3)
    #random point
    point_plane = np.random.randn(3)
    sample_points = []

    for int in range(0, n):
        #random second point(only choosing x and y)
        sample_2coord = np.random.randn(2)
        #getting a vector on the plane
        last_coord = sample_2coord - point_plane[0:2]
        #scaling for Z to obtain the equation
        last_coord = -(np.dot(normal_vec[0:2], last_coord)-normal_vec[2] * point_plane[2])/normal_vec[2]
        sample_2coord = np.append(sample_2coord, last_coord)
        sample_points = np.append(sample_points, sample_2coord, axis=0)

    sample_points = np.reshape(sample_points, (n,3))

    return sample_points


# # Visual

# In[4]:

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from numpy.random import rand
from pylab import figure


P=sample_plane(1000)# m is an array of (x,y,z) coordinate triplets
#n=exits_sorted['name']
#print(m)

fig=figure(figsize=(30,15))
##fig = figure()
ax = Axes3D(fig)


for i in range(len(P)): #plot each point + it's index as text above
 ax.scatter(P[i][0],P[i][1],P[i][2],color='b') 
 #ax.text(m[i][0],m[i][1],m[i][2],  '%s' % (str(i)), size=20, zorder=1,  
 #color='k')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
pyplot.show()


# # Sampling a Sphere

# In[5]:

import numpy as np


def sample_sphere(n):
    vec = np.random.randn(3, n)
    vec /= np.linalg.norm(vec, axis=0)
    return np.transpose(vec)


# In[6]:

#test code
sample_sphere(20)


# # Visual

# In[7]:

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from numpy.random import rand
from pylab import figure


S=sample_sphere(1000)# m is an array of (x,y,z) coordinate triplets
#n=exits_sorted['name']
#print(m)

fig=figure(figsize=(30,15))
##fig = figure()
ax = Axes3D(fig)


for i in range(len(S)): #plot each point + it's index as text above
    ax.scatter(S[i][0],S[i][1],S[i][2],color='b') 
 #ax.text(m[i][0],m[i][1],m[i][2],  '%s' % (str(i)), size=20, zorder=1,  
 #color='k')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
pyplot.show()


# In[8]:

np.linalg.svd(P)[1]


# In[9]:

get_ipython().system('jupyter nbconvert --to script Sampling_Points_GEO.ipynb')

