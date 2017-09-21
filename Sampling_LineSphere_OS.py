
# coding: utf-8

# # Line & Sphere

# In[1]:

#%run Sampling_Points_Individually.py
import Sampling_Points_GEO as SPI
from Sampling_Points_GEO import *


# In[2]:

import numpy as np
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from numpy.random import rand
from pylab import figure
get_ipython().magic('matplotlib inline')


# # Obtaining a translating the scaled version of the line to the surface of the sphere

# In[3]:

#Centre of the Sphere
x=np.array([0,0,0])
#Point on the surface of the sphere
#print(SPI.P[1])
v=(SPI.S[0][0],SPI.S[0][1],SPI.S[0][2])
#print(p)
# vector from centre to point p
#l=x-p
#scaling up the vector
Scale_L=5*v
#vector on the sphere
Sphere_L=Scale_L
#print(Scale_L)
#random parameters for scaling
parameter = np.transpose(abs(np.random.randn(1000)[np.newaxis]))
#Sampling from vector on the sphere
sphere_line=parameter*Sphere_L
sphereline_list=sphere_line.tolist()
sphere_line_OS=[]
for i in sphere_line:
    if (i[0]**2+i[1]**2+i[2]**2>=1):
        sphere_line_OS.append((i[0],i[1],i[2]))
#test code: should be equal to 1000

parameter = np.transpose(abs(np.random.randn(1000)[np.newaxis]))
#Sampling from vector on the sphere
sphere_line=parameter*Sphere_L
sphereline_list=sphere_line.tolist()
for i in sphere_line:
    if (i[0]**2+i[1]**2+i[2]**2>=1):
        sphere_line_OS.append((i[0],i[1],i[2]))

parameter = np.transpose(abs(np.random.randn(1000)[np.newaxis]))
#Sampling from vector on the sphere
sphere_line=parameter*Sphere_L
sphereline_list=sphere_line.tolist()
for i in sphere_line:
    if (i[0]**2+i[1]**2+i[2]**2>=1):
        sphere_line_OS.append((i[0],i[1],i[2]))  
        
parameter = np.transpose(abs(np.random.randn(1000)[np.newaxis]))
#Sampling from vector on the sphere
sphere_line=parameter*Sphere_L
sphereline_list=sphere_line.tolist()
for i in sphere_line:
    if (i[0]**2+i[1]**2+i[2]**2>=1):
        sphere_line_OS.append((i[0],i[1],i[2]))        

print(len(sphere_line_OS))        


# # Adding the points sampled from the new translated line to the set of points sampled from sphere

# In[4]:

#Coverting to list from numpy array
Sample_L=SPI.L.tolist()
Sample_P=SPI.P.tolist()
Sample_S=SPI.S.tolist()
Sample_LS=[]
#test code: should be equal to 0


#creating final list of points vector above surface and points on surface
for i in range(len(sphere_line_OS)):
    Sample_LS.append(sphere_line_OS[i])
for i in range(len(Sample_S)):
    Sample_LS.append(SPI.S[i])    

print(len(Sample_LS))


# In[5]:

#test code: should be equal to 2000
Sample_LS[1]
np.linalg.svd(Sample_LS)[1]


# # Visual

# In[6]:

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from numpy.random import rand
from pylab import figure


SS=SPI.S# m is an array of (x,y,z) coordinate triplets
LS=sphere_line_OS
#print(LS)
#n=exits_sorted['name']
#print(m)

fig=figure(figsize=(30,15))
##fig = figure()
ax = Axes3D(fig)


for i in range(len(LS)): #plot each point + it's index as text above
    ax.scatter(LS[i][0],LS[i][1],LS[i][2],color='b')
    #ax.scatter(SS[i][0],SS[i][1],SS[i][2],color='r')
for i in range(len(SS)): #plot each point + it's index as text above
    #ax.scatter(LS[i][0],LS[i][1],LS[i][2],color='b')
    ax.scatter(SS[i][0],SS[i][1],SS[i][2],color='r')
 #ax.scatter(S1[i][0],S1[i][1],S1[i][2],color='r')
 #ax.text(m[i][0],m[i][1],m[i][2],  '%s' % (str(i)), size=20, zorder=1,  
 #color='k')


ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
pyplot.show()


# In[7]:

get_ipython().system('jupyter nbconvert --to script Sampling_LineSphere_OS.ipynb')

