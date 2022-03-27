import csv
from utils import is_float


class DataWrapper:

    def __init__(self, csv_file):
        self.csv_file = csv_file

    def load(self):

        # variable to store our data as a list of list.
        data = []

        # open our file in read-only mode.
        with open(self.csv_file, 'r') as f:

            # create our csv_reader so that we can read the previous opened file.
            csv_reader = csv.reader(f)

            # for every line in the csv, try to convert the data to float if possible.
            for row in csv_reader:
                data.append([float(row[i]) for i in range(0, len(row)) if is_float(row[i])])

        # return the data we read.
        return data
