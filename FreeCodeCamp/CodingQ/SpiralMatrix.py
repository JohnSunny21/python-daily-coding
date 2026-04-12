""" 

Spiral Matrix
Given a 2D matrix, return a flat array with all of its values in clockwise order.

The returned array should have the top-left value first, move right along the top row, then down the right column, then left along the bottom row, then up the left column. Repeat inward for any remaining layers.

For example, given:

[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
Return [1, 2, 3, 6, 9, 8, 7, 4, 5].
"""


import unittest

class SpiralMatrixTest(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(spiral_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test2(self):
        self.assertEqual(spiral_matrix([["a", "b", "c", "d"], ["l", "m", "n", "e"], ["k", "p", "o", "f"], ["j", "i", "h", "g"]]), ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"])

    def test3(self):
        self.assertEqual(spiral_matrix([[True, False, False], [False, True, True], [False, True, False], [True, True, False]]), [True, False, False, True, False, False, True, True, False, False, True, True])

    def test4(self):
        self.assertEqual(spiral_matrix([[25, 24, 23, 22, 21], [10, 9, 8, 7, 20], [11, 2, 1, 6, 19], [12, 3, 4, 5, 18], [13, 14, 15, 16, 17]]), [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


TESTCASES = [
    (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    (([["a", "b", "c", "d"], ["l", "m", "n", "e"], ["k", "p", "o", "f"], ["j", "i", "h", "g"]],), ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]),
    (([[True, False, False], [False, True, True], [False, True, False], [True, True, False]],), [True, False, False, True, False, False, True, True, False, False, True, True]),
    (([[25, 24, 23, 22, 21], [10, 9, 8, 7, 20], [11, 2, 1, 6, 19], [12, 3, 4, 5, 18], [13, 14, 15, 16, 17]],), [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
]





def spiral_matrix(matrix):

    result = []

    while matrix:

        # Take the top row
        result += matrix.pop(0)


        # Take the right column
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        # Take the bottom row (reversed)
        if matrix:
            result += matrix.pop()[::-1]

        # Take the left column (bottom to top)

        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))


    return result







from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark(
        {"first": spiral_matrix},
        TESTCASES,
        10000
    )

    unittest.main()

