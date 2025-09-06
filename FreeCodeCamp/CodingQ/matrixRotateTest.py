import unittest
from matrixRotate import rotate

class matrixRotateTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(rotate([[1]]),[[1]])

    def test2(self):
        self.assertEqual(rotate([[1, 2], [3, 4]]),[[3, 1], [4, 2]])

    def test3(self):
        self.assertEqual(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),[[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    def test4(self):
        self.assertEqual(rotate([[0, 1, 0], [1, 0, 1], [0, 0, 0]]),[[0, 1, 0], [0, 0, 1], [0, 1, 0]])



if __name__ == "__main__":
    unittest.main()