from Distance import *
from math import sqrt


class DistancePicker:

    def __init__(self, distance_type=Distance.EUCLIDEAN):
        self.distance_type = distance_type

    def calculate(self, a, b):

        if self.distance_type == Distance.EUCLIDEAN:
            return self._euclidean_distance(a, b)

        elif self.distance_type == Distance.MANHATTAN:
            return self._manhattan_distance(a, b)

        elif self.distance_type == Distance.MINKOWSKI:
            return self._minkowski_distance(a, b, 5)

        raise Exception("Undefined distance_type: " + str(self.distance_type))

    @staticmethod
    def _euclidean_distance(a, b):

        # initialize our result.
        result = 0

        # loop through all the elements.
        for index in range(0, len(a)):
            result += (a[index] - b[index]) ** 2

        # return the result.
        return sqrt(result)

    @staticmethod
    def _manhattan_distance(a, b):

        # initialize our result.
        result = 0

        # loop through all the elements.
        for index in range(0, len(a)):
            result += abs(a[index] - b[index])

        # return the result.
        return result

    @staticmethod
    def _minkowski_distance(a, b, p):

        # initialize our result.
        result = 0

        # loop through all the elements.
        for index in range(0, len(a)):
            result += abs(a[index] - b[index]) ** p

        # minkowski distance is the sum of the distances at the power p ; everything at the p-sqrt.
        # return the result at the same time.
        return result ** (1 / p)
