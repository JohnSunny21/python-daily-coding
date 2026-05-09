""" 

Transposed Matrix
Given a matrix (an array of arrays), return the transposed version of it.

To transpose the matrix, swap the rows and columns. E.g: a value at index [0, 1] should move to index [1, 0].

For example, given:

[
  [1, 2, 3],
  [4, 5, 6]
]
Return:

[
  [1, 4],
  [2, 5],
  [3, 6]
]
"""



import unittest

class TransposedMatrixTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(transpose([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])

    def test2(self):
        self.assertEqual(transpose([[1, 2], [3, 4], [5, 6]]), [[1, 3, 5], [2, 4, 6]])

    def test3(self):
        self.assertEqual(transpose([[1, 2], [3, 4], [5, 6], [7, 8]]), [[1, 3, 5, 7], [2, 4, 6, 8]])

    def test4(self):
        self.assertEqual(transpose([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"]]), [["a", "d", "g", "j"], ["b", "e", "h", "k"], ["c", "f", "i", "l"]])

    def test5(self):
        self.assertEqual(transpose([[True, False, True, False], [False, True, False, True], [True, True, False, False], [False, False, True, True], [True, False, False, True]]), [[True, False, True, False, True], [False, True, True, False, False], [True, False, False, True, False], [False, True, False, True, True]])


TESTCASES = [
    (([[1, 2, 3], [4, 5, 6]],), [[1, 4], [2, 5], [3, 6]]),
    (([[1, 2], [3, 4], [5, 6]],), [[1, 3, 5], [2, 4, 6]]),
    (([[1, 2], [3, 4], [5, 6], [7, 8]],), [[1, 3, 5, 7], [2, 4, 6, 8]]),
    (([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"]],), [["a", "d", "g", "j"], ["b", "e", "h", "k"], ["c", "f", "i", "l"]]),
    (([[True, False, True, False], [False, True, False, True], [True, True, False, False], [False, False, True, True], [True, False, False, True]],), [[True, False, True, False, True], [False, True, True, False, False], [True, False, False, True, False], [False, True, False, True, True]])
]



def transpose(matrix):

    return [list(row) for row in zip(*matrix)]



def transpose_manual(matrix):

    rows , cols = len(matrix), len(matrix[0])
    result = []

    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)

    return result



from utils.benchmark import benchmark


if __name__ == "__main__":
    scores = benchmark(
        {"first": transpose,
         "second": transpose_manual},
        TESTCASES,
        10000
    )

    unittest.main()