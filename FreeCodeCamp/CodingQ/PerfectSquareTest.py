import unittest
from PerfectSquare import is_perfect_square

class PerfectSquareTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_perfect_square(9),True)

    def test2(self):
        self.assertEqual(is_perfect_square(49),True)

    def test3(self):
        self.assertEqual(is_perfect_square(1),True)

    def test4(self):
        self.assertEqual(is_perfect_square(2),False)

    def test5(self):
        self.assertEqual(is_perfect_square(99),False)

    def test6(self):
        self.assertEqual(is_perfect_square(-9),False)

    def test7(self):
        self.assertEqual(is_perfect_square(0),True)

    def test8(self):
        self.assertEqual(is_perfect_square(25281),True)

    
if __name__ == "__main__":
    unittest.main()