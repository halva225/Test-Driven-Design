import unittest
import numpy

class levenshtein_Distance_Matrix_test:
    def test_levenshtein_distance_matrix_with_10_columns_returns_success():
        # test init
        rows = 10
        cols = 10
        distances = numpy.zeros((rows + 1, cols + 1))

        # test execution

        for t1 in range(rows + 1):
            distances[t1][0] = t1

        for t2 in range(cols + 1):
            distances[0][t2] = t2

        for col in range(cols + 1):
            for row in range(rows + 1):
                print(int(distances[col][row]), end=" ")
            print()

    
print(levenshtein_Distance_Matrix_test.test_levenshtein_distance_matrix_with_10_columns_returns_success()) 