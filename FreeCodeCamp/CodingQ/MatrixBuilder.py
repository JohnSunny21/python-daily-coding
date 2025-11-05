"""
Matrix Builder
Given two integers (a number of rows and a number of columns), return a matrix (an array of arrays) filled with zeros (0) of the given size.

For example, given 2 and 3, return:

[
  [0, 0, 0],
  [0, 0, 0]
]
"""

import unittest

class MatrixBuilderTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(build_matrix(2,3),[[0,0,0],[0,0,0]])

    def test2(self):
        self.assertEqual(build_matrix(3,2),[[0,0],[0,0],[0,0]])

    def test3(self):
        self.assertEqual(build_matrix(4,3),[[0,0,0],[0,0,0],[0,0,0],[0,0,0]])

    def test4(self):
        self.assertEqual(build_matrix(9,1),[[0],[0],[0],[0],[0],[0],[0],[0],[0]])

def build_matrix(rows,cols):
    matrix = []
    for row in range(rows):
        matrix_row = [0]*cols
        matrix.append(matrix_row)

    return matrix

def build_matrix_optimxed(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]



if __name__ == "__main__":
    print(build_matrix(2,3))
    print(build_matrix(3,0))
    print(build_matrix(0,3))
    print(build_matrix(0,0))
    unittest.main()