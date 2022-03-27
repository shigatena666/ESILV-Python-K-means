from matplotlib import pyplot as plt
from matplotlib.pyplot import cm
import numpy as np


class DataViewer:

    def __init__(self, clustered_data):
        self.__clustered_data = clustered_data

    def show(self, k, file_name, first_variable_index, second_variable_index):

        # set our title.
        plt.title(f"K-means({k}) result for {file_name}")

        # set our axis.
        plt.xlabel("x")
        plt.ylabel("y")

        # show the grid in the plot.
        plt.grid()

        # will be used so that the clusters have all different colors.
        colors = iter(cm.rainbow(np.linspace(0, 1, len(self.__clustered_data.keys()))))

        # iterate through the clusters.
        for cluster_index in self.__clustered_data.keys():

            # get current cluster from the index.
            current_cluster = self.__clustered_data[cluster_index]

            # initialize our axis list.
            x = []
            y = []

            for element_index in range(0, len(current_cluster)):

                # get current element in the cluster.
                current_element = current_cluster[element_index]

                if first_variable_index < 0 or first_variable_index > len(current_element) or \
                        second_variable_index < 0 or second_variable_index > len(current_element):
                    raise Exception("Variable index to study in the plot doesn't exist!")

                # append to our list axis.
                x.append(current_element[first_variable_index])
                y.append(current_element[second_variable_index])

            plt.scatter(x, y, color=next(colors))

        # show the plot.
        plt.show()
