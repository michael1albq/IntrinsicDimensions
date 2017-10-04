# Project: IntrinsicDimensions
# Author: Michael Albuquerque
# Date Created: 10/4/17
# Python Version: 3.6.2

# Description: Visualize 3D

import numpy as np
from random import randint
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from pylab import figure


def visualize_3d(data, dim_list):

    # Color Map
    """

    :param data: coordinates of 'n' points [x,y,z]
    :param dim_list: list of intrinsic dimension of 'n' points
    """
    c_map = {1: 'r', 2: 'g', 3: 'b'}

    # Set up axes , fig
    fig = figure(figsize=(20, 15))
    ax = Axes3D(fig)

    try:
        # Set up 3-D Scatter plot
        for row in range(len(data)):
            ax.scatter(data[row][0], data[row][1], data[row][2], c=c_map[dim_list[row]])

        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        pyplot.show()

    except Exception as e:
        print("Error -", e)
        print("An error was encountered. Check data type of inputs. Also first two parameters should have same number \
        of elements. ")


if __name__ == "__main__":

    dummyList = list()

    # Create dummy list
    for i in range(9):
        dummyList.append(randint(1, 3))

    # Create dummy data
    dummyData = np.array([[-1.0356457581534786, 0.6239971187570623, 0.4116486393964163],
                          [-0.631562706734726, 0.7104771696473557, -0.07891446291262973],
                          [-0.518076147772892, 0.008210618904429808, 0.5098655288684623],
                          [-0.9704778210138871, 0.7133056380877726, 0.2571721829261146],
                          [-1.8250532779987676, 0.5574935244452879, 1.2675597535534797],
                          [-1.482112264159786, 0.11688841243074462, 1.3652238517290414],
                          [-0.6714528172537867, 0.6482192070708985, 0.02323361018288818],
                          [-0.9329919278574447, 0.5159567443941191, 0.41703518346332563],
                          [-0.8428077855784617, -0.3502110378360248, 1.1930188234144865]])

    visualize_3d(dummyData, dummyList)







