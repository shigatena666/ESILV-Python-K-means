class DataModel:

    def __init__(self, data, clusters):
        self.__data = data
        self.__clusters = clusters

    def get_data(self):
        return self.__data

    def get_clusters(self):
        return self.__clusters

    def __get_average_for_variable(self, index):

        # if the cluster only contains 1 coordonate, then the centroid for one variable is the same point as this
        # variable.
        if len(self.__data) == 1:
            return self.__data[0][index]

        # get all values of variables at given index.
        variables_at_index = [coordonates[index] for coordonates in self.__data]

        # sum them up and divide by length.
        return sum(variables_at_index) / len(variables_at_index)

    def __get_average(self):

        # if the cluster only contains 1 coordonate, then the centroid is the same point.
        if len(self.__data) == 1:
            return self.__data[0]

        # initialize our result.
        centroid = []

        # get centroid for all lines.
        for i in range(0, len(self.__data[0])):
            centroid.append(self.__get_average_for_variable(i))

        return centroid

    def get_centroid_of_cluster(self, cluster_index):

        # from a sub data sample, gives the centroid.
        data_model_sample = DataModel(self.__clusters[cluster_index],
                                      {cluster_index: self.__clusters[cluster_index]})

        # if the length of the cluster is one, then it means the centroid is the element itself.
        if len(self.__clusters[cluster_index]) == 1:
            return self.__clusters[cluster_index][0]

        return data_model_sample.__get_average()

    def __get_total_dispersion_for_variable(self, variable_index):

        # get coordonates for the given variable.
        variable_coordonates = [self.__data[i][variable_index] for i in range(0, len(self.__data))]

        # get average of this variable.
        variable_average = self.__get_average_for_variable(variable_index)

        # initialize our result.
        total_dispersion_for_variable = 0

        # apply the formula we've seen in classes on the element.
        for i in range(0, len(variable_coordonates)):
            total_dispersion_for_variable += (variable_coordonates[i] - variable_average) ** 2

        return total_dispersion_for_variable

    # not used in algorithm but still useable.
    def __get_total_dispersion(self):

        # initialize our result.
        total_dispersion = 0

        # for all indexes, get their dispersion and sum it up.
        for i in range(0, len(self.__data[0])):
            total_dispersion += self.__get_total_dispersion_for_variable(i)

        return total_dispersion

    def __get_intraclass_dispersion_for_variable_in_cluster(self, axis_index, cluster_index):

        # initialize our result.
        intraclass_dispersion = 0

        # get the clusters keys.
        cluster_keys = list(self.__clusters.keys())

        # if the cluster only has one coordonate, then its intraclass dispersion is 0.
        if len(self.__clusters[cluster_index]) == 1:
            return 0

        # get the centroid of the cluster.
        centroid = self.get_centroid_of_cluster(cluster_index)

        # get the size of a cluster.
        cluster_size = len(self.__clusters[cluster_keys[0]])

        # for each element (index) in this cluster.
        for element_index in range(0, cluster_size):

            # for each cluster in the datas.
            for current_cluster in list(self.__clusters.keys()):

                # apply the formula we've seen in the courses and sum it up.
                intraclass_dispersion += (self.__clusters[current_cluster][element_index][axis_index] -
                                          centroid[axis_index]) ** 2

        return intraclass_dispersion

    # not used in algorithm but still useable.
    def __get_intraclass_dispersion_for_cluster(self, cluster_index):

        # from a sub data sample, gives the intraclass dispersion.
        data_model_sample = DataModel(self.__clusters[cluster_index],
                                      {cluster_index: self.__clusters[cluster_index]})

        # if the length of the cluster is one, then it means the intraclass dispersion is 0
        if len(self.__clusters[cluster_index]) == 1:
            return 0

        return data_model_sample.get_intraclass_dispersion()

    def get_intraclass_dispersion(self):

        # initialize our result.
        total_intraclass_dispersion = 0

        # sum the intraclass dispersion for every variable.
        for cluster_index in list(self.__clusters.keys()):

            # get the dimension of one element.
            element_dim = len(self.__clusters[cluster_index][0])

            # create sub data sample, to generate sub intraclass dispersion.
            data_model_sample = DataModel(self.__clusters[cluster_index],
                                          {cluster_index: self.__clusters[cluster_index]})

            # for each axis the element is made of.
            for variable_index in range(0, element_dim):

                # get the intraclass dispersion for the cluster.
                to_add = data_model_sample.__get_intraclass_dispersion_for_variable_in_cluster(variable_index,
                                                                                               cluster_index)

                # sum it up.
                total_intraclass_dispersion += to_add

        return total_intraclass_dispersion

    def __get_interclass_dispersion_for_cluster(self, cluster_index):

        # initiliaze our value.
        interclass_dispersion = 0

        # get centroid of current cluster.
        centroid = self.get_centroid_of_cluster(cluster_index)

        # for each axis this centroid is made of.
        for variable_index in range(0, len(centroid)):

            # apply the formula we've seen in the courses and sum it up.
            interclass_dispersion += (centroid[variable_index] - self.__get_average_for_variable(variable_index)) ** 2

        # do not forget to * as it's in the formula.
        interclass_dispersion *= len(self.__clusters[cluster_index])

        return interclass_dispersion

    def get_interclass_dispersion(self):

        # initiliaze our value.
        interclass_dispersion = 0

        # iterate through all clusters.
        for cluster_index in list(self.__clusters.keys()):

            # add interclass cluster dispersion to total.
            interclass_dispersion += self.__get_interclass_dispersion_for_cluster(cluster_index)

        return interclass_dispersion
