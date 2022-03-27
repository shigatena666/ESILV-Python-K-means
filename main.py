import DataWrapper as Dw
import KMeans as Km
import DataViewer as Dv

from Distance import *


def run_all(k_clusters, file_name, first_var, second_var, distance_type: Distance, debug=False):

    # create our data wrapper to read from the file.
    data_wrapper = Dw.DataWrapper(f'Datasets/{file_name}.csv')
    data = data_wrapper.load()

    # instantiate our kmeans class.
    kmeans = Km.KMeans(k_clusters, data, distance_type)

    # run our algorithm and store the result in a variable.
    clusters = kmeans.run(debug)

    # create our data viewer so that we can plot the clusters.
    data_viewer = Dv.DataViewer(clusters)

    # show the result of the K-means output.
    data_viewer.show(k_clusters, file_name, first_var, second_var)


if __name__ == "__main__":

    # user input.
    k = int(input("Enter amount of clusters (k): "))
    file = input("Enter file name in Datasets folder (without .csv): ")
    first_variable = int(input("Enter first variable (index) to show in plot: "))
    second_variable = int(input("Enter second variable (still index) to show in plot: "))
    distance = input("Enter your distance choice (euclidean, manhattan, minkowski): ")
    should_debug = int(input("Verbosity (0 or 1): "))

    # small print for better readability in console output.
    print("")

    # start everything.
    try:
        run_all(k, file, first_variable, second_variable, getattr(Distance, distance.upper()), bool(should_debug))
    except Exception as e:
        print("An error occured during the execution of the algorithm:\n" + str(e))

    # test purposes.
    # run_all(4, "td_example", 1, 3, Distance.MANHATTAN, True)
