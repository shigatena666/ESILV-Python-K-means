import csv
import random
from utils import is_float


class DataWrapper:

    def __init__(self, csv_file):
        self.csv_file = csv_file

    def load(self, first_variable_index, second_variable_index):

        # variable to store our data as a list of list.
        data = []

        # open our file in read-only mode.
        with open(self.csv_file, 'r') as f:

            # create our csv_reader so that we can read the previous opened file.
            csv_reader = csv.reader(f)

            # for every line in the csv, try to convert the data to float if possible, and only load the ones we are
            # going to show.
            for row in csv_reader:

                element = [float(row[i]) for i in range(0, len(row))
                           if is_float(row[i])
                           and (i == first_variable_index or i == second_variable_index)]

                # eliminate duplicates as well (will show weird points on the plot otherwise).
                if element in data:
                    continue

                data.append(element)

        # shuffle data.
        random.shuffle(data)

        # return the data we read.
        return data
