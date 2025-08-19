import unittest
from sumOfSquares import sum_of_squares

class sumOfSquares(unittest.TestCase):

    def test1(self):
        self.assertEqual(sum_of_squares(5),55)

    def test2(self):
        self.assertEqual(sum_of_squares(10),385)

    def test3(self):
        self.assertEqual(sum_of_squares(25),5525)

    def test4(self):
        self.assertEqual(sum_of_squares(500),41791750)

    def test5(self):
        self.assertEqual(sum_of_squares(1000),333833500)


if __name__ == "__main__":
    unittest.main()