import DataModel as Dm
import DistancePicker as Dsp
import random as rd

from utils import format_clusters


class KMeans:

    def __init__(self, k, data, distance_type):
        self.__k = k
        self.__data = data
        self.__distance_picker = Dsp.DistancePicker(distance_type)
        self.__clusters = None
        self.__data_model = None

    def __initialize_clusters(self):

        # initialize a var to store our clusters.
        clusters = {}

        # list to not add same element in different clusters.
        seen_elements = []

        # pre-allocate list for the custers, we need to have them non-empty.
        for cluster_index in range(0, self.__k):

            # update seed of random using system.time.
            rd.seed()

            # create a random index alongside its value in the data to initialize our clusters with.
            rand_element_index = rd.randint(0, len(self.__data) - 1)
            rand_element = self.__data[rand_element_index]

            clusters[cluster_index] = [rand_element]
            seen_elements.append(rand_element)

        # iterate through the data.
        for data_index in range(0, len(self.__data)):

            # update seed of random using system.time.
            rd.seed()

            # get the current element in the datas.
            current_data = self.__data[data_index]

            # create a random index for the clusters.
            rand_cluster_index = rd.randint(0, self.__k - 1)

            # check if we haven't added the current_data in another cluster.
            if current_data not in seen_elements:

                # append to the cluster.
                clusters[rand_cluster_index].append(current_data)

                # and to not have duplicates.
                seen_elements.append(current_data)

        return clusters

    def __reallocate_clusters(self):

        # initialize our new clusters.
        reallocated_clusters = {}

        # for each element, get its index in the datas.
        for element_index in range(0, len(self.__data_model.get_data())):

            # get the current element from the index.
            current_element = self.__data_model.get_data()[element_index]

            # list of distances, so that we can get the lowest value after.
            distances = []

            # iterate through all the clusters to get their centroids and check for the lowest value of all.
            for cluster_index in range(0, len(self.__data_model.get_clusters())):

                # get the centroid for the current cluster.
                centroid = self.__data_model.get_centroid_of_cluster(cluster_index)

                # add the distance to the list of distances.
                distances.append(self.__distance_picker.calculate(current_element, centroid))

            # get the lowest value alongside its index.
            lowest = min(distances)
            lowest_index = distances.index(lowest)

            # reallocate it in the new cluster dictionary.
            if lowest_index not in reallocated_clusters.keys():
                reallocated_clusters[lowest_index] = [current_element]
            else:
                reallocated_clusters[lowest_index].append(current_element)

        return reallocated_clusters

    def run(self, debug=False):

        # randomly create our clusters.
        self.__clusters = self.__initialize_clusters()

        if debug:
            print("Initial clusters: ")
            print(format_clusters(self.__clusters))

        # create our data model in which we have the methods the algorithm needs to run.
        self.__data_model = Dm.DataModel(self.__data, self.__clusters)

        # save our initial clusters and create a variable to store the last encountered one.
        initial_clusters = self.__data_model.get_clusters()
        last_encountered_clusters = initial_clusters

        # infinite loop, will break out of it later.
        while True:

            # get the new partition.
            reallocated_clusters = self.__reallocate_clusters()

            # check if the clusters have changed or not.
            if reallocated_clusters == last_encountered_clusters:
                break

            # assign the variable to the reallocated one, to check in another iteration.
            last_encountered_clusters = reallocated_clusters

        # create data models to check for intra and interclass partitions.
        data_model_initial = Dm.DataModel(self.__data_model.get_data(), initial_clusters)
        data_model_clustered = Dm.DataModel(self.__data_model.get_data(), last_encountered_clusters)

        if debug:

            # check if the final intraclass dispersion is lesser than the initial intraclass dispersion.
            if data_model_clustered.get_intraclass_dispersion() < data_model_initial.get_interclass_dispersion():
                print("Clusters are fine.")
            else:
                print("Inacurate clustering.")

            print("Final clusters: ")
            print(format_clusters(data_model_clustered.get_clusters()))

        return data_model_clustered.get_clusters()
